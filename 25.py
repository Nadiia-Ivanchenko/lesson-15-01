class Group:
    def __init__(self, group_name):
        self.group_name = group_name
        self.students = []

    def add_student(self, student_name):
        if len(self.students) >= 10:
            raise ValueError("Group is full. Cannot add more than 10 students.")
        self.students.append(student_name)
        print(f"Student {student_name} added to the group {self.group_name}.")

# Приклад використання класу та обробки винятку користувача
group_name = "Group A"
group = Group(group_name)

try:
    for i in range(11):
        student_name = f"Student {i+1}"
        group.add_student(student_name)
except ValueError as e:
    print(f"Error: {e}")