import csv
import math
import random
import statistics


def calculate_probability(x, mean, stdev):
    exponent = math.exp(-(math.pow(x - mean, 2) / (2 * math.pow(stdev, 2))))
    return (1 / (math.sqrt(2 * math.pi) * stdev)) * exponent


dataset = []
dataset_size = 0
with open('data.csv') as csvfile:
    lines = csv.reader(csvfile)
    for row in lines:
        dataset.append([float(attr) for attr in row])
dataset_size = len(dataset)
print('Size of dataset is : ', dataset_size)

train_size = int(0.7 * dataset_size)  # 70 % as test data

print(train_size)

X_train = []
X_test = dataset.copy()
training_indexes = random.sample(range(dataset_size), train_size)

# Split Data
for i in training_indexes:
    X_train.append(dataset[i])
    X_test.remove(dataset[i])

# Separate Data based on class value
classes = {}
for samples in X_train:
    last = int(samples[-1])
    if last not in classes:
        classes[last] = []
    classes[last].append(samples)

print(classes)

# Find mean and variance of each attribute by adding all attributes
summaries = {}
for classValue, training_data in classes.items():
    summary = [(statistics.mean(attribute), statistics.stdev(attribute)) for attribute in zip(*training_data)]
    del summary[-1]
    summaries[classValue] = summary

print(summaries)
X_prediction = []

# Predict the output of test data
for i in X_test:
    probabilities = {}
    for classValue, classSummary in summaries.items():
        probabilities[classValue] = 1
        for index, attr in enumerate(classSummary):
            probabilities[classValue] *= calculate_probability(i[index], attr[0], attr[1])

    best_label, best_prob = None, -1
    for classValue, probability in probabilities.items():
        if best_label is None or probability > best_prob:
            best_prob = probability
            best_label = classValue
    X_prediction.append(best_label)

# Find Accuracy
correct = 0
for index, key in enumerate(X_test):
    if X_test[index][-1] == X_prediction[index]:
        correct += 1

print("Accuracy : ", correct / (float(len(X_test))) * 100)