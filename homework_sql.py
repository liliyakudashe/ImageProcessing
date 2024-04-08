import sqlite3


class University:
    def __init__(self, name):
        self.name = name
        self.conn = sqlite3.connect('students.db')
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS grades (
                id INTEGER PRIMARY KEY,
                student_id INTEGER,
                subject TEXT,
                grade REAL,
                FOREIGN KEY (student_id) REFERENCES students(id)
            )
        ''')
        self.conn.commit()

    def add_student(self, name, age):
        self.cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", (name, age))
        self.conn.commit()

    def add_grade(self, student_id, subject, grade):
        self.cursor.execute("INSERT INTO grades (student_id, subject, grade) VALUES (?, ?, ?)", (student_id, subject, grade))
        self.conn.commit()

    def get_students(self, subject=None):
        if subject:
            self.cursor.execute('''
                SELECT students.name, students.age, grades.subject, grades.grade 
                FROM students 
                INNER JOIN grades ON students.id = grades.student_id 
                WHERE grades.subject = ?
            ''', (subject,))
        else:
            self.cursor.execute('''
                SELECT students.name, students.age, grades.subject, grades.grade 
                FROM students 
                INNER JOIN grades ON students.id = grades.student_id
            ''')

        return self.cursor.fetchall()


u1 = University('Urban')

u1.add_student('Ivan', 26)
u1.add_student('Ilya', 24)

u1.add_grade(1, 'Python', 4.8)
u1.add_grade(2, 'PHP', 4.3)

print(u1.get_students())
print(u1.get_students('Python'))
