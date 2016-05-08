import csv
from sklearn import tree
import helpers


class ml_operations():

    def __init__(self):
        with open("features.csv", "rb") as f:
            self.csvreader = csv.reader(f)
            self.features = list(self.csvreader)

        with open("labels.csv", "rb") as f:
            self.csvreader = csv.reader(f)
            self.labels = list(self.csvreader)

        i = 0
        self.meta_features = []
        for rows in self.features:
            self.meta_features.append([self.features[1]])
            print([self.features[1]])


    def predict(self):
        classifier = tree.DecisionTreeClassifier()
        classifier = classifier.fit(self.meta_features, self.labels)
        print classifier.predict([[0.5, 0.6]])

if __name__ == "__main__":
    ml = ml_operations()
    ml.predict()
