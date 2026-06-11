import os
base_dir = r"c:\Users\admin\Downloads\Gesture-Controlled-Virtual-Mouse-main\Gesture-Controlled-Virtual-Mouse-main\src"
target = os.path.join(base_dir, "Gesture_Controller.py")

with open(target, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_block = """        handmajor = HandRecog(HLabel.MAJOR)
        handminor = HandRecog(HLabel.MINOR)

        with mp_hands.Hands(
            max_num_hands=2,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        ) as hands:

            while GestureController.cap.isOpened() and GestureController.gc_mode:

                success, image = GestureController.cap.read()

                if not success:
                    print("Ignoring empty camera frame")
                    continue

                # Flip camera
                image = cv2.flip(image, 1)

                # Convert BGR to RGB for MediaPipe
                rgb_image = cv2.cvtColor(
                    image,
                    cv2.COLOR_BGR2RGB
                )

                rgb_image.flags.writeable = False

                results = hands.process(rgb_image)

                rgb_image.flags.writeable = True



                if results.multi_hand_landmarks:

                    GestureController.classify_hands(results)


                    handmajor.update_hand_result(
                        GestureController.hr_major
                    )

                    handminor.update_hand_result(
                        GestureController.hr_minor
                    )


                    handmajor.set_finger_state()
                    handminor.set_finger_state()


                    gest_name = handminor.get_gesture()


                    if gest_name == Gest.PINCH_MINOR:

                        Controller.handle_controls(
                            gest_name,
                            handminor.hand_result
                        )

                    else:

                        gest_name = handmajor.get_gesture()

                        Controller.handle_controls(
                            gest_name,
                            handmajor.hand_result
                        )


                    # Draw green hand lines
                    for hand_landmarks in results.multi_hand_landmarks:

                        mp_drawing.draw_landmarks(
                            image,
                            hand_landmarks,
                            mp_hands.HAND_CONNECTIONS
                        )


                else:

                    Controller.prev_hand = None


                # Display webcam
                cv2.imshow(
                    "Gesture Controller",
                    image
                )


                # Press Enter to exit
                if cv2.waitKey(5) & 0xFF == 13:
                    break


        GestureController.cap.release()
        cv2.destroyAllWindows()
"""

# replace lines 768 to 868 with the new_block
new_lines = new_block.split('\n')
new_lines = [line + '\n' for line in new_lines]
# removing the last empty newline from split
if new_lines[-1] == '\n':
    new_lines = new_lines[:-1]

lines[768:869] = new_lines

with open(target, 'w', encoding='utf-8') as f:
    f.writelines(lines)
