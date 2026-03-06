# Grade Calculator with Continuous Execution and Formatted Output

while True:
    name = input("Enter student's name (type 'Exit' to stop): ")

    if name.lower() == "exit":
        print("Program ended.")
        break

    mark1 = float(input("Enter mark for subject 1: "))
    mark2 = float(input("Enter mark for subject 2: "))
    mark3 = float(input("Enter mark for subject 3: "))

    average = (mark1 + mark2 + mark3) / 3

    if average >= 75:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 40:
        grade = "C"
    else:
        grade = "Fail"

    print("------------------------------")
    print("Name   :", name)
    print("Average:", round(average, 1))
    print("Grade  :", grade)
    print("------------------------------")