import cv2  # import할때는 cv2, install할때는 opencv-python

# ctrl + shift + f10
print('현재 opencv 버전: ', cv2.__version__)

# 컬러영상(BGR), cv2.IMREAD_GRAYSCALE => 그레이스케일 영상으로 읽어옴

img = cv2.imread('./dog.bmp') # 아무런 옵션을 주지 않으면 컬러영상으로 읽어옴
cv2.imshow('img', img) # 창이름 / 영상 객체
cv2.waitKey() # 이러면 화면이 안꺼지고 보인다 / 아무런 키를 입력시 닫히게 된다