import csv
from sklearn import tree
import helpers
import statistics

class ml_operations():

    def __init__(self):
        with open("features.csv", "r") as f:
            self.csvreader = csv.reader(f)
            self.features = list(self.csvreader)

        with open("labels.csv", "r") as f:
            self.csvreader = csv.reader(f)
            self.labels = list(self.csvreader)

        i = 0
        self.meta_features = []
        for rows in self.features:
            self.meta_features.append([self.features[i][0], self.features[i][1]])
#            print([self.meta_features[i]])
            i += 1


    def predict(self):
        classifier = tree.DecisionTreeClassifier()
        classifier = classifier.fit(self.meta_features, self.labels)
        print(classifier.predict([0.219, 0.165]))

    def aggregate(self, playlist):
        values = []
        i = 0
        for item in playlist:
            values[i] = item[0]
            i += 1

        return statistics.mode(values)
        
if __name__ == "__main__":
    ml = ml_operations()
    ml.predict()
