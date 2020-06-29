import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import glob

from steps import Step

'''Loading files from dataset'''
abnormal_filenames=sorted(glob.glob('dataset/circ-calc/*.pgm'))
normal_filenames=sorted(glob.glob('dataset/normal/*.pgm'))
# print(abnormal_filenames)
# print(normal_filenames)

image = cv2.imread(normal_filenames[-1],-1) # choose a file you want to apply image processing

kernel_size = 5 # kernel size for averaging
T = 3 # Threshold value for eliminating film artifacts

# Implementing first step
S = Step(image).First(kernel_size, T)
cv2.imwrite('outputs/filtered.jpg', S)
plt.imshow(S,cmap='gray')
plt.show()

# Implementing second step
G1, G2, e = Step(image).Second(S)
G = G1+G2
cv2.imwrite('outputs/gradient.jpg', G)

cv2.imwrite('outputs/hor_gradient.jpg', G1)
plt.imshow(G1,cmap='gray')
cv2.imwrite('outputs/ver_gradient.jpg', G2)
plt.imshow(G2,cmap='gray')
plt.show()

# Implementing third step
N=2 # size of window for local standard deviation
g_1, g_2 = Step(image).Third(S, G1, G2, e, N)

# Final step
S_enhanced = S + np.multiply(g_1,G1) + np.multiply(g_2,G2)

S_enhanced = S_enhanced.astype('uint64')
for i in range(G2.shape[0]):
    for j in range(G2.shape[1]):
        if S_enhanced[i][j]>=255:
            S_enhanced[i][j]=255
fig, axs = plt.subplots(1, 2)

axs[0].set_title('Original Image')
cv2.imwrite('outputs/original.jpg', image[0:800,250:650])
axs[0].imshow(image,cmap='gray')

axs[1].set_title('Enhanced Image')
cv2.imwrite('outputs/enhanced.jpg', S_enhanced)
axs[1].imshow(S_enhanced,cmap='gray')

plt.show()