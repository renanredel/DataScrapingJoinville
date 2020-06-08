import urllib.request
import pandas as pd
import re
import warnings
from decimal import Decimal
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from classificador.training import Training
from classificador.predict import Predict
from plot.graphs import PlotClass

plot = PlotClass()
treinar = Training()
prever = Predict()

# IGNORA WARNINGS
warnings.filterwarnings("ignore")

url = "https://transparencia.joinville.sc.gov.br/?p=5&inicio=01/01/2020&fim=31/12/2020"
page = urllib.request.urlopen(url)
driver = webdriver.Firefox()

values = pd.DataFrame()
# INICIA AS VARIAVEIS
name, prov, desc, liqui, admin, anostrab = [], [], [], [], [], []


def savecsv():
    # PEGA O PRIMEIRO NOME
    values['primeiro_nome'] = ([x.split()[0] for x in name])
    values['nome_completo'] = name
    values['proventos'] = prov
    values['descontos'] = desc
    values['liquido'] = liqui
    values['admissão'] = admin
    values['anos_trabalhados'] = anostrab
    values['genero'] = prever.predicting(name)
    values.to_csv("/home/renanredel/PycharmProjects/DataScrapingJoinville/resultado/valores.csv")


def getvalues():
    proventos = driver.find_element_by_xpath("/html/body/form/div[4]/table[4]/thead/tr/td[2]").text
    descontos = driver.find_element_by_xpath("/html/body/form/div[4]/table[4]/thead/tr/td[3]").text
    admissao = driver.find_element_by_xpath("//*[@id='colDir']/table/tbody/tr[2]/td[2]").text

    # PEGA SOMENTE O ANO
    admissao = (admissao[-4:])

    # REMOVE R$
    descontos = (descontos[3:])
    proventos = (proventos[3:])

    # SUBSTITUI ',' POR '.'
    proventos = (re.sub("[.]", "", proventos))
    proventos = (re.sub("[,]", ".", proventos))

    descontos = (re.sub("[.]", "", descontos))
    descontos = (re.sub("[,]", ".", descontos))

    anosvar = (2020 - (Decimal(admissao)))
    admin.append(admissao)
    prov.append(proventos)
    desc.append(descontos)
    anostrab.append(anosvar)
    liqui.append(Decimal(proventos) - Decimal(descontos))


def scrap(driverPage):
    soup = BeautifulSoup(driverPage, 'html.parser')

    indice = 0
    for result in soup.findAll('table', {'class': 'tableDados'}):
        i = 0
        for line in result.findAll('td'):
            i = i + 1
            if i / 3 == 1:
                print(line.text.ljust(10))  # PRINT PARA VISUALIZAÇÃO DO PROGRESSO
                # SALVA A JANELA PRINCIPAL (PAGINA ATUAL)
                curWindowHndl = driver.current_window_handle

                # CLICA NO LINK
                driver.find_element_by_partial_link_text(line.text).click()

                # AGUARDA 4 SEGUNDOS ATÉ A PAGINA CARREGAR COMPLETAMENTE
                sleep(4)

                # TROCA PARA A ABA ABERTA
                driver.switch_to_window(driver.window_handles[1])

                # RESOLVE O ERRO CASO NÃO EXISTA SALARIO LANÇADO
                try:
                    getvalues()
                except NoSuchElementException as e:
                    print("Erro: " + str(e))
                    driver.close()
                    driver.switch_to_window(curWindowHndl)
                    continue

                # FECHA A ABA
                driver.close()

                name.append(line.text)
                # RETORNA PARA JANELA PRINCIPAL
                driver.switch_to_window(curWindowHndl)
            else:
                if i / 3 == 2:
                    i = 0
            indice = indice + 1
    # VAI PARA A PRÓXIMA PÁGINA
    if indice / 6 == 50:
        try:
            driver.find_element_by_xpath("//*[@id='menuPaginacao']/li[5]/a").click()
            scrap(driver.page_source)
        except:
            print("Próxima pagina não encontrada, vá para próximo mês")


def proximomes():
    i = 1
    sleep(4)
    while i <= 12:
        print("Mes" + str(i))
        driver.find_element_by_xpath("//*[@id='nr_mes']/option[" + str(i) + "]").click()
        driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[6]/td[2]/input").click()
        scrap(driver.page_source)
        i = i + 1


#treinar.train()

driver.get(url)

# SELECIONA A UNIDADE
driver.find_element_by_xpath("//*[@id='id_entidade']/option[15]").click()

# SELECIONA O MES
driver.find_element_by_xpath("//*[@id='nr_mes']/option[1]").click()

# SELECIONA O ANO
driver.find_element_by_xpath("//*[@id='nr_ano']/option[2]").click()

# SELECIONA A SITUAÇÃO
driver.find_element_by_xpath("//*[@id='id_situacao']/option[19]").click()

# SELECIONA O VÍNCULO
driver.find_element_by_xpath("//*[@id='iVinculoFiltroPeloCampo']/option[6]").click()

# DIGITA O CARGO
driver.find_element_by_id("ds_cargo").send_keys("Engenheiro civil")

# REALIZA A CONSULTA
driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[6]/td[2]/input").click()

proximomes()
savecsv()

plot.plot1()
