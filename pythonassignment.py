employee_data = [
    {"Employee ID": "161E90", "Name": "sanjay", "Age": 41, "Salary": 56000},
    {"Employee ID": "161F91", "Name": "harshiti", "Age": 38, "Salary": 67500},
    {"Employee ID": "161F99", "Name": "arshul", "Age": 51, "Salary": 82100},
    {"Employee ID": "171E20", "Name": "sham", "Age": 30, "Salary": 55000},
    {"Employee ID": "171G30", "Name": "ram", "Age": 45, "Salary": 44000},
]
def sort_employee_data(choice):
    if choice == 1:  
        sorted_data = sorted(employee_data, key=lambda x: x["Age"])
    elif choice == 2:  
        sorted_data = sorted(employee_data, key=lambda x: x["Name"])
    elif choice == 3: 
        sorted_data = sorted(employee_data, key=lambda x: x["Salary"])
    else:
        print("Invalid choice. Please select a valid sorting parameter (1, 2, or 3).")
        return

    print("\nSorted Employee Data:")
    print("Employee ID\tName\tAge\tSalary")
    for employee in sorted_data:
        print(
            f"{employee['Employee ID']}\t{employee['Name']}\t{employee['Age']}\t{employee['Salary']}"
        )

print("Sort Employee Data:")
print("1. Sort by Age")
print("2. Sort by Name")
print("3. Sort by Salary")
choice = int(input("Enter your choice (1/2/3): "))

sort_employee_data(choice)