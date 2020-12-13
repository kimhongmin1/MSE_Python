#!/usr/bin/env python
# coding: utf-8

# In[9]:


리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in 리스트:
    split = i.split(".")
    if (split[1] == "h") or (split[1] == "c"):
        print(i)
#for문에서 split함수를 이용해 "."을 기준으로 나눈다.
#if문을 이용해 "."뒤에 있는 문자를 통해 출력한다.


# In[ ]:




