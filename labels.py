from sklearn import tree
import csv

f = open('features.csv')
csv_f = csv.reader(f)

for row in csv_f:
    print(row)
labels = ["Happy","Joyful","Sad","Inspiring","Anger"]


clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
