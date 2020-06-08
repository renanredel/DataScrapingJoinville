import matplotlib
import numpy
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from mpldatacursor import datacursor
import tornado

matplotlib.use("WebAgg")

class PlotClass:
    def plot1(self):
        data = pd.read_csv("/home/renanredel/PycharmProjects/DataScrapingJoinville/resultado/valores.csv",
                           sep=",")
        # REMOVE A PRIMEIRA COLUNA DO CSV #
        data = data.drop(data.columns[0], axis=1)

        # REMOVE OS DADOS QUE POSSUEM SALÁRIO LÍQUIDO IGUAL A ZERO
        data.drop(data[data['liquido'] == 0].index, inplace=True)

        # REMOVE TRABALHADORES COM MAIS DE 30 ANOS DE SERVIÇO
        data.drop(data[data['anos_trabalhados'] >= 30].index, inplace=True)
        data.reset_index(drop=True, inplace=True)

        # DIVIDE OS DADOS ENTRE OS DOIS GRUPOS
        mens = data[data.genero == "M"]
        womans = data[data.genero == "F"]

        # AGRUPA OS ANOS TRABALHDOS, E PEGA O VALOR MEDIO DE TODOS OS SALARIOS #
        womans = womans.groupby(['anos_trabalhados']).agg({'liquido': 'mean'}).reset_index()
        mens = mens.groupby(['anos_trabalhados']).agg({'liquido': 'mean'}).reset_index()

        # ADICIONA A LINHA DAS MULHERES
        plt.plot(womans.anos_trabalhados, womans.liquido, label='Mulheres', marker='o', color='r')
        # CRIA E ADICIONA A LINHA DE TENDENCIA
        z = numpy.polyfit(womans.anos_trabalhados, womans.liquido, 1)
        p = numpy.poly1d(z)
        plt.plot(womans.anos_trabalhados, p(womans.anos_trabalhados), "r--", color='lightcoral')

        # ADICIONA A LINHA DOS HOMENS
        plt.plot(mens.anos_trabalhados, mens.liquido, label='Homens', marker='o', color='dodgerblue')
        # CRIA E ADICINHA A LINHA DE TENDENCIA
        z = numpy.polyfit(mens.anos_trabalhados, mens.liquido, 1)
        p = numpy.poly1d(z)
        plt.plot(mens.anos_trabalhados, p(mens.anos_trabalhados), "r--", color='deepskyblue')

        # DEFINE OS TITULOS E NOMES
        plt.title("Salario conforme tempo trabalhado")
        plt.xlabel("Anos de serviço")
        plt.ylabel("Salário")
        plt.legend()

        # CHAMA O SEGUNDO GRAFICO
        self.plot2()



    def plot2(self):
        data = pd.read_csv("/home/renanredel/PycharmProjects/DataScrapingJoinville/resultado/valores.csv",
                           sep=",")
        # REMOVE A PRIMEIRA COLUNA DO CSV #
        data = data.drop(data.columns[0], axis=1)

        # REMOVE OS DADOS QUE POSSUEM SALÁRIO LÍQUIDO IGUAL A ZERO
        data.drop(data[data['liquido'] == 0].index, inplace=True)

        # REMOVE TRABALHADORES COM MAIS DE 30 ANOS DE SERVIÇO
        data.drop(data[data['anos_trabalhados'] >= 30].index, inplace=True)
        # DEFINE DUAS STRINGS PARA SER UTILIZADOS COMO LEGENDA
        labels = 'Homens', 'Mulheres'

        # DIVIDE OS DADOS ENTRE OS DOIS GRUPOS
        male = data[data.genero == "M"]
        woman = data[data.genero == "F"]
        # SALVA O TAMANHO DE CADA DATASET E DIVIDE POR 12 (MESES)
        sizemale = (len(male) / 12)
        sizewoman = (len(woman) / 12)

        # AGRUPA POR ANOS TRABALHADOS, E ADICIONA UMA LINHA COM A QUANTIDADE DE LANÇAMENTOS PARA CADA ANO
        manostrabalhados = woman.groupby(['anos_trabalhados']).size()
        hanostrabalhados = male.groupby(['anos_trabalhados']).size()

        # ORDENA OS VALORES
        manostrabalhados = round((manostrabalhados/12)+ .5).sort_values()
        hanostrabalhados = round((hanostrabalhados/12)+ .5).sort_values()

        # DEFINE QUE SERÁ UMA FIGURA COM 4 GRAFICOS (2X2)
        fig, ax = plt.subplots(2,2)

        size = 0.3
        vals = ([[sizemale], [sizewoman]])

        # DEFINE AS CORES
        cmap = plt.get_cmap("tab20c")
        outer_colors = cmap(np.arange(3) * 4)
        inner_colors = cmap(np.array([1, 2, 5, 6, 9, 10]))

        ax[0,0].pie(vals, radius=1.3, colors=outer_colors,
               wedgeprops=dict(width=size, edgecolor='w'), labels=labels, autopct='%1.1f%%')

        ax[0,1].pie(manostrabalhados, radius=1.5 - size, colors=inner_colors,
                    labels=manostrabalhados.index.tolist(), autopct='%1.0f%%')

        ax[1,1].pie(hanostrabalhados, radius=1.5 - size, colors=inner_colors,
               labels=hanostrabalhados.index.tolist(), autopct='%1.0f%%')

        # NAO EXIBE ESTE GRAFICO
        ax[1,0].remove()

        # DEFINE SEUS TITULOS
        ax[0,0].set(aspect="equal", title='Porcentagem Homens e Mulheres')
        ax[0,1].set(aspect="equal", title='Tempo de serviço - Mulheres')
        ax[1,1].set(aspect="equal", title='Tempo de serviço - Homens')

        # HABILITA A POSSIBILIDADE DE UTILIZAR O CURSOR NOS GRAFICOS
        datacursor(bbox=dict(fc='white'),
                  arrowprops=dict(arrowstyle='simple', fc='white', alpha=0.5), draggable=True)

        # EXIBE OS GRÁFICOS
        plt.show()





