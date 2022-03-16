import cv2

cap = cv2.VideoCapture("Resources/test_video.mp4")

while True:
    succes, img = cap.read()
    cv2.imshow("video", img)
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break