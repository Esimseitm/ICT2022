'''
The objective of this assignment is to clean the csv file of the attendance.
The path to the csv file is "attendance_to_clean.csv"
You can find it in the instruction folder.
List of installed and authorized packages :
    - csv
    - pandas
    - datetime
    - numpy
You cannot use other packages than the listed ones (except built-in default package in python).
You can write you code after this comment :
'''

#Your code here:
import pandas as pd
import datetime
import csv
import numpy as numpy1


# first STEP 
sorted = ['NaN','_','error']
# df = pd.read_csv(r"C:\Users\Manarbek\Desktop\ICT\Assignment\5\attendance_to_clean.csv", na_values = sorted)
df = pd.read_csv(r"attendance_to_clean.csv", na_values = sorted)

#REPLACE
for index, row in df.iterrows():
    try:
        int(row['NAME_STUDENT'])
        df.loc[index, 'NAME_STUDENT'] = numpy1.NAN
    except:
        pass    

#REPLACE
for index, row in df.iterrows():
    try:
        int(row['COUNT'])
    except:
        df.loc[index, 'COUNT'] = numpy1.NAN

#HIGH
for x in df.index:
      if df.loc[x, "BEGIN_HOUR"] > 17:
            df.loc[x, "BEGIN_HOUR"] = numpy1.NAN
#LOW  
for x in df.index:
      if float(df.loc[x, "COUNT"]) > 2:
        df.loc[x, 'COUNT'] = numpy1.NAN
#datetime  replace
for index, row in df.iterrows():
    try:
        datetime.datetime.strptime(row['DATE'], '%Y-%m-%d')
    except:
        df.loc[index, 'DATE'] = numpy1.NAN
# inplace use to save new changes
df.dropna(inplace = True) 

# CHanges to final result to output
for index, row in df.iterrows():
    df.loc[index, 'COUNT'] = float(row['COUNT'])
    df.loc[index, 'WEEK'] = int(row['WEEK'])
    if (datetime.datetime.strptime(row['DATE'], '%Y-%m-%d') < datetime.datetime(2022, 8, 1)):
        df.loc[index, 'DATE'] = numpy1.NAN


df = df.dropna()
# DELETE DUBLICATES AND SORTED
df = df.drop_duplicates().sort_values(by = ['NAME_STUDENT', 'DATE','BEGIN_HOUR', 'WEEK'])
# RESET_INDEX
df = df.reset_index( drop = True)
# PRINT FINAL RESULT
print(df)