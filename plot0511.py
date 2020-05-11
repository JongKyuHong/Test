#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt # 시각화 기본 프로그램 , pyplot 그래프를 그리는 기능들을 모아놓음
import pandas as pd# 데이터 처리 프로그램
from sklearn.linear_model import LinearRegression # 머신러닝의 종합 패키지 sklearn 안의 선형회귀
import seaborn as sns
import numpy as np # 


# In[3]:


matplotlib.pyplot.plot([1,2],[10,20],'o')


# In[36]:


plt.figure(figsize=(10,50))
plt.plot([1,2,5,9,3],[10,20,36,14,22],'^')


# In[8]:


x = np.linspace(0,14,100)
y = np.sin(x)
y1 = np.sin(x) * 2
y2 = np.sin(x) * 4


# In[9]:


plt.plot(x,y,'yo')


# In[10]:


plt.plot(x,y,x,y1,x,y2)


# In[11]:


tips = sns.load_dataset("tips")


# In[12]:


type(tips)


# In[13]:


tips.head()


# In[22]:


tips['total_bill'].head(5)


# In[16]:


tips.smoker.head(10)


# In[17]:


sns.boxplot(x='day',y='total_bill',data=tips)


# In[19]:


sns.boxplot(x='day',y='size',data=tips)


# In[20]:


sns.boxplot(x='day',y='tip',data=tips)


# In[26]:


sns.boxplot(x='day',y='total_bill',hue='sex',data=tips)


# In[37]:


import seaborn as sns


# In[39]:


tips = sns.load_dataset("tips")
tips.head(10)


# In[40]:


tips.shape


# In[42]:


tips.head(5)


# In[43]:


tips.tail(5)


# In[44]:


tips.columns


# In[47]:


tips.describe() # 요악값 확인


# In[49]:


tips.isnull().sum() # 결측치가 몇개가있는지


# In[51]:


tips.shape


# In[59]:


sns.barplot(x='day',y='total_bill',hue='sex',data=tips); #데이터가 어떤 구간안에 일정하게 있을때 그걸 범주형이라고 한다
plt.title("barplot")


# In[55]:


#히스토그램은 연속형 데이터일때 찍어준다(정규분포인지 아닌지 확인하기 위해서),정규화 
#,log를 씌워주는 식으로 정규화를 한다


# In[69]:


### 회귀직선 함수 - total_bill과 tips의 관계
### 회귀직선 함수 - hue이용 담배를 피는사람과 안피는사람을 찍어라

sns.lmplot(x='total_bill',y='tip',hue='smoker',data=tips)


# In[71]:


fg = sns.load_dataset('flights')
fg.head()


# In[72]:


fg.tail(5)


# In[73]:


fg.describe()


# In[74]:


fg.columns


# In[75]:


fg.shape


# In[76]:


fg.isnull().sum()


# In[83]:


fg.info()


# In[77]:


sns.barplot("year","passengers",data=fg)


# In[81]:


sns.barplot("month","passengers",data=fg)


# In[84]:


### 행과열 shape
### 컬럼명 columns
### 요약값 describe
### 정보 info()
### 결측값 isnull().sum()
### 연속형 데이터는 히스토그램 찍어보고 
### boxplot, 막대그래프는 범주형 데이터


# In[3]:


fg = sns.load_dataset("flights")
fg.head()


# In[7]:


sns.scatterplot(x="year",y="passengers",hue="month",data=fg)


# In[15]:


### boxplot 그리기
#x축은 month, y축은 passengers
# 데이터는 기본적으로 데이터프레임으로 되어있다. 
# 데이터를 받아오면 기본적으로 pandas의 데이터프레임이다
plt.figure(figsize=(10,10)) # 인치개념이다.
sns.boxplot(x="month",y="passengers",data=fg)


# In[16]:


fgpivot = fg.pivot("month","year","passengers")
fgpivot


# In[22]:


plt.figure(figsize=(10,8))
sns.heatmap(fgpivot, annot=True, fmt='d')


# In[23]:


### iris데이터셋을 읽어오자 
### 데이터를 읽어와 간단히 데이터 파악하고 시각화 2,3개 그려보자
iris = sns.load_dataset("iris")


# In[24]:


iris.head(5)


# In[25]:


iris.tail(5)


# In[26]:


iris.shape


# In[27]:


iris.columns


# In[28]:


iris.info() #결측치 있는지 이것도 보는겨


# In[29]:


iris.isnull().sum() #데이터가 비어있는지 아닌지


# In[30]:


iris.describe()


# In[38]:


### 데이터를 읽어와 간단히 데이터 파악하고 시각화 2,3개 그려보자
plt.figure(figsize=(10,8))
sns.lmplot(x="sepal_length",y="sepal_width",hue="species",data=iris)


# In[35]:


plt.figure(figsize=(10,8))
sns.scatterplot(x="petal_length",y="petal_width",hue="species",data=iris)


# In[37]:


plt.figure(figsize=(10,8))
sns.violinplot(x="species",y="petal_length",data=iris)


# In[ ]:




