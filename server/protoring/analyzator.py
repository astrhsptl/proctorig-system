import cv2
import numpy as np
import face_recognition

def face(vid):
    filt_path = r'/home/nia/Desktop/proctorig-system/haarcascade_frontalface_default.xml'
    filt = cv2.CascadeClassifier(filt_path)
    camera = cv2.VideoCapture(vid)
    _, frame = camera.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = filt.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(5, 5),
    )
    return len(faces)

def compare_face(im1: np.array or str, im2: np.array or str) -> bool:
    img1 = face_recognition.load_image_file(im1)
    img2 = face_recognition.load_image_file(im2)

    img1_code = face_recognition.face_encodings(img1)[0]
    img2_code = face_recognition.face_encodings(img2)[0]

    result = face_recognition.compare_faces([img1_code], img2_code)
    return result[0]