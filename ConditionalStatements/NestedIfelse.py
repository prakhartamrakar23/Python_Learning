'''Write a program that checks if a number is positive, negative, or zero. 
If its positive or negative'''

num=int(input("enter a number: "))
if(num>0):
    print("number is positive")
elif(num<0):
    print("number is negative")
elif(num==0):
    print("number is 0")
else: 
    print("wrong input")