import logistic
import histogram
import cv2
import numpy as np
import rsa
import pywt
path=raw_input("Enter the path of the watermark: ")
x0=input("Enter the value of X(0) between 0 and 1: ")
u=input("Enter the value of u between 3.5699456 and 4: ")

#sending scrambling parameters for RSA
s=str(x0)+','+str(u)
rsa.encrypt(s)
 
img=cv2.imread(path,0)
histogram.get_histogram(path,'histogram/watermark.png')
h,w = np.shape(img)

#generating array of pseudo-random numbers using CLM
x=logistic.get_x_array(x0,u,h)

#scrambling
c=0
for py in range(0,h):
    for px in range(0,w):
        img[py][px]=(img[py][px]^x[c])%256
        c=c+1
cv2.imwrite('images/scrambled_watermark.jpg',img)
histogram.get_histogram('images/scrambled_watermark.jpg','histogram/scrambled_watermark.jpg')
#DWT
hpath=raw_input("Enter the path of the host image: ")
img = cv2.imread(hpath,0)
histogram.get_histogram(hpath,'histogram/host_image_watermark.jpg')
#Finding components
Coefficients = pywt.wavedec2(img, wavelet='haar', level=1)
shape_LL = Coefficients[0].shape #Coefficients[0] is LL

#SVD
Uc, Sc, Vc = np.linalg.svd(Coefficients[0])
W= cv2.imread('images/scrambled_watermark.jpg',0)

#converting 1-d Sc to diagonal matrix
SLL = np.zeros(shape_LL)
row = min(shape_LL)
SLL[:row, :row] = np.diag(Sc)
Sc=SLL

#adding watermark
alpha=0.1
Snew=np.zeros((min(shape_LL),min(shape_LL)))
for py in range(0,min(shape_LL)):
    for px in range(0,min(shape_LL)):
        Snew[py][px]=Sc[py][px]+alpha*(W[py][px])
        
#SVD again
Uw, Sw, Vw = np.linalg.svd(Snew)

LLnew=np.zeros((min(SLL.shape),min(SLL.shape)))
LLnew=Uc.dot(np.diag(Sw)).dot(Vc)

Coefficients[0]=LLnew
i=pywt.waverec2(Coefficients, 'haar')
cv2.imwrite('images/watermarked_image.jpg',i)
histogram.get_histogram('images/watermarked_image.jpg','histogram/watermarked_image.jpg')

###################extraction#######################

xyz=raw_input("Press Enter to start extraction")
path=raw_input("Enter the path of original host image: ")
oimg=cv2.imread(path,0)
path2="images/watermarked_image.jpg"
wimg=cv2.imread(path2,0)


#DWT
C = pywt.wavedec2(oimg, wavelet='haar', level=1)
shape_LL = C[0].shape #C[0] is LL
Cw= pywt.wavedec2(wimg, wavelet='haar', level=1)

#SVD
Ucw, Scw, Vcw = np.linalg.svd(Cw[0])
Uc, Sc, Vc = np.linalg.svd(C[0])

Uw, Sw, Vw = np.linalg.svd(Snew)
LLnew1=Uw.dot(np.diag(Scw)).dot(Vw)


Wdnew=np.zeros((min(shape_LL),min(shape_LL)))

Scdiag = np.zeros(shape_LL)
row = min(shape_LL)
Scdiag[:row, :row] = np.diag(Sc)
Sc=Scdiag


alpha=0.1
for py in range(0,min(shape_LL)):
    for px in range(0,min(shape_LL)):
        Wdnew[py][px]=(LLnew1[py][px]-Sc[py][px])/alpha

cv2.imwrite('images/recovered_watermark.jpg',Wdnew)

with open('rsain.txt') as f:
    content = f.readlines()
content = [int(x.strip()) for x in content]
st=rsa.decrypt(content)
comma=st.find(',')
x0=float(st[0:comma])
u=float(st[comma+1:])

#Unscrambling
x=logistic.get_x_array(x0,u,min(shape_LL)) #generating array of pseudo-random numbers using CLM
img=cv2.imread('images/recovered_watermark.jpg',0)
h,w = np.shape(img)
c=0
for py in range(0,h):
    
    for px in range(0,w):
        img[py][px]=(img[py][px]^x[c])%256
        c=c+1
cv2.imwrite('images/unscrambled_watermark.jpg',img)
histogram.get_histogram('images/unscrambled_watermark.jpg','histogram/unscrambled_watermark.jpg')


