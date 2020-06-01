import matplotlib
import pandas as pd
from matplotlib import pyplot as plt
import tornado

matplotlib.use("WebAgg")


class PlotClass:
    def anostrabalhadosxsalario (self):



    def plot1(self):
        data = pd.read_csv("/home/renanredel/PycharmProjects/DataScrapingJoinville/resultado/valores.csv")
        ### TODO excluir valores igual a zero
        mens = data[data.genero == "M"]
        mens.sort_values(by=['liquido', 'anos_trabalhados'])
        womans = data[data.genero == "F"]
        #womans = womans.sort_values(by=['liquido', 'anos_trabalhados'])

        print(womans)
        print("average")
        avr = womans.loc[:, "liquido"].mean()
        print(avr)
        ## AGRUPA OS ANOS TRABALHDOS, E PEGA O VALOR MEDIO DE TODOS OS SALARIOS ##
        womans = womans.groupby(['anos_trabalhados']).agg({'liquido':'mean'})
        print("groupby")
        print(womans)


        plt.plot(womans.liquido, womans.anos_trabalhados)
        plt.plot(mens.liquido, mens.anos_trabalhados)
        plt.title("Salario conforme tempo trabalhado")
        plt.xlabel("Salario")
        plt.ylabel("Anos")
        plt.legend("Mulheres", "Homens")
        plt.show()
