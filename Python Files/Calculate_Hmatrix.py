import numpy as np
import scipy.io
import skimage.io
import skimage.color
from scipy import ndimage
from matplotlib import pyplot as plt
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
from scipy import interpolate

extracted_folder_path="D:/IISc/second sem/CV"
#extracted_folder_path="Enter the path to extracted folder"

def swap(arr):
    temp=arr.copy()    
    temp[0]=arr[1]
    temp[1]=arr[0]
    return temp


def build_Arow(coo1,coo2):
    temp=np.array([[-coo2[0],-coo2[1],-1,0,0,0,coo2[0]*coo1[0],coo2[1]*coo1[0], coo1[0]],
                   [0,0,0,-coo2[0],-coo2[1],-1,coo2[0]*coo1[1],coo2[1]*coo1[1], coo1[1]]])
    return temp


def calc_H(f1,f2,matches,trials,threshold):
    mean1=np.mean(f1,axis=1)
    mean2=np.mean(f2,axis=1)
    
    norm1=np.linalg.norm(f1[0:2,:],axis=0)
    norm2=np.linalg.norm(f2[0:2,:],axis=0)
    
    cov1=np.mean(norm1)
    cov2=np.mean(norm2)
    
    mean_matrix1=np.array([[1,0,-mean1[0]],
                           [0,1,-mean1[1]],
                           [0,0,       1]])
    mean_matrix2=np.array([[1,0,-mean2[0]],
                           [0,1,-mean2[1]],
                           [0,0,       1]])
    cov_matrix1=np.array([[(np.sqrt(2)/cov1),    0,          0],
                          [0,        (1.414/cov1),      0],
                          [0,           0,              1]])
    cov_matrix2=np.array([[(np.sqrt(2)/cov2),    0,          0],
                          [0,        (1.414/cov2),      0],
                          [0,           0,              1]])   
    
    T1=cov_matrix1 @ mean_matrix1
    T2=cov_matrix2 @ mean_matrix2
    
    f1_mod=T1 @ f1
    f2_mod=T2 @ f2
    
    f1_mod=f1_mod/f1_mod[2]     #scaling to get a proper homographic form
    f2_mod=f2_mod/f2_mod[2]

    a,l=matches.shape

    count_max=0
    h_max=0
    for _ in range(trials):
        rand_index = np.random.randint(l,size=4)
        index       =matches.T[rand_index].astype('int32')

        first       =build_Arow(f1_mod[:,index[0][0]],f2_mod[:,index[0][1]])
        second      =build_Arow(f1_mod[:,index[1][0]],f2_mod[:,index[1][1]])
        third       =build_Arow(f1_mod[:,index[2][0]],f2_mod[:,index[2][1]])
        fourth      =build_Arow(f1_mod[:,index[3][0]],f2_mod[:,index[3][1]])
        A=np.concatenate((first,second,third,fourth),axis=0)
        ATA= A.T @ A
        vec1,sin,vec2=np.linalg.svd(ATA)
        print(np.linalg.cond(ATA))
        h=vec1[:,-1]
        count=0
        for i in range(l):           
            indi=matches.T[i].astype('int32')
            build=build_Arow(f1_mod[:,indi[0]],f2_mod[:,indi[1]])
            check= build @ h
            
            if abs(check[0])<threshold and abs(check[1])<threshold:
                count+=1
        if count>count_max:
            count_max=count
            h_max=h
    h_max=h_max/h_max[-1]
    h_max=h_max.reshape(3,3)
    H_max=(np.linalg.inv(T1) @ h_max @ T2)
    return H_max,count_max        




path=extracted_folder_path+"/Assignment-2/My_Dataset/Image Features"

f1=scipy.io.loadmat(path+"/f1.mat")["f1"][0:3,:]
f2=scipy.io.loadmat(path+"/f2.mat")["f2"][0:3,:]
f3=scipy.io.loadmat(path+"/f3.mat")["f3"][0:3,:]
f4=scipy.io.loadmat(path+"/f4.mat")["f4"][0:3,:]
f5=scipy.io.loadmat(path+"/f5.mat")["f5"][0:3,:]


f1[2]=1
f2[2]=1
f3[2]=1
f4[2]=1
f5[2]=1

i13_matches=scipy.io.loadmat(path+"/i13_matches.mat")["matches13"]
i13_matches=i13_matches-np.ones(shape=(2,1))


i23_matches=scipy.io.loadmat(path+"/i23_matches.mat")["matches23"]
i23_matches=i23_matches-np.ones(shape=(2,1))


i34_matches=scipy.io.loadmat(path+"/i34_matches.mat")["matches34"]
i34_matches=i34_matches-np.ones(shape=(2,1))


i35_matches=scipy.io.loadmat(path+"/i35_matches.mat")["matches35"]
i35_matches=i35_matches-np.ones(shape=(2,1))

H13,count_max=calc_H(f1,f3,i13_matches,trials=500,threshold=0.0005)
H23,count_max=calc_H(f2,f3,i23_matches,trials=500,threshold=0.0005)
H34,count_max=calc_H(f3,f4,i34_matches,trials=500,threshold=0.0005)
H35,count_max=calc_H(f3,f5,i35_matches,trials=500,threshold=0.0005)

np.save(extracted_folder_path+"/Assignment-2/My_Dataset/H matrices/H13.npy",H13)
np.save(extracted_folder_path+"/Assignment-2/My_Dataset/H matrices/H23.npy",H23)
np.save(extracted_folder_path+"/Assignment-2/My_Dataset/H matrices/H34.npy",H34)
np.save(extracted_folder_path+"/Assignment-2/My_Dataset/H matrices/H35.npy",H35)




