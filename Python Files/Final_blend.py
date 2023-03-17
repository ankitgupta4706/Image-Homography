import numpy as np
import scipy.io
import skimage.io
import skimage.color
from scipy import ndimage
from matplotlib import pyplot as plt
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
from scipy import interpolate
import cv2

#extracted_folder_path="D:/IISc/second sem/CV"
extracted_folder_path="Enter the path to extracted folder"

image_path1 = extracted_folder_path+"/Assignment-2/My_Dataset/Output/c13.jpg"
image_path2 = extracted_folder_path+"/Assignment-2/My_Dataset/Output/c23.jpg"
image_path3 = extracted_folder_path+"/Assignment-2/My_Dataset/Output/c33.jpg"
image_path4 = extracted_folder_path+"/Assignment-2/My_Dataset/Output/c34.jpg"
image_path5 = extracted_folder_path+"/Assignment-2/My_Dataset/Output/c35.jpg"

image1 = skimage.io.imread(image_path1)
image2 = skimage.io.imread(image_path2)
image3 = skimage.io.imread(image_path3)
image4 = skimage.io.imread(image_path4)
image5 = skimage.io.imread(image_path5)

image1 = image1/255
image2 = image2/255
image3 = image3/255
image4 = image4/255
image5 = image5/255

image1[image1<0.2]=0
image2[image2<0.2]=0
image3[image3<0.2]=0
image4[image4<0.2]=0
image5[image5<0.2]=0

final=np.zeros(shape=image1.shape)
a,b,c=image1.shape

for ch in range(3):
    for i in range(a):
        for j in range(b):
            if image1[i][j][ch]>0:
                i1=1
            else:
                i1=0
            if image2[i][j][ch]>0:
                i2=1
            else:
                i2=0            
            if image3[i][j][ch]>0:
                i3=1
            else:
                i3=0
            if image4[i][j][ch]>0:
                i4=1
            else:
                i4=0
            if image5[i][j][ch]>0:
                i5=1
            else:
                i5=0 
            num=0.2*(image1[i][j][ch]+image2[i][j][ch]+image3[i][j][ch]+image4[i][j][ch]+image5[i][j][ch])
            den=0.2*(i1+i2+i3+i4+i5)
            if den!=0:
                final[i][j][ch]=num/den  
plt.imsave(extracted_folder_path+"/Assignment-2/My_Dataset/Output/Final_blend.jpg",final)
