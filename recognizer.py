import cv2
import numpy as np

import recog_data_builder
import global_variables

FACE_RECOGNIZER_LBPH = 1
FACE_RECOGNIZER_EIGEN = 2
FACE_RECOGNIZER_FISHER = 3


class Recognizer:
    def __init__(self, databuilder, algorithm):
        self.is_trained = False
        self.trainingResultLoaded = False
        self.labels_map = {}
        self.data_builder = databuilder
        if algorithm == FACE_RECOGNIZER_LBPH:
            self.recognizer = cv2.face.createLBPHFaceRecognizer()
        elif algorithm == FACE_RECOGNIZER_EIGEN:
            self.recognizer = cv2.face.createEigenFaceRecognizer()
        elif algorithm == FACE_RECOGNIZER_FISHER:
            self.recognizer = cv2.face.createFisherFaceRecognizer()
        self.algorithm = algorithm

        self.recog_data_builder = recog_data_builder.RecogDataBuilder(global_variables.RECOG_DATA_PATH)

    def train(self):
        labels, images = self.data_builder.read()
        tmp_images = []
        if labels == [] or images == []:
            return

        if self.algorithm == FACE_RECOGNIZER_EIGEN or self.algorithm == FACE_RECOGNIZER_FISHER:
            for image in images:
                tmp_images.append(cv2.resize(image, (100, 100)))
            images = tmp_images

        self.labels_map = {}
        current_label = ''
        count = 0
        int_labels = []
        self.labels_map[0] = ''
        for label in labels:
            if label != current_label:
                current_label = label
                count += 1
                self.labels_map[count] = label
            int_labels.append(count)

        self.recognizer.train(images, np.array(int_labels))
        self.is_trained = True

    def predict(self, image):

        if self.algorithm == FACE_RECOGNIZER_EIGEN or self.algorithm == FACE_RECOGNIZER_FISHER:
            image = cv2.resize(image, (100, 100))

        conf = self.recognizer.predict(image)[1]
        result = self.recognizer.predict(image)[0]
        print(result, conf)
        if result < 0:
            return ""
        else:
            return self.labels_map[result]

    def set_threshold(self, threshold):
        self.recognizer.setThreshold(threshold)
