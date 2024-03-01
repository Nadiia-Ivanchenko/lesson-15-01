class Student:
    def __init__(self, gender, age, first_name, last_name, group):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        self.group = group

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        return str(self) == str(other)
class Group:
    def __init__(self, group_name):
        self.group_name = group_name
        self.students = []

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)

    def delete_student(self, last_name):
        self.students = [student for student in self.students if student.last_name != last_name]

    def find_student(self, last_name):
        for student in self.students:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        return f"Group {self.group_name}: {[str(student) for student in self.students]}"

from student import Student
from group import Group

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert gr.find_student('Jobs') == st1
assert gr.find_student('Jobs2') is None

gr.delete_student('Taylor')
print(gr)
