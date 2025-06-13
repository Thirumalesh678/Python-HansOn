from Employee import Employee

#Initializing all the employee in our org
employees= {
    675:  Employee('thiru',675,'A1',2500000),
    678:  Employee('chinna',678,'A1',1500000),
    679:  Employee('sai',679,'A1',4500000)
}
#Display total payroll for our org
def totalpayroll(employees):
    totalsalary = 0
    for emp in employees.values():
        totalsalary += emp.salary
    print(totalsalary)

#Display Bonus and salary for all the employee in our org
def showBonusAndSalary():
    for emp_id,emp in employees.items():
         print(emp.name +"'s bonus is: ",emp.salary)
         bouns = emp.calculatebouns(0.12)
         print(emp.name +"'s bonus is: ",bouns)

#Finding employee from the collection
def findTheEmployee(empId):
    if(employees.get(empId)):
        return employees.get(empId)
    else:
        return []


#Displaying all the employee in our org
for emp_id,emp  in employees.items():
    e = emp.showEmployee()
    print("\n")


showBonusAndSalary()
print("\n")
#calibration for employee having less ctc 
employees[678].updateSalary(2500000)
print(employees[678].name+"'s bouns is: ",employees[678].salary)
print("\n")

#Bonues for all the employee in our org 
print("bonus after salary incremental \n")
showBonusAndSalary()

print("\n")
#Display total payroll for our org
totalpayroll(employees)

eId= int(input("input the employee id to find"))
empl =findTheEmployee(eId)
if empl!=[]:
    empl.showEmployee()
else:
    print("Employee not found!")







'''emp = Employee('thiru',678,'A1',2500000)

emp.showEmployee()

print(emp.name ," bouns is added & here is the updated CTC: ",emp.calculatebouns(0.12))'''
