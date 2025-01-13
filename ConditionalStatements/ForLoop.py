#for loop 
num="1234"
for i in num :
    print(i)
print()
str="prakhar"
for i in str: 
    print(i)

#we can use range() function to give last iteration value like length in java
#range() takes three arguments 1. start value(optional)
#2. stop mandatory 3. step

n=2
for i in range(1,11):
    result=2*i
    print(result,end="")

#use of if-else in for loop
list = [1, 2, 4, 5, 6, 7, 8]
flag_even = False
flag_odd = False

for i in list:
    if i % 2 == 0:
        flag_even = True
    else:
        flag_odd = True

if flag_even:
    print("Even numbers in the list are:", [i for i in list if i % 2 == 0])
else:
    print("No even numbers in the list.")

if flag_odd:
    print("Odd numbers in the list are:", [i for i in list if i % 2 != 0])
else:
    print("No odd numbers in the list.")
