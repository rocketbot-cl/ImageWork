# ImageWork
  
Módulo para el manejo de imágenes. Permite fusionar, buscar imagen en imagen, combinar, recortar imágenes y más.  

*Read this in other languages: [English](README.md), [Português](README.pr.md), [Español](README.es.md)*

## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  


## Overview


1. Fusionar imágenes  
Este comando permite fusionar dos imágenes en una sola, la segunda imagen se superpone a la primera en las coordenadas indicadas. La ruta del archivo resultante será la misma de la primer imagen

2. Convertir a PDF  
Convierte archivos de imágenes de una carpeta a PDF

3. Buscar imagen en imagen  
Este comando busca si la imagen 1 contiene la imagen 2 dentro y devuelve True o False dependiendo del resultado

4. Extraer texto  
Extrae el texto de un área específica de una imagen

5. Recortar imagen  
Corta una imagen desde coordenadas

6. Combinar imágenes  
Combina dos imágenes en una sola manteniendo el tamaño de cada imagen. Puede combinarse horizontal o verticalmente

7. Comparar similitudes entre imágenes  
Compara una imagen con una carpeta de imágenes y devuelve el porcentaje de similitud entre ellas.  



----
### OS

- windows

### Dependencies
- [**Pillow**](https://pypi.org/project/Pillow/)
### License
  
![MIT](https://camo.githubusercontent.com/107590fac8cbd65071396bb4d04040f76cde5bde/687474703a2f2f696d672e736869656c64732e696f2f3a6c6963656e73652d6d69742d626c75652e7376673f7374796c653d666c61742d737175617265)  
[MIT](http://opensource.org/licenses/mit-license.ph)