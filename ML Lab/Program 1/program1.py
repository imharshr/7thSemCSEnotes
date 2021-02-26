'''
1. Implement and demonstratethe FIND-Salgorithm for finding the most specific
hypothesis based on a given set of training data samples. Read the training data from a
.CSV file.
'''

import csv
h = [['%', '%', '%','%','%','%']]
examples = []
with open('Training_examples.csv') as csv_file:
    readcsv = csv.reader(csv_file, delimiter = ',')
    examples = list(readcsv)
print("The given training examples are: ")
for i in examples:
    print(i)
print("The positive training examples are: ")
for i in examples:
    if i[-1] == 'Yes':
        print(i)
print("Steps of Find-S algorithm are: ")
print(h)
#initialise h to the most specific hypothesis
pos_e = []
for i in examples:
    if i[-1] == 'Yes':
        pos_e = examples[:-1]
        print("Examples : ",examples[:-1])
for x in examples:
    if x[-1] == 'Yes':
        j = 0
        h = examples[j]
        print(h[:-1])
        for i in range(0,6):
            if h[i] != examples[j][i]:
                h[i] = '?'
            else:
                j += 1
    else:
         continue
print(f"The most specific hypothesis: {h[:-1]}")
