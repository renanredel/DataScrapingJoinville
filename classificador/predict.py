from classificador.genderclassifier import GenderClassifier

pred, firstname = [], []


class Predict:
    def predicting(self, fullnames):
        classifier = GenderClassifier()
        classifier.load("/home/renanredel/PycharmProjects/DataScrapingJoinville/models/example")
        for i in range(0, len(fullnames)):
            fullnames[i] = fullnames[i].lower()
            firstname.append(fullnames[i].split()[0])
        pred = classifier.predict(firstname)
        print("%s - %s" % (firstname, pred))
        return pred
