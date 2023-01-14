#!/usr/bin/env python
# coding: utf-8

# ### 1. Data :

#  ### Grupa A:
#   
#      Explorer
#      Proud
#      Freedom 
#  
#  
#  ### Grupa B:
#  
#     Amnesia
#     Atomic
#     Barista
#     Bringhton
#     Cabaret
#     Candelight
#     Carrousle
#     Creme de la creme
#     Deep Purple
#     Dekora
#     Engagement
#     Esperance
#     Freedom
#     Frutteto
#     Gotcha
#     H&Magic
#     Iguana
#     Kahala
#     Mondial
#     Newflash
#     Novia
#     Pink Flovd
#     Pink mondial
#     Playa blanca
#     Priceless
#     Pricesless
#     Shimmer
#     Sialntoi
#     Symbol
#     Tiffany 
#     
#     
#  ### Grupa C: 
#  
#  
#     Phoenix
#     Bumblbee
#     Impact
#     Red panthera
#     Iguazu
#     Polo
#     Blue mondial
#     Roval explorer
#     Full Monty

# In[1]:


gr_A = open('grupa A.txt').read()
gr_a = []
for i in gr_A.split("\n"):
    gr_a.append(i)
for i in enumerate(gr_a):
    print(i)


# In[2]:


gr_B = open('grupa B.txt').read()
gr_b = []
for i in gr_B.split("\n"):
    gr_b.append(i)
for i in enumerate(gr_b):
    print(i)


# In[3]:


gr_C = open('grupa C.txt').read()
gr_c = []
for i in gr_C.split("\n"):
    gr_c.append(i)
for i in enumerate(gr_c):
    print(i)


# ### 2. ORDER READER - not important because of excel ocr existence

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ### 3. Counting how much from box to trollies 

# In[6]:


vba20 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
vba48 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48]
print(max(vba20))
print(min(vba48))


# In[7]:


dl_male = [40,50,60]
dl_duze = [70,80,90,100,110,120,130]

gotowe = []
    


# ### 4. Reading file 

# In[8]:


gr_A = open('grupa A.txt').read()
gr_a = []
for i in gr_A.split("\n"):
    gr_a.append(i)
for i in enumerate(gr_a):
    print(i)
    
    ###
pliki = open("przyklad.txt").read()
plik = []
res = []
rodzaje= []
a = []
for i in enumerate(pliki):
    pliki=pliki.replace('\n','')
for i in pliki:
    plik = pliki.split()
for x in plik:
    if x in gr_a: 
        rodzaje.append(x)
    if x in gr_b:
        rodzaje.append(x)
    if x in gr_c:
        rodzaje.append(x)
#rodzaje = s1.intersection(s2, s3,s4)
print(rodzaje)

## KURWAAAAAAAAAAAA


# JAK JA MAM TO GOWNO TERAZ WYPRINTOWAC --> 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




