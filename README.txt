Libraries Requirements:
numpy
scipy
sklearn
pillow
opencv3
PyQt5 (in Windows: python3.dll required, this can be acquired from WinPython)

Folder Structure:
"data": pre-trained model for object detection
"FaceData": path for face training data (pre-defined in DATA_PATH in global_variables)
 ______personName1____img1
    |               |_img2
    |               |_img3
    |
    ___personName2____img1
    |               |_img2
    |               |_img3
    |
    ___personName3____img1
                    |_img2
                    |_img3
"UI": ui designing file (Qt Designer) & pyuic5

Modules:
global_variables:
data_builder: supporting functions for face data storage
recognizer: implement recognizing methods in opencv
recog_data_builder: supporting functions for recognizer data
collector_requirements: requirements for face data collecting
jh_data_collector_gui: program for auto collecting face data
jh_face_gui: program that implements all functions