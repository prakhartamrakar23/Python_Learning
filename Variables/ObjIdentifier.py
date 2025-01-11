# a=10
# b=a
# print(a)
# print (b)
# print(id(a))
# print(id(b))

'''here the two objects are created and refrences are stored in a and b 
we can check this by built in id function'''
x=40
y=39
print(id(x))
print(id(y))


a = 50  
b = a  
print("same address",id(a))  
print(id(b))  
# Reassigned variable a  
a = 500  
print('adress change',id(a))  