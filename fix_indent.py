import os
base_dir = r"c:\Users\admin\Downloads\Gesture-Controlled-Virtual-Mouse-main\Gesture-Controlled-Virtual-Mouse-main\src"
target = os.path.join(base_dir, "Gesture_Controller.py")

with open(target, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(767, 869):
    if lines[i].strip() != '':
        if not lines[i].startswith('        '):
            lines[i] = '    ' + lines[i]

with open(target, 'w', encoding='utf-8') as f:
    f.writelines(lines)
