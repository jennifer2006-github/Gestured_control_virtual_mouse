#!/usr/bin/env python3
"""
Simple webcam test - check if camera works and display video
"""
import cv2
import time

print("Testing webcam...")
print("-" * 60)

# Try to open camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("ERROR: Cannot open webcam")
    print("Possible causes:")
    print("  - Webcam not connected")
    print("  - Webcam in use by another application")
    print("  - No camera drivers installed")
    exit(1)

print("✓ Webcam opened successfully")

# Get camera properties
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

print(f"✓ Camera resolution: {width}x{height}")
print(f"✓ Camera FPS: {fps}")
print("-" * 60)

print("Displaying video from webcam...")
print("Press 'q' or ESC to stop, or wait 10 seconds")
print("-" * 60)

frame_count = 0
start_time = time.time()

try:
    while True:
        ret, frame = cap.read()
        
        if not ret:
            print("ERROR: Failed to read frame")
            break
        
        frame_count += 1
        
        # Add text to frame
        cv2.putText(frame, f'Frame: {frame_count}', (10, 30), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(frame, 'Press Q to quit', (10, 70), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        # Show the frame
        cv2.imshow('Webcam Test', frame)
        
        # Check for quit
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q') or key == 27:  # q or ESC
            break
        
        # Auto-exit after 10 seconds
        if time.time() - start_time > 10:
            print("\n10 seconds elapsed, stopping...")
            break
            
except KeyboardInterrupt:
    print("\nStopped by user")
    
finally:
    cap.release()
    cv2.destroyAllWindows()
    print(f"✓ Captured {frame_count} frames successfully")
    print("Webcam test complete!")
