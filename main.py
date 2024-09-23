class person():
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber=idnumber
    def display(self):
        print(self.name,self.idnumber)

class employee(person):
    def __init__(self, name, idnumber, salary, post):
        self.salary=salary
        self.post=post
        person.__init__(self, name, idnumber)
    
a=employee("Ayesha", 2785, 35000, "Teacher" )
a.display()
    
