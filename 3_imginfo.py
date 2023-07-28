import cv2

img_gray = cv2.imread('./dog.bmp', cv2.IMREAD_GRAYSCALE)
print('img1 type: ', type(img_gray))
print('img1 shape: ', img_gray.shape) # (364, 548) / opencv는 특이하게 height가 먼저임 :: (h, w) 순
print('img1 dtype: ', img_gray.dtype)

img_color = cv2.imread('./dog.bmp')
print('img_color type: ', type(img_color))
print('img_color shape: ', img_color.shape)

# img_color의 가로*세로 사이즈를 화면에 프린트 찍어보기
# 548 * 364
# print('img_color shape: ',(img_gray.shape[1], img_gray.shape[0])) // 내가 한것이다

h, w = img_color.shape[:2]
print(f'img_color 사이즈 : {w} * {h}')

# 그레이스케일 영상과 컬러 영상을 구별하는 방법
if len(img_gray.shape) == 2:  # 3이면 컬러라
    print('img_gray는 그레이스케일 영상입니다.')
elif len(img_gray.shape) == 3:
    print('img_gray는 컬러 영상입니다.')

# img_color의 특정 색 정보로 영상을 출력
# (255, 102, 255) = BGR 정보, 이걸로 화면을 다 덮어버려라

# 표준 ! 내가 기억해야 할 것
img_color[:,:] = (255, 102, 255) # 한방에 데이터가 적용되기 때문에 좋다고 함
cv2.imshow('img_color', img_color)
cv2.waitKey()

# for 문을 2바퀴를 돌기 때문에 느릴수 밖에 없음
'''
for x in range(h):
    for y in range(w):
        img_color[x, y] = (255, 102, 255)

cv2.imshow('img_color', img_color)
cv2.waitKey()
'''