#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random


# In[6]:


def Gerador():
    lista = []
    
    while True:
        numero = random.randint(1,25)
        if numero not in lista:
            lista.append(numero)
        if len(lista) == 15:
            break
    return lista

lista = Gerador()
print(lista)


# In[ ]:





# In[ ]:




