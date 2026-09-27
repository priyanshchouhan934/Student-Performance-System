from students_store import students
def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    subjects = ["Python", "Mathematics", "Communication", "Science"]
    marks = []
    for sub in subjects:
        m = float(input("Enter " + sub + " marks: "))
        marks.append(m)
    att = float(input("Enter attendance %: "))
    assignment = float(input("Enter assignment %: "))
    quiz = float(input("Enter quiz %: "))
    study = float(input("Enter daily study hours: "))
    student = {
        "name": name,
        "roll": roll,
        "marks": marks,
        "attendance": att,
        "assignment": assignment,
        "quiz": quiz,
        "study": study
    }
    students.append(student)
    print("Student added successfully.")