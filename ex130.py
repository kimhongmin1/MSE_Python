#!/usr/bin/env python
# coding: utf-8

# In[4]:


import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

변동폭 = float(btc['max_price']) - float(btc['min_price'])
시가 = float(btc['opening_price'])
최고가 = float(btc['max_price'])
#각 변수에 대한 값을 지정해준다.

if (시가+변동폭) > 최고가:
    print("상승장")
else:
    print("하락장")
#if문을 통해 변수의 변화에 따른 출력결과를 정해준다.


# In[ ]:




