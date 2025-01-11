'''here we define x as global variable  and and if we want to do change in this variable 
then we have to use global keyword

Accessing a global variable: No need for the global keyword.
Modifying a global variable: You must use the global keyword inside the function.
'''
x=100
def add():
    global x
    b=20
    c=x+b
    print(c) 
add()

# here in this it gives error to change the value of y becaue we have not used global keyword
y=20
def sum():
    y
    print("global variable ",y)
    #y=45          #can not redeclare a global
sum()
