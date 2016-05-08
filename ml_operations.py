import csv
import sklearn
import helpers
from sklearn import tree

class ml_operations():

    def __init__(self):
        with open("features.csv", "rt") as f:
            reader = csv.reader(f)
            features = list(reader)

        with open("labels.csv", "rt") as f:
            reader = csv.reader(f)
            labels = list(reader)

        labels = helpers.adjectives_to_int(labels)
        i = 0
        meta_features = []
        for rows in features:
            meta_features.append([features[1]])
            print([features[1]])



    def predict(self, song_values):
	classifier = sklearn.tree.DecisionTreeClassifier()
        classifier = classifier.fit(meta_features, labels)
        print(classifier.predict([[song_values]]))

if __name__ == "__main__":
    ml = ml_operations()
    ml.predict([0.5, 0.6])
