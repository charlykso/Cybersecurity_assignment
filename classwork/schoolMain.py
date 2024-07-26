from faculty import Faculty as f
from department import Department as d
from course import Course as c
from course import Invoice
from course import AddNumbers


faculty1 = f("Natural Science", "naturalSc@gmail.com")
department1 = d("Computer Science", "csc@gmail.com", faculty1.id)
print(faculty1)
faculty1.departments.append(department1.name)
print(department1)
print(faculty1.departments)
department2 = d("Mathematics", "maths@gmail.com", faculty1.id)
faculty1.departments.append(department2.name)
print(faculty1.departments)
course1 = c("Machine Learning", "ML202", department1.id)
department1.courses.append(course1.code)
print(department1.courses)
print(department1.getId())
print(" ")
invoice1 = Invoice(2, "new invoice", 3, 100)

def invoiceAmount(qtt=None , price=None):
    if qtt is None and price is None:
        return 4 * 100
    elif qtt is None:
        price * 1
    elif price is None:
        return qtt * 50
    return qtt * price

print(invoiceAmount())