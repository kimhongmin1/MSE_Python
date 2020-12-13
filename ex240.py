#!/usr/bin/env python
# coding: utf-8

# In[30]:


def 함수0(num) :
    return num * 2

def 함수1(num) :
    return 함수0(num + 2)

def 함수2(num) :
    num = num + 10
    return 함수1(num)

c = 함수2(2)
#함수2(2)는 12를 함수1()에 넣는다
#함수1(12)는 14를 함수0()에 넣는다
#함수0(14)는 28이다.
print(c)


# In[ ]:




