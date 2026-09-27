from students_store import students, find_student
from add_student import add_student
from report import show_report
from analysis import show_analysis
def main():
    while True:
        print("\n===== STUDENT PERFORMANCE SYSTEM =====")
        print("1. Add Student")
        print("2. Performance Report")
        print("3. Array/List Analysis")
        print("4. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            if not students:
                print("No records available.")
                continue
            roll = input("Enter roll number: ")
            student = find_student(roll)
            if student:
                show_report(student)
            else:
                print("Student not found.")
        elif choice == "3":
            if not students:
                print("No records available.")
                continue
            roll = input("Enter roll number: ")
            student = find_student(roll)
            if student:
                show_analysis(student)
            else:
                print("Student not found.")
        elif choice == "4":
            print("Thank you.")
            break
        else:
            print("Invalid choice.")
main()