import urllib.request

from bs4 import BeautifulSoup
from selenium import webdriver

url = "https://transparencia.joinville.sc.gov.br/?p=5&inicio=01/01/2020&fim=31/12/2020"
page = urllib.request.urlopen(url)

driver = webdriver.Firefox()

driver.get(url)


#### SELECIONA A UNIDADE

unidadeSelect = driver.find_element_by_id("id_entidade")
unidadeSelect.click()
#unidadeSelect.send_keys("Prefeitura")
unidadeEscolhida = driver.find_element_by_xpath("//*[@id='id_entidade']/option[15]").click()

#### SELECIONA O MES
mesSelect = driver.find_element_by_id("nr_mes").click()
mesEscolhido = driver.find_element_by_xpath("//*[@id='nr_mes']/option[1]").click()

#### SELECIONA O ANO
anoSelect = driver.find_element_by_id("nr_ano").click()
anoEscolhido = driver.find_element_by_xpath("//*[@id='nr_ano']/option[2]").click()

#### SELECIONA A SITUAÇÃO
situacaoSelect = driver.find_element_by_id("id_situacao").click()
situacaoEscolhida = driver.find_element_by_xpath("//*[@id='id_situacao']/option[19]").click()

#### SELECIONA O VINCULO
vinculoSelect = driver.find_element_by_id("iVinculoFiltroPeloCampo").click()
vinculoEscolhido = driver.find_element_by_xpath("//*[@id='iVinculoFiltroPeloCampo']/option[6]").click()

#### DIGITA O CARGO
cargo = driver.find_element_by_id("ds_cargo").send_keys("EDUCADOR")

#### CONSULTAR
driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[6]/td[2]/input").click()

soup = BeautifulSoup(driver.page_source)

for result in soup.findAll('table', {'class' : 'tableDados'}):
    for line in result.findAll('td'):
        print(line.text.ljust(10))