#!/usr/bin/env python
# coding: utf-8

# # Correction of the practice

# ## Check Python

# In[1]:


#Check that your python environnment is working:
print("It's working!")


# ## Open csv file with Python

# In[2]:


#installation => anaconda prompt => pip install csv
#Import the csv package
import csv


# In[11]:


#import the csv package and print every row in the console
#'r' : read
#'w' : write
#'a' : append
#you can iterate only one time on csvfile

file = open(r"D:\KBTU\2022-2023\Python Course\Course\Pratices\Practice_1\CAT.csv",             'r')
csvfile = csv.reader(file)
# csvfile.__next__()
for row in csvfile:
    print(row)
    break
for row in csvfile:
    print(row)
    break
    
file.close() #Important!


# In[16]:


#I recommend : with open
#you can only iterate one time on it

with open(r"D:\KBTU\2022-2023\Python Course\Course\Pratices\Practice_1\CAT.csv",             'r') as file:
    csvfile = csv.reader(file)
    csvfile.__next__()
    for row in csvfile:
        print(row)


# In[19]:


#opened with a dictionnary
with open(r"D:\KBTU\2022-2023\Python Course\Course\Pratices\Practice_1\CAT.csv",             'r') as file:
    csvfile = csv.DictReader(file)
    for row in csvfile:
        print(row)
        print(row['Open'])


# ## Get CSV data into python console

# In[20]:


#import csv package
import csv


# In[26]:


#Create lists to store data (here a list of list to go faster)
list1, list2, list3 = [], [], []

#Do not do that
# list1 = list2 = []
# list1.append(5)
# print(list1, list2)

#If you use names of columns : high, volume, open (Warning : open)
#do not do : open = []


# In[27]:


#Open csv file and store data in lists
#be careful with name of lists (ex : data, open)
with open(r"D:\KBTU\2022-2023\Python Course\Course\Pratices\Practice_1\CAT.csv",             'r') as file:
    csvfile = csv.reader(file)
    csvfile.__next__()
    for row in csvfile:
        list1.append(row[0])
        list2.append(row[1])
        list3.append(row[2])


# In[29]:


#Check your lists
print(list1[:10])
print(list2[:10])


# In[30]:


#create lists
lists = [[] for i in range(7)]
print(lists)


# In[31]:


#take csv data.
with open(r"D:\KBTU\2022-2023\Python Course\Course\Pratices\Practice_1\CAT.csv",             'r') as file:
    csvfile = csv.reader(file)
    csvfile.__next__()
    for row in csvfile:
        for i in range(0, len(row)): lists[i].append(row[i])
                       


# In[35]:


#Check your lists
print(lists[0][:10])
print(lists[1][:10])


# # Modify your data

# In[33]:


#check type
print(type(lists[0][0]))


# In[36]:


#First: Text into number (float)
#lists 1 to 6
for i in range(1,6):
    lists[i] = [float(j) for j in  lists[i] ]
    
print(lists[1][:10])  


# In[38]:


#Second: date
#import datetime
import datetime


# In[39]:


#first whats is the format ?
print(lists[0][0])
# 1962-01-02
print(datetime.datetime.strptime("1962-01-02", "%Y-%m-%d"))


# In[40]:


#let's do it for all the list
lists[0] = [datetime.datetime.strptime(j, "%Y-%m-%d") for j in  lists[0] ]


# In[45]:


print(lists[0][1])
print(lists[0][1].weekday())


# In[ ]:


#For next practice :
#Prepare your code : clean
#result : 7 lists with datetime and float


# # DataFrame

# ## What are the advantages

# ### Using lists to manage data

# In[62]:


#You have a list of informations on students:
#Create the list

name = ['Brad', 'Leila', 'Saule']
surname = ['Pitt', 'Beken', 'Arystanbek']
age = [50, 18, 19]
print(name)


# In[48]:


#Diplay your data
print(name[:2])
print(surname[:2])
print(age[:2])


# In[60]:


# Operate on this lists : delete one value,   
#delete leila
print(len(name))
for i in range(0,len(name)):
    if name[i] == 'Leila' and surname[i] == 'Beken':
        index_delete = i
   
del name[index_delete]
del surname[index_delete]
del age[index_delete]
print(name[:2])
print(surname[:2])
print(age[:2])


# In[ ]:


# Operate on this lists : add one value
#easy


# In[63]:


# Operate on this lists : extract information on one student
for i in range(0,len(name)):
    if name[i] == 'Leila' and surname[i] == 'Beken':
        print(name[i])
        print(surname[i])
        print(age[i])


# In[64]:


# Operate on this lists : extract information on several students
# 
names_wanted = ['Leila', 'Brad']
for i in range(0,len(name)):
    if name[i] in names_wanted:
        print(name[i])
        print(surname[i])
        print(age[i])


# In[68]:


# Sort datas
surname.sort()
print(name[:])
print(surname[:])
print(age[:])


# # Pandas

# ## The pandas package

# In[ ]:


#Install pandas
# pip install pandas


# In[69]:


#Import pandas package
#use pd
import pandas as pd


# ## Let's create our first DataFrame

# In[71]:


#Create your first DataFrame
#Do not forget Uppercas for "D" and "F"
df = pd.DataFrame()
print(df)


# ## Populate it

# In[ ]:


#Create a dictionnary with data from student
name = ['Brad', 'Leila', 'Saule']
surname = ['Pitt', 'Beken', 'Arystanbek']
age = [50, 18, 19]


# In[76]:


#Create a dataframe from this dictionnary
dictio = {'key' : [100, 50], 'another_key' : 1}
print(dictio)
dictio = {'name' : name, 'surname':surname , 'age': age}
df = pd.DataFrame(dictio)


# In[77]:


# Display all your dataframe
print(df)


# In[78]:


#Your turn:
#Create a empty dataframe
#Populate it with 3 lines of 6 columns (invent your own data)
#end at 17:00
dictio = {'1' : [1,2,3], 
          '2' : [11,2,3], 
          '3' : [12,212,35], 
          '4' : [13,25,33], 
          '5' : [14,234,37], 
          '6' : [15,2,38]}

df = pd.DataFrame(dictio)
print(df)


# ## Populate with csv file

# In[121]:


#download csv file
import pandas as pd

df = pd.read_csv(r"D:\KBTU\2022-2023\Python Course\Course\Pratices\Practice_1\CAT.csv")
print(df)
#"\" => dataframe continuer next lines
#"..." undisplayed lines


# In[81]:


# Select some data of the dataframe
print(df.head(20))
print(df.tail(20))


# In[91]:


# Remove 2 last columns to be more clear
del df['Volume']
del df['Adj Close']
print(df)


# In[85]:


#Modify data for later use (date and float)
#float ?
print(type(df['Open'][0]))
print(type(df['Date'][0]))


# In[117]:


#YOUR TURN
#Use you data from last pratice to make a dataframe from it
#Choose your own names for the columns (check the documentation of read_csv method)
#Column names should be : 
#['Date', 'Open price', 'High price', 'Low price', 'Close price', 'Adjusted close price', 'Volume exchanged']
#Try to automaticaly change Date into datetime object with the read_csv emthod 
#(check the documentation of read_csv method)
#17:25

df = pd.read_csv(r"D:\KBTU\2022-2023\Python Course\Course\Pratices\Practice_1\CAT.csv",
                header = 0,
                 names = ['Date', 'Open price', 'High price', 'Low_price', 'Close price', 'Adjusted close price', 'Volume exchanged'],
                 parse_dates = ['Date']
                )
print(df)
print(type(df['Date'][0]))
print(df['Date'][0])


# In[ ]:


#~ 65 students
#~ 90 crosses on attendance
#=> one attendance per hour next lecture


# ## Select data

# In[97]:


# Display of the first data of the dataframe
# print(df[:10])
# print(df['Date'])
# loc function => [index, column]
print(df.loc[4, 'High'])


# In[100]:


#select only a line with index (iloc)
print(df.iloc[4, 2])


# In[105]:


#Select several lines with indexes

print(df.loc[range(2153,2160), ['Date', 'High']])

print(df.iloc[range(2153,2160), [1, 3]])


# In[107]:


#Creation of a selection DataFrame
print(  df['Open'] > 100   )

selection_df = df['Open'] > 100


# In[109]:


#select a part.
print(df[selection_df])


print(df[ df['Close'] < 100 ])


# In[111]:


#Select a part of a Dataframe  ( () &() or .between())
print(df[ (df['Close'] < 100) & (df['Open'] > 100) ])

print(df[ (df['Close'] < 100) | (df['Open'] > 100) ])


# In[114]:


begin = datetime.datetime(year = 2020, month = 5, day = 15)
print(df[ df['Date'] > begin ])


# ##### Sort the dataframe (.sort_values)
# print(df.sort_values('Low Price'))

# In[123]:


# Sort the dataframe (.sort_values)
print(df.sort_values('Open'))


# In[145]:


#YOUR TURN
#From your dataframe: extract data with the following conditions:
# - Only in 2021
# - Only date, Volume and High
# - Only when high price is superior than 2019 average high price
#17:55

# print(df)
df = pd.read_csv(r"D:\KBTU\2022-2023\Python Course\Course\Pratices\Practice_1\CAT.csv",
                parse_dates = ['Date']
                )
begin_mean = datetime.datetime(year = 2019, month = 1, day = 1)
end_mean = datetime.datetime(year = 2020, month = 1, day = 1)

begin = datetime.datetime(year = 2021, month = 1, day = 1)
end = datetime.datetime(year = 2022, month = 1, day = 1)


df = df.loc[:, ['Date', 'Volume', 'High']]

mean = df[ (df['Date'] > begin_mean) & (df['Date'] < end_mean) ]['High'].mean()

df = df[ (df['Date'] > begin) & (df['Date'] < end) & (df['High']  > mean) ]

# print(df)



# mean = df[ (df['Date'] > begin_mean) & (df['Date'] < end_mean) ]['High'].mean()
# print(mean)

# print(df.loc[:, ['Date', 'Volume', 'High']][ (df['Date'] > begin) & (df['Date'] < end) & (df['High']  > mean) ])


print(df.loc[:, ['Date', 'Volume', 'High']]       [ (df['Date'] > begin) &       (df['Date'] < end) &        (df['High']  > (df[ (df['Date'] > begin_mean) & (df['Date'] < end_mean) ]['High'].mean()))])


# In[ ]:




