# Grade Calculator with Continuous Execution

while True:
    name = input("Enter student's name (type 'Exit' to stop): ")
    
    if name.lower() == "exit":
        print("Program ended.")
        break

    mark1 = float(input("Enter mark for subject 1: "))
    mark2 = float(input("Enter mark for subject 2: "))
    mark3 = float(input("Enter mark for subject 3: "))

    average = (mark1 + mark2 + mark3) / 3

    print("Student Name:", name)
    print("Average:", average)

    if average >= 75:
        print("Grade: A")
    elif average >= 60:
        print("Grade: B")
    elif average >= 40:
        print("Grade: C")
    else:
        print("Result: Fail")

    print("---------------------------")