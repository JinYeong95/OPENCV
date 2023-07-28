import cv2
import numpy as np

img1 = np.empty((240, 320), dtype=np.uint8) # 이상한 값을 넣어준다
img2 = np.zeros((240, 320, 3), dtype=np.uint8) # 비었다, 검은색 화면만 보여줄 것
img3 = np.ones((240, 320), dtype=np.uint8) * 120 # 240*320 짜리를 회색으로 만들겠다(120,120,120인거같은데)
img4 = np.full((240, 320, 3), (255, 102, 255), dtype=np.uint8)


cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.imshow('img4', img4)
cv2.waitKey()