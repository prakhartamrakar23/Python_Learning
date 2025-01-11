'''In Python, everything is an object, and each object belongs to a particular class. 
When we create a piece of data (like a number or a string), 
Python creates an object of the appropriate class to store that data.
variables are references (or pointers) to objects'''

a="prakhar"
print(a)
print(type(a))

#here still the value is same but both represent the different objects
a=10
b=10

#here the a and b both refering the same objects
a=10
b=a
