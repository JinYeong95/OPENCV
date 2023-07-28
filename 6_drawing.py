import cv2
import numpy as np

img = np.full((500, 500, 3), 255, np.uint8) # 500*500 이미지 파일 컬러, 흰색으로 다 채워버리겟다

cv2.line(img, (70, 70), (200, 70), (0, 0, 255), 5) # GBR이라 빨강색, 두께는 5
cv2.rectangle(img, (50, 200, 150, 100), (0, 255, 0), -1) # (x, y, w, h)
cv2.circle(img, (300, 100), 50, (255, 255, 0), -1) # 300*100짜리 원을 반지름 50cm만큼 했음

str = 'Hello OpenCV'
cv2.putText(img, str,( 30, 350), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255)) # 2 : 두께
cv2.imshow('img', img)
cv2.waitKey()