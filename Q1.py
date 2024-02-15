employee_salary_dict = {}

while True:
    employee_name = input("Enter employee name (or 'no' to exit): ")
    
    if employee_name.lower() == 'no':
        break
    
    try:
        employee_salary = float(input("Enter employee salary: "))
    except ValueError:
        print("Invalid input for salary. Please enter a valid number.")
        continue

    employee_salary_dict[employee_name] = employee_salary

print("\nEmployee data entered:")
for name, salary in employee_salary_dict.items():
    print(f"{name}: ${salary}")
