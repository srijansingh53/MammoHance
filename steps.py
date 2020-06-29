import cv2
from scipy import ndimage
import numpy as np


class Step():

    def __init__(self,image):
        self.image = image[0:800,250:650]
    
    def First(self, kernel_size, T):
        '''
        This function removes film artifacts that may be seen as noise by averaging the image with a proper sized kernel and a Threshold value. 
        '''
        kernel = np.ones((kernel_size,kernel_size),np.float32)/(kernel_size**2)
        mean = cv2.filter2D(self.image,-1,kernel)
        diff = self.image-mean
        
        S = np.ones((800,400))

        for i in range(self.image.shape[0]):
            for j in range(self.image.shape[1]):
                if diff[i][j]>T:
                    S[i][j]=mean[i][j]
                else:
                    S[i][j]=self.image[i][j]
        return S

    def Second(self, S):
        '''
        This function calculates the Gradient images and the edge binary image
        '''
        S1 = np.array([[-1,-2,-1],[0,0,0],[1,2,1]]) # Horizontal Sobel Operator 
        S2 = np.array([[-1,0,1],[-2,0,2],[-1,0,1]]) # Vertical Sobel Operator 
        S = S.astype(np.uint8)
        G1 = cv2.filter2D(S,-1,S1)
        G2 = cv2.filter2D(S,-1,S2)
        G = G1+G2
        e = np.where(G>=127, 1, 0)

        return G1,G2,e

    def Third(self, S, G1, G2, e, N):
        '''
        This function calculates signal adaptive gain for different Gradient images
        '''
        def std_convoluted(image, N):
            '''
            This function calculates the local standard deviation of the filtered image S
            '''
            im = np.array(image, dtype=float)
            im2 = im**2
            ones = np.ones(im.shape)

            kernel = np.ones((2*N+1, 2*N+1))
            s = ndimage.convolve(im, kernel, mode="nearest")
            s2 = ndimage.convolve(im2, kernel, mode="nearest")
            ns = ndimage.convolve(ones, kernel, mode="nearest")

            return np.sqrt((s2 - s**2 / ns) / ns)


        S_sig = std_convoluted(S,N)
        S_sig_max = np.max(S_sig)

        G1_mean = np.mean(G1)
        G2_mean = np.mean(G2)

        G1_std = np.std(G1)
        G2_std = np.std(G2)

        sig_max = np.maximum(G1_std,G2_std)
        
        '''
        Calculating maximum gain for each pixel of G1
        '''
        g_1_max = np.ones((800,400))

        for i in range(G1.shape[0]):
            for j in range(G1.shape[1]):
                if abs(G1_mean-G1_std)<=G1[i][j] and G1[i][j]>=(G1_mean+G1_std):
                    g_1_max[i][j]=(sig_max/G1_std)+(G1_std/(G1_std+G2_std))
                else:
                    g_1_max[i][j]=sig_max/G1_std

        '''
        Calculating maximum gain for each pixel of G1
        '''
        g_2_max = np.ones((800,400))

        for i in range(G2.shape[0]):
            for j in range(G2.shape[1]):
                if abs(G2_mean-G2_std)<=G2[i][j] and G2[i][j]>=(G2_mean+G2_std):
                    g_2_max[i][j]=(sig_max/G2_std)+(G2_std/(G1_std+G2_std))
                else:
                    g_2_max[i][j]=sig_max/G2_std
        '''
        Calculating signal adaptive gain for G1
        '''
        g_1 = np.ones((800,400))

        for i in range(G1.shape[0]):
            for j in range(G1.shape[1]):
                if e[i][j]==1:
                    g_1[i][j]=-1.0*((g_1_max[i][j]-1)*S_sig[i][j]/S_sig_max)+g_1_max[i][j]
                else:
                    g_1[i][j]=1

        '''
        Calculating signal adaptive gain for G1
        '''
        g_2 = np.ones((800,400))

        for i in range(G2.shape[0]):
            for j in range(G2.shape[1]):
                if e[i][j]==1:
                    g_2[i][j]=-1.0*((g_2_max[i][j]-1)*S_sig[i][j]/S_sig_max)+g_2_max[i][j]
                else:
                    g_2[i][j]=1

        return g_1, g_2