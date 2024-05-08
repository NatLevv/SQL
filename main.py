import sqlite3
class University:
    def __init__(self, name):
        self.name = name
        self.conn = sqlite3.connect('students.db')
        self.cur = self.conn.cursor()
        self.cur.execute('''create table if not exists students (
            id integer primary key,
            name text,
            age integer
        )''')
        self.cur.execute('''create table if not exists grades (
            id integer primary key,
            student_id integer,
            subject text,
            grade real,
            foreign key (student_id) references students(id)
        )''')

    def add_student(self, name, age):
        self.cur.execute('insert into students (name, age) values (?, ?)', (name, age))
        self.conn.commit()

    def add_grade(self, student_id, subject, grade):
        self.cur.execute('insert into grades (student_id, subject, grade) values (?, ?, ?)',
                         (student_id, subject, grade))
        self.conn.commit()

    def get_students(self, subject=None):
        if subject:
            self.cur.execute(
                'select s.name, s.age, g.subject, g.grade from students s inner join grades g on s.id = g.student_id where g.subject = ?',
                (subject,))
        else:
            self.cur.execute(
                'select s.name, s.age, g.subject, g.grade from students s inner join grades g on s.id = g.student_id')
        return self.cur.fetchall()


u1 = University('Urban')

u1.add_student('Ivan', 26)
u1.add_student('Ilya', 24)
u1.add_student('Asy', 29)
u1.add_student('Vasy', 27)

u1.add_grade(1, 'python', 4.8)
u1.add_grade(1, 'english', 4.5)
u1.add_grade(2, 'python', 4.3)
u1.add_grade(2, 'english', 4.7)
u1.add_grade(3, 'python', 4.6)
u1.add_grade(3, 'english', 4.9)
u1.add_grade(4, 'python', 5)
u1.add_grade(4, 'english', 5)

print(u1.get_students('python'))
print(u1.get_students('english'))

