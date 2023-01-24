#!/usr/bin/env python
# coding: utf-8

# # Correction of practice 6

# In[ ]:


# import packages
import requests
from bs4 import BeautifulSoup


# In[ ]:


headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'}
resp = requests.get('https://news.google.com/search?q=apple', headers = headers)
print(resp.content)


# In[ ]:


soup = BeautifulSoup(resp.content)
print(soup.prettify())


# In[ ]:


for i in soup.find_all('a', class_ = "DY5T1d RZIKme"):
    print(i.text)


# In[ ]:


for i in soup.find_all('a', class_ = "DY5T1d RZIKme"):
    print("www.news.google.com" + i['href'][1:])


# In[ ]:


import datetime
for i in soup.find_all('time', class_ = "WW6dff uQIVzc Sksgp slhocf"):
    t = i['datetime']
    t = datetime.datetime.strptime(t, '%Y-%m-%dT%H:%M:%SZ')
    print(t)


# In[ ]:


url = "http://www.news.google.com" + soup.find('a', class_ = "DY5T1d RZIKme")['href'][1:]

r = requests.get(url, headers= headers)
s = BeautifulSoup(r.content)
print(s.prettify())


# In[ ]:


print(s.find('a', jsname = "tljFtd").text)


# # Lecture 7 : Data cleaning

# In[ ]:


# import
import pandas as pd
import numpy as np


# In[ ]:


# Read csv file into a pandas dataframe
df = pd.read_csv(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_7\csv_to_clean.csv")
print(df)


# ## Finding missing values

# In[ ]:


#Find the standard missing values isnull function
print(df.isnull().sum())


# In[ ]:


#Non standard missing values : na_values in the read_csv function
#use of unique function to identify them
a = ['na', '--']
df = pd.read_csv(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_7\csv_to_clean.csv",
                na_values = a)
print(df)


# In[ ]:


#Unexpected format missing values : check if value can be int for example
# print(df)
for index, lines in df.iterrows():
    try:
        a = int(lines['OWN_OCCUPIED'])
        print(a)
        df.loc[index, 'OWN_OCCUPIED'] = np.nan
    except:
        pass
print(df)


# In[ ]:


#Check the sum of missing values
print(df.isnull().sum().sum())


# In[ ]:


try:
    prit('hi')
except:
    print('ho')


# In[ ]:


#YOUR TURN (15 minutes)
#Find all missing values in the provided dataframe
#Check all the null
#Find the other types of missing values
#There are '-', 'ERROR', wrong date, 'NaN', no data
#and then break
import datetime
a = ['ERROR', '-']
df = pd.read_csv(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_7\Apple_price_to_clean.csv",
                na_values = a)
print(df)
for index, lines in df.iterrows():
    try:
        a = datetime.datetime.strptime(lines['Date'], '%Y-%m-%d')
    except:
        print(lines['Date'])
        df.loc[index, 'Date'] = np.nan
print(df)


# ## Replacing missing values

# In[ ]:


#delete lines with dropna with subset and inplace aeguments

df.dropna(inplace = True, subset = ['PID'])
print(df)


# In[ ]:


# Location based replacement with the loc function
df.loc[2, 'ST_NUM'] = 200
print(df)


# In[ ]:


# Replace missing values with a number (fillna() function with inplace arg)
df.fillna(100, inplace = True)
print(df)


# In[ ]:


#Replacing the missing values with a median 
#(calculate median and then use the replace with a number)
print(df['NUM_BEDROOMS'].mean())
df['NUM_BEDROOMS'].fillna(df['NUM_BEDROOMS'].mean(), inplace = True)
print(df)


# In[ ]:


#Replacing the values by the one before or after : df.fillna(method='bfill')
print(df)
df.fillna(method = 'bfill', inplace = True)
print(df)


# In[ ]:


#YOUR TURN (5 minutes)
#replace all the missing values in the previous dataframe with the frontfilling method 
#put 0 for the first ones


# ## Removing useless data

# In[ ]:


#Use the drop() function with inplace and axis arg
#axis 0 => lines
#axis 1 => columns
df.drop(['ST_NUM'], axis = 0, inplace = True)
print(df)


# In[ ]:


#Use the drop duplicates to remove useless lines
df.drop_duplicates(inplace = True)
print(df)


# In[ ]:


#YOUR TURN 5 minutes
#Drop all duplicates in your df
#11 duplicated rows


# ## Outliers

# In[ ]:


#Read csv with clean data
a = ['na', '--']
df = pd.read_csv(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_7\csv_to_clean.csv",
                na_values = a)
print(df)


# In[ ]:


#With the describe method
print(df.describe())


# In[ ]:


# With the plot method
df.plot(y = 'SQ_M')


# In[ ]:


#SELECT the datas
df = df[df['SQ_M'] < 10000]
df.plot(y = 'SQ_M')


# In[ ]:


#YOUR TURN
#Find the outliers in your dataset and remove them

