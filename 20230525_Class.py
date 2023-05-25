import mediapipe as mp
import cv2

face_det = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils


img = cv2.imread("S__86515719_2.jpg")
newing = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
faceDetection = face_det.FaceDetection(model_selection=1)
result = faceDetection.process(newing)
print(result.detections)
if not result.detections:
    print("no detect")
else:
    for result in result.detections:
        mp_drawing.draw_detection(img,result)
    cv2.imshow("people",img)
    cv2.waitKey(0)