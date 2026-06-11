import cv2
import sys

print("Testing camera...")
cap = cv2.VideoCapture(0)
print(f"Camera opened: {cap.isOpened()}")

if cap.isOpened():
    ret, frame = cap.read()
    print(f"Frame captured: {ret}")
    if ret:
        print(f"Frame shape: {frame.shape}")
        print(f"Frame type: {type(frame)}")
    else:
        print("Failed to read frame")
    cap.release()
    print("Camera test passed!")
else:
    print("ERROR: Camera not found or not accessible")
    print("Make sure your webcam is connected and not in use by another application")
    sys.exit(1)
