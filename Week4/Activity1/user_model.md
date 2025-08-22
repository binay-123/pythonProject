
Project Scope
The Yoobee College database is designed to store and manage information about students, admin, lecturers, courses, and classes.
It helps track which students are enrolled in which courses, which lecturers teach them, and when classes are scheduled.
The database ensures data consistency, avoids redundancy, and provides easy access for academic and administrative tasks.

Entities
STUDENT: Each student has a unique ID, name, profile, and contact info.
ADMIN: Managing communication, scheduling, data management, and maintaining office systems.
LECTURERS: Each lecturer has a unique ID, name, profile, and contact info.
COURSE: Each course has a unique ID, a name, and is taught by many lecturers (lecturer_id is a foreign key).
ENROLLMENT: Links students to courses, recording each enrollment with its own ID, and foreign keys for student and course.

Actors
- Student
- Admin 
- Lecturers

Use case for:
Student
-student Registration
-class timetable
-course enrollment
-assignment work

Lecturer
- course updation
- schedule classes
- Assignment  grading
- teaching materials
- student feedback

Admin
- student management including lecture info
- schedule of classroom & timetable management
- report generation
- course offering

