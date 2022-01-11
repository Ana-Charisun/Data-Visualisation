#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import pandas as pd
import numpy as np
import seaborn
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[99]:


#Data frame
Gender = ['Laki-Laki', 'Perempuan']
Jumlah = [376, 624]

#input to data
sizes = Jumlah
labels = list(Gender)

#plot
fig, ax = plt.subplots(figsize =(10, 7),subplot_kw=dict(aspect="equal"), dpi= 90)
ax.pie(sizes, labels=labels, autopct='%1.1f%%')
ax.axis('equal')
ax.set_title('JENIS KELAMIN')

#legend
ax.legend(title ="Jenis Kelamin", 
          loc ="center left", 
          bbox_to_anchor =(0, 0, 1, 1)) 
  
plt.show()


# In[46]:


#Data frame
Umur = ['>65 Tahun', '12-25 Tahun', '26-45 Tahun', '46-65 Tahun', '5-11 Tahun']
Jumlah = [2, 167, 687, 135, 9]

#input to data
sizes = Jumlah
labels =(Umur)

#plot
def make_autopct (sizes):
    def my_autopct(pct):
        total = sum(sizes)
        val = int(round(pct*total/100.0))
        return '{p:1f}% ({v:d})'.format(p=pct, v=val)
    return my_autopct
fig, ax = plt.subplots(figsize =(10, 7), subplot_kw=dict(aspect="equal"), dpi= 90)
ax.pie(sizes, labels=labels, autopct='%.1f%%')
ax.axis('equal')
ax.set_title('USIA ANGGOTA')

#legend
ax.legend(title ="Usia", 
          loc ="upper left", 
          bbox_to_anchor =(0, 0, 1, 1)) 
  
plt.show()
fig.savefig('usia', bbox_inches='tight', pad_inches=0, dpi=400)


# In[13]:


fig.savefig('usia', bbox_inches='tight', pad_inches=0, dpi=400)


# In[45]:


fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.axis('equal')
Umur = ['5-11 Tahun', '12-25 Tahun', '26-45 Tahun', '46-65 Tahun', '>65 Tahun']
Jumlah = [9, 167, 687, 135, 2]
def make_autopct (Jumlah):
    def my_autopct(pct):
        total = sum(sizes)
        val = int(round(pct*total/100))
        return '{p:f}% ({v:d})'.format(p=pct, v=val)
    return my_autopct
ax.pie(Jumlah, labels=Umur, autopct=make_autopct(Jumlah))
plt.show()


# In[5]:


df = pd.read_csv(r'C:\Users\User\Desktop\Data Responden\Daftar_Pekerjaan.csv')


# In[6]:


df


# In[145]:


plt.figure(figsize=(14,8), dpi=500)
 
plt.bar(x=df['PEKERJAAN'],
 
        height=df['JUMLAH'],
 
        color='rgbgymc')

plt.xticks(rotation=82)
plt.title("Data Jenis Pekerjaan Anggota", fontsize=14)
plt.xlabel('PEKERJAAN', fontsize=14)
plt.ylabel('JUMLAH', fontsize=14)
plt.grid(True)
plt.savefig('Pekerjaan.png',dpi=600, bbox_inches='tight')
plt.show()


# In[8]:


#Create our bar chart as before
plt.figure(figsize=(16,9))
plt.bar(x=df['PEKERJAAN'],
 
        height=df['JUMLAH'],
 
        color='rgbgymc')

#Give it a title
plt.title("Data Jenis Pekerjaan Anggota", fontsize=14)
plt.xticks(rotation=82)
plt.xlabel('PEKERJAAN', fontsize=14)
plt.ylabel('JUMLAH', fontsize=14)
plt.grid(False)
#Give the x axis some labels across the tick marks.
#Argument one is the position for each label
#Argument two is the label values and the final one is to rotate our labels
#Finally, show me our new plot

fig.savefig('Jenis Pekerjaan', alpha=0.9, bbox_inches='tight', pad_inches=0, dpi=500)
plt.show()


# In[18]:


fig.savefig('pekerjaan', bbox_inches='tight', pad_inches=0, dpi=400)


# In[146]:


df_2 = pd.read_csv(r'C:\Users\User\Desktop\Data Responden\kantor cabang.csv')


# In[157]:


df_2


# In[169]:


dff = pd.DataFrame(df_2)


# In[243]:


dff


# In[257]:


CABANG = dff['KANTOR CABANG']
JUMLAH = dff['JUMLAH']
plt.figure(figsize=(14,8), dpi=500)
plt.bar(CABANG,JUMLAH, color=['red', 'blue', 'purple', 'green', 'yellow'])
plt.xticks(rotation=90)
plt.title("Asal Kantor Cabang", fontsize=14)
plt.xlabel('KANTOR CABANG', fontsize=14)
plt.ylabel('JUMLAH', fontsize=14)
plt.grid(True)
# zip joins x and y coordinates in pairs
for x,y in zip(CABANG,JUMLAH):

    label = "{:.0f}".format(y)

    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,11), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
fig.savefig('kantor', bbox_inches='tight', pad_inches=0, dpi=500)
plt.show()


# In[142]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])

Tahun = ['< 1 Tahun', '1-5 Tahun', '5-10 Tahun', '10-15 Tahun', '> 65 Tahun']
Jumlah = [197, 574, 161, 44, 24]
ax.bar(Tahun,Jumlah)
plt.show()


# In[4]:


Income = ['< dari 1 Juta', '1-5 Juta', '5-10 Juta','> 10 Juta']
Jumlah = [199, 677, 84, 40]
plt.figure(figsize=(14,8), dpi=500)
plt.bar(Income,Jumlah, color=['yellow', 'blue', 'purple', 'green'])
plt.xticks(rotation=0)
plt.title("NOMINAL PENGHASILAN ANGGOTA", fontsize=16)
plt.xlabel('Penghasilan', fontsize=16)
plt.ylabel('Jumlah', fontsize=16)
plt.grid(b=True, which='major', color='burlywood', linestyle='')
# zip joins x and y coordinates in pairs

for x,y in zip(Income,Jumlah):

    label = "{:.0f}".format(y)

    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,11), # distance from text to points (x,y)
                 ha='center')
fig.savefig('npaka.jpg', alpha=0.9, bbox_inches='tight', pad_inches=0, dpi=500)
plt.show()  


# In[80]:


#Data frame
Produk = ['Produk Pembiayaan', 'Produk Simpanan', 'Produk Simpanan dan Pembiayaan']
Jumlah = [182, 563, 255]

#input to data
sizes = Jumlah
labels = list(Produk)
colors = ['#ff9999','#66b3ff','#99ff99']
explode = (0.05,0.05,0.05)
#plot
fig, ax = plt.subplots(figsize =(7, 7),subplot_kw=dict(aspect="equal"), dpi= 650)
ax.pie(sizes, colors = colors, startangle=90, pctdistance=0.85, explode = explode, labels=labels, autopct='%1.1f%%')
ax.axis('equal')
ax.set_title('PRODUK YANG DIGUNAKAN')

#legend
ax.legend(title ="Produk", 
          loc ="center", 
          bbox_to_anchor =(0, 0, 1, 1)) 

centre_circle = plt.Circle((0,0),0.70,fc='grey')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
ax.axis('equal')  
plt.tight_layout() 
plt.savefig('pyd.jpg',dpi=500, alpha=0.9, bbox_inches='tight')
plt.show()


# In[275]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])

ProdukDigital = ['Belum Menggunakan', 'Mobile Transaksi', 'Pay-BMT','M-BMT', 'Menggunakan Semua']
Jumlah = [787, 131, 60, 20, 2]
ax.bar(ProdukDigital,Jumlah)
plt.show()


# In[303]:


ProdukDigital = ['Belum Menggunakan', 'Mobile Transaksi', 'Pay-BMT','M-BMT', 'Menggunakan Semua']
Jumlah = [787, 131, 60, 20, 2]

plt.figure(figsize=(14,8), dpi=500)
plt.bar(ProdukDigital,Jumlah, color=['yellow', 'blue', 'purple', 'green', 'red'])
plt.xticks(rotation=0)
plt.title("Produk Digital yang Digunakan", fontsize=14)
plt.ylabel('Jumlah', fontsize=14)
plt.grid(True)
# zip joins x and y coordinates in pairs
for x,y in zip(ProdukDigital,Jumlah):

    label = "{:.0f}".format(y)

    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,11), # distance from text to points (x,y)
                 ha='center')
plt.savefig('ProdukDigital.jpg',dpi=600, bbox_inches='tight')
plt.show()


# In[78]:


ProdukDigital = ['Belum Menggunakan', 'Mobile Transaksi', 'Pay-BMT','E-BMT', 'Menggunakan Semua']
Jumlah = [787, 131, 60, 20, 2]
plt.figure(figsize=(14,8), dpi=500)
plt.bar(ProdukDigital,Jumlah, color=['yellow', 'blue', 'purple', 'green', 'red'])
plt.xticks(rotation=0)
ax = plt.axes()
ax.set_facecolor("lightgrey")
plt.xticks(rotation=0)
plt.xticks(size = 12)
plt.yticks(size = 12)
plt.title("Produk Digital yang Digunakan", fontsize=14)
plt.ylabel('Jumlah', fontsize=14)
plt.grid(False)
ax.set_facecolor("gainsboro")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["bottom"].set_visible(False)
# zip joins x and y coordinates in pairs
for x,y in zip(ProdukDigital,Jumlah):

    label = "{:.0f}".format(y)

    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,11), # distance from text to points (x,y)
                 ha='center')
plt.savefig('Pdg.jpg',dpi=600, bbox_inches='tight')
plt.show()


# In[ ]:




