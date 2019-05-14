import cv2
import numpy as np
import math
def psnr(path1, path2):
    """ Compute Peak Signal-to-Noise Ratio """
    image1=cv2.imread(path1,0)
    image2=cv2.imread(path2,0)
    image_size = image1.shape[0] * image1.shape[1]
    if np.array_equal(image1, image2):
        return float('inf')
    error = np.sum((image1 - image2) ** 2.0) / image_size
    return 10 * math.log((255.0 ** 2) / error, 10)
path2=raw_input("Enter the path of the host image: ")
path1='images/watermarked_image.jpg'
x=psnr(path1,path2)
print('PSNR between host image and watermarked image')
print(x)

path1=raw_input("Enter the path of the watermark image: ")
path2='images/unscrambled_watermark.jpg'
x=psnr(path1,path2)
print('PSNR between watermark and recovered watermark')
print(x)


