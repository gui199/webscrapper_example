#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  6 20:30:04 2021

@author: gui
"""
#Lista de Constantes Xpath
start_urls = 'https://telefonesimportados.netlify.app/'
produto = '//*[@class="single-product-area"] /div[@class="container"]/div[@class="row"][1]//div[@class="col-md-3 col-sm-6"]'
imagem = './div[@class="single-shop-product"]//div[@class="product-upper"]/img'
nome = './div[@class="single-shop-product"]//h2/a'
preço = './div[@class="single-shop-product"]//div[@class="product-carousel-price"]//ins'
nextt = '//a[@aria-label="Next"]'
itens = []

#Função de parse/analise de elementos
def get_itens(quotes):
    global itens
    for x in quotes:
        img = start_urls+x.find_element_by_xpath(imagem).get_attribute("src")
        name = x.find_element_by_xpath(nome).text
        price = x.find_element_by_xpath(preço).text
#        print(name)
#        print(img)
#        print(price)
        itens.append({ "Nome": name,
                       "Imagem": img,
                       "Price": price,
                      } )
    
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
#inicializando selenium em modo invisivel headless
options = Options()
options.headless = True
#iniciando o driver 
brower = webdriver.Firefox(options=options)
#opção para usar Chrome,
#brower = webdriver.Chrome(executable_path='/path/chromedriver')
#abrir página
brower.get(start_urls) 

next_page  =  ""
#percorendo páginas até encontrar ultima
while next_page is not None:
    print("-"*50) #mostra separação   
    print(brower.current_url) #indica página atual
    quotes = brower.find_elements_by_xpath(produto) #encontra todos os elementos
    get_itens(quotes)#parse    
    try:#encontrar o link para próxima página
        next_page = brower.find_element_by_xpath(nextt)
        next_link = next_page.get_attribute("href")
        brower.get(next_link) #ir next page
    except NoSuchElementException:# se não encontrar, é a a última página
        next_page = None#sair do loop
    
#desligar o driver
brower.quit()

#salvar os dados encotrados em tabela csv
import csv
field_names= ['Nome', 'Imagem', 'Price']

with open('ItensShop.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(itens)
    
print("The End.")    