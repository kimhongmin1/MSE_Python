#!/usr/bin/env python
# coding: utf-8

# In[16]:


low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]

volatility = []
for i in range(len(low_prices)):
        volatility.append(high_prices[i] - low_prices[i])
#for문을 이용해 변수와 구간(low혹은high prices의 수)을정한다.
#append  함수를 통해 변동폭을 순서대로 volatility리스트에 넣는다
print(volatility)


# In[ ]:




