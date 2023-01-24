#!/usr/bin/env python
# coding: utf-8

# # Correction of practice 9

# In[ ]:


#See the excel file


# # Lecture 10: Machine Learning II

# ## Installation of packages

# In[ ]:


#Install the package numpy and scikit-learn


# In[1]:


pip install numpy


# In[2]:


pip install scikit-learn


# In[3]:


#import the packages
import numpy as np
import sklearn.linear_model as skmod


# ## Reminder of numpy

# In[5]:


#Our data: the goats and the altitude
alt = [3.25, 0.816, 4.376, 1.314, 3.982, 2.957, 2.482, 3.7]
n_goats = [21, 22, 13, 25, 17, 23, 23, 27]


# In[8]:


#Reorder your arrays
arr_x = np.array(alt)
arr_x = arr_x.reshape(-1,1)
print(arr_x)
arr_y = np.array(n_goats)
arr_y = arr_y.reshape(-1,1)
print(arr_y)


# ## The linear regression

# In[9]:


#Plot your data first
import matplotlib.pyplot as plt
plt.scatter(arr_x, arr_y)


# In[10]:


#Create a linear regression model: LinearRegression()
model = skmod.LinearRegression()


# In[ ]:


#some parameters than you can change:
#fit_intercept (consider b=0 if False, default is True)


# In[11]:


#Train your model
model_trained = model.fit(arr_x, arr_y)


# In[15]:


#get the result: the intercept (b)(.intercept_), 
#the coeff (w1)(.coef_) and the R2 (.score(x, y))
print(model_trained.coef_) #w1
print(model_trained.intercept_)#b
#equation of my model: y'=-1.829*x + 26.60
print(model_trained.score(arr_x, arr_y))


# In[16]:


#draw your model on the graph
plt.scatter(arr_x, arr_y)
plt.plot([0,5], [-1.829*0+ 26.60, -1.829*5+ 26.60])


# In[19]:


#Now use your model to predict data (.predict(x))
x_predict = np.array([[1], [2], [3]])
print(x_predict)
print(model.predict(x_predict))


# In[20]:


#Predict the result without predict but with intercept and coeff
print(model.coef_*1+ model.intercept_)
print(model.coef_*2+ model.intercept_)
print(model.coef_*3+ model.intercept_)


# In[ ]:


#YOUR TURN (15 minutes)
#Use the folowwing data to create a linear regression model and train it:
# feature 1 | Label
#--------------------
#   25      |   80
#   100     |   254
#   30      |   152
#   5       |   4
#   85      |   271

#The coeff use to preduce data was 2,56 and the intercept was 23
#How close are you (How high is the score)?
#Draw the graph of the datas and your prediction


# In[25]:


arr_x = np.array([[25], [100], [30], [5], [85]])
arr_y = np.array([[80], [254], [152], [4], [271]])
model = skmod.LinearRegression()
model = model.fit(arr_x, arr_y)
print(model.coef_)
print(model.intercept_)
print(model.score(arr_x, arr_y))
plt.scatter(arr_x, arr_y)
plt.plot([0, 100], model.predict(np.array([[0], [100]])))


# ## For mutiple dimension
# 

# In[26]:


#Our datas: the students work
x1 = [9, 10, 16, 22, 17, 7, 10, 24, 15]
x2 = [14, 18, 1, 22, 6, 12, 4, 28, 22]
y = [42.8, 48.8, 36.8, 81.1, 44.8, 32.4, 28.8, 100, 73.1]


# In[27]:


#Draw the data in 2d with colors
plt.scatter(x1, x2, c = y, cmap = 'Reds')


# In[28]:


#Draw in 3D
ax = plt.subplot(projection='3d')
ax.scatter(x1, x2, y)


# In[31]:


#Transform our data for scikit-learn
x1 = np.array(x1).reshape(-1,1)
x2 = np.array(x2).reshape(-1,1)
y = np.array(y).reshape(-1,1)
x = np.hstack([x1, x2])
print(x)


# In[32]:


#create and train the model
model = skmod.LinearRegression()
model = model.fit(x,y)


# In[33]:


#get the result and write the equation
print(model.coef_)
print(model.intercept_)
#Equation is: y' = 2.12*x1 + 1.69*x2 -1.51


# In[34]:


#Prediction with the model
# 15 hours/week, 20 classes
# 5 hours/week, 2 classes
x_for_predict = np.array([[15, 20], [5, 2]])
print(x_for_predict)
print(model.predict(x_for_predict))


# In[40]:


#use the model for prediction
print(model.coef_[0][0] * 15 + model.coef_[0][1] * 20 + model.intercept_)


# In[ ]:


#YOUR TURN (15 minutes)
#Here is your data
#x1 = [7, 0, 3, 3, 5]
#x2 = [2, 0, 7, 3, 9]
#y = [44, 0, 25, 21, 39]
#Make the linear regression between these datas.
#What are the weights and the bias? Write the final equation of your model.
#What would be the prediction for x1 = 5 and x2 = 6


# ## The polynomial regression

# In[41]:


#Remember: A polynomial regression of degree two is just 
#a linear regression with two features where the second feature
#is the square of the first one


# In[42]:


#Our data: the number of goats
alt = [3.25, 0.816, 4.376, 1.314, 3.982, 2.957, 2.482, 3.7]
n_goats = [21, 22, 13, 25, 17, 23, 23, 27]


# In[46]:


#The simplest way to do it: the square method
alt_sq = []
for i in alt:
    alt_sq.append(i**2)
# print(alt_sq)

x1 = np.array(alt).reshape(-1,1)
x2 = np.array(alt_sq).reshape(-1,1)
y = np.array(n_goats).reshape(-1,1)
x = np.hstack([x1, x2])
print(x)


# In[47]:


#Create the model and train it
model = skmod.LinearRegression()
model = model.fit(x, y)


# In[48]:


#show the coefficients
print(model.coef_)
print(model.intercept_)
#Equation: 
#with x1 and x2: y' = 8.23*x1 - 1.967*x2 + 16.66
#with x1 and x1^2: y' = 8.23*x1 - 1.967*x1**2 + 16.66


# In[60]:


#Draw your datas and the model
plt.scatter(x1, y) #draw the observation
x_predict = np.arange(0,5,0.1) #range function with integer only
x_predict = x_predict.reshape(-1,1) #to transform it into column
x_predict_sq = x_predict*x_predict #the second feature = x1**2
x_predict_final = np.hstack([x_predict, x_predict_sq]) #my 2 columns matrix
y_predict = model.predict(x_predict_final) #prediction from the x
# print(y_predict)
plt.plot(x_predict, y_predict) #draw the graph with w (not x2)

plt.plot([0,5], [-1.829*0+ 26.60, -1.829*5+ 26.60])


# In[ ]:


#YOUR TURN (15 minutes)
#Find the link between these values (use linear and polynomial regression)
#
# feature  Label
# 13       505
# 3        35
# 17       836
# 0        -6
# 2         16
#The equation used is 2,56*x^2 + x*6 -6, 
#Can you find it with your regression?


# In[71]:


arr_x = np.array([13, 3, 17, 0, 2]).reshape(-1,1)
arr_x2 = arr_x*arr_x
x = np.hstack([arr_x, arr_x2])
y = np.array([505, 35, 836, -6, 16]).reshape(-1,1)
# print(x)
# print(y)
model = skmod.LinearRegression().fit(x, y)
print(model.coef_)
print(model.intercept_)
print(model.score(x,y))


# In[67]:


#Let's show the difference with a linear regression - make the linear model

model = skmod.LinearRegression().fit(arr_x, y)
print(model.coef_)
print(model.intercept_)


# In[69]:


#draw the datas, the linear and polynomial model on the same graph
plt.scatter(arr_x, y)


# In[ ]:





# In[ ]:




