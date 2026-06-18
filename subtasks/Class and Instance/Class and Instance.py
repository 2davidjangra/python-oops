class Student:

    college = "ABC College"     # Class Variable

    def __init__(self, name):
        self.name = name        # Instance Variable

s1 = Student("David")
s2 = Student("Rahul")

print(Student.college)

print(s1.name)
print(s2.name)
