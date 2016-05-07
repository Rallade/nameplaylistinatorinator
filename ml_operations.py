import csv
import sklearn

class ml_operations():

    def __init__(self):
        with open("features.csv", "rb") as f:
            reader = csv.reader(f)
            features = list(reader)

        with open("labels.csv", "rb") as f:
            reader = csv.reader(f)
            labels = list(reader)

        classifier = sklearn.tree.DecisionTreeClassifier()


    def predict(song_values, adjective):
        classifier = classifier.fit(features, labels)
        print classifier.predict([[song_values, adjective]])
