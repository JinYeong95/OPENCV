import cv2
import sys
import numpy as np

cap = cv2.VideoCapture('./hak.mp4')
cap2 = cv2.VideoCapture('./encorewat.mp4')

frame_cnt1 = round(cap.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
print(frame_cnt1)
print(frame_cnt2)

fps1 = cap.get(cv2.CAP_PROP_FPS)
fps2 = cap2.get(cv2.CAP_PROP_FPS)
print(fps1)
print(fps2)

w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print('w', w)
print('h', h)

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('mix.avi', fourcc, fps1, (w, h))

for i in range(frame_cnt1):
    ret1, frame1 = cap.read()
    cv2.imshow('output', frame1)
    out.write(frame1)
    if cv2.waitKey(10) == 27:
        break

for i in range(frame_cnt2):
    ret2, frame2 = cap2.read()
    cv2.imshow('output', frame2)
    out.write(frame2)
    if cv2.waitKey(10) == 27:
        break

cap.release()
cap2.release()
out.release()


# # 내가 한 것이 아닌 chatgpt로 해버렸다
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         cap.release()
#         break
#
#     cv2.imshow('Video', frame)
#
#     if cv2.waitKey(10) == 27:
#         cap.release()
#         break
#
# while True:
#     ret, frame2 = cap2.read()
#     if not ret:
#         cap2.release()
#         break
#
#     cv2.imshow('Video', frame2)
#
#     if cv2.waitKey(10) == 27:
#         cap2.release()
#         break
#
# cv2.destroyAllWindows()