#!/usr/bin/env python
# coding: utf-8

# In[26]:


def message1():
    print("A")

def message2():
    print("B")

def message3():
    for i in range (3) :
        message2()
        print("C")
    message1()

message3()
#def함수로 함수를 만든다.
#message3에서 for문에 의해 BC출력이 3번 반복되고 마지막으로 A가 출력된다.
#MESSAGE3에 의해 BCBCBCA가 출력된다


# In[ ]:




