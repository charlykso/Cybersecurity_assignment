from schoolBase import SchoolBase as SB


class Faculty(SB):
    def __init__(self, name, email) -> None:
        super().__init__(name, email)
        self.departments = []
        self.members = []
    
    def getDepartments(self):
        return self.departments
    def getMembers(self):
        return self.members
    
    def __str__(self) -> str:
        return super().__str__()