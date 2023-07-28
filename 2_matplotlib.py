import cv2
import matplotlib.pyplot as plt
'''
img_gray = cv2.imread('dog.bmp', cv2.IMREAD_GRAYSCALE) # 읽어오는데 흑백으로 읽어오겠다
cv2.imshow('img_gray', img_gray)

cv2.waitKey()
'''

'''
img_gray = cv2.imread('./dog.bmp', cv2.IMREAD_GRAYSCALE)
plt.axis('off') # 격자를 없애달라
plt.imshow(img_gray, cmap='gray') # cmap :: gray / color 선택 가능
plt.show()

# matplotlib로 표기

'''

'''
# cv2.IMREAD_COLOR는 생략 가능
img_rgb = cv2.imread('./dog.bmp', cv2.IMREAD_COLOR)
# BGR을 RGB로 변환
img_rgb = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB)
plt.axis('off') # 격자를 없애달라
plt.imshow(img_rgb)
plt.show()
'''

img_gray = cv2.imread('./dog.bmp', cv2.IMREAD_GRAYSCALE)
img_rgb = cv2.imread('./dog.bmp', cv2.IMREAD_COLOR)
img_rgb = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB)

plt.subplot(121) # 1행 2열의 1번째
plt.axis('on') # 이미지 주변의 눈금을 표시
plt.imshow(img_gray, cmap='gray')

plt.subplot(122) # 1행 2열의 2번째
plt.axis('off')
plt.imshow(img_rgb)
plt.show()