def fun():          #it is outer funtion/ parent function

    def f():        #it is inner function/child

        print("inner function f")
    return f()          #returning the child from parent

fun()      #calling parent
#whenever we call fun(), f automatically calls