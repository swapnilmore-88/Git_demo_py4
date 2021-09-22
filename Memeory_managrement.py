# when two variable of immutable data with same value is created then id will be same
# so it creates one object and two refrence with same id
x= 11
y =11
z =x
print(id(x))
print(id(y))
print(id(z))
x =x+11
print(id(x))
print(id(y))
print(id(z))
# print(x is y)


#
x +=11
print(x is y)
# # But when two variable of mutable data with same value is created then id will be different
# # it means it creates two objects and two refrence with diff  ids
a =[1,2]
b = [1,2]
print(a is b)
print(id(a))
print(id(b))


s= "swap"
s2 ="swap"
print(s is s2)


set ={1,2,3}
set2 ={1,2,3}
print(set is set2)