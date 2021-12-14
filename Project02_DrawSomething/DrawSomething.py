%matplotlib inline
 
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import math
 
# 提前设定画布的长宽以及下方文字大概所占的长度
W = 1000
Height = int(1.3 * W)
D = int(0.2 * W)
# O = (int(0.5 * W), int(0.5 * W))

# 放置一个白色底的画布
img = np.zeros((Height, W, 3), np.uint8)
#img[0:Height,0:W] = 255
img[:] = 255
 
# 大圆的半径
A = (int(0.5 * W), int(0.5 * W - D))
B = (int(0.5 * W - math.sqrt(3)/2 * D), int(0.5 * W + 0.5 * D))
C = (int(0.5 * W + math.sqrt(3)/2 * D), int(0.5 * W + 0.5 * D))
R1 = int(math.sqrt(3) * 0.4 * D)
 
# 小圆的半径
R2 = int(math.sqrt(3) * 0.2 * D)
 
# 旋转的角度
ang = 60
 
# 绘制大圆
cv.circle(img, A, R1, (255,0,0), -1)
cv.circle(img, B, R1, (0,255,0), -1)
cv.circle(img, C, R1, (0,0,255), -1)
 
# 绘制小圆
cv.circle(img, A, R2, (255,255,255), -1)
cv.circle(img, B, R2, (255,255,255), -1)
cv.circle(img, C, R2, (255,255,255), -1)
 
# 绘制椭圆形
cv.ellipse(img, A, (R1,R1), ang, 0, ang, (255,255,255), -1)
cv.ellipse(img, B, (R1,R1), 360 - ang, 0, ang, (255,255,255), -1)
cv.ellipse(img, C, (R1,R1), 360 - 2 * ang, 0, ang, (255,255,255), -1)
 
# 绘制文本
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, 'OpenCV', (100,1000), font, 7, (0,0,0), 25)
 
plt.imshow(img)
plt.show()