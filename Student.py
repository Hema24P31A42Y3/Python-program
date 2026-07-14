def add_student(students):
    roll = input("Enter Roll Number: ")

    if roll in students:
        print("Student already exists!")
        return

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    branch = input("Enter Branch: ")

    marks = []
    for i in range(5):
        mark = int(input(f"Enter Subject {i+1} Marks: "))
        marks.append(mark)

    students[roll] = {
        "name": name,
        "age": age,
        "branch": branch,
        "marks": marks
    }

    print("Student Added Successfully!")


def display_students(students):
    if not students:
        print("No Students Found")
        return

    for roll, data in students.items():
        total = sum(data["marks"])
        average = total / 5

        result = "Pass"
        for mark in data["marks"]:
            if mark < 35:
                result = "Fail"
                break

        print("-" * 40)
        print("Roll Number :", roll)
        print("Name        :", data["name"])
        print("Age         :", data["age"])
        print("Branch      :", data["branch"])
        print("Marks       :", data["marks"])
        print("Total       :", total)
        print("Average     :", average)
        print("Result      :", result)


def search_student(students):
    roll = input("Enter Roll Number: ")

    if roll in students:
        print(students[roll])
    else:
        print("Student Not Found")


def update_student(students):
    roll = input("Enter Roll Number: ")

    if roll not in students:
        print("Student Not Found")
        return

    students[roll]["name"] = input("Enter New Name: ")
   
