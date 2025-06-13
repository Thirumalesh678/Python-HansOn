class Employee:

    def __init__(self,name,e_id,dept, salary):
        self.name=name
        self.e_id=e_id       
        self.dept=dept
        self.salary=salary

    def showEmployee(self):
        print("hello my name is: ", self.name)
        print("my Employee Id is: ", self.e_id)
        print("hello I belong to "+self.dept+" department")


    def calculatebouns(self,bounsRate=0.1):
        return self.salary * bounsRate
    
    def updateSalary(self , newSalary):
        if( newSalary >0):
            self.salary=newSalary
            return True
        return False
    

   ''' class Manager(Employee):
        def __init__(self,name,e_id,salary,team_size=0):
            super().__init__(name)'''
         


