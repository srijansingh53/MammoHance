import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import glob

from steps import Step

'''Loading files from dataset'''
abnormal_filenames=sorted(glob.glob('dataset/circ-calc/*.pgm'))
normal_filenames=sorted(glob.glob('dataset/normal/*.pgm'))
print(abnormal_filenames)

centre = (525,425)
radius = 33

image = cv2.imread(abnormal_filenames[3],-1)
temp = image.copy()
cv2.circle(temp,centre,26,(0,0,255),1)
cv2.imshow('roi', temp)
cv2.waitKey(0)

image_zoomed = image.copy()
image_zoomed = image_zoomed[centre[1]-radius:centre[1]+radius,centre[0]-radius:centre[0]+radius]
image_zoomed = cv2.resize(image_zoomed,(200,200), interpolation = cv2.INTER_LINEAR)

enhanced = cv2.imread('outputs/enhanced.jpg',-1)
enhanced_zoomed = enhanced.copy()
enhanced_zoomed = enhanced_zoomed[centre[1]-radius:centre[1]+radius,centre[0]-radius:centre[0]+radius]
enhanced_zoomed = cv2.resize(enhanced_zoomed,(200,200), interpolation = cv2.INTER_LINEAR)
# print(enhanced_zoomed.shape)

fig, axs = plt.subplots(1, 2)
axs[0].set_title('Original')
axs[0].imshow(image_zoomed,cmap='gray')

axs[1].set_title('Enhanced')
axs[1].imshow(enhanced_zoomed,cmap='gray')
fig.savefig('outputs/zoomed_result.png')
plt.show()
