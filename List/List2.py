list=[1,2,34,5,6,7]
print(list)

#adding value to list
list[0]=10
print(list)
list.append(30) # it add at the last in any list
print(list)

#it simply removes the elements from 0 to 3 position and replace by given values like 89,78
#list[0:3]=[89,78]
print(list)
#it simply removes the current value and prints the new at mentioned index
list[1]=67
print(list)
#remove() method it rempves the value that is exists in list and gives value error if not exixts
list.remove(67)
print(list)