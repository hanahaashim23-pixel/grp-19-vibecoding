# Grade Calculator

name = input("Enter student's name: ")

mark1 = float(input("Enter mark for subject 1: "))
mark2 = float(input("Enter mark for subject 2: "))
mark3 = float(input("Enter mark for subject 3: "))

average = (mark1 + mark2 + mark3) / 3

print("Student Name:", name)
print("Average Mark:", average)

if average >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")