from student import Student
from lecturer import Lecturer

student1 = Student("Emeka", "Eze", "emeka@gmail.com", "emeka123", "LISTACC/CS/0001", "Cyber security")
student2 = Student("Henry", "Nwafor", "henry@gmail.com", "henry123", "LISTACC/ML/00002", "Machine Learning")

lecturer1 = Lecturer("Miracle", "Sixtus", "miracle@gmail.com", "miracle123", "LIS020")
lecturer2 = Lecturer("Councel", "Okeke", "councel@gmail.com", "councel123", "LIS030")

print(student1.getLoginDetails())
print(student1.getStudentDetails())

print(student2.getLoginDetails())
print(student2.getStudentDetails())

print(lecturer1.getLoginDetails())
print(lecturer1.getLecturerDetails())

print(lecturer2.getLoginDetails())
print(lecturer2.getLecturerDetails())