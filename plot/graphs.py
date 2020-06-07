import matplotlib
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import tornado

matplotlib.use("WebAgg")


class PlotClass:
    def plot1(self):
        data = pd.read_csv("/home/renanredel/PycharmProjects/DataScrapingJoinville/resultado/professores.csv",
                           sep=",")
        ### REMOVE A PRIMEIRA COLUNA DO CSV ###
        data = data.drop(data.columns[0], axis=1)
        print(data)
        data.drop(data[data['liquido'] == 0].index, inplace=True)
        data.drop(data[data['anos_trabalhados'] >= 30].index, inplace=True)
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

        plt.plot(womans.anos_trabalhados, womans.liquido, label='Mulheres')
        plt.plot(mens.anos_trabalhados, mens.liquido, label='Homens')
        plt.title("Salario conforme tempo trabalhado")
        plt.xlabel("Anos de serviço")
        plt.ylabel("Salário")
        plt.legend()

        plt.show()


    def plot2(self):
        data = pd.read_csv("/home/renanredel/PycharmProjects/DataScrapingJoinville/resultado/professores.csv",
                           sep=",")
        data = data.drop(data.columns[0], axis=1)
        data.drop(data[data['liquido'] == 0].index, inplace=True)
        data.drop(data[data['anos_trabalhados'] >= 30].index, inplace=True)
        labels = 'Homens', 'Mulheres'
        male = data[data.genero == "M"]
        woman = data[data.genero == "F"]
        sizemale = (len(male) / 12)
        sizewoman = (len(woman) / 12)
        manostrabalhados = woman.groupby(['anos_trabalhados']).size()
        hanostrabalhados = male.groupby(['anos_trabalhados']).size()


        manostrabalhados = round((manostrabalhados/12)+ .5).sort_values()
        hanostrabalhados = round((hanostrabalhados/12)+ .5).sort_values()

        fig, ax = plt.subplots(2,2)

        size = 0.3
        vals = ([[sizemale], [sizewoman]])

        cmap = plt.get_cmap("tab20c")
        outer_colors = cmap(np.arange(3) * 4)
        inner_colors = cmap(np.array([1, 2, 5, 6, 9, 10]))

        ax[0,0].pie(vals, radius=1.3, colors=outer_colors,
               wedgeprops=dict(width=size, edgecolor='w'), labels=labels, autopct='%1.1f%%')

        ax[0,1].pie(manostrabalhados, radius=1.5 - size, colors=inner_colors,
                    labels=manostrabalhados.index.tolist(), autopct='%1.0f%%')

        ax[1,1].pie(hanostrabalhados, radius=1.5 - size, colors=inner_colors,
               labels=hanostrabalhados.index.tolist(), autopct='%1.0f%%')

        ax[1,0].remove()

        ax[0,0].set(aspect="equal", title='Porcentagem Homens e Mulheres')
        ax[0,1].set(aspect="equal", title='Tempo de serviço - Mulheres')
        ax[1,1].set(aspect="equal", title='Tempo de serviço - Homens')

        plt.show()





