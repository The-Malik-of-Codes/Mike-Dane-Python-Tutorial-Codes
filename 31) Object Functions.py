from student import Student

student1 = Student("Ahmad Mosaku", 21, "Systems Engineering", 5.0, False)
student2 = Student("Asmaau Mosaku", 19, "Mech Engineering", 4.45, True)
student3 = Student("Hind Mosaku", 21, "Medicine", 4.0, True)

print(student1.on_honour_roll())
print(student2.on_honour_roll())
print(student3.on_honour_roll())
