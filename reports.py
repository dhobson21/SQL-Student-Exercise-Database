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

print("\n Students")
reports = StudentExerciseReports()
reports.all_students()
print("\n Cohorts")
reports.all_cohorts()
print("\n Exercises")
reports.all_exercises()
print("\n JavaScript Exercises")
reports.JS_exercises()
print("\n Pyhton Exercises")
reports.python_exercises()
print("\n C# Exercises")
reports.csharp_exercises()
print("\n Instructors")
reports.all_instructors()
