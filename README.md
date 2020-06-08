# DataScrapingJoinville
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)

Algoritmo de raspagem de dados no site da transparencia de Joinville - SC.

### Pré-requisitos

Este projeto utiliza as especificações do Python 3 e possuí as seguintes dependencias:

|  |  
| ------ | 
| Selenium |
| BeautifulSoup |
| Pandas |
| Keras |
| Numpy |
| Scipy |
| Tensorflow |
| Scikit-Learn |
| [Mpldatacursor][A3Link] |
| Matplotlib | 

### Utilização

 Realize a copia do repositório para seu computador:
 
 ```shell script
$ git clone  https://github.com/renanredel/DataScrapingJoinville.git
```
 Caso queira realizar o o treinamento da IA de identificação de sexo, execute a função ```treinar.train()``` disponível em [mainscraping.py][A2Link].
 O dataset com os nomes para treinamento, se encontram em [Dataset][A4Link].
 
 Escolha qual cargo será buscado utilizando a linha abaixo, também disponível em [mainscraping.py][A2Link].
 
 ```shell script
driver.find_element_by_id("ds_cargo").send_keys("CARGO")
 ```

 Por fim, execute a classe [mainscraping.py][A2Link].
 
### TODO

 - GUI

### Licença

MIT License

### Créditos

- [Name Gender Classifier][A1Link]


[A1Link]:<https://github.com/joaoalvarenga/namegenderclassifier>
[A2Link]:<https://github.com/renanredel/DataScrapingJoinville/blob/master/webscraping/mainscraping.py>
[A3Link]:<https://github.com/joferkington/mpldatacursor>
[A4Link]:<https://github.com/renanredel/DataScrapingJoinville/blob/master/dados/nomes.csv>