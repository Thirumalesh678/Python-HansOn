from Employee import Employee

employees= {
    401:  Employee('thiru',678,'A1',2500000),
    402:  Employee('chinna',679,'A1',1500000),
    403:  Employee('sai',675,'A1',4500000)
}
for emp_id,emp  in employees.items():
    e = emp.showEmployee()
    print(e)
for emp_id,emp in employees.items():
    bouns = emp.calculatebouns(0.12)
    print(emp.name +"'s bouns is: ",bouns)







'''emp = Employee('thiru',678,'A1',2500000)

emp.showEmployee()

print(emp.name ," bouns is added & here is the updated CTC: ",emp.calculatebouns(0.12))'''
