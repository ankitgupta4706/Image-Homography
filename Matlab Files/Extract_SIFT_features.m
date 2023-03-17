%Please paste the path to the extracted Folder
directory_path='Enter_here';
%directory_path='D:\IISc\second sem\CV';
change_path=strcat(directory_path,'\Assignment-2\My_Dataset\Images');
cd (change_path)


%image03 has been chosen as reference
image1=imread('image01.jpg');
image2=imread('image02.jpg');
image3=imread('image03.jpg');
image4=imread('image04.jpg');
image5=imread('image05.jpg');

%converting the images into grayscale format
image1_gray = single(rgb2gray(image1));
image2_gray = single(rgb2gray(image2));
image3_gray = single(rgb2gray(image3));
image4_gray = single(rgb2gray(image4));
image5_gray = single(rgb2gray(image5));

%getting the feature vectors out of every image
[f1, d1] = vl_sift(image1_gray);
[f2, d2] = vl_sift(image2_gray);
[f3, d3] = vl_sift(image3_gray);
[f4, d4] = vl_sift(image4_gray);
[f5, d5] = vl_sift(image5_gray);

%getting the matching features between image3 and other images
[matches13, scores13]= vl_ubcmatch(d1, d3);
[matches23, scores23]= vl_ubcmatch(d2, d3);
[matches34, scores34]= vl_ubcmatch(d3, d4);
[matches35, scores35]= vl_ubcmatch(d3, d5);

%saving the files
save_path=strcat(directory_path,'\Assignment-2\My_Dataset\Image Features');

save(strcat(save_path,'\f1.mat'),'f1')
save(strcat(save_path,'\f2.mat'),'f2')
save(strcat(save_path,'\f3.mat'),'f3')
save(strcat(save_path,'\f4.mat'),'f4')
save(strcat(save_path,'\f5.mat'),'f5')
save(strcat(save_path,'\i13_matches.mat'),'matches13')
save(strcat(save_path,'\i23_matches.mat'),'matches23')
save(strcat(save_path,'\i34_matches.mat'),'matches34')
save(strcat(save_path,'\i35_matches.mat'),'matches35')

