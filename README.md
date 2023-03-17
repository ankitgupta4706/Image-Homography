# Image-Homography

Image Homography is a fundamental concept in computer vision and image processing that refers to the geometric transformation of a 2D image onto another 2D image plane. This transformation is particularly useful for image registration, object tracking, image stitching, and perspective correction.

Homography is a mathematical transformation that relates the corresponding points between two images captured from different viewpoints or with different camera orientations. It allows the transformation of image features, such as points, lines, or planes, from one image to another, preserving their geometric relationships.

** Sample Inputs **

<img width="560" alt="Sample Inputs" src="https://user-images.githubusercontent.com/81372735/225910932-c9b1f21c-f0ac-440d-bda7-9cd9b3195f4c.PNG">
** Sample Output **

<img width="338" alt="Sample Output" src="https://user-images.githubusercontent.com/81372735/225911729-378c73cd-6b6d-4633-b0b5-0672410ff184.PNG">

** Steps to use **
- Install feature extractor from https://www.vlfeat.org/applications/apps.html, required for matlab script.
- pip install -requirements.txt
- Open 'Matlab Files' folder run "Extract_SIFT_features.m". It takes input as images fro "Images" folder and returns image features as output and saves them in "Images Features" Folder.
- Open 'Python Files' folder run "Calculate_Hmatrix.py". It takes input as feature vectors and returns H matrices as outputs and saves them in "H matrix" Folder.
- run "Generate Images.py" . It takes input as H matrices and returns warped images w.r.t image03 coordinate (reference frame) as outputs and saves them in "Output" Folder.
- run "Final_blend.py or Final_wo_blend.py".It takes canvases as inputs and returns blended images/ without blended images and saves them in "Output" Folder.

