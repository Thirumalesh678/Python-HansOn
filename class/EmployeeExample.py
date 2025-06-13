class Employee:

    def __init__(self,name,e_id,dept):
        self.name=name
        self.e_id=e_id       
        self.dept=dept

    def addEmployee(self):
        print("hello my name is: ", self.name)
        print("my Employee Id is: ", self.e_id)
        print("hello I belong to "+self.dept+" department")
         

emp = Employee('thiru',678,'A1')
print(emp.name)
print(emp.e_id)
print(emp.dept)
emp.addEmployee()
