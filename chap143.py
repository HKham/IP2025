import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('dsu6.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
rows,cols,ch = img.shape

pts1 = np.float32([[284,169],[734,241],[289,562],[752,543]])
pts2 = np.float32([[0,0],[424,0],[0,300],[424,300]])

M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(424,300))
dst_rgb = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)

plt.subplot(121),plt.imshow(img_rgb),plt.title('Input')
plt.subplot(122),plt.imshow(dst_rgb),plt.title('Output')
plt.show()
