'''
For your assignment, please use the code below first and then write your code.
DO NOT DELETE THE FOLLOWING CODE
'''
import sys
try:
    input1 = sys.argv[1]
    input2 = sys.argv[2]
    input3 = sys.argv[3]
except:
    print("You didn't put any input when you run your code! Please add an input!")
    input1 = ""
    input2 = ""
    input3 = ""
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
import sklearn.model_selection as sksel
import sklearn.preprocessing as skprepro
import numpy as nump

input1 = [int(i) for i in input1.split(',')]
input2 = [int(i) for i in input2.split(',')]
input3 = [int(i) for i in input3.split(',')]

x1 = nump.array(input1).reshape(-1,1)
x3 = nump.array(input3).reshape(-1,1)
x2 = nump.array(input2).reshape(-1,1)

array = nump.hstack([x1.reshape(-1,1), x2.reshape(-1,1), x3.reshape(-1,1) ])
scaler_f = skprepro.StandardScaler()
## Проверяемая функция
copernam = scaler_f.fit_transform(array)
array_x = sksel.train_test_split(copernam,shuffle=False)[0]
## выводим итоговый результат
print("{}".format(nump.round(array_x,2)))