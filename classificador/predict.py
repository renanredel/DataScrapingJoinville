from classificador.genderclassifier import GenderClassifier

from classificador.genderclassifier import GenderClassifier
# class Predict:
#     def predicting(self):
#         classifier = GenderClassifier()
#         classifier.load("/home/renanredel/PycharmProjects/DataScrapingJoinville/models/example")
#         name = input()
#         while name is not "q":
#             pred = classifier.predict([name.lower()])
#             print("%s - %s" % (name, pred))
#             name = input()
#

#
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
