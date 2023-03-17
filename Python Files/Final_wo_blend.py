# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 17:14:43 2021

@author: ankit
"""
import numpy as np
import scipy.io
import skimage.io
import skimage.color
from scipy import ndimage
from matplotlib import pyplot as plt
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
from scipy import interpolate


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

image1[image1<0.1]=0
image2[image2<0.1]=0
image3[image3<0.1]=0
image4[image4<0.1]=0
image5[image5<0.1]=0

blend23=np.where(image3[:,:,0]>0,image3[:,:,0],image2[:,:,0])
blend234=np.where(blend23>0,blend23,image4[:,:,0])
blend2345=np.where(blend234>0,blend234,image5[:,:,0])
blend12345R=np.where(blend2345>0,blend2345,image1[:,:,0])

blend23=np.where(image3[:,:,1]>0,image3[:,:,1],image2[:,:,1])
blend234=np.where(blend23>0,blend23,image4[:,:,1])
blend2345=np.where(blend234>0,blend234,image5[:,:,1])
blend12345Y=np.where(blend2345>0,blend2345,image1[:,:,1])

blend23=np.where(image3[:,:,2]>0,image3[:,:,2],image2[:,:,2])
blend234=np.where(blend23>0,blend23,image4[:,:,2])
blend2345=np.where(blend234>0,blend234,image5[:,:,2])
blend12345B=np.where(blend2345>0,blend2345,image1[:,:,2])

final=np.dstack([blend12345R,blend12345Y,blend12345B])

plt.imsave(extracted_folder_path+"/Assignment-2/My_Dataset/Output/Final_wo_blend.jpg",final)


