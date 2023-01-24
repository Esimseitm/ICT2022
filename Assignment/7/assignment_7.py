'''
For your assignment, please use the code below first and then write your code.
DO NOT DELETE THE FOLLOWING CODE
'''
import sys
try:
    input1 = sys.argv[1]
    input2 = sys.argv[2]
except:
    print("You didn't put any input when you run your code! Please add an input!")
    input1 = ""
    input2 = ""


'''
The objective of this assignment is to print the expected output.
You can find it in the instruction folder.
List of installed and authorized packages :
    - numpy
    - scikit-learn (import sklearn)
You cannot use other packages than the listed ones (except built-in default package in python).
You can write you code after this comment :
'''

#Your code here:
import numpy as np
import sklearn.linear_model as skmod
input1 = [int(i) for i in input1.split(',')]
input2 = [int(i) for i in input2.split(',')]
input1 = np.array(input1)
input2 = np.array(input2)
input1 = input1.reshape(-1,1)
input2 = input2.reshape(-1,1)
model = skmod.LinearRegression()
model_trained = model.fit(input1, input2)
w1 = model_trained.coef_
w1 = w1[0][0]
b = model_trained.intercept_
b = b[0]


#use this printing (where "w1" is the weight and "b" the bias)
print("The most accurate linear regression has the following equation: y' = {:0.2f}*x + {:0.2f}".format(w1, b))