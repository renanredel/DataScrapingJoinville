import urllib.request
from time import sleep

from bs4 import BeautifulSoup
from selenium import webdriver

url = "https://transparencia.joinville.sc.gov.br/?p=5&inicio=01/01/2020&fim=31/12/2020"
page = urllib.request.urlopen(url)
driver = webdriver.Firefox()



def values(driverPage, url):
    print(url)


def scrap(driverPage):
    soup = BeautifulSoup(driverPage, 'html.parser')

    indice = 0
    for result in soup.findAll('table', {'class': 'tableDados'}):
        i = 0
        for line in result.findAll('td'):
            i=i+1
            if i/3 == 1:
                print(line.text.ljust(10))
                curWindowHndl = driver.current_window_handle
                driver.find_element_by_partial_link_text(line.text).click()
                sleep(2)
                driver.switch_to_window(driver.window_handles[1])
                values(driver.page_source, driver.current_url)
                driver.close()
                driver.switch_to_window(curWindowHndl)
            else:
                if i/3 == 2:
                    i = 0
            indice = indice + 1
            ###GO TO NEXT PAGE###
            if indice / 6 == 50:
                driver.find_element_by_xpath("//*[@id='menuPaginacao']/li[5]/a").click()
                scrap(driver.page_source, driver.current_url)


driver.get(url)

#### SELECIONA A UNIDADE

unidadeSelect = driver.find_element_by_id("id_entidade")
unidadeSelect.click()
# unidadeSelect.send_keys("Prefeitura")
driver.find_element_by_xpath("//*[@id='id_entidade']/option[15]").click()

#### SELECIONA O MES
driver.find_element_by_id("nr_mes").click()
driver.find_element_by_xpath("//*[@id='nr_mes']/option[1]").click()

#### SELECIONA O ANO
driver.find_element_by_id("nr_ano").click()
driver.find_element_by_xpath("//*[@id='nr_ano']/option[2]").click()

#### SELECIONA A SITUAÇÃO
driver.find_element_by_id("id_situacao").click()
driver.find_element_by_xpath("//*[@id='id_situacao']/option[19]").click()

#### SELECIONA O VINCULO
driver.find_element_by_id("iVinculoFiltroPeloCampo").click()
driver.find_element_by_xpath("//*[@id='iVinculoFiltroPeloCampo']/option[6]").click()

#### DIGITA O CARGO
driver.find_element_by_id("ds_cargo").send_keys("EDUCADOR")

#### CONSULTAR
driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[6]/td[2]/input").click()

# soup = BeautifulSoup(driver.page_source)

scrap(driver.page_source)
