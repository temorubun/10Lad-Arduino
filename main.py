import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='google.protobuf')

import inspect

# Patch untuk mendukung Python 3.8 dan seterusnya
if not hasattr(inspect, 'getargspec'):
    inspect.getargspec = inspect.getfullargspec

import cv2
import serial
from cvzone.HandTrackingModule import HandDetector

# Inisialisasi komunikasi serial ke Arduino
ser = serial.Serial('COM11', 9600)
detector = HandDetector(detectionCon=0.8, maxHands=2)
video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    if not ret:
        print("Failed to grab frame")
        break

    frame = cv2.flip(frame, 1)
    hands, img = detector.findHands(frame)

    fingerUp = [0] * 10  # Inisialisasi status jari untuk dua tangan

    if hands:
        for i, hand in enumerate(hands):
            lmList = hand["lmList"]
            hand_fingerUp = detector.fingersUp(hand)
            fingerUp[i*5:(i+1)*5] = hand_fingerUp

        num_fingers = sum(fingerUp)
        ser.write((str(num_fingers) + '\n').encode())  # Mengirim data dengan newline

        cv2.putText(frame, f'Jumlah Jari: {num_fingers}', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)

    cv2.imshow("frame", frame)
    k = cv2.waitKey(1)
    if k == ord("k"):
        break

video.release()
cv2.destroyAllWindows()
ser.close()
