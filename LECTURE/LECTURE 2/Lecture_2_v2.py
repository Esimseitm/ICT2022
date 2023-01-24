#!/usr/bin/env python
# coding: utf-8

# # Correction of the practice

# ## Check Python

# In[3]:


#Check that your python environnment is working:
print('Python working !')


# ## Open csv file with Python

# In[4]:


#installation => anaconda prompt => pip install csv
#Import the csv package
import csv


# In[5]:


#import the csv package and print every row in the console
#use "with open" instead of "file = open" (because otherwise the file could not close and take mmemory on your computer)
#You can only iterate one time on csvreader
#'r' = reading
#'w' = writing
#'a' = append (write)

file = open(r"D:\KBTU\2022-2023\Python Course\Course\Pratices\Practice_1\CAT.csv", 'r')
csvfile = csv.reader(file)
for row in csvfile:
    print(row)
file.close()
#! not efficient and risky !


# In[10]:


#I recommend : with open
#you can only iterate one time on it

with open(r"D:\KBTU\2022-2023\Python Course\Course\Pratices\Practice_1\CAT.csv", 'r') as file:
    csvfile = csv.reader(file)
    csvfile.__next__()
    for row in csvfile:
        print(row)
        break
    for row in csvfile:
        print(row)
        break
        


# In[13]:


#opened with a dictionnary

with open(r"D:\KBTU\2022-2023\Python Course\Course\Pratices\Practice_1\CAT.csv", 'r') as file:
    csvfile = csv.DictReader(file)
    for row in csvfile:
        print(row)


# ## Get CSV data into python console

# In[14]:


#import csv package
import csv


# In[20]:


#Create lists to store data (here a list of list to go faster)
list1, list2, list3 = [], [], []


# In[21]:


#Open csv file and store data in lists
#be careful with name of lists (ex : data, open)

with open(r"D:\KBTU\2022-2023\Python Course\Course\Pratices\Practice_1\CAT.csv", 'r') as file:
    csvfile = csv.reader(file)
    for row in csvfile:
        list1.append(row[0])
        list2.append(row[1])
        list3.append(row[2])


# In[23]:


#Check your lists
print(list1[:10])


# In[24]:


lists = [[] for i in range(7)]
print(lists)


# In[25]:


with open(r"D:\KBTU\2022-2023\Python Course\Course\Pratices\Practice_1\CAT.csv", 'r') as file:
    csvfile = csv.reader(file)
    for row in csvfile:
        for i in range(7):
            lists[i].append(row[i])
            


# In[27]:


print(lists[0][:10])
print(lists[1][:10])


# # Modify your data

# In[30]:


#First: Text into number (float)
for i in range(1,len(lists[1:])):
    lists[i] = [float(j) for j in lists[i][1:]]
    
print(lists[1][:10])


# In[37]:


#Second: date
# use datetime.datetime.strptime()
import datetime
date = "01/02/2025 15:06:13"
date_object = datetime.datetime.strptime(date, "%d/%m/%Y %H:%M:%S")
print(date_object.weekday())

#datetime object : calculte timedelta, weekdays


# In[44]:


#let's do it for all the list
#the format is :1962-01-02

# lists[0] = [datetime.datetime.strptime(j, "%Y-%m-%d") for j in lists[0][1:]]
print(lists[0][:10])


# In[ ]:


#For next week :
#Prepare your code : clean
#result : 7 lists with datetime and float


# # DataFrame

# ## What are the advantages

# ### Using lists to manage data

# In[60]:


#You have a list of informations on students:
#Create lists with these students

name = ['Brad', 'Angelina', 'Robert']
surname = ['Pitt', 'Joly', 'wilson']
age = [50, 40, 60]


# In[61]:


#Diplay your data
print(name)
print(surname)
print(age)
for i in range(0, len(name)):
    print(name[i], surname[i], age[i])


# In[62]:


# Operate on this lists : delete one value,   
#delete student angelina joly

for i in range(0, len(name)):
    if name[i] == 'Angelina' and surname[i] == 'Joly':
        index_to_delete = i

del name[index_to_delete]
del surname[index_to_delete]
del age[index_to_delete]
print(name)


# In[63]:


# Operate on this lists : add one value
# Elon musk 55

name.append('Elon')
surname.append('Musk')
age.append(55)
print(name)


# In[65]:


# Operate on this lists : extract information on one student

for i in range(0, len(name)):
    if name[i] == 'Elon' and surname[i] == 'Musk':
        print(name[i])
        print(surname[i])
        print(age[i])


# In[66]:


# Operate on this lists : extract information on several students
names_wanted = ['Elon', 'Robert']

for i in range(0, len(name)):
    if name[i] in names_wanted:
        print(name[i])
        print(surname[i])
        print(age[i])


# In[71]:


# Sort datas
#ordered by name
name = ['Brad', 'Robert', 'Elon',]
print(name)
name.sort()
print(name)
for i in range(0, len(name)):
    print(name[i], surname[i], age[i])


# # Pandas

# ## The pandas package

# In[ ]:


#Install pandas
# pip install pandas


# In[73]:


#Import pandas package
#Recommended as pd
import pandas as pd


# ## Let's create our first DataFrame

# In[75]:


#Create your first DataFrame
#Do not forget Uppercas for "D" and "F"
df = pd.DataFrame()
print(df)


# ## Populate it

# In[77]:


#Create a dictionnary with data from student
# name = ['Brad', 'Angelina', 'Robert']
# surname = ['Pitt', 'Joly', 'wilson']
# age = [50, 40, 60]

dictio = {'name' : ['Brad', 'Angelina', 'Robert'], 'surname' : ['Pitt', 'Joly', 'wilson'], 'age' : [50, 40, 60]}
print(dictio)


# In[79]:


#Create a dataframe from this dictionnary
df = pd.DataFrame(dictio)
print(df)


# In[80]:


# Display all your dataframe
print(df.head())


# In[86]:


# Display some lines of your dataframe
print(df['name'], '\n')
print(df['name'][1], '\n')


# In[ ]:


#Your turn:
#Create a empty dataframe
#Populate it with 3 lines of 6 columns 
#Ignore index (your dataframe should not have indexes) => Check on pandas.pydata.org documentation how to do it
#break at 17:55


# ## Populate with csv file

# In[ ]:


# Select some data of the dataframe


# In[ ]:


#display it


# In[ ]:


# Remove 2 last columns to be more clear


# In[ ]:


#display it


# In[ ]:


#Modify data for later use (date and float)


# In[ ]:


#YOUR TURN
#Use you data from last pratice to make a datafrme from it
#Choose your own names for the columns (check the documentation of read_csv method)
#Column names should be : 
#['Date', 'Open price', 'High price', 'Low price', 'Close price', 'Adjusted close price', 'Volume exchnaged']
#Try to automaticaly change Date into datetime object with the read_csv emthod 
#(check the documentation of read_csv method)


# ## Select data

# In[ ]:


# Display of the first data of the dataframe


# In[ ]:


#select only a line with index (iloc)


# In[ ]:


#Select several lines with indexes


# In[ ]:


#Select only a column with name (loc)


# In[ ]:


#Creation of a selection DataFrame


# In[ ]:


#Select a part of a Dataframe  ( () &() or .between)


# In[ ]:


#Sort the dataframe (.sort_value)   


# In[ ]:


#YOUR TURN
#From your dataframe: extract data with the following conditions:
# - Only in 2021
# - Only date, Volume and High
# - Only when high price is superior than 2019 average high price

