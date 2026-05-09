#BISMILLAH
import sys
students = {}

#Adding Student
def add_student():
    name = input("Enter student name: ").strip().lower()
    if name in students:
        print("Student already exists")
        return
    try:
        score = float(input("Enter student's score: "))
    except ValueError:
        print("Error! Student score must be a number")
        return
    grade = calculate_grade(score)
    students[name] = {"score" : score,
                      "grade" : grade}
    print("Student added successfully")

#Viewing student with scores
def view_student():
    name = input("Enter student name to search: ").strip().lower()
    if name in students:
        print(f"{name.capitalize()} : {students[name]['score']} - {students[name]['grade']}")
    else:
        print("Student not found")
        return

#Updating existing student record
def update_student():
    name = input("Enter student's name to update: ").strip().lower()
    if name in students:
        try:
            score = float(input("Enter student's new score: "))
            students[name]["score"] = score
            students[name]["grade"] = calculate_grade(score)
            print("Student updated successfully")
        except ValueError:
            print("Error! Student score must be a number")
    else:
        print("Sorry! Student not found")
        return

#Checking grade
def calculate_grade(score):
    if score >= 90:
        return "A+"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B+"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 45:
        return "D"
    else:
        return "F"

#Deleting student from record
def delete_student():
    name = input("Enter student name to delete: ").strip().lower()
    if name in students:
        del_choice = input("Are you sure you want to delete this student? (y/n)").lower().strip()
        if del_choice == "y":
            del students[name]
            print("Student deleted successfully")
        else:
            print("Deletion aborted")
            return
    else:
        print("Sorry! Student not found")
        return

def view_all_students():
    if not students:
        print("No student record found")
    else:
        print("Student name | Score | Grade")
        print("--------------------------")
        for name in students:
            print(f"{name.capitalize()} : {students[name]['score']} - {students[name]['grade']}")

def exit_program():
    print("Goodbye!")
    sys.exit()

def user_options():
    print("1.Add Student")
    print("2.View Student")
    print("3.Update Student")
    print("4.Delete Student")
    print("5.View All Students' records")
    print("0.Exit")

def main():
    print("---Welcome to Student Manager---")
    user_options()
    while True:
        choice = input("Enter your choice: ")
        if choice == '1':
            add_student()
        elif choice == '2':
            view_student()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            view_all_students()
        elif choice == '0':
            exit_program()
        else:
            print("Sorry! Please enter a valid choice")

main()
