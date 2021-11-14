# Create a program that will ask for grade percentage. Display the equivalent Grade/Mark and Description
# Example:
# Input grade: 87.6
# Grade/Mark: 1.75
# Description: Very Good

# Ask for grade percentage.
grade = float(input("Input Grade: "))
# Test grades 97-100
if grade <= 100 and grade >= 97:
    print("Grade/Mark: 1.0")
    print("Description: Excellent")
else:
    if grade <= 96 and grade >= 94:
        print("Grade/Mark: 1.25")
        print("Description: Excellent")
    else:
        if grade <= 93 and grade >= 91:
            print("Grade/Mark: 1.5")
            print("Description: Very Good")
        else:
            if grade <= 90 and grade >= 88:
                print("Grade/Mark: 1.75")
                print("Description: Very Good")
