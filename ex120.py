#!/usr/bin/env python
# coding: utf-8

# In[1]:


fruit ={"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user = input("좋아하는 과일은?")
# 질문을 설정한다
if user in fruit.values():
    print("정답입니다.")
else:
    print("오답입니다.")
# if else문을 사용하여 출력해야할 대답을 정한다.


# In[ ]:




