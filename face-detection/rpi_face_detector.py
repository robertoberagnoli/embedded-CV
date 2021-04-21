#import face_recognition
import subprocess
import cv2
import sys

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades+cascPath)

video_capture = cv2.VideoCapture(0)

while True:
    print("Capture")
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )


   # faces=face_recognition.face_locations(frame)

    # Draw a rectangle around the faces
    for face in faces:
       # cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        print("Trovata")
        video_capture.release()
        subprocess.run(["raspivid","-o","videoTest.h264","-t","10000"])
        video_capture=cv2.VideoCapture(0)
        
    # Display the resulting frame
    #cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
