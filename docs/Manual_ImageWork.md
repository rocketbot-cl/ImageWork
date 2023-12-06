# ImageWork
  
Module for image management. Allows you to merge, search image in image, combine, crop images and more.  

*Read this in other languages: [English](Manual_ImageWork.md), [Português](Manual_ImageWork.pr.md), [Español](Manual_ImageWork.es.md)*
  
![banner](imgs/Banner_ImageWork.png)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  


## Description of the commands

### Merge images
  
This command allows you to merge two images into one, the second image is superimposed on the first at the indicated coordinates. The path of the resulting file will be the same as the first image
|Parameters|Description|example|
| --- | --- | --- |
|JPG path to merge|Path of the JPG file that will be merged with the second JPG. The resulting image will be saved in the same path as the first JPG.|JPG|
|Second JPG path to merge|Path of the second JPG file that will be merged with the first JPG. The resulting image will be saved in the same path as the first JPG.|JPG|
|coordinates|Coordinates where the second image is superimposed on the first. The format is X, Y.|150, 340|
|Result|Variable where True or False is stored according to the result of the operation||

### Convert to PDF
  
Convert image files from a folder to PDF 
|Parameters|Description|example|
| --- | --- | --- |
|Path of the folder with image files|Folder with image files to convert to PDF|C:/Users/User/Desktop/images_folder|
|Name and path of PDF|Path and name of PDF to create|PDF|
|Result|Variable where True or False is stored according to the result of the operation||

### Search image in image
  
This command searches if image 1 contains image 2 inside and returns True or False depending on the result
|Parameters|Description|example|
| --- | --- | --- |
|Image 1|Image path where to search image 2|image1.JPG|
|Image 2|Image path to be searched in image 1|image2.JPG|
|Minimum similarity|Minimum similarity that should exist between images for it to be taken as valid. Value between 0 and 1|0.9|
|Result|Variable where True or False will be stored depending on the result|result|

### Extract text
  
Extract text from a specific area of an image
|Parameters|Description|example|
| --- | --- | --- |
|JPG path or PDF path |JPG or PDF file path to be processed|JPG or PDF|
|coordinates|Coordinates of the upper left corner of the area to be extracted|150, 340|
|size|Dimensions of the area to be extracted|250x200|
|Page|Page to be read from the PDF||
|Result|Variable where the extracted text is stored||

### Crop image
  
Crop an image from coordinates
|Parameters|Description|example|
| --- | --- | --- |
|Image|Path where the image to crop is located|/path/to/image.png|
|Path and file name JPG|Path and file name of JPG output file|JPG|
|Coordinates|Coordinates of start of cut|x,y|
|Size|Crop dimensions|width, height|

### Combine images
  
Combines two images into one while maintaining the size of each image. It can be combined horizontally or vertically
|Parameters|Description|example|
| --- | --- | --- |
|Image 1|Image 1 to combine. It will be positioned to the left or above image 2 according to the selected orientation|C:/Users/User/desktop/image1.png|
|Image 2|Image 2 to combine. It will be positioned to the right or below image 1 according to the selected orientation|C:/Users/User/desktop/image2.png|
|Orientation|Select the orientation of the resulting image|Horizontal|
|Combined image|Path of the resulting image|C:/Users/User/desktop/combinedImage.png|

### Compare similarities between images
  
Compares an image with a folder of images and returns the percentage of similarity between them.
|Parameters|Description|example|
| --- | --- | --- |
|Image to compare|Image to compare with the images of the selected folder.|C:/Users/User/desktop/image1.png|
|Images folder|Folder with the images to compare with the selected image.|C:/Users/User/desktop/imagesFolder|
|Results folder|Folder where the results of the comparison will be stored.|C:/Users/User/desktop/results|
|Resize size in px|For the command to work correctly, it is necessary to establish a resize size for the images. By default it is 500,500|500,500|
|Result|Variable where the level of matches with each image will be stored|variable|
