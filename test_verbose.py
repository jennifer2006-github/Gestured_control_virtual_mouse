#!/usr/bin/env python3
"""
Test Gesture Controller with verbose debugging output
"""
import sys
import os

print("=" * 70)
print("GESTURE CONTROLLER - VERBOSE TEST")
print("=" * 70)

print("\n[1] Importing modules...")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from Gesture_Controller import GestureController
    print("✓ Import successful")
except Exception as e:
    print(f"✗ Import failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("\n[2] Creating GestureController instance...")
try:
    gc = GestureController()
    print("✓ GestureController created")
except Exception as e:
    print(f"✗ Failed to create GestureController: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("\n[3] Starting gesture detection...")
print("   Press Ctrl+C to stop")
print("-" * 70)
try:
    gc.start()
except KeyboardInterrupt:
    print("\n\n✓ Stopped by user")
except Exception as e:
    print(f"\n✗ Error: {e}")
    import traceback
    traceback.print_exc()

print("-" * 70)
print("Done!")
