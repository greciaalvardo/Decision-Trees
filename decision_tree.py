#-------------------------------------------------------------------------
# AUTHOR: Grecia Alvarado
# FILENAME: decision_tree.py
# SPECIFICATION: Complete code to output decision tree
# FOR: CS 4210- Assignment #1
# TIME SPENT: code: ~3hr (mostly figuring out python syntax), assignment total (excluding code): ~2.5hr
#-----------------------------------------------------------*/
#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH 
#AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays
#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []
#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)
#transform the original categorical training features to numbers and add to the 4D 
#array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
# so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
#--> add your Python code here
tracker = {}
num = 1
for i in db:
  indices = i
  row = []
  for j in range(0, len(indices)-1):
    if indices[j] in tracker:
      row.append(tracker.get(indices[j]))
      indices[j] = tracker.get(indices[j])
    else:
      tracker[indices[j]] = num
      row.append(num)
      indices[j] = num
      num += 1
  X.append(row)


# X =
#transform the original categorical training classes to numbers and add to the 
#vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> addd your Python code here
tracker2 = {}
num2 = 1
for j in db:
  for i in range(len(j)-1, len(j)):
    if j[i] in tracker2:
      Y.append(tracker2.get(j[i]))
    else:
      tracker2[j[i]] = num2
      Y.append(num2)
      num2 += 1

# Y =
#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy', )
clf = clf.fit(X, Y)
#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], 
class_names=['Yes','No'], filled=True, rounded=True)
plt.show()