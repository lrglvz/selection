# Create a program that will ask for grade percentage. Display the equivalent Grade/Mark and Description
# Example:
# Input grade: 87.6
# Grade/Mark: 1.75
# Description: Very Good

# Ask for grade percentage.
grade = round(float(input("Input Grade: ")))
# Test grades 97-100
if grade <= 100 and grade >= 97:
    print("Grade/Mark: 1.0")
    print("Description: Excellent")
else: # grades 94-96
    if grade <= 96 and grade >= 94:
        print("Grade/Mark: 1.25")
        print("Description: Excellent")
    else: # grades 91-93
        if grade <= 93 and grade >= 91:
            print("Grade/Mark: 1.5")
            print("Description: Very Good")
        else: # grades 88-90
            if grade <= 90 and grade >= 88:
                print("Grade/Mark: 1.75")
                print("Description: Very Good")
            else: # grades 85-87
                if grade <= 87 and grade >= 85:
                    print("Grade/Mark: 2.0")
                    print("Description: Good")
                else: # grades 82-84
                    if grade <= 84 and grade >= 82:
                        print("Grade/Mark: 2.25")
                        print("Description: Good")
                    else: # grades 79-81
                        if grade <= 81 and grade >= 79:
                            print("Grade/Mark: 2.5")
                            print("Description: Satisfactory")
                        else: # grades 76-78
                            if grade <= 78 and grade >= 76:
                                print("Grade/Mark: 2.75")
                                print("Description: Satisfactory")
                            else: # grade 75
                                if grade == 75:
                                    print("Grade/Mark: 3.0")
                                    print("Description: Passing")
                                else: # grade 65-74
                                    if grade <= 74 and grade >= 65:
                                        print("Grade/Mark: 5.0")
                                        print("Description: Failure")
                                    else: # grade 1-64 (Inc)
                                        if grade <= 64 and grade > 1:
                                            print("Grade/Mark: Inc.")
                                            print("Description: Incomplete")
                                        else: # grade 0 (W)
                                            if grade == 0:
                                                print("Grade/Mark: W")
                                                print("Description: Withdrawn")
                                            else: # grade -1 below (D)
                                                if grade <= -1:
                                                    print("Grade/Mark: D")
                                                    print("Description: Dropped")
print(input("Done"))
          
