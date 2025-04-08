class Person:
    def __init__(self, age, full_name, married):
        self.age = age
        self.full_name = full_name
        self.married = married
    def introduce_myself(self):
        status = " is married" if self.married else "single"
        print(f'Full name: {self.full_name} Age: {self.age} Marital status: {status}')



class Student(Person):
    def __init__(self,age, full_name, married, marks):
        super().__init__(age, full_name, married)
        self.marks = marks

    def introduce_myself(self):
        super().introduce_myself()
        print("Оценки:")
        for subject, marks in self.marks.items():
            print(f" - {subject}: {marks}")

    def average_mark(self):
        if self.marks:
            average = sum(self.marks.values()) / len(self.marks)
            return round(average, 2)
        return 0

class Teacher(Person):
    base_salary = 30000

    def __init__(self, full_name, age, married, experience):
        super().__init__(full_name, age, married)
        self.experience = experience

    def calculate_salary(self):
        if self.experience <= 3:
            return self.base_salary
        bonus = 0.05 * (self.experience - 3) * self.base_salary
        return self.base_salary + bonus

    def introduce_myself(self):
        super().introduce_myself()
        print(f'Experience: {self.experience} years')
        print(f'Calculated Salary: {self.calculate_salary():.2f}')
teacher_math = Person( 34, 'Aleksandr', 'married' )
print( f'Age: {teacher_math.age} Full_name: {teacher_math.full_name} maried:{teacher_math.married}')


def create_students():
    student1 = Student('Alice Johnson', 16, False, {'Math': 85, 'Physics': 90, 'English': 88})
    student2 = Student('Bob Smith', 17, False, {'Math': 70, 'Physics': 75, 'English': 80})
    student3 = Student('Carol Davis', 16, False, {'Math': 92, 'Physics': 89, 'English': 94})
    return [student1, student2, student3]


teacher = Teacher('John Doe', 40, True, 10)
teacher.introduce_myself()

students = create_students()
for student in students:
    student.introduce_myself()
    print('-' * 40)
