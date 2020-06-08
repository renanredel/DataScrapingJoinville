from classificador.genderclassifier import GenderClassifier

pred, firstname = [], []


class Predict:
    def predicting(self, fullnames):
        # RECEBE OS NOMES COMPLETOS
        classifier = GenderClassifier()
        # CARREGA OS MODELS DE IA JÁ TREINADA
        classifier.load("/home/renanredel/PycharmProjects/DataScrapingJoinville/models/example")
        # RETIRA SOMENTE O PRIMEIRO NOME DO NOME COMPLETO
        for i in range(0, len(fullnames)):
            fullnames[i] = fullnames[i].lower()
            firstname.append(fullnames[i].split()[0])
        # CHAMA A FUNÇÃO DE CLASSIFICAÇÃO ENVIANDO TODOS OS NOMES DE UMA VEZ
        pred = classifier.predict(firstname)
        # REALIZA UM PRINT COM O RESULTADO
        #print("%s - %s" % (firstname, pred))
        return pred
