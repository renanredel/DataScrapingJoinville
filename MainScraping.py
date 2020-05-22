import urllib.request

from bs4 import BeautifulSoup
from selenium import webdriver

url = "https://transparencia.joinville.sc.gov.br/?p=5&inicio=01/01/2020&fim=31/12/2020"
page = urllib.request.urlopen(url)
driver = webdriver.Firefox()




def scrap(driverPage, url):
    soup = BeautifulSoup(driverPage, 'html.parser')

    indice = 0
    for result in soup.findAll('table', {'class': 'tableDados'}):
        for line in result.findAll('td'):
            indice = indice + 1
            #print(indice)
            print(line.text.ljust(10))
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

scrap(driver.page_source, driver.current_url)