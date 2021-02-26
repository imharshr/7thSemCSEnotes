from sklearn import neighbors, datasets
from sklearn.metrics import confusion_matrix, accuracy_score

iris = datasets.load_iris()
X, y = iris.data, iris.target

target = iris.target_names

knn = neighbors.KNeighborsClassifier(n_neighbors=5)

knn.fit(X, y)

predictions = knn.predict(X)

for i in range(len(predictions)):
	print("Actual: {} - Prediction: {}".format(target[y[i]], target[predictions[i]]))


print("\nAccuracy Score: {0:.2f} %".format(accuracy_score(y, predictions)*100))

cm =confusion_matrix(y, predictions)
print("\nconfusion_matrix:")
print(cm)