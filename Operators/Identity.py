# this identity operator helps to detect that variable is referring to same object or not
a = ["Rose", "Lotus"]    
b = ["Rose", "Lotus"]    
  
# initializing a variable c and storing the value of a in c  
c = a    
   
print("a is c => ", a is c)   #true
print("a is not c => ", a is not c)  
print("a is b => ", a is b)  
print("a is not b => ", a is not b)  
print("a == b => ", a == b)  
print("a != b => ", a != b)  