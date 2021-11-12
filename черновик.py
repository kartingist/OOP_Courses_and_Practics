import os
import os.path
import re


# x=os.listdir(path=".")
# print(x)
# for i in x:
#     if '.py' in i:
#         print(i)
#
top=''
x=os.walk(top,  topdown=True, onerror=None, followlinks=False)
print(x)