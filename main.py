# Python Project: Employee Salary Analyzer
# This program demonstrates file handling, functions, loops, and simple data analysis.

employees = [
    {"name": "Rahul Sharma", "department": "IT", "salary": 55000},
    {"name": "Sneha Mishra", "department": "HR", "salary": 45000},
    {"name": "Amit Patel", "department": "Finance", "salary": 60000},
    {"name": "Priya Das", "department": "IT", "salary": 52000}
]

# Function to display all employees
def display_employees(data):
    print("Employee List:")
    for emp in data:
        print(emp["name"], "-", emp["department"], "-", emp["salary"])
    print()

# Function to calculate highest salary
def highest_salary(data):
    return max(data, key=lambda x: x["salary"])

# Function to calculate department-wise total salary
def salary_by_department(data):
    totals = {}
    for emp in data:
        dept = emp["department"]
        totals[dept] = totals.get(dept, 0) + emp["salary"]
    return totals

display_employees(employees)

highest = highest_salary(employees)
print("Highest Salary:", highest["name"], "-", highest["salary"])

totals = salary_by_department(employees)
print("\nDepartment-wise Salary Total:")
for dept, total in totals.items():
    print(dept, ":", total)
