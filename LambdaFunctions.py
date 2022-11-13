"""
li= [5,6,4,3,8,9,7,1,22,58]
final_list=list(filter(lambda x: (x%2!=0),li))
print(final_list)
"""
"""
li= [5,6,4,3,8,9,7,1,22,58]
final_list=list(map(lambda x:x*2,li ))
print(final_list)
"""
"""
from functools import reduce
li= [5,6,4,3,8,9,7,1,22,58]
final_list=reduce(lambda x,y:x+y,li)
print(final_list)

"""