import cv2
import numpy as np
import matplotlib.pyplot as plt


image = cv2.imread('outputs/original.jpg',-1)
enhanced = cv2.imread('outputs/enhanced.jpg',-1)
img_equ = cv2.equalizeHist(image)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
img_clahe = clahe.apply(image)

fig, axs = plt.subplots(1, 4)
axs[0].set_title('Original')
axs[0].imshow(image,cmap='gray')

axs[1].set_title('Equalized')
axs[1].imshow(img_equ,cmap='gray')

axs[2].set_title('CLAHE')
axs[2].imshow(img_clahe,cmap='gray')

axs[3].set_title('Proposed')
axs[3].imshow(enhanced,cmap='gray')
fig.tight_layout(pad=1.0)
plt.show()
fig.savefig('outputs/comparison.jpg', pad_inches=0.3)