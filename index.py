# Assignment 5 Program 2: Find the lowest number

# Create a program that ask 3 numbers. 
# Find the lowest number using only if-else statement.
# Display the lowest number


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 < num2 and num1 < num3:
    print(str(num1) + " is the lowest number.")
elif num2 < num1 and num1 < num3:
    print(str(num2) + " is the lowest number.")
elif num3 < num2 and num3 < num1:
    print(str(num3) + " is the lowest number.")
else:
    print("error")