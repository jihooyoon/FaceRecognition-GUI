import os
import cv2
import numpy as np
from PIL import Image

import global_variables


class DataBuilder:
    def __init__(self, path):
        self.path = path
        self.num_of_images = {}
        self.standardized = False

    def read(self):
        if not os.path.isdir(self.path):
            return [], []

        object_paths = []
        for f in os.listdir(self.path):
            object_paths.append(os.path.join(self.path, f))

        cascade_path = global_variables.CASCADE_PATH
        face_cascade = cv2.CascadeClassifier(cascade_path)
        images = []
        labels = []
        for object_path in object_paths:
            if not os.path.isdir(object_path):
                continue

            image_paths = [os.path.join(object_path, f)
                           for f in os.listdir(object_path)]
            object_name = os.path.split(object_path)[1]
            for image_path in image_paths:
                try:
                    image_pil = Image.open(image_path).convert('L')
                    image = np.array(image_pil, 'uint8')
                    faces = face_cascade.detectMultiScale(image)
                    for (x, y, w, h) in faces:
                        images.append(image[y: y + h, x: x + w])
                        labels.append(object_name.lower())
                except IOError:
                    print('Not an image: ', image_path)
        return labels, images

    def standardize(self):
        if not os.path.isdir(self.path):
            os.makedirs(self.path)
        object_paths = []
        self.num_of_images = {}
        for f in os.listdir(self.path):
            object_paths.append(os.path.join(self.path, f))

        for object_path in object_paths:
            if not os.path.isdir(object_path):
                continue

            image_paths = [os.path.join(object_path, f)
                           for f in os.listdir(object_path)]
            n = 0
            for image_path in image_paths:
                try:
                    image_pil = Image.open(image_path).convert('L')
                    extension = image_pil.format
                    print(extension)
                    if extension is None:
                        extension = 'raw'
                    filename = 'img' + str(n) + "." + str(extension)
                    parent_path = os.path.split(image_path)[0]
                    os.rename(image_path, os.path.join(parent_path, filename))
                    print(os.path.split(image_path)[1] + '=>' + filename)
                    n += 1

                except IOError:
                    print('Not an image: ', image_path)

            object_name = os.path.split(object_path)[1]
            self.num_of_images[object_name.lower()] = n
        self.standardized = True

    def synchronize(self, image, label):
        num = 0
        label = label.lower()
        if label in self.num_of_images:
            num = self.num_of_images[label]
            self.num_of_images[label] += 1
        else:
            self.num_of_images[label] = 1

        filename = 'img' + str(num) + '.jpg'
        file_path = os.path.join(self.path, label)
        if not os.path.isdir(file_path):
            os.makedirs(file_path)
        file_path = os.path.join(file_path, filename)
        cv2.imwrite(file_path, image, [cv2.IMWRITE_JPEG_OPTIMIZE])
