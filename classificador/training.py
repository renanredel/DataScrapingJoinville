import pandas as pd

from classificador.genderclassifier import GenderClassifier


class Training:
    def train(self):
        dataset = pd.read_csv("/home/renanredel/PycharmProjects/DataScrapingJoinville/dados/nomes.csv").values

        classifier = GenderClassifier()
        classifier.train(dataset)
        classifier.save("/home/renanredel/PycharmProjects/DataScrapingJoinville/models/example")
        precision, recall, accuracy, f1 = classifier.evaluate(dataset)
        print("Accuracy: %f" % accuracy)
        print("Precision: %f" % precision)
        print("Recall: %f" % recall)
        print("F1: %f" % f1)
