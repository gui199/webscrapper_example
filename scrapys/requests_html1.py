#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  7 22:18:26 2021

@author: gui
"""
#Lista de Constantes Xpath
start_urls = 'https://telefonesimportados.netlify.app/'
produto = '//*[@class="single-product-area"] /div[@class="container"]/div[@class="row"][1]//div[@class="col-md-3 col-sm-6"]'
imagem = './/div[@class="single-shop-product"]//div[@class="product-upper"]/img/@src'
nome = './/div[@class="single-shop-product"]//h2/a/text()'
preço = './/div[@class="single-shop-product"]//div[@class="product-carousel-price"]//ins/text()'
nextt = '//a[@aria-label="Next"]'
itens = []

#Função de parse/analise de elementos
def get_itens(quotes):
    global itens
    for x in quotes:
        img = start_urls+x.xpath(imagem, first=True)
        name = x.xpath(nome, first=True)
        price = x.xpath(preço, first=True)
#        print(name)
#        print(img)
#        print(price)
        itens.append({ "Nome": name,
                       "Imagem": img,
                       "Price": price,
                      } )
    
#Make a GET request :
from requests_html import HTMLSession
session = HTMLSession()
r = session.get(start_urls)

next_page  =  ""
#percorendo páginas até encontrar ultima
while next_page is not None:
    print("-"*50) #mostra separação   
    print(r.url) #indica página atual
    quotes = r.html.xpath(produto) #encontra todos os elementos
    get_itens(quotes)#parse    
    try:#encontrar o link para próxima página
        next_page  =  r.html.xpath(nextt, first=True)
        next_link = next_page.absolute_links.pop()
        r = session.get(next_link) 
    except :# se não encontrar, é a a última página
        next_page = None#sair do loop
    
    
#salvar os dados encotrados em tabela csv
import csv
field_names= ['Nome', 'Imagem', 'Price']

with open('ItensReqShop.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(itens)
#    
print("The End.")    
