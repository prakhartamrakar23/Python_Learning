#capitalize it is used to capitalize first letter of string
str="PRAKHAR"
s="hello world"
str1=str.capitalize()
print(str1)
#casefold() it is used to return the lower case letters
str2=str.casefold()
print("casefold() method",str2)

#it fill the space or character left and right of the string and makes it total to first argument
str3=str.center(10,'#')
print("center() method ",str3)

#upper() it converts all to upper case
print("epper() method",str.upper())  

#lower() converts all to lower case
print("lower() method ",str.lower())

#it capitalize the first letter of each string 
print(s.title())

#swapcase() method Swaps the case of each character (lowercase to uppercase and vice versa)
s1="  HeLLo WoRLd    "
print(s1.swapcase())

#strip() method Removes any leading (at the beginning) and trailing (at the end) whitespace characters from a string.
print(s1.strip())

#count() helps to count the substring or any character in a string it returns the count of that char
#Counts occurrences of the substring within the string, within the optional start and end range
print(s1.count("o"))

print(s.encode())

