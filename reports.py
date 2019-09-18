import sqlite3


class Student():

    def __init__(self, first, last, handle, cohort):
        self.first_name = first
        self.last_name = last
        self.slack_handle = handle
        self.cohort = cohort

    def __repr__(self):
        return f"{self.first_name} {self.last_name}'s slack handle is @{self.slack_handle} and is in {self.cohort}"

class Cohort():

    def __init__(self, name, firstName, lastName):
        self.name = name
        self.instructor = f"{firstName} {lastName}"

    def __repr__(self):
        return f"This is {self.name} and it is taught by {self.instructor}"

class Exercise():

    def __init__(self, exid, name, language):
        self.id = exid
        self.name = name
        self.language = language

    def __repr__(self):
        return f"Exercise {self.id} is called {self.name} and uses the {self.language} language"

class JSExercise():

    def __init__(self, exid, name, language):
        self.id = exid
        self.name = name
        self.language = language

    def __repr__(self):
        return f"Exercise {self.id} is called {self.name} and uses the {self.language} language. I like this exercise"

class PythonExercise():

    def __init__(self, exid, name, language):
        self.id = exid
        self.name = name
        self.language = language

    def __repr__(self):
        return f"Exercise {self.id} is called {self.name} and uses the {self.language} language. Python is fun so this exercise isn't bad."

class CsharpExercise():

    def __init__(self, exid, name, language):
        self.id = exid
        self.name = name
        self.language = language

    def __repr__(self):
        return f"Exercise {self.id} is called {self.name} and uses the {self.language} language. I don't know C# so this exercise is impossible."

class Instructor():

    def __init__(self, firstname, lastname, slackhandle, cohort, specialty):
        self.first_name = firstname
        self.last_name = lastname
        self.slack_handle = slackhandle
        self.cohort = cohort
        self.specialty = specialty

    def __repr__(self):
        return f"{self.first_name} {self.last_name} is the instructor for {self.cohort} and can be messaged on slack at @{self.slack_handle}. {self.first_name}'s specialty is {self.specialty}"

class StudentExerciseReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/Users/dhobs/workspace/python/SQL/StudentExercises/studentexercises.db"


    # Display all students with cohort name
    def all_students(self):

        """Retrieve all students with the cohort name"""

        """shorthand that lets us open up a connection to our database"""
        """Asking sqlite to conenct to our db using path and then reference connection as 'conn'"""
        """with keyword is turning on connection to the database and keeping it open...it then turns off the connection because you want to turn it off when done...'with' allows us to execute everything within it and disconnect when done"""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Student(
                row[1], row[2], row[3], row[5]
            )


            """Now that we have a connection, we need to create a cursor (a virtual version of the db that handles talking to db for you)---has certain methods on its own, LOOK AT DOCUMENTATION"""

            db_cursor = conn.cursor()

            """Execute method is one of these methods that when called, allows us to start writing SQL"""
            db_cursor.execute("""
            select s.Id,
                s.FirstName,
                s.LastName,
                s.SlackHandle,
                s.CohortId,
                c.Name
            from Student s
            join Cohort c on s.CohortId = c.Id
            order by s.CohortId
            """)

            """then set a variable back out in python to fetchall"""
            all_students = db_cursor.fetchall()

            """this prints a list of tuples that we pulled from the db using SQL"""
            for student in all_students:
                print(student)

    # Display all cohorts.
    def all_cohorts(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Cohort(
                row[1], row[2], row[3]
            )

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select c.Id,
                c.Name,
                i.FirstName,
                i.LastName,
                i.CohortId
            from Cohort c
            join Instructor i on c.Id = i.cohortId
            order by c.Id
            """)

            all_cohorts = db_cursor.fetchall()

            for cohort in all_cohorts:
                print(cohort)

    #Display all exercises.
    def all_exercises(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(
                row[0], row[1], row[2]
            )

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select e.Id,
                e.ExerciseName,
                e.ExerciseLanguage
            from Exercise e
            order by e.Id
            """)

            all_exercises = db_cursor.fetchall()

            for exercise in all_exercises:
                print(exercise)
    # Display all JavaScript exercises.
    def JS_exercises(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: JSExercise(
                row[0], row[1], row[2]
            )

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select e.id,
                e.ExerciseName,
                e.ExerciseLanguage
            from Exercise e
            where ExerciseLanguage = "JavaScript"
            order by e.id
            """)

            js_exercises = db_cursor.fetchall()

            for js_exercise in js_exercises:
                print(js_exercise)
    #Display all Python exercises.
    def python_exercises(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: PythonExercise(
                row[0], row[1], row[2]
            )

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select e.id,
                e.ExerciseName,
                e.ExerciseLanguage
            from Exercise e
            where ExerciseLanguage = "Python"
            order by e.id
            """)

            python_exercises = db_cursor.fetchall()

            for python_exercise in python_exercises:
                print(python_exercise)

    def csharp_exercises(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: CsharpExercise(
                row[0], row[1], row[2]
            )

        db_cursor = conn.cursor()

        db_cursor.execute("""
        select e.id,
            e.ExerciseName,
            e.ExerciseLanguage
        from Exercise e
        where ExerciseLanguage = "C#"
        order by e.id
        """)

        csharp_exercises = db_cursor.fetchall()

        for csharp_exercise in csharp_exercises:
            print(csharp_exercise)
    # Display all instructors with cohort name.
    def all_instructors(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Instructor(
                row[1], row[2], row[3], row[6], row [5]
            )

        db_cursor = conn.cursor()

        db_cursor.execute("""
        select i.Id,
            i.FirstName,
            i.LastName,
            i.SlackHandle,
            i.CohortId,
            i.Specialty,
            c.name
        from Instructor i
        join Cohort c on i.CohortId = c.Id
        order by i.Id
        """)

        all_instructors = db_cursor.fetchall()

        for instructor in all_instructors:
            print(instructor)

    #CHAPTER 6 MULTIPLE ROWS
    def students_exercises(self):

        exercises = dict()

        with sqlite3.connect(self.db_path) as conn:

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select e.Id ExerciseId,
                e.ExerciseName,
                s.Id,
                s.FirstName,
                s.LastName,
                e.ExerciseLanguage
            from Exercise e
            join StudentExercise se on se.ExerciseId = e.Id
            join Student s on s.Id = se.StudentId
            order by e.id
            """)

            dataset = db_cursor.fetchall()

            for row in dataset:
                exercise_id = row[0]
                exercise_name = row[1]
                student_id = row[2]
                student_name = f'{row[3]} {row[4]}'

                if exercise_name not in exercises:
                    exercises[exercise_name] = [student_name]
                else:
                    exercises[exercise_name].append(student_name)
            for exercise_name, students in exercises.items():
                print(exercise_name)
                for student in students:
                    print(f'\t* {student}')

#Practice: Student Workload

#List the exercises assigned to each student. Display each student name and the exercises s/he has been assigned beneath their name. Use a dictionary to track each student. Remember that the key should be the student id and the value should be the entire student object.

    def assigned_exercises(self):
        students = dict()

        with sqlite3.connect(self.db_path) as conn:

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select e.Id ExerciseId,
                e.ExerciseName,
                s.Id,
                s.FirstName,
                s.LastName,
                e.ExerciseLanguage
            from Exercise e
            join StudentExercise se on se.ExerciseId = e.Id
            join Student s on s.Id = se.StudentId
            order by e.id
            """)

            data_set = db_cursor.fetchall()

            for row in data_set:
                exercise_id = row[0]
                exercise_name = row[1]
                student_id = row[2]
                student_name = f'{row[3]} {row[4]}'

                if student_name not in students:
                    students[student_name] = [exercise_name]
                else:
                    students[student_name].append(exercise_name)
            for student, exercises in students.items():
                print(f'{student} is working on:')
                for exercise in exercises:
                    print(f'\t* {exercise}')

#Practice: Assigned Exercises

# List all exercises assigned by each instructor. Display each instructor name and the exercises s/he has assigned beneath their name. Use a dictionary to track each instructor. Remember that the key should be the instructor id and the value should be the entire instructor object.

    def instructor_exercises(self):
        instructors = dict()

        with sqlite3.connect(self.db_path) as conn:

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select i.Id,
                        i.FirstName,
                        i.LastName,
                        i.CohortId,
                        se.ExerciseId,
                        e.ExerciseName
                    from Instructor i
                    join Student s on i.CohortId = s.CohortId
                    join StudentExercise se on s.id = se.StudentId
                    join Exercise e on se.ExerciseId = e.id
                    order by i.Id
            """)

            data_set = db_cursor.fetchall()

            for row in data_set:
                instructor_name = f'{row[1]} {row[2]}'
                exercise_name = row[5]

                if instructor_name not in instructors:
                    instructors[instructor_name] = [exercise_name]
                elif instructor_name in instructors and exercise_name not in instructors[instructor_name]:
                    instructors[instructor_name].append(exercise_name)
                else:
                    pass

            for instructor, exercises in instructors.items():
                print(f'{instructor} has assigned:')
                for exercise in exercises:
                    print(f'\t*{exercise}')

#Practice: Popular Exercises

#Output a report in your terminal that lists all students and the exerices each is assigned. Use a dictionary to track each exercise. Remember that the key should be the exercise id and the value should be the entire exercise object.

    def student_exercises(self):
        exercises = dict()

        with sqlite3.connect(self.db_path) as conn:

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select e.Id,
                e.ExerciseName,
                se.ExerciseId,
           	    se.StudentId,
                s.FirstName,
                s.LastName
            from Exercise e
            join StudentExercise se on e.Id = se.ExerciseId
            join Student s on se.StudentId = s.id
            order by s.Id
            """)

            data_set = db_cursor.fetchall()

            for row in data_set:
                student_name = f'{row[4]} {row[5]}'
                exercise_name = row[1]

                if exercise_name not in exercises:
                    exercises[exercise_name] = [student_name]
                else:
                    exercises[exercise_name].append(student_name)

            for exercise, students in exercises.items():
                print (f'{exercise} is being worked on by:')
                for student in students:
                    print(f'\t*{student}')



#Advanced Challenge: Who is Working on What and Why?

#List the students working on each exercise. Also include the instructor who assigned the exercise. Use a dictionary to track each exercise.

    def assigned_by(self):
        exercises = dict()

        with sqlite3.connect(self.db_path) as conn:

            db_cursor = conn.cursor()


            db_cursor.execute("""
            select e.Id,
                e.ExerciseName,
                se.ExerciseId,
           	    se.StudentId,
                s.FirstName,
                s.LastName,
                i.FirstName,
                i.LastName
            from Exercise e
            join StudentExercise se on e.Id = se.ExerciseId
            join Student s on se.StudentId = s.id
            join Instructor i on s.CohortId = i.CohortId
            order by s.Id
            """)

            data_set = db_cursor.fetchall()

            for row in data_set:
                student_name = f'{row[4]} {row[5]}'
                exercise_name = row[1]
                instructor_name = f'{row[6]} {row[7]}'

                if exercise_name not in exercises:
                    exercises[exercise_name] = [{student_name: instructor_name}]
                else:
                    exercises[exercise_name].append({student_name: instructor_name})

            for exercise, students in exercises.items():
                print (f'{exercise}:')
                for student in students:
                    for k, v in student.items():
                        print(f'\t*{v} assigned this to {k}')

    def instructors_and_students(self):
        cohorts = dict()


        with sqlite3.connect(self.db_path) as conn:

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select c.Id,
                c.Name ,
                s.FirstName,
           	    s.LastName,
                i.FirstName,
                i.LastName
            from Cohort c
            join Student s on c.Id = s.CohortId
            join Instructor i on s.CohortId = i.CohortId
            order by c.Id
            """)

            data_set = db_cursor.fetchall()

            for row in data_set:
                instructor_id = row[0]
                cohort_name = row[1]
                student_name = f'{row[2]} {row[3]}'
                instructor_name = f'{row[4]} {row[5]}'

                if cohort_name not in cohorts:
                    cohorts[cohort_name] = {'Students' : set(), 'Instructor' : set()}
                    cohorts[cohort_name]['Students'].add(student_name)
                    cohorts[cohort_name]['Instructor'].add(instructor_name)

                else:
                    cohorts[cohort_name]['Students'].add(student_name)
                    cohorts[cohort_name]['Instructor'].add(instructor_name)

            for cohort, people in cohorts.items():
                    print(f'{cohort}:'  )
                    for type, persons in people.items():
                        print(f'  {type}')
                        for person in persons:
                            if type == "Students":
                                print(f'  * {person} is a student in {cohort}.')
                            else:
                                print(f'  * {person} is an instructor for {cohort}.')




# print("\n Students")
reports = StudentExerciseReports()
# reports.all_students()
# print("\n Cohorts")
# reports.all_cohorts()
# print("\n Exercises")
# reports.all_exercises()
# print("\n JavaScript Exercises")
# reports.JS_exercises()
# print("\n Pyhton Exercises")
# reports.python_exercises()
# print("\n C# Exercises")
# reports.csharp_exercises()
# print("\n Instructors")
# reports.all_instructors()
#print("\n Student's Exercises")
# reports.students_exercises()
#reports.student_exercises()
# reports.assigned_by()
reports.instructors_and_students()
