#!/usr/bin/env python
# coding: utf-8

# # Correction of practice 7

# In[2]:


import pandas as pd
import csv


# In[3]:


list_of_symbols = []
with open(r"D:\KBTU\2022-2023\Python Course\Course\Pratices\Practice_7\list_symbols_euronext.csv", 'r') as file:
    csvfile = csv.reader(file)
    for row in csvfile:
        list_of_symbols += row
#         for i in row:
#             list_of_symbols.append(i)
        break
print(len(list_of_symbols))


# In[4]:


with open(r"D:\KBTU\2022-2023\Python Course\Course\Pratices\Practice_7\list_symbols_US.csv", 'r') as file:
    csvfile = csv.reader(file)
    for row in csvfile:
        list_of_symbols += row
#         for i in row:
#             list_of_symbols.append(i)
        break
print(len(list_of_symbols))


# In[7]:


list_df = []
for i in list_of_symbols[:10]:
    print(i)
    try:
        df_temp = pd.read_csv("https://query1.finance.yahoo.com/v7/finance/download/"+i+"?period1=0&period2=1661904000&interval=1d&events=history&includeAdjustedClose=true")
        df_temp['SYMBOL'] = i
        list_df.append(df_temp)
        
    except:
        print('error')
df = pd.concat(list_df, ignore_index = True)
print(df)


# In[ ]:


#to use read and to parquet => "pip install pyarrow" and "pip install fastparquet"


# In[8]:


df.to_csv(r"D:\KBTU\2022-2023\Python Course\Course\Pratices\Practice_7\the_csv_version.csv")


# In[9]:


df.to_parquet(r"D:\KBTU\2022-2023\Python Course\Course\Pratices\Practice_7\the_parquet_version.parquet")


# # Lecture 8: Data graph

# In[10]:


#import
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import seaborn as sns


# In[11]:


#load our data
#"pip install pyarrow" and "pip install fastparquet"
df_origin = pd.read_parquet(r"D:\KBTU\2022-2023\Python Course\Course\Lecture\Lecture_8\df_final_US_EUR.parquet")


# In[12]:


print(df_origin)


# In[14]:


#Select only a part of the data and reset_index (drop = True)
df_select = df_origin[df_origin['Name'] == 'GOOGL']
df_select.reset_index(inplace = True, drop = True)
print(df_select)


# In[ ]:


#install packages:
#pip install matplotlib


# In[15]:


#Make you first plot without x axis (default is index)
df_select.plot(y = 'Open')


# In[17]:


#you can also use another column as x axis
df_select.plot(x = 'Date', y = 'Open')


# In[18]:


#You can select even smaller amount of data
df_select = df_select[df_select['Date'] > datetime.datetime(2022,8,1)]
print(df_select)


# In[20]:


#use the bar kind
#use the kind attribute
df_select.plot(kind = 'bar', x = 'Date', y = ['Close', 'High'])


# In[21]:


#use the horizontal bar kind
df_select.plot(kind = 'barh', x = 'Date', y = 'Open')


# In[24]:


# use the histogram
df_select.plot(kind = 'hist', y = ['Open', 'Close'])


# In[25]:


# use the boxplot (kind  = 'box')
df_select.plot(kind = 'box', y = ['Open', 'Close'])


# In[26]:


# use the area
df_select.plot(kind = 'area', y = ['Open', 'Close'])


# In[29]:


#the scatter version
df_select.plot(kind = 'scatter', x = 'Date', y = 'Open')


# In[30]:


df_select.plot(kind = 'scatter', x = 'High', y = 'Open')


# In[35]:


#YOUR TURN (15 minutes)(with my parquet file install pyarrow and fastparquet package first)
#) or any csv data (price))
#%matplotlib inline
#Draw the evolution of the volume with the date in line
#Draw the scatter plot of the volume in function of the Open price
#import matplotlib.pyplot as plt
#plt.show()
import matplotlib.pyplot as plt

df.plot(x = 'Date', y = 'Volume')
plt.show()
df.plot(kind = 'scatter', x = 'Open', y = 'Volume')


# In[43]:


# Add column:
#percentage change for 'Open'
#price_day(i) - price_day(i-1) / price_day(i) *100
df = df_origin[df_origin['Name'] == 'GOOGL'].copy()
df.reset_index(inplace = True, drop = True)
perc = []
for index, line in df.iterrows():
    if index == 0:
        perc.append(0)
    else:
        perc.append((line['Open'] - df.loc[index-1, 'Open'] ) / line['Open'] *100)

df['perc_Open'] = perc
print(df)


# In[45]:


#YOUR TURN (10 minutes)
#Add the percentage change for all prices column and the volume
print(df.columns)
col = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
for i in col:
    perc = []
    for index, line in df.iterrows():
        if index == 0:
            perc.append(0)
        else:
            perc.append((line[i] - df.loc[index-1, i] ) / line[i] *100)

    df['perc_'+i] = perc
print(df)


# In[47]:


#print the link between datas (ex: perc or volume)
df.plot(kind = 'scatter', x = 'Volume', y = 'perc_Open')
df.plot(kind = 'scatter', x = 'perc_Close', y = 'perc_Open')


# In[48]:


#Use matplotlib also
#https://matplotlib.org one of the most famous package to plot
# the command : "%matplotlib inline" may be necessary
import matplotlib.pyplot as plt


# In[50]:


#create a figure with subplots and scatter
fig, ax = plt.subplots()
ax.scatter(df['Date'], df['Open'])
plt.show()


# In[55]:


#Is the volume and the perc of change are linked? And the perc and the voume of the day before?
fig, ax = plt.subplots(2)
ax[0].scatter(df['Volume'], df['perc_Open'])
ax[1].scatter(df['Volume'], df['perc_High'])
plt.show()


# In[56]:


#Seaborn to draw plots
#https://seaborn.pydata.org/
import seaborn as sns


# In[59]:


#draw your first plot, use data = df and the relplot() function, use linewidth to change the white order
sns.relplot(data = df, x = 'Date', y = 'Open', linewidth = 0, hue = 'perc_Open')


# In[61]:


#Change min et max (ylim)
sns.relplot(data = df, x = 'Date', y = 'Open', linewidth = 0, hue = 'perc_Open')
plt.ylim(60, 150)
plt.show()


# In[65]:


#another style with the set_style function
#list of style: https://seaborn.pydata.org/tutorial/aesthetics.html#seaborn-figure-styles
sns.set_style = "darkgrid"
sns.relplot(data = df, x = 'Date', y = 'Open', linewidth = 0, hue = 'perc_Open')


# In[ ]:




