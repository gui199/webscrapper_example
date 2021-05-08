#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  7 16:05:38 2021

@author: gui
"""
#Lista de Constantes Xpath
start_urls = 'https://telefonesimportados.netlify.app/'
itens = []

def get_itens(quotes):
    global itens
    for x in quotes:
        img = start_urls+x.find('img').attrs["src"]
        name = x.find('a').text
        price = x.find('ins').text
#        print(name)
#        print(img)
#        print(price)
        itens.append({ "Nome": name,
                       "Imagem": img,
                       "Price": price,
                      } )

#Navigate to start_urls
import mechanicalsoup
browser = mechanicalsoup.StatefulBrowser()
browser.open(start_urls)


while True:
    print("-"*50) #mostra separação
    print(browser.get_url())#indica página atual
    page = browser.page #get the page-html to parse it
    products = page.find_all('div', class_="single-shop-product")
    
    get_itens(products)#parse  itens
    #encontrar o link para próxima página
    lists= page.find("ul", class_="pagination")
    last = lists.find_all("a")[-1]
    test = last.has_attr("aria-label")  
    if test:
        next_link = start_urls+last.attrs["href"]
        browser.open(next_link)
    else:#sair do loop se next_link None
         break

#salvar os dados encotrados em tabela csv
import csv
field_names= ['Nome', 'Imagem', 'Price']

with open('ItensMShop.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(itens)
    
print("The End.")            