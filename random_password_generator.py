#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random

#shuffle all characters of a string
def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

#generating a random uppercase letters based on ASCII code
uppercaseLetter1 = chr(random.randint(65, 90))
uppercaseLetter2 = chr(random.randint(65, 90))

#generating passwords using all characters at random
password = uppercaseLetter1 + uppercaseLetter2
password = shuffle(password)

print(password)


# In[ ]:




