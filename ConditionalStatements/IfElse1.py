'''Write a Python program that checks if a given year is a leap year or a century year. If it's a century year, further check if it is a leap year.
A year is a leap year if divisible by 4, and if divisible by 100, it should also be divisible by 400.
A century year is a year that is divisible by 100 but not by 400.'''

year = int(input("Enter a year: "))
if year % 100 == 0:
    if year % 400 == 0:
        print( "year is a Century Leap Year.")
    else:
        print("year is a Century Year but not a Leap Year.")
elif year % 4 == 0:
    print("year is a Leap Year.")
else:
    print("Year is not a Leap Year.")
