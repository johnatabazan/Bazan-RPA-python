# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 20:29:58 2018

@author: Johnata.Bazan
"""

import json
from collections import defaultdict
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#para facilitar criação do dicionário, usei biblioteca collections
output=defaultdict(list)

#abrindo o input.json no diretório
with open(r'C:\Users\Johnata.Bazan\Desktop\Milestones FY18\TESTES.N\input.json', 'r') as infile:
    arquivo=json.load(infile)

driver = webdriver.Chrome(r'C:/Users/Johnata.Bazan/Desktop/chromedriver.exe')  
driver.get('http://www.google.com')

#selecionando o elemento de pesquisa que possui nome q
elem = driver.find_element_by_name("q")
elem.clear()

for chave in arquivo:
    #busca os nomes na lista do dicionário, referente ao json de entrada
    for busca in arquivo[chave]:
        elem.send_keys(busca)
        elem.send_keys(Keys.RETURN)
        #mapeando os elementos de resultado da pesquisa, por default, retorna 10
        resultados=  driver.find_elements_by_xpath("//div[@id='search']//div[@class='srg']//h3[@class='LC20lb']")
        #loop para selecionar os 3 primeiros resultados da página
        for i in range(0, 3):
            #adicionando os três primeiros nomes apendado a lista no dicionário de output
            output[busca].append(resultados[i].text)
        #voltar ao conteúdo default da página, garantindo que encontrarei o campo de pesquisa
        driver.switch_to.default_content()
        elem = driver.find_element_by_name("q")
        elem.clear()

#transformando o dicionário em json e salvando no diretório 
with open(r'C:\Users\Johnata.Bazan\Desktop\Milestones FY18\TESTES.N\output.json', 'w') as outfile:
    json.dump(output, outfile, ensure_ascii=False)
