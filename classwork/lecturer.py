from user import User

class Lecturer(User):
    def __init__(self, firstname, lastname, email, password, staffId):
        super().__init__(firstname, lastname, email, password)
        self.staffId = staffId
    
    def getStaffId(self):
        return self.staffId
    
    def getLecturerDetails(self):
        return f" firstName: {self.firstname}\nlastName: {self.lastname}\nemail: {self.email}\npassword: {self.password}\nstaffId: {self.staffId}"