# Projeto Scrapy PT
Esse repositório tem objetivo fazer o scrapy, raspagem de dados, do site:  
https://telefonesimportados.netlify.app/

Para isso é usado várias ferramentas para atingir o mesmo resultado  
- Scrapy
- Selenium
- MechanicalSoup
- Requests_html

O resultado é um arquivo csv com os itens coletados.

# Scrapy Project EN
This repository aims to do the scrapy, scraping of data, from the site:  
https://telefonesimportados.netlify.app/

For this, several tools are used to achieve the same result 
- Scrapy
- Selenium
- MechanicalSoup
- Requests_html

The result is a csv file with the collected items. 

## Rodando o aplicativo PT   
Usando Scrapy  
```bash
#Na pasta raiz do projeto
scrapy crawl scrapper -O items.csv
```  
Para os outros Projetos
```bash
python3 scrapys/selenium1.py
#ou
python3 scrapys/requests_html1.py
#ou
python3 scrapys/mechanicalsoup1.py
```  
Instale as dependências antes.


## Running the app  EN   
Using Scrapy  
```bash
#In the project root folder
scrapy crawl scrapper -O items.csv
```  
For the other Projects 
```bash
python3 scrapys/selenium1.py
#or
python3 scrapys/requests_html1.py
#or
python3 scrapys/mechanicalsoup1.py
```  
Install the dependencies first. 

----------------
### link idéia original
[Automação Selenium Python + Excel + E-mail | Avaliei 2 Projetos REAIS](https://www.youtube.com/watch?v=Rt-g2xVlGyI)
