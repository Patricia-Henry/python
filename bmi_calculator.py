weight = input("enter your weight in lbs: ")
height = input("enter your height in inches: ")

height = int(height)**2
weight = int(weight)* 703

print(type(height))
print(type(weight))

bmi = weight / height
bmi_integer = int(bmi)
print(bmi_integer)

if bmi_integer < 18.5:
    print("A person with a BMI of " + str(bmi_integer ) + " is said to be underweight. ")
elif bmi_integer < 24.9:
    print("A person with a BMI of " + str(bmi_integer ) + " this is accepted as a person who is of normal weight. But hey, what is normal anyway?  ")
else:
    print("A person with a BMI of " + str(bmi_integer ) + " is said to be overweight. But that is pretty vague, don't you think? ")

