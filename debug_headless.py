#!/usr/bin/env python3
"""
Headless test version of Gesture Controller - outputs to terminal instead of display
"""
import sys
sys.path.insert(0, '.')

from Gesture_Controller import GestureController
import cv2

# Patch to disable display
original_imshow = cv2.imshow
frame_count = 0

def no_display_imshow(window_name, image):
    """Skip actual display, just count frames"""
    global frame_count
    frame_count += 1
    if frame_count % 30 == 0:
        print(f"[Frame {frame_count}] Processing gestures...", flush=True)

cv2.imshow = no_display_imshow

# Run the gesture controller
print("Starting Gesture Controller (headless mode - no window display)")
print("This will process video from your camera and output status to this terminal")
print("Press Ctrl+C to stop")
print("-" * 60)

try:
    gc1 = GestureController()
    gc1.start()
except KeyboardInterrupt:
    print("\nGesture Controller stopped by user")
except Exception as e:
    print(f"\nError: {e}")
    import traceback
    traceback.print_exc()
