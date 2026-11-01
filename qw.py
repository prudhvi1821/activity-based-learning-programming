
name = input("Enter Employee Name: ")
emp_id = input("Enter Employee ID: ")

basic = float(input("Enter Basic Salary: "))
hra = float(input("Enter House Rent Allowance: "))
da = float(input("Enter Dearness Allowance: "))
overtime_hours = float(input("Enter Overtime Hours: "))
overtime_rate = float(input("Enter Overtime Rate per Hour: "))
incentive = float(input("Enter Incentive Amount: "))
if gross_salary <= 10000:
    deduction = 0

elif gross_salary <= 20000:
    deduction = (gross_salary - 10000) * 0.05

else:
    deduction = (10000 * 0.05) + ((gross_salary - 20000) * 0.10)

print("\n========================================")
print("          EMPLOYEE SALARY SLIP")
print("========================================")

print("Employee Name       :", name)
print("Employee ID         :", emp_id)

print("----------------------------------------")
print("              EARNINGS")
print("----------------------------------------")

print("Basic Salary        : Rs.", basic)
print("House Rent Allowance: Rs.", hra)
print("Dearness Allowance  : Rs.", da)
print("Overtime Amount     : Rs.", overtime)
print("Incentive Amount    : Rs.", incentive)

print("----------------------------------------")
print("Gross Salary        : Rs.", round(gross_salary, 2))

print("----------------------------------------")
print("              DEDUCTIONS")
print("----------------------------------------")

print("Total Deduction     : Rs.", round(deduction, 2))

print("----------------------------------------")
print("Net Salary          : Rs.", round(net_salary, 2))
print("========================================")
print("       Salary Process Completed")
print("========================================")
