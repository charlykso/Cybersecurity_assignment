from schoolBase import SchoolBase as SB

class Department(SB):
    def __init__(self, name, email, facultyId) -> None:
        super().__init__(name, email)
        self.facultyId = facultyId
        self.lecturers = []
        self.courses = []
    
    def getLecturers(self):
        return self.lecturers
    def getCourses(self):
        return self.courses
    
    def getId(self):
        return f"{self.name} {self.email}"
    
    def __str__(self) -> str:
        return super().__str__()+ " " + str(self.facultyId)