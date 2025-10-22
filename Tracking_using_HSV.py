import cv2
import numpy as np

def nothing(x):
    pass

# Create a window for trackbars
cv2.namedWindow("Trackbars")

# Create trackbars for color change
cv2.createTrackbar("L-H", "Trackbars", 0, 179, nothing)
cv2.createTrackbar("L-S", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L-V", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("U-H", "Trackbars", 179, 179, nothing)
cv2.createTrackbar("U-S", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U-V", "Trackbars", 255, 255, nothing)

# ✅ Set default values **after** creating all trackbars
cv2.setTrackbarPos("L-H", "Trackbars", 100)
cv2.setTrackbarPos("L-S", "Trackbars", 150)
cv2.setTrackbarPos("L-V", "Trackbars", 0)
cv2.setTrackbarPos("U-H", "Trackbars", 140)
cv2.setTrackbarPos("U-S", "Trackbars", 255)
cv2.setTrackbarPos("U-V", "Trackbars", 255)

# Start webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get current positions of all trackbars
    l_h = cv2.getTrackbarPos("L-H", "Trackbars")
    l_s = cv2.getTrackbarPos("L-S", "Trackbars")
    l_v = cv2.getTrackbarPos("L-V", "Trackbars")
    u_h = cv2.getTrackbarPos("U-H", "Trackbars")
    u_s = cv2.getTrackbarPos("U-S", "Trackbars")
    u_v = cv2.getTrackbarPos("U-V", "Trackbars")

    # Create mask
    lower = np.array([l_h, l_s, l_v])
    upper = np.array([u_h, u_s, u_v])
    mask = cv2.inRange(hsv, lower, upper)

    # Apply mask to original image
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Show frames
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    # Exit on ESC key
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
