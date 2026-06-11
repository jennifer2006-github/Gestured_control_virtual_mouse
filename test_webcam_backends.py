#!/usr/bin/env python3
"""
Webcam test with multiple backend attempts
"""
import cv2
import time

print("Webcam Test with Backend Options")
print("=" * 60)

# Try different camera indices and backends
backends = [
    (0, "Default (0)"),
    (1, "Alternative (1)"),
]

for camera_idx, desc in backends:
    print(f"\nTrying camera {desc}...")
    
    # Try with different backends
    cap = cv2.VideoCapture(camera_idx, cv2.CAP_DSHOW)  # DirectShow backend for Windows
    
    if not cap.isOpened():
        print(f"  ✗ Failed with DirectShow")
        cap = cv2.VideoCapture(camera_idx)  # Try default
        if not cap.isOpened():
            print(f"  ✗ Failed with default backend")
            continue
    
    print(f"  ✓ Camera opened")
    
    # Set camera properties
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)  # Use single buffer to reduce latency
    cap.set(cv2.CAP_PROP_FPS, 30)
    
    # Try to read frames
    success = False
    for attempt in range(5):
        ret, frame = cap.read()
        if ret:
            success = True
            print(f"  ✓ Successfully read frame on attempt {attempt + 1}")
            print(f"  ✓ Frame shape: {frame.shape}")
            break
        else:
            print(f"  ✗ Attempt {attempt + 1} failed")
            time.sleep(0.1)
    
    if success:
        print(f"  ✓ Camera {desc} is working!")
        print("\n" + "=" * 60)
        print("Displaying webcam feed (press Q to stop, or wait 15 seconds)...")
        print("=" * 60 + "\n")
        
        frame_count = 0
        start_time = time.time()
        
        try:
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                
                frame_count += 1
                
                # Add text
                cv2.putText(frame, f'Frame: {frame_count}', (10, 30),
                           cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                cv2.putText(frame, 'Press Q to quit', (10, 70),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                
                # Display
                cv2.imshow('Webcam', frame)
                
                key = cv2.waitKey(1) & 0xFF
                if key == ord('q') or key == 27:
                    break
                
                if time.time() - start_time > 15:
                    break
        finally:
            cap.release()
            cv2.destroyAllWindows()
        
        print(f"\n✓ Displayed {frame_count} frames")
        break
    
    cap.release()

print("Test complete!")
