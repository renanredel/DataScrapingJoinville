import matplotlib
import pandas as pd
from matplotlib import pyplot as plt
import tornado

matplotlib.use("WebAgg")


class PlotClass:
    def plot1(self):
        data = pd.read_csv("/home/renanredel/PycharmProjects/DataScrapingJoinville/resultado/valores.csv",
                           sep=",")
        ### REMOVE A PRIMEIRA COLUNA DO CSV ###
        data = data.drop(data.columns[0], axis=1)
        # print(data.loc[data['liquido'] == 0])
        print(data)
        data.drop(data[data['liquido'] == 0].index, inplace=True)
        data.reset_index(drop=True, inplace=True)
        print(data)
        mens = data[data.genero == "M"]
        womans = data[data.genero == "F"]

        ## AGRUPA OS ANOS TRABALHDOS, E PEGA O VALOR MEDIO DE TODOS OS SALARIOS ##
        womans = womans.groupby(['anos_trabalhados']).agg({'liquido': 'mean'}).reset_index()
        mens = mens.groupby(['anos_trabalhados']).agg({'liquido': 'mean'}).reset_index()

        print("homens")
        print(mens)
        print("mulheres")
        print(womans)

        plt.plot(womans.liquido, womans.anos_trabalhados)
        plt.plot(mens.liquido, mens.anos_trabalhados)
        plt.title("Salario conforme tempo trabalhado")
        plt.xlabel("Salario")
        plt.ylabel("Anos de serviço")
        plt.legend("Mulheres", "Homens")
        plt.show()
