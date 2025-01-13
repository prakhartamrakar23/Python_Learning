weight=int(input("Enter your weight "))
height=float(input("enter your height "))
bmi=(weight//height) **2
print(bmi)
if bmi<=17:
    print("Underweight")
elif (bmi>=18 and bmi<=25):
    print("Normal range")
elif(bmi>25 and bmi<=30):
    print("Overweight")
elif bmi>30:
    print("Obese")
else :
    print("wrong input")