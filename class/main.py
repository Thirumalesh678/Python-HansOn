from Employee import Employee

#Initializing all the employee in our org
employees= {
    675:  Employee('thiru',675,'A1',2500000),
    678:  Employee('chinna',678,'A1',1500000),
    679:  Employee('sai',679,'A1',4500000)
}

def totalpayroll(employees):
    totalsalary = 0
    for emp in employees.values():
        totalsalary += emp.salary
    print(totalsalary)



#Displaying all the employee in our org
for emp_id,emp  in employees.items():
    e = emp.showEmployee()
    print("\n")

#Bonues for all employee in our org
for emp_id,emp in employees.items():
    print(emp.name +"'s bonus is: ",emp.salary)
    bouns = emp.calculatebouns(0.12)
    print(emp.name +"'s bonus is: ",bouns)
print("\n")

employees[678].updateSalary(2500000)
print(employees[678].name+"'s bouns is: ",employees[678].salary)
print("\n")


print("bonus after salary incremental \n")
for emp_id,emp in employees.items():
    print(emp.name +"'s bonus is: ",emp.salary)
    bouns = emp.calculatebouns(0.12)
    print(emp.name +"'s bonus is: ",bouns)

print("\n")

totalpayroll(employees)








'''emp = Employee('thiru',678,'A1',2500000)

emp.showEmployee()

print(emp.name ," bouns is added & here is the updated CTC: ",emp.calculatebouns(0.12))'''
