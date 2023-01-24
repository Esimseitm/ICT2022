#!/usr/bin/env python
# coding: utf-8

# # Lecture 9: Machine Learning

# In[3]:


pip install numpy


# In[5]:


pip install scikit-learn


# In[7]:


#import the packages (numpy and linear_model from scikit)
import numpy as np


# ## Introduction to numpy

# In[8]:


#Create your fisrt numpy array in 1 dimension
array = np.array([1, 2, 3, 4])
print(array)


# In[9]:


#Create your first 2 dimensionnal arry
array_2d = np.array([[1,2,3], [4,5,6]])
print(array_2d)


# In[10]:


#getting access to numpy array items
print(array_2d[0][1])


# In[13]:


#the copy and the view
list1 = [1,2,3]
list2 = list1.copy()
list2[0] = 55
print(list2)
print(list1)


# In[17]:


#Create your first 2 dimensionnal arry
array_2d = np.array([[1,2,3], [4,5,6]])
array_2d2 = array_2d.view()
array_2d3 = array_2d.copy()
array_2d2[0][1] = 55
array_2d3[0][1] = 1000
print(array_2d)
print(array_2d2)
print(array_2d3)


# In[18]:


#The shape of an array
print(array.shape)


# In[27]:


#reshape your array from 1D to 2D
array = np.array([1,2,3,4,5,6,7,8,9])
print(array)
array = array.reshape((3,3))
print(array)
#reshape your array from 1D to 2D
array = np.array([1,2,3,4,5,6])
print(array)
array = array.reshape((3,2))
print(array)
array = array.reshape((2,3))
print(array)
array = array.reshape((6,1))
print(array)


# In[32]:


#reshape your array from 1D to another D (with -1)
array = np.array([1,2,3,4,5,6,7,8])
print(array)
array = array.reshape((-1, 2))
print(array)
array = array.reshape((-1, 1))
print(array)


# In[36]:


#The avantage of numpy, the use of array for addition or multiplication for example
lis = [1, 2, 3]
arr = np.array(lis)
# print(lis +2)
print(arr +2 )
print(arr * arr )


# In[42]:


#YOUR TURN (5 minutes)
#Change this array [1,5,9,31,45,78]
#into this one:
#[[1 5]
#[9 31]
#[45 78]]
#It should be a copy not a view

arr = np.array([1,5,9,31,45,78])
print(arr.reshape((3,2)))
print(arr.reshape((-1,2)))
print(arr.reshape((3,-1)))

