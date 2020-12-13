#!/usr/bin/env python
# coding: utf-8

# In[32]:


종목 = []

삼성전자 = stock("삼성전자", "005930", 15.79, 1.33, 2.93)
현대차 = stock("현대차", "005380", 8.70, 0.35, 4.27)
LG전자 = stock("LG전자", "066570", 317.34, 0.69, 1.37)
#stock 클래스를 통해 정보를 정리한다
종목.append(삼성전자)
종목.append(현대차)
종목.append(LG전자)
#append 함수를 통해 리스트로 만든다
for i in 종목:
    print(i.code, i.per)
#for문을 통해 정보를 출력한다.


# In[ ]:




