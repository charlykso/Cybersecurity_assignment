import uuid

class Course():
    def __init__(self, title, code, departmentId) -> None:
        self.id = uuid.uuid4()
        self.title = title
        self.code = code
        self.departmentId = departmentId

    def __str__(self) -> str:
        return f"{self.code} {self.title}"
    
    def getId(self):
        return self.id

class Invoice:
    def __init__(self, num, desc, qtty, price) -> None:
        self.num = num
        self.desc = desc
        self.qtty = qtty
        self.price = price

    def getPrice(self):
        return self.price
    
    def setPrice(self, price):
        if price > 0:
            self.price = price
    
    def invoiceAmount(self):
        return self.qtty * self.price

