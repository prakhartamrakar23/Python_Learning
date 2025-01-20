'''We can format string by using formatmethod format(), % operator and by fstings'''

# #The curly braces {} are used as the placeholder in the string and replaced by the format() method argument.

# # Using Curly braces  
# print("{} and {} both are the best friend".format("Devansh","Abhishek"))  
  
# #Positional Argument  
# print("{1} and {0} best players ".format("Virat","Rohit"))  
  
# #Keyword Argument  
# print("{a},{b},{c}".format(a = "James", b = "Peter", c = "Ricky")) 


'''An f-string is created by prefixing a string with the letter f or F.
 Within the string, you can include expressions inside curly braces {} 
which will be evaluated at runtime and inserted into the string.'''

name="prakhar"
age=23
str=f"Your name is {name} and your age is {age}"
print(str)