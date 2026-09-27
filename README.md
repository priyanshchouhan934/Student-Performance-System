Student Performance System

Overview:

The Student Performance System is a command-line Python application for recording student academic data and generating performance insights. It lets a user add student records (marks, attendance, assignments, quizzes, and study habits), view a computed performance report with an outcome prediction, and run basic list/array analysis on a student's marks. The project is organized into small, single-purpose modules — data storage, data entry, reporting, and analysis — that are tied together by a simple text-menu driver in `main.py`.

Features:

- Add Student Records: Capture name, roll number, marks in four subjects (Python, Mathematics, Communication, Science), attendance %, assignment %, quiz %, and daily study hours.
- Performance Report:
  - Total, average, highest, and lowest marks
  - Pass/fail count per subject (pass mark: 40)
  - A weighted performance score based on average marks, attendance, assignments, quizzes, and a capped study-hours bonus
  - An outcome prediction: Excellent, Good, Average, Needs Improvement, or At Risk
- Array/List Analysis on a student's marks:
  - Reversed marks list
  - Unique mark values
  - Count of marks scoring 75 or above
  - 3rd smallest mark (via a simple bubble sort)
- In-Memory Student Lookup: Find any stored student by roll number.
- Menu-Driven Interface: Simple numbered menu loop for navigating all features.

Technologies / Tools Used:

- Language: Python 3 (compiled `.pyc` files included are built for CPython 3.14)
- Standard Library Only: no external/third-party packages required
- Modules:
  - `main.py` – menu loop and program entry point
  - `students_store.py` – shared in-memory student list and lookup function
  - `add_student.py` – student data entry
  - `report.py` – statistics, scoring, and outcome prediction
  - `analysis.py` – list-based analysis (reverse, unique, threshold count, kth smallest)

Installation & Setup:

1. Prerequisites: Install Python 3.8 or later (the project was compiled/tested against Python 3.14, but the source code has no version-specific syntax).
   - Check your version:
     bash
     python --version
2. Get the project files: Place the following files in the same folder:
   main.py
   students_store.py
   add_student.py
   report.py
   analysis.py
3. No dependencies to install — the project uses only Python's standard library, so there is no `requirements.txt` or virtual environment needed.
 
Running the Project:

From the project folder, run:
bash
python main.py
You will see a menu:
===== STUDENT PERFORMANCE SYSTEM =====
1. Add Student
2. Performance Report
3. Array/List Analysis
4. Exit
Enter a number and follow the prompts. Note that student data is stored in memory only for the duration of the program — it is not saved to a file or database, so all records are lost when the program exits.

Testing Instructions:

Since this is a console application without an automated test suite, testing is done manually by exercising each menu option:
1. Test "Add Student" (Option 1)
   - Run the program and choose option `1`.
   - Enter a name, roll number, and marks for all four subjects, then attendance, assignment, quiz, and study hours.
   - Confirm the message `"Student added successfully."` appears.
   - Try adding two or more students to test multiple records.
2. Test "Performance Report" (Option 2)
   - Choose option `2` and enter the roll number of a student you added.
   - Verify the report shows correct total, average, highest, and lowest marks.
   - Verify pass/failed counts match marks against the 40-mark threshold.
   - Cross-check the performance score and outcome prediction against the logic in `report.py` (e.g., low attendance under 75% should show "Needs Improvement"; failing marks with a low score should show "At Risk").
   - Enter a roll number that doesn't exist and confirm `"Student not found."` is shown.
3. Test "Array/List Analysis" (Option 3)
   - Choose option `3` and enter a valid roll number.
   - Verify the reversed marks list is correct.
   - Verify unique marks are listed without duplicates.
   - Verify the count of marks ≥ 75 is accurate.
   - Verify the 3rd smallest mark matches manual sorting of the four marks.
4. Test Edge Cases
   - Attempt options 2 or 3 before adding any students — confirm `"No records available."` is shown.
   - Enter an invalid menu choice (e.g., `9`) and confirm `"Invalid choice."` is shown.
   - Choose option `4` and confirm the program exits with `"Thank you."`
5. Regression Testing
   - After any code changes, repeat the above steps to confirm existing functionality (adding students, reports, and analysis) still behaves as expected.

Screenshots:
