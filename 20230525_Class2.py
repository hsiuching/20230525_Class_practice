import mediapipe as mp
import cv2

face_det = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

img = cv2.imread("Lenna.jpg")
newimg = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
faceDetection = face_det.FaceDetection(model_selection=1)
result = faceDetection.process(newimg)

print(result.detections)

if not result.detections:
    print("no detect")

else:
    h,w,c = img.shape

    #for detection in result.detections:
        #print(detection)
    for detection in result.detections:

        '''p = face_det.get_key_point(detection,0)
        print(p.x)
        print(p.y)
        pixelX = int(p.x*w)
        pixelY = int(p.y*h)
        cv2.circle(img,(pixelX,pixelY),3,(255,0,0),-1)'''

        p = face_det.get_key_point(detection,face_det.FaceKeyPoint.LEFT_EYE)
        print(p.x)
        print(p.y)
        pixelX = int(p.x*w)
        pixelY = int(p.y*h)
        cv2.circle(img,(pixelX,pixelY),3,(255,0,0),-1)

        p2 = face_det.get_key_point(detection,face_det.FaceKeyPoint.RIGHT_EYE)
        print(p2.x)
        print(p2.y)
        pixelX2 = int(p2.x*w)
        pixelY2 = int(p2.y*h)
        cv2.circle(img,(pixelX2,pixelY2),3,(255,0,0),-1)

        p3 = face_det.get_key_point(detection,face_det.FaceKeyPoint.NOSE_TIP)
        print(p3.x)
        print(p3.y)
        pixelX3 = int(p3.x*w)
        pixelY3 = int(p3.y*h)
        cv2.circle(img,(pixelX3,pixelY3),3,(255,0,0),-1)
 
        p4 = face_det.get_key_point(detection,face_det.FaceKeyPoint.MOUTH_CENTER)
        print(p4.x)
        print(p4.y)
        pixelX4 = int(p4.x*w)
        pixelY4 = int(p4.y*h)
        cv2.circle(img,(pixelX4,pixelY4),3,(255,0,0),-1)

        p5 = face_det.get_key_point(detection,face_det.FaceKeyPoint.LEFT_EAR_TRAGION)
        print(p5.x)
        print(p5.y)
        pixelX5 = int(p5.x*w)
        pixelY5 = int(p5.y*h)
        cv2.circle(img,(pixelX5,pixelY5),3,(255,0,0),-1)

        p6 = face_det.get_key_point(detection,face_det.FaceKeyPoint.RIGHT_EAR_TRAGION)
        print(p6.x)
        print(p6.y)
        pixelX6 = int(p6.x*w)
        pixelY6 = int(p6.y*h)
        cv2.circle(img,(pixelX6,pixelY6),3,(255,0,0),-1)

        cv2.line(img,(pixelX,pixelY),(pixelX2,pixelY2),color=(0,0,0),thickness=2)
        cv2.rectangle(img,(pixelX6,pixelY6),(pixelX5,pixelY4),color=(0,0,255),thickness=2)                
        #mp_drawing.draw_detection(img,result)
    cv2.imshow("people",img)
    cv2.waitKey(0)