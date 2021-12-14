# import json
lst = "[Prajwal Sharma, prajwal@1, tuition, development]"
res = lst.strip('][').split(', ')
print(res)
print(type(res))