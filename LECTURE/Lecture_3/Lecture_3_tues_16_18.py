#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#I will be online from 22 september to 02 october => teams or videos
#Thursday 29/09 => 9am from 11:59 am on teams


# # Creating a DataFrame

# In[1]:


import pandas as pd


# In[2]:


print(pd.__version__)


# ## Using a dictionary

# In[3]:


# Data :
# Brand : 'Coca', 'pepsi', 'Sprite', 'water'
# Taste : 5, 6, 9, 8
# Sugar content : 'high', 'high', 'high', 'low'
# YOUR TURN : Create a dataframe from the dictionnary (10 minutes) => 16:22
df = pd.DataFrame({'brand' : ['Coca', 'pepsi', 'Sprite', 'water'], 
                   'taste' : [5, 6, 9, 8],
                  'Sugar_content' : ['high', 'high', 'high', 'low']})


# In[4]:


print(df)


# In[6]:


# Take csv data to dictionary and create dataframe
import csv
with open(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_3\Apple_price_csv.csv", 'r') as file:
    csvfile = csv.DictReader(file)
    df = pd.DataFrame(csvfile)
    
print(df)


# ## Using a list

# In[7]:


# Data :
# Brand : 'Coca', 'pepsi', 'Sprite', 'water'
#Taste : 5, 6, 9, 8
#Sgar content : 'high', 'high', 'high', 'low'
#YOUR TURN : 
#Create a dtaframe from the lists (10 minutes) => 16.35
brand = ['Coca', 'pepsi', 'Sprite', 'water']
taste = [5, 6, 9, 8]
sugar_content = ['high', 'high', 'high', 'low']  
df = pd.DataFrame([brand, taste, sugar_content] )
print(df)


# In[11]:


#The zip function
a = [1, 2, 3]
b = ['a', 'b', 'c']
list0 = list(zip(a, b))
df = pd.DataFrame(list0)
print(df)


# In[16]:


#YOUR TURN
# Come back to your previous dataframe and use the zip function (5 minutes) => 16:42
df = pd.DataFrame(list(zip(brand, taste, sugar_content)), columns = ['brand', 'taste', 'sugar_content'])
print(df)
print(list(zip(brand, taste, sugar_content)))


# In[21]:


#With the csv file (easier)
import csv
with open(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_1\Apple_price_csv.csv", 'r') as file:
    csvfile = csv.reader(file)
    name_column = csvfile.__next__()
    df = pd.DataFrame(csvfile, columns = name_column)
    
print(df)


# ## Using read_csv method

# In[54]:


#create dataframe from read_csv method
df = pd.read_csv(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_1\Apple_price_csv.csv")
print(df)


# In[82]:


# with the date in datetime object
df = pd.read_csv(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_1\Apple_price_csv.csv",
                parse_dates = ['Date'])

print(type(df['Date'][0]))


# # Modify the dataframe

# In[46]:


# Change the column names (2 methods)
df.columns =['Date', 'Open_price', 'High_price', 'Low', 'Close', 'Adj Close', 'Volume']
df = df.rename(columns = {'Date' : 'Date_and_time'})
print(df)


# In[47]:


#sort values
df = df.sort_values('Open_price')
print(df)


# In[48]:


# Reset index of dataframe
df = df.reset_index(drop = True)
print(df)


# In[43]:


#Use your own index: (set_index function)
df = df.sort_values('Date_and_time')
df = df.set_index(['Date_and_time'])
print(df)


# In[49]:


# use several indexes

df = df.sort_values('Date_and_time')
df = df.set_index(['Date_and_time', 'Open_price'])
print(df)


# In[51]:


#Your TURN
#Use your csv data to get your df and put dates as index (10 minutes) 17:05
# with the date in datetime object
df = pd.read_csv(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_1\Apple_price_csv.csv",
                parse_dates = ['Date'])
df = df.set_index(['Date'])
print(df)


# In[52]:


# Why indexes and not columns (use %timeit function)
get_ipython().run_line_magic('timeit', "print('a')")


# In[56]:


print(df)


# In[62]:


#display columns of dataframe (2 methods)
get_ipython().run_line_magic('timeit', "df[df['Open'] == 26.772499]")


# In[63]:


get_ipython().run_line_magic('timeit', 'df.loc[1]')


# In[67]:


#Adding a new columns to your DataFrame
df['Name'] = ['Gaétan' for i in range(0,1763)]
df['Surname'] = 'Chardon'
print(df)


# In[73]:


# Apply a function to your dataframe
df['double_open'] = df['Open'] *2
def my_function(x):
    return int(x**2)
df['square_open'] = df['Open'].apply(my_function)
print(df)


# In[75]:


# iterate on a Dataframe
for index, items in df.iterrows():
    print(items)


# In[79]:


# Concatenate two dataframes
df1 = pd.DataFrame({'brand' : ['Coca', 'pepsi', 'Sprite', 'water'], 
                   'taste' : [5, 6, 9, 8],
                  'Sugar_content' : ['high', 'high', 'high', 'low']})
df2 = pd.DataFrame({'brand' : ['Coca', 'sdg', 'sdfe', 'wssdfer'], 
                   'taste' : [5, 6, 9, 8],
                  'Sugar_content' : ['high', 'high', 'high', 'low']})
df = pd.concat([df1, df2])
# df = df.reset_index(drop = True)
print(df)


# In[80]:


# Delete the duplicate drop_duplicates function (see doc)
df = df.drop_duplicates()
print(df)


# # Save the Dataframe

# In[83]:


#Save it to excel
writer = pd.ExcelWriter(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_3\df.xlsx")
df.to_excel(writer, 'DataFrame')
writer.save()


# In[86]:


#SAve it to csv
df.to_csv(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_3\df.csv", index = False)
print(pd.read_csv(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_3\df.csv"))


# In[ ]:


# save it to json
df.to_json(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_3\df.json")


# # Useful functions

# In[88]:


# Getting info about the dataframe
print(df.info())


# In[89]:


# Getting shapes of dataframe
print(df.shape)


# In[90]:


# description of the dataframe
print(df.describe())


# In[92]:


# Count similar values (.value_counts() method)
print(df.value_counts('Open'))


# In[93]:


# get correlation
print(df.corr())


# In[94]:


# Quick plotting
#pip install matplotlib
df.plot(x = 'Date', y = 'Open')


# In[ ]:


#YOUR TURN 
#Plot the evolution of volume exchanged through the time of your csv file (10 minutes) 17:40

