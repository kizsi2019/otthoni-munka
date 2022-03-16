import cv2

cap = cv2.VideoCapture(0)

while True:
    succes, img = cap.read()
    cv2.imshow("Kamera", img)
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break