# ImageWork
  
Módulo para o gerenciamento de imagens. Permite mesclar, pesquisar imagem em imagem, combinar, cortar imagens e muito mais.  

*Read this in other languages: [English](Manual_ImageWork.md), [Português](Manual_ImageWork.pr.md), [Español](Manual_ImageWork.es.md)*
  
![banner](imgs/Banner_ImageWork.png o jpg)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  


## Descrição do comando

### Mesclar imagens
  
Esse comando permite mesclar duas imagens em uma; a segunda imagem é sobreposta à primeira nas coordenadas especificadas. O caminho do arquivo resultante será o mesmo da primeira imagem
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Caminho do JPG para mesclar|Caminho do arquivo JPG que será mesclado com o segundo JPG. A imagem resultante será salva no mesmo caminho que o primeiro JPG.|JPG|
|Caminho do segundo JPG para mesclar|Caminho do segundo arquivo JPG que será mesclado com o primeiro JPG. A imagem resultante será salva no mesmo caminho que o primeiro JPG.|JPG|
|Coordenadas|Coordenadas onde a segunda imagem é sobreposta à primeira. O formato é X, Y.|150, 340|
|Resultado|Variável onde True ou False é armazenado de acordo com o resultado da operação||

### Converter para PDF
  
Converter arquivos JPG para PDF
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Caminho da pasta com arquivos JPG|Pasta com arquivos JPG para converter para PDF|JPG|
|Nome e caminho do PDF|Caminho e nome do PDF a criar|PDF|
|Resultado|Variável onde True ou False é armazenado de acordo com o resultado da operação||

### Buscar imagem em imagem
  
Este comando procura se a imagem 1 contém a imagem 2 dentro e retorna True ou False dependendo do resultado
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Image 1|Caminho da imagem onde procurar a imagem 2|image1.JPG|
|Image 2|Caminho da imagem a ser pesquisada na imagem 1|image2.JPG|
|Mínimo de similaridade|Mínima similaridade que deve existir entre imagens para que seja considerada válida. Valor entre 0 e 1|0.9|
|Resultado|Variável onde True ou False será armazenado dependendo do resultado|result|

### Extrair texto
  
Extrair texto de uma área específica de uma imagem
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Caminho JPG ou caminho PDF|Caminho do arquivo JPG ou PDF a ser processado|JPG ou PDF|
|coordenadas|Coordenadas do canto superior esquerdo da área a ser extraída|150, 340|
|tamanho|Dimensões da área a ser extraída|250x200|
|Página|Página a ser lida do PDF||
|Resultado|Variável onde o texto extraído é armazenado||

### Recortar imagem
  
Corta uma imagem a partir de coordenadas
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Image|Caminho onde a imagem a ser cortada está localizada|/path/to/image.png|
|Caminho e nome do arquivo JPG|Caminho e nome do arquivo de saída JPG|JPG|
|Coordenadas|Coordenadas de início de corte|x,y|
|Tamanho|Dimensões de corte|largura, altura|

### Combine imagens
  
Combina duas imagens em uma mantendo o tamanho de cada imagem. Pode ser combinado horizontal ou verticalmente
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Imagem 1|Imagem 1 para combinar. Será posicionada à esquerda ou acima da imagem 2 de acordo com a orientação selecionada|C:/Users/User/desktop/imagem1.png|
|Imagem 2|Imagem 2 para combinar. Será posicionada à direita ou abaixo da imagem 1 de acordo com a orientação selecionada|C:/Users/User/desktop/imagem2.png|
|Orientação|Selecione a orientação da imagem resultante|Horizontal|
|Imagem combinada|Caminho da imagem resultante|C:/Users/User/desktop/imagemCombinada.png|
