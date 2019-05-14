import cv2
from matplotlib import pyplot as plt
def get_histogram(x,path):
    img = cv2.imread(x)
    hist = cv2.calcHist([img],[0],None,[256],[0,256])
    plt.plot(hist)
    plt.xlim([0,256])
    plt.savefig(path)
    plt.close()
    
