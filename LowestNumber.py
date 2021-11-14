# Find the lowest number
# Create a program that ask 3 numbers. 
# Find the lowest number using only if-else statement.
# Display the lowest number

# Ask 3 numbers.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# if-else statement:
if num1 < num2 and num2 < num3:
    print("The lowest number is",num1)
else:
    if num2 < num1 and num2 < num3:
        print("The lowest number is",num2)
    else:
        if num3 < num1 and num3 < num2:
            print("The lowest number is",num3)
# display the lowest number

# end of program
print("Done")
