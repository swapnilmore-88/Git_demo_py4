import operator
from functools import reduce
def add(a,b):
    print("hi")
    return a+b

l = [1,2,3,4]
x= reduce(add, l)
print(x)

print(reduce(add, l, 11))

def greater(a,b):
    return a if a>b else b

y =reduce(greater,l)
print(y)

print(reduce(operator.add,l))
print(reduce(operator.mul,l))

print("**************    ACCUMULATE    ***********************************")

from itertools import accumulate
result = list(accumulate([1,2], operator.add,initial=11))
print(result)
result2 = list(accumulate([1,2,3], operator.add))
print(result2)

print("**************    LAMBDA    ***********************************")
add = lambda a,b : a+b
print(add(22,33))

even_list = list(filter(lambda num : num%2==0,[1,2,3,4,5,6]))
print(even_list)

greater_num =reduce(lambda a,b:a if a>b else b,[11,44,66,22,88])
print(greater_num)

upper_case = list(map(lambda s: str.upper(s), ["swap","nit"]))
print(upper_case)

# QQQQQ----Sort a dictionary according to values
d= {4:"a",1:"d" ,3:"b", 2:"c", }

def fun(i):
    return i[1]

print(sorted(d))
print(sorted(d.items()))
l= sorted(d.items(),  key=fun)
print(l)
d2 = {k:v for k,v in l }
print(d2)
print(d.items())

# QQQQQ----Sort a dictionary according to values by using lambda
print("*********now by using lambda*****")
d= {4:"a",1:"d" ,3:"b", 2:"c", }
dict_filter = sorted(d.items(),key = lambda i :i[1])
print(dict_filter)
d2 = {k:v for k,v in dict_filter}
print(d2)


import collections
dup_list =[11,22,33,11,22,11]
print(collections.Counter(dup_list))