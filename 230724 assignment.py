import cv2
import numpy as np
import sys

cap1 = cv2.VideoCapture('./hak.mp4')
cap2 = cv2.VideoCapture('./encorewat.mp4')

frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
print(frame_cnt1)
print(frame_cnt2)

fps1 = round(cap1.get(cv2.CAP_PROP_FPS))
fps2 = round(cap2.get(cv2.CAP_PROP_FPS))
print(fps1)
print(fps2)

w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
# print(w)
# print(h)

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('plus.avi', fourcc, fps1, (w, h))

delay = fps1 * 2
print(delay)

for i in range(int(frame_cnt1) - delay):
    ret1, frame1 = cap1.read()
    cv2.imshow('assign', frame1)
    out.write(frame1)
    if cv2.waitKey(10) == 27:
        break

for i, x in zip(range(delay), range(1, w, int(w/delay))):
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    delay_frame = frame1
    delay_frame[:, :x] = frame2[:, :x]

    cv2.imshow('assign', delay_frame)
    out.write(delay_frame)
    if cv2.waitKey(10) == 27:
        break

for i in range(frame_cnt2):
    ret2, frame2 = cap2.read()
    cv2.imshow('assign', frame2)
    out.write(frame2)
    if cv2.waitKey(10) == 27:
        break

cap1.release()
cap2.release()
out.release()