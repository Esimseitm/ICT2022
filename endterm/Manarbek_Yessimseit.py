'''
-------------------------ENDTERM EXAM-----------------
DO NOT DELETE THE FOLLOWING CODE
'''
import sys
try:
    input1 = sys.argv[1]
except:
    pass
'''
In the following file, do not delete anything (comments, code, ...). Just add you code in every part (one per exercise).
Use my variable for input (if there is any), use my printing for output (if there is any).
You can upload your code to codepost.io to check the tests. A sucess in one test doesn't always mean than your exercise is correct,
a fail doesn't always mean that your exercise is wrong. I will check all codes.
At the end of exam, you should upload the last version of your code to codepost.io or to the online folder on Teams.
The only authorized packages are:
- pandas
- pyarrow
- fastparquet
- numpy
- sklearn
- matplotlib
- datetime

'''

if input1 == '1':
# ----------------------EXERCISE 1 - Data Cleaning--------------------------------------
# Instructions:
# Open the dataframe (Ex_1_price_to_clean_v15.parquet) with the read_parquet() function of the pandas package.
# If you upload your code to codepost use the the following path in the read_parquet() function : "Ex_1_price_to_clean_v15.parquet".
# Remove the duplicated line(s) from the dataframe, reset the indexes, sort it by the date column and print it.
# Do not change the format of columns (for example, if one column has int values, don't change it to float)
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
# df_origin = pd.read_parquet(r"C:\Users\Manarbek\Desktop\endtermict\Ex_1_price_to_clean_v15.parquet")
# print(df_origin)
df_origin = pd.read_parquet(r"Ex_1_price_to_clean_v15.parquet")
for index, lines in df_origin.iterrows():
    try:
        x = float(lines['Low'])
    except:
        df_origin.loc[index, 'Low'] = np.nan

for index, lines in df_origin.iterrows():
    df_origin['Adj Close'] = df_origin['Adj Close'].astype(float)
    df_origin['Volume'] = df_origin['Volume'].astype(float)
    df_origin['Open'] = df_origin['Open'].astype(float)
    df_origin['High'] = df_origin['High'].astype(float)
    df_origin['Low'] = df_origin['Low'].astype(float)
    df_origin['Close'] = df_origin['Close'].astype(float)

df_origin.dropna(inplace = True)
df_origin = df_origin.sort_values(by=['Date'])
df_origin.reset_index(drop = True, inplace = True)
df = df_origin


# Here is the printing instruction (where df is the final dataframe cleaned, sorted by date and with reset indexes)
print(df)
# ---------------------End of EXERCISE 1 --------------------------------------

elif input1 == '4':
# ----------------------EXERCISE 4 - Machine Learning II--------------------------------------
# Instructions:
# You have a model (linear regression) trained with two features and a label : feature1, feature2 and label.
# What is the prediction of this model for three samples : 
#	- feature 1 : 1 and feature 2 : 151
#	- feature 1 : -9 and feature 2 : 178
#	- feature 1 : -10 and feature 2 : 191
# You can find the wanted predictions in the file named Ex_4_predictions_V15.txt

import sklearn.linear_model as skmod
import numpy as np
feature1 = np.array([-5, 5, -9, 9, 1, 5, 3, 3, 7, -1, -3, -3, 4, 6, 3, -5, -6, -2, 0, 2])
feature2 = np.array([143, 198, 146, 194, 169, 141, 199, 180, 199, 104, 126, 144, 125, 180, 168, 198, 175, 191, 182, 190])
label = np.array([16.0, -16.0, 21.0, -40.0, -2.0, -19.0, -11.0, -8.0, -22.0, 5.0, 13.0, 16.0, -8.0, -25.0, -6.0, 15.0, 14.0, 6.0, 3.0, -5.0])
model = skmod.LinearRegression().fit(np.hstack([feature1.reshape(-1,1), feature2.reshape(-1,1)]), label.reshape(-1,1))
x_predict = np.array([[1, 151], [-9, 178], [-10,191]])
predictions = model.predict(x_predict)
	





# Here is the command to print the final data (where predictions is all the predictions of your model.)
	print(np.around(predictions,3))
# ----------------------End of EXERCISE 4 --------------------------------------
