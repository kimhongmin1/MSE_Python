#!/usr/bin/env python
# coding: utf-8

# In[16]:


data = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(data, close_price))
#두개의 리스트를 합쳐주는 zip함수를 이용해 딕셔너리로 나타낸다.
print(close_table)


# In[ ]:




