import cv2 as cv
import sys
import numpy as np

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Camera Open Failed!")
    sys.exit()

width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv.CAP_PROP_FPS)

four_cc = cv.VideoWriter_fourcc(*'DIVX')
wait_msec = int(1000 / fps)

out = cv.VideoWriter('Recording.avi', four_cc, fps, (width, height))
recording = False
flip = False

if not out.isOpened():
    print('File open failed')
    cap.release()
    sys.exit()

while True:
    valid, frame = cap.read()
    key = cv.waitKey(wait_msec)
    # waitKey의 return값은 ASCII코드의 값이므로 정수임! 따라서 키 입력 받을때 ord()함수를 활용해야 정상 작동!

    if not valid:
        print("Error occurred")
        break

    if recording:
        # record 화면에 표시
        out.write(frame)
        cv.circle(frame, (100, 15), radius=10, color=(0, 0, 255), thickness=-1)
        cv.putText(frame, 'Recording', (10, 20), cv.FONT_HERSHEY_DUPLEX, 0.5, color=(0, 0, 255))
    else:
        # introduction 화면에 표시 (메인화면)
        cv.putText(frame, 'Press Space to start recording', (80, 50), cv.FONT_HERSHEY_TRIPLEX, 0.5, color=(0, 0, 0), thickness = 2)
        cv.putText(frame, 'Press M to change the mode', (80, 70), cv.FONT_HERSHEY_TRIPLEX, 0.5, color=(0, 0, 0), thickness = 2)
    
    if flip:
        frame = cv.bitwise_not(frame)

    cv.imshow('Camcorder', frame)

    if key == ord(' '):
        if not recording:
            # record 모드 돌입
            recording = True
        
            continue
        else:
            # preview 모드 돌입
            recording = False
            continue
    
    elif key == ord('m') or key == ord('M'):
        if not flip:
            flip = True
            continue
        else:
            flip = False
            continue

    
    elif key == 27:
        break



cap.release()
out.release()
cv.destroyAllWindows()
