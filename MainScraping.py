import urllib.request
from decimal import Decimal

import pandas as pd
from time import sleep
import re

from bs4 import BeautifulSoup
from selenium import webdriver

url = "https://transparencia.joinville.sc.gov.br/?p=5&inicio=01/01/2020&fim=31/12/2020"
page = urllib.request.urlopen(url)
driver = webdriver.Firefox()

values = pd.DataFrame()
name = []
prov = []
desc = []
liqui = []


def savecsv():
    ### PEGA O PRIMEIRO NOME ###
    values['primeiro nome'] = ([x.split()[0] for x in name])
    values['nome completo'] = name
    values['proventos'] = prov
    values['descontos'] = desc
    values['liquido'] = liqui
    values.to_csv('valores.csv')


def getvalues():
    proventos = driver.find_element_by_xpath("/html/body/form/div[4]/table[4]/thead/tr/td[2]").text
    descontos = driver.find_element_by_xpath("/html/body/form/div[4]/table[4]/thead/tr/td[3]").text

    ### REMOVE R$ ###
    descontos = (descontos[3:])
    proventos = (proventos[3:])

    ### SUBSTITUI ',' POR '.' ###
    proventos = (re.sub("[.]", "", proventos))
    proventos = (re.sub("[,]", ".", proventos))

    descontos = (re.sub("[.]", "", descontos))
    descontos = (re.sub("[,]", ".", descontos))

    prov.append(proventos)
    desc.append(descontos)
    liqui.append(Decimal(proventos) - Decimal(descontos))
    print(proventos)
    print(descontos)


def scrap(driverPage):
    soup = BeautifulSoup(driverPage, 'html.parser')

    indice = 0
    for result in soup.findAll('table', {'class': 'tableDados'}):
        i = 0
        for line in result.findAll('td'):
            i = i + 1
            if i / 3 == 1:
                print(line.text.ljust(10))
                name.append(line.text)

                ### SALVA A JANELA PRINCIPAL (PAGINA ATUAL) ###
                curWindowHndl = driver.current_window_handle

                ### CLICA NO LINK ###
                driver.find_element_by_partial_link_text(line.text).click()

                ### AGUARDA 4 SEGUNDOS ATÉ A PAGINA CARREGAR COMPLETAMENTE ###
                sleep(4)

                ### TROCA PARA A ABA ABERTA ###
                driver.switch_to_window(driver.window_handles[1])
                getvalues()

                ### FECHA A ABA ###
                driver.close()

                ### RETORNA PARA JANELA PRINCIPAL ###
                driver.switch_to_window(curWindowHndl)
            else:
                if i / 3 == 2:
                    i = 0
            indice = indice + 1
    ###GO TO NEXT PAGE###
    if indice / 6 == 50:
        driver.find_element_by_xpath("//*[@id='menuPaginacao']/li[5]/a").click()
        scrap(driver.page_source)


driver.get(url)

### SELECIONA A UNIDADE ###

unidadeSelect = driver.find_element_by_id("id_entidade")
unidadeSelect.click()
driver.find_element_by_xpath("//*[@id='id_entidade']/option[15]").click()

### SELECIONA O MES ###
driver.find_element_by_id("nr_mes").click()
driver.find_element_by_xpath("//*[@id='nr_mes']/option[2]").click()

### SELECIONA O ANO ###
driver.find_element_by_id("nr_ano").click()
driver.find_element_by_xpath("//*[@id='nr_ano']/option[2]").click()

### SELECIONA A SITUAÇÃO ###
driver.find_element_by_id("id_situacao").click()
driver.find_element_by_xpath("//*[@id='id_situacao']/option[19]").click()

### SELECIONA O VINCULO ###
driver.find_element_by_id("iVinculoFiltroPeloCampo").click()
driver.find_element_by_xpath("//*[@id='iVinculoFiltroPeloCampo']/option[6]").click()

### DIGITA O CARGO ###
driver.find_element_by_id("ds_cargo").send_keys("EDUCADOR")

### CONSULTAR ###
driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[6]/td[2]/input").click()

scrap(driver.page_source)
