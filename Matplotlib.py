#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install matplotlib


# In[2]:


import matplotlib.pyplot as plt
import numpy as np


# In[3]:


fig, ax = plt.subplots()
ax.plot([1,2,3,4],[1,4,2,3])
plt.show()


# In[4]:


np.random.seed(300)
data = {'a':np.arange(50),
        'c':np.random.randint(0,50,50),
        'd':np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

fig, ax = plt.subplots(figsize=(5, 2.7), sharey=True)
ax.scatter('a','b',c = 'c', data=data)
#ax.xlabel('entery x')
#ax.ylabel('entry y')


# In[6]:


x = np.linspace(0,2,100)
fig, ax = plt.subplots(figsize=(5,2.7))
ax.plot(x, x, label = 'linear')
ax.plot(x, x**2, label='quadratic')
ax.plot(x, x**3, label= 'cubic')
ax.legend()


# In[9]:


data1 = [3,4,5,5,2,3]
data2 = [12,34,2,5,8,9]
fig, ax = plt.subplots(figsize= (5,2.7))
x = np.arange(len(data1))
ax.plot(x, np.cumsum(data1), color='blue', linewidth =3 , linestyle = '--')
l , = ax.plot(x, np.cumsum(data2), color = 'orange', linewidth = 2)


# In[12]:


fig , ax = plt.subplots(figsize=(5,2.7))
ax.scatter(data1, data2, s=50, facecolor = 'C0', edgecolor = 'k')


# In[13]:


fig, ax = plt.subplots(figsize=(5,2.7))
ax.plot(data1, 'o', label = 'data1')
ax.plot(data2, 'd', label = 'data2')
ax.plot(data1, 'v', label = 'data1')
ax.plot(data2, 's', label= 'data2')


# In[17]:


fig , ax = plt.subplots(figsize = (5,2.7))
t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2 * np.pi * t)
line, = ax.plot(t,s ,lw=2)
ax.annotate('local  max', xy=(2,1), xytext=(3,1.5),
          arrowprops = dict(facecolor='black',shrink = 0.05))
ax.set_ylin(-2,2)


# In[18]:


fig, ax = plt.subplots(figsize= (5,2.7))
categories = ['turnips', 'rutubaga','cucumber','pumpkins']
ax.bar(categories, np.random.rand(len(categories)))


# In[24]:


fig, axd = plt.subplot_mosaic([['upleft','right'],
                              [['lowleft'],['right']]
axd['upleft'].set_title('upleft')


# In[25]:


x = 4 + np.random.normal(0,2,4)
y = 4 + np.random.normal(0,2 ,len(x))

sizes = np.random.uniform(15, 80, len(x))
colors = np.random.uniform(15, 80, len(x))

fig, ax = plt.subplots()
ax.scatter(x,y, s=sizes, c= colors)
plt.show()


# In[27]:


x = 0.5 + np.arange(8)
y = [4.8, 5.5, 3.5, 4.6, 6.5, 6.6,2.6, 3.0]

fig, ax = plt.subplots()
ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)

ax.set(xlim=(0,8), xticks=np.arange(1,8),
      ylim=(0,8), yticks=np.arange(1,8))
plt.show()


# In[29]:


x = 0.5 + np.arange(8)
y = [4.8, 5.5, 3.5, 4.6, 6.5, 6.6,2.6, 3.0]

fig, ax = plt.subplots()
ax.stem(x, y)

ax.set(xlim=(0,8), xticks=np.arange(1,8),
      ylim=(0,8), yticks=np.arange(1,8))
plt.show()


# In[31]:


np.random.seed(1)
x = 4 + np.random.normal(0, 1.5, 200)
fig, ax = plt.subplots()
ax.hist(x, bins=8, linewidth=0.5, edgecolor= "white")

ax.set(xlim= (0,8), xticks= np.arange(1,8),
      ylim = (0,56), yticks = np.arange(0, 56, 9))

plt.show()


# In[35]:


np.random.seed(10)
D = np.random.normal((3,5,4), (1.25,1.00, 1.25),(100,3))
fig, ax = plt.subplots()
VP = ax.boxplot(D, positions=[2,4,6], widths= 1.5, patch_artist = True,
               showmeans= False, showfliers = False,
               medianprops = {"color":"white", "linewidth":"0.5"},
               boxprops ={"facecolor":"C0","edgecolor":"white",
                         "linewidth":0.5},
               whiskerprops= {"color":"C0", "linewidth":"1.5"})
ax.set(xlim =(0,8), xticks = np.arange(1,8),
      ylim =(0,8), yticks= np.arange(1,8))
plt.show()


# In[38]:


x = [1,2,3,4]
colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(x)))
fig, ax= plt.subplots()
ax.pie(x, colors= colors, radius = 3, center=(4,4),
      wedgeprops = {"linewidth":1, "edgecolor":"white"}, frame=True)

ax.set(xlim=(0,8), xticks = np.arange(1,8),
      ylim = (0,8), yticks = np.arange(1,8))
plt.show()


# In[40]:


fig, ax = plt.subplots()
fruits =['apple', 'blueberry','cherry','orange']
counts = [40, 100, 30, 55]
bar_labels = ['red','blue','_red','orange']
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']
ax.bar(fruits, counts, label = bar_labels, color = bar_colors)
plt.show()


# In[42]:


np.random.seed(1000)
fig, ax = plt.subplots()
people = ('tom','dick','harry','slim','jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))
ax.barh(y_pos, performance, xerr= error, align = 'center')
plt.show()


# In[44]:


data = {'apple':10, 'orange':20, 'lemon':30, 'lime':40}
names = list(data.keys())
values = list(data.values())
fig, axs= plt.subplots(1,3)
axs[0].bar(names,values)
axs[1].scatter(names,values)
axs[2].plot(names,values)


# In[ ]:




