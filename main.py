print("EMPLOYEE PAYROLL MANAGEMENT SYSTEM")

company = "PT SINERGI"
employee_name = "Budi Santoso"
employee_id = "EMP001"
department = "Accounting"
position = "Junior Accountant"

basic_salary = 5000000
transport_allowance = 650000
meal_allowance = 400000
overtime_pay = 350000
performance_bonus = 1000000

gross_salary = (
    basic_salary
    + transport_allowance
    + meal_allowance
    + overtime_pay
    + performance_bonus
)

tax = gross_salary * 0.05
bpjs = 250000

total_deduction = tax + bpjs
net_salary = gross_salary - total_deduction

print(f"Company Name      : {company}")
print(f"Employee Name     : {employee_name}")
print(f"Employee ID       : {employee_id}")
print(f"Department        : {department}")
print(f"Position          : {position}")

print("SALARY DETAILS")

print(f"Basic Salary          : Rp {basic_salary:,}")
print(f"Transport Allowance   : Rp {transport_allowance:,}")
print(f"Meal Allowance        : Rp {meal_allowance:,}")
print(f"Overtime Pay          : Rp {overtime_pay:,}")
print(f"Performance Bonus     : Rp {performance_bonus:,}")

print(f"Gross Salary          : Rp {gross_salary:,.0f}")

print("\nDEDUCTIONS")
print(f"Income Tax (5%)       : Rp {tax:,.0f}")
print(f"BPJS                  : Rp {bpjs:,}")

print(f"Total Deduction       : Rp {total_deduction:,.0f}")

print(f"NET SALARY            : Rp {net_salary:,.0f}")

if net_salary >= 8000000:
    salary_status = "Excellent Salary"
elif net_salary >= 6000000:
    salary_status = "Good Salary"
else:
    salary_status = "Standard Salary"

print(f"Salary Status     : {salary_status}")

attendance = 22
present = 21
absent = attendance - present

attendance_percentage = (present / attendance) * 100

print("\nATTENDANCE SUMMARY")
print(f"Working Days      : {attendance}")
print(f"Present           : {present}")
print(f"Absent            : {absent}")
print(f"Attendance Rate   : {attendance_percentage:.2f}%")

if attendance_percentage >= 95:
    performance = "Outstanding"
elif attendance_percentage >= 85:
    performance = "Very Good"
else:
    performance = "Needs Improvement"

print(f"Performance       : {performance}")

print("\nREPORT STATUS")
print("Payroll Process   : Completed")
print("Report Status     : Successfully Generated")