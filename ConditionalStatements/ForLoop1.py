'''here we iterate the list to its length by using len() and range()
it is used when we need indices'''

# list=["prakhar","ganesh","vikas","sachin"]
# for i in range(len(list)):
#     print(list[i],end=" ")

list=[3, 5, 23, 6, 5, 1, 2, 9, 8]
sum=0
for i in list :
    sum=sum+i**2
print("The sum of squares is: ",sum)