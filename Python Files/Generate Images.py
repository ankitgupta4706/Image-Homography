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

image_path=extracted_folder_path+'/Assignment-2/My_Dataset/Images'
H_matrix_path=extracted_folder_path+'/Assignment-2/My_Dataset/H matrices'
output_path=extracted_folder_path+'/Assignment-2/My_Dataset/Output'

image_path1 = image_path+"/image01.jpg"
image_path2 = image_path+"/image02.jpg"
image_path3 = image_path+"/image03.jpg"
image_path4 = image_path+"/image04.jpg"
image_path5 = image_path+"/image05.jpg"

image1 = skimage.io.imread(image_path1)
image2 = skimage.io.imread(image_path2)
image3 = skimage.io.imread(image_path3)
image4 = skimage.io.imread(image_path4)
image5 = skimage.io.imread(image_path5)

ya,xb,c=image3.shape

H13=np.load(H_matrix_path+"/H13.npy")
H23=np.load(H_matrix_path+"/H23.npy")
H34=np.load(H_matrix_path+"/H34.npy")
H35=np.load(H_matrix_path+"/H35.npy")


x = np.arange(xb)
y = np.arange(ya)
z1=image1
z2=image2
z4=image4
z5=image5
f1R = interpolate.interp2d(x, y, z1[:,:,0], kind='cubic')
f1Y = interpolate.interp2d(x, y, z1[:,:,1], kind='cubic')
f1B = interpolate.interp2d(x, y, z1[:,:,2], kind='cubic')

f2R = interpolate.interp2d(x, y, z2[:,:,0], kind='cubic')
f2Y = interpolate.interp2d(x, y, z2[:,:,1], kind='cubic')
f2B = interpolate.interp2d(x, y, z2[:,:,2], kind='cubic')

f4R = interpolate.interp2d(x, y, z4[:,:,0], kind='cubic')
f4Y = interpolate.interp2d(x, y, z4[:,:,1], kind='cubic')
f4B = interpolate.interp2d(x, y, z4[:,:,2], kind='cubic')


f5R = interpolate.interp2d(x, y, z5[:,:,0], kind='cubic')
f5Y = interpolate.interp2d(x, y, z5[:,:,1], kind='cubic')
f5B = interpolate.interp2d(x, y, z5[:,:,2], kind='cubic')


inv34=np.linalg.inv(H34)
inv35=np.linalg.inv(H35)


canvas33=np.zeros(shape=(900,1000,3))
canvas33[200:200+ya,300:300+xb,:]=image3

canvas13=np.zeros(shape=(900,1000,3))
canvas23=np.zeros(shape=(900,1000,3))
canvas34=np.zeros(shape=(900,1000,3))
canvas35=np.zeros(shape=(900,1000,3))

for i in range(-200,699):
    print(i)
    for j in range(-300,699):
        temp=np.array([j,i,1]).reshape(3,1)        
        coo23= H23 @ temp
        coo23=coo23/(coo23[2][0])

        coo13= H13 @ temp
        coo13= coo13/(coo13[2][0])
        
        if coo23[0][0]<xb and coo23[0][0]>0 and coo23[1][0]<ya and coo23[1][0]>0:
            canvas23[i+200][j+300][0]=f2R(coo23[0][0],coo23[1][0])
            canvas23[i+200][j+300][1]=f2Y(coo23[0][0],coo23[1][0])
            canvas23[i+200][j+300][2]=f2B(coo23[0][0],coo23[1][0])
            

        if coo13[0][0]<xb and coo13[0][0]>0 and coo13[1][0]<ya and coo13[1][0]>0:

            canvas13[i+200][j+300][0]=f1R(coo13[0][0],coo13[1][0])
            canvas13[i+200][j+300][1]=f1Y(coo13[0][0],coo13[1][0])
            canvas13[i+200][j+300][2]=f1B(coo13[0][0],coo13[1][0])
        
        coo34= inv34 @ temp
        coo34=coo34/(coo34[2][0])

        coo35= inv35 @ temp
        coo35=coo35/(coo35[2][0])
        
        if coo34[0][0]<xb and coo34[0][0]>0 and coo34[1][0]<ya and coo34[1][0]>0:
            canvas34[i+200][j+300][0]=f4R(coo34[0][0],coo34[1][0])
            canvas34[i+200][j+300][1]=f4Y(coo34[0][0],coo34[1][0])
            canvas34[i+200][j+300][2]=f4B(coo34[0][0],coo34[1][0])

        if coo35[0][0]<xb and coo35[0][0]>0 and coo35[1][0]<ya and coo35[1][0]>0:
            canvas35[i+200][j+300][0]=f5R(coo35[0][0],coo35[1][0])
            canvas35[i+200][j+300][1]=f5Y(coo35[0][0],coo35[1][0])
            canvas35[i+200][j+300][2]=f5B(coo35[0][0],coo35[1][0])



canvas13[canvas13<0]=0
canvas23[canvas23<0]=0
canvas33[canvas33<0]=0
canvas34[canvas34<0]=0
canvas35[canvas35<0]=0

canvas13=canvas13/np.max(canvas13)
canvas23=canvas23/np.max(canvas23)
canvas33=canvas33/np.max(canvas33)
canvas34=canvas34/np.max(canvas34)
canvas35=canvas35/np.max(canvas35)

plt.imsave(output_path+"/c13.jpg",canvas13)
plt.imsave(output_path+"/c23.jpg",canvas23)
plt.imsave(output_path+"/c33.jpg",canvas33)
plt.imsave(output_path+"/c34.jpg",canvas34)
plt.imsave(output_path+"/c35.jpg",canvas35)
      
        

