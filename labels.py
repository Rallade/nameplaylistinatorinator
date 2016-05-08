from sklearn import tree
import csv

features = open('features.csv')
csv_featurea = csv.reader(features)

for row in csv_f:
    print(row)
labels = ["Happy","Joyful","Sad","Inspiring","Anger"]


clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
