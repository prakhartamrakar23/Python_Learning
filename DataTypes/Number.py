#integer type
a=5
print("the type of a ",type(a))
#here this functionn gives that it is a instance of or object of any class or not
# means it returns true or  false it takes two arguments first is variable, class type
print(isinstance(a,int))

#floating point 
b=2.3
print("the type of b", type(b))
print(isinstance(b,float))

#complex j is imaginary part
c=2+3j
print("the type of c ",type(c))
print(isinstance(c,complex))

z1=2+3j
z2=2-5j
# we can Getting the real and imaginary parts of a complex number by this .real and .imag are attributes
'''Yes, in Python, the .real and .imag attributes are part of the complex class,
 which is used to represent complex numbers.'''
 
print("Real part of z1:", z1.real)  # Output: 3.0
print("Imaginary part of z1:", z1.imag) 
z3=z1+z2
print("sum of complex is",z3)

'''we can also differenciate numbers by some prefixes'''
x=0b10  #it is prefix for binary '0b'  or '0B' convert to binary
print(x)

y=0o10  #it is prefix for octal '0o'  or '0O' convert to octal
print(y)

z=0x10  #it is prefix for binary '0x'  or '0X' convert to hexadecimal
print(z)
