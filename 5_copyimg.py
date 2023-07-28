import cv2

img_origin = cv2.imread('./dog.bmp')
'''
img_origin = img_origin[91:210, 125:245] # H / W
img_copy = img_origin
# 이러면 같이 잘라진 모습으로 나오게된다
'''
img_copy = img_origin[91:210, 125:245].copy()

cv2.imshow('img_origin', img_origin)
cv2.imshow('img_copy', img_copy)

cv2.waitKey()

# 원본 변형 -> 카피본도 같이 변형 ( 같은 메모리 주소이다 / 객체가)