# ImageWork
  
Module for image management. Allows you to merge, search image in image, combine, crop images and more.  

*Read this in other languages: [English](README.md), [Português](README.pr.md), [Español](README.es.md)*

## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  


## Overview


1. Merge images  
This command allows you to merge two images into one, the second image is superimposed on the first at the indicated coordinates. The path of the resulting file will be the same as the first image

2. Convert to PDF  
Convert image files from a folder to PDF 

3. Search image in image  
This command searches if image 1 contains image 2 inside and returns True or False depending on the result

4. Extract text  
Extract text from a specific area of an image

5. Crop image  
Crop an image from coordinates

6. Combine images  
Combines two images into one while maintaining the size of each image. It can be combined horizontally or vertically

7. Compare similarities between images  
Compares an image with a folder of images and returns the percentage of similarity between them.  



----
### OS

- windows

### Dependencies
- [**Pillow**](https://pypi.org/project/Pillow/)
### License
  
![MIT](https://camo.githubusercontent.com/107590fac8cbd65071396bb4d04040f76cde5bde/687474703a2f2f696d672e736869656c64732e696f2f3a6c6963656e73652d6d69742d626c75652e7376673f7374796c653d666c61742d737175617265)  
[MIT](http://opensource.org/licenses/mit-license.ph)