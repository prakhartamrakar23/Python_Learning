'''Python provides the facility to define the function inside another function.
 These types of functions are called inner functions.'''

def func():
    print("we are in function")
    def func1():
        print("we are in inner fuction 1")
    def func2():
 
        print("we are in inner function 2")
    func1()
    func2()
   
func()

#These child functions are locally bounded with the func() so they cannot be called separately.