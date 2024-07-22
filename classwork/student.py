from user import User

class Student(User):
    def __init__(self, firstname, lastname, email, password, regNo, department) -> None:
        super().__init__(firstname, lastname, email, password)
        self.regNo = regNo
        self.department = department
    
    def getRegNo(self):
        return self.regNo
    
    def getStudentDetails(self):
        return f" firstName: {self.firstname}\nlastName: {self.lastname}\nemail: {self.email}\npassword: {self.password}\nregNo: {self.regNo}\ndepartment: {self.department}"
    