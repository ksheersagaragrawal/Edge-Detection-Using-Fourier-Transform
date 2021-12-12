#Importing numpy,cv2 & matplotlib
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Reading image in grayscale
img = cv.imread('lal_minar.jpg',0)

#Frequency transform is a complex array
f = np.fft.fft2(img)

#Shifting the zero frequency component to the center
fshift = np.fft.fftshift(f)

#Finding the magnitude spectrum
A1 = 20;
magnitude_spectrum = A1*np.log(np.abs(fshift))
#Plotting
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()

Page 27

MA201

#Center
rows, cols = img.shape
crow,ccol = rows//2 , cols//2

# HPF masking, center 12X12 grid masked 0, remaining all ones
mask = 12;
fshift[crow-mask:crow+mask, ccol-mask:ccol+mask] = 0

# Finding the magnitude spectrum of masked Fourier Transform
A2 = 2000;
fshift_mask_mag = A2 * np.log(np.abs(fshift))
#Restoring the original indexing
f_ishift = np.fft.ifftshift(fshift)
#Inverse FFT
img_back = np.fft.ifft2(f_ishift)

#Finding the magnitude spectrum
img_back = np.real(img_back)
#Plotting
plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Lal Minar'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(fshift_mask_mag , cmap = 'gray')
plt.title('FFT + Mask'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(img_back, cmap = 'Reds')
plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])
plt.show()