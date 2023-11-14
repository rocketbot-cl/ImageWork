# ImageWork
  
Módulo para o gerenciamento de imagens. Permite mesclar, pesquisar imagem em imagem, combinar, cortar imagens e muito mais.  

*Read this in other languages: [English](README.md), [Português](README.pr.md), [Español](README.es.md)*

## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  


## Overview


1. Mesclar imagens  
Esse comando permite mesclar duas imagens em uma; a segunda imagem é sobreposta à primeira nas coordenadas especificadas. O caminho do arquivo resultante será o mesmo da primeira imagem

2. Converter para PDF  
Converter arquivos JPG para PDF

3. Buscar imagem em imagem  
Este comando procura se a imagem 1 contém a imagem 2 dentro e retorna True ou False dependendo do resultado

4. Extrair texto  
Extrair texto de uma área específica de uma imagem

5. Recortar imagem  
Corta uma imagem a partir de coordenadas

6. Combine imagens  
Combina duas imagens em uma mantendo o tamanho de cada imagem. Pode ser combinado horizontal ou verticalmente

7. Comparar semelhanças entre imagens  
Compara uma imagem com uma pasta de imagens e retorna a porcentagem de semelhança entre elas.  



----
### OS

- windows

### Dependencies
- [**Pillow**](https://pypi.org/project/Pillow/)
### License
  
![MIT](https://camo.githubusercontent.com/107590fac8cbd65071396bb4d04040f76cde5bde/687474703a2f2f696d672e736869656c64732e696f2f3a6c6963656e73652d6d69742d626c75652e7376673f7374796c653d666c61742d737175617265)  
[MIT](http://opensource.org/licenses/mit-license.ph)