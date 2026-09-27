Project Statement

Problem Statement:

Educators and academic coordinators often need to track a student's marks, attendance, and study habits, but manually calculating averages, pass/fail status, and performance outlook for each student is time-consuming and error-prone. There is a need for a simple, lightweight tool that can record a student's academic data and instantly generate a clear performance summary and outcome prediction, without requiring a database, spreadsheet software, or internet connection.
The Student Performance System addresses this by providing a console-based application where a user can enter student details once and immediately retrieve calculated statistics, a performance score, and a predicted outcome category, along with basic analytical operations on the marks data.

Scope of the Project:

- The system manages student records in memory only, for a single running session — it does not persist data to a file or database, so records do not carry over between runs.
- It supports:
  - Adding a student with marks in four fixed subjects (Python, Mathematics, Communication, Science), attendance %, assignment %, quiz %, and daily study hours.
  - Looking up a student by roll number for both reporting and analysis.
  - Generating a performance report with totals, averages, pass/fail counts, a weighted performance score, and an outcome prediction.
  - Running basic list-based analysis on a student's marks (reverse order, unique values, count above a threshold, kth smallest value).
- The scope is intentionally limited to a single-user, single-session, command-line tool. It does not include:
  - A graphical user interface
  - Persistent storage (files, databases)
  - Multi-user access or authentication
  - Editing or deleting existing student records
  - Handling more or fewer than four fixed subjects

Target Users:

- Teachers / Instructors who want a quick way to log a student's marks and get an instant, calculated performance summary.
- Academic Coordinators / Class Mentors who need a fast, no-setup tool to review a student's standing (pass/fail, risk of falling behind) during counseling or review sessions.
- Students learning Python who may study or extend this project as an example of a small modular application (data storage, input handling, computation, and reporting separated into modules).
- Small coaching centers or tutors without access to full-fledged school management software, who need a lightweight way to track a handful of students' performance.

High-Level Features:

1. Student Data Entry — Collect a student's name, roll number, subject marks, attendance, assignment score, quiz score, and study hours through guided prompts.
2. Student Lookup — Retrieve any previously added student by roll number for reporting or analysis.
3. Performance Reporting — Automatically compute total and average marks, highest/lowest marks, pass/fail counts, a weighted performance score (factoring in marks, attendance, assignments, quizzes, and study hours), and a predicted outcome (Excellent, Good, Average, Needs Improvement, or At Risk).
4. List/Array Analysis — Provide additional insight into a student's marks through reversed ordering, unique value extraction, a count of high-scoring subjects, and kth-smallest-value calculation.
5. Simple Menu-Driven Navigation — A continuously looping text menu lets the user move freely between adding students, viewing reports, running analysis, or exiting the program.
