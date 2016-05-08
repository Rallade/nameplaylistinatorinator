import csv
import sklearn
import helpers


class ml_operations():

    def __init__(self):
        with open("features.csv", "rb") as f:
            reader = csv.reader(f)
            features = list(reader)

        with open("labels.csv", "rb") as f:
            reader = csv.reader(f)
            labels = list(reader)

        labels = helpers.adjectives_to_int(labels)
        i = 0
        meta_features = []
        for rows in features:
            meta_features.append([features[1],features[2]])
            print(" " + [features[1],features[2]])
        
        classifier = sklearn.tree.DecisionTreeClassifier()


    def predict(song_values, adjective):
        classifier = classifier.fit(meta_features, labels)
        print classifier.predict([[song_values, adjective]])
