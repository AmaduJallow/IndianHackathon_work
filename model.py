import math

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB

data = np.genfromtxt("diabetes_model.csv", delimiter=",")

y_axis = data[1:, -1]
# print(y_axis)
x_axis = data[1:, 0:-1]
# print(x_axis)
log_clf = LogisticRegression(solver='liblinear', max_iter=300, C=10.0, random_state=0)
gnb = GaussianNB()
classify = log_clf.fit(x_axis, y_axis)
x_test = np.genfromtxt("diabetes_test.csv", delimiter=",")[1:, :-1]
output = classify.predict(x_test)
print(classify.coef_)
intergerResults = []
for point in output:
    intergerResults.append(int(point))

print(intergerResults)
gnb.fit(x_axis, y_axis)
print("This is the episolon: " + str(gnb.epsilon_))
y_result = gnb.predict(x_test)

intergerResultant = []
for point in y_result:
    intergerResultant.append(int(point))

print(intergerResultant)

for i in range(0, len(intergerResultant)):
    if y_result[i] == intergerResultant[i]:
        print("They are equal here at position: " + str(i))
    else:
        print("They are not equal here at position: " + str(i))

vari = [1.17352550e-01, 3.09894672e-02, -1.10023669e-02, -2.26731834e-03,
        -7.59322260e-04, 9.45008367e-02, 9.61730284e-01, 6.99536800e-03]


def predictor(pregnancies, glucose, diastolic, triceps, insulin, bmi, dpf, age):
    exponent = math.exp((
            log_clf.intercept_ + vari[0] * pregnancies + vari[1] * glucose + vari[2] * diastolic + vari[3] * triceps +
            vari[4] * insulin +
            vari[
                5] * bmi + vari[6] * dpf + vari[7] * age))
    result = exponent / (1 + exponent)
    print(result)


predictor(2, 56, 56, 28, 45, 24.2, 0.332, 22)
