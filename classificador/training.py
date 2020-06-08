import pandas as pd

from classificador.genderclassifier import GenderClassifier


class Training:
    def train(self):
        # CARREGA O DATASET
        dataset = pd.read_csv("/home/renanredel/PycharmProjects/DataScrapingJoinville/dados/nomes.csv").values
        classifier = GenderClassifier()
        # REALIZA O TREINAMENTO UTILIZANDO O DATASET
        classifier.train(dataset)
        # SALVA OS MODELOS DE IA
        classifier.save("/home/renanredel/PycharmProjects/DataScrapingJoinville/models/example")
        precision, recall, accuracy, f1 = classifier.evaluate(dataset)
        # REALIZA UM PRINT COM OS RESULTADOS
        print("Accuracy: %f" % accuracy)
        print("Precision: %f" % precision)
        print("Recall: %f" % recall)
        print("F1: %f" % f1)
