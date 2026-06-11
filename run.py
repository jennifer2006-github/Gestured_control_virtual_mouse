#!/usr/bin/env python3
"""
Gesture Controller - Interactive launcher with display options
"""
import sys
import os

# Add src to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

print("\n" + "=" * 70)
print("GESTURE-CONTROLLED VIRTUAL MOUSE")
print("=" * 70)

print("\nSelect mode:")
print("  1. Display mode (webcam window visible)")
print("  2. Headless mode (process video, output to terminal)")
print("  3. Test webcam only")
print()

choice = input("Enter choice (1-3): ").strip()

if choice == "1":
    print("\n[Starting in Display Mode]")
    print("A webcam window should appear. Press ENTER in the window to exit.")
    print("-" * 70 + "\n")
    from Gesture_Controller import GestureController
    gc = GestureController()
    gc.start()
    
elif choice == "2":
    print("\n[Starting in Headless Mode]")
    print("Video will be processed from your camera.")
    print("Status updates will appear below.")
    print("Press Ctrl+C to stop.")
    print("-" * 70 + "\n")
    
    # Patch cv2.imshow to not display
    import cv2
    frame_count = [0]
    
    def fake_imshow(name, image):
        frame_count[0] += 1
        if frame_count[0] % 30 == 0:
            print(f"✓ Processing frame {frame_count[0]}...")
    
    cv2.imshow = fake_imshow
    
    try:
        from Gesture_Controller import GestureController
        gc = GestureController()
        gc.start()
    except KeyboardInterrupt:
        print("\n✓ Stopped by user")
    
elif choice == "3":
    print("\n[Testing Webcam Only]")
    print("This will test if your webcam is working properly.")
    print("-" * 70 + "\n")
    
    import cv2
    import time
    
    print("Opening camera...")
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    
    if not cap.isOpened():
        print("DirectShow failed, trying default...")
        cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("✗ ERROR: Cannot open webcam")
        print("\nTroubleshooting:")
        print("  1. Check if webcam is connected")
        print("  2. Check if another app is using the camera")
        print("  3. Restart your computer")
        sys.exit(1)
    
    print("✓ Webcam opened successfully")
    
    # Try to read frames
    success_count = 0
    for i in range(10):
        ret, frame = cap.read()
        if ret:
            success_count += 1
            print(f"✓ Read frame {i+1}: {frame.shape}")
        else:
            print(f"✗ Failed to read frame {i+1}")
        time.sleep(0.1)
    
    cap.release()
    
    if success_count > 0:
        print(f"\n✓ Webcam test PASSED ({success_count}/10 frames)")
    else:
        print("\n✗ Webcam test FAILED")
        sys.exit(1)

else:
    print("Invalid choice")
    sys.exit(1)

print("\n" + "=" * 70)
print("Program ended successfully")
print("=" * 70 + "\n")
