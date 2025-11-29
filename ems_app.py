
class Employee:
    num_of_employees = 0 


    existing_ids = set() 


    def __init__(self, name, emp_id, salary, position, length_of_service, age, sex, department = "General"):

        if emp_id in Employee.existing_ids:
            raise ValueError(f"Employee ID {emp_id} already exists!")

        if not name.strip():
            raise ValueError("Name cannot be empty.")

        if age <= 0 or age > 120:
            raise ValueError("Invalid age: must be between 1 and 120.")

        Employee.existing_ids.add(emp_id)

        Employee.num_of_employees += 1 
         
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
        self.position = position
        self.length_of_service = length_of_service
        self.age = age
        self.sex = sex
        self.department = department

    def show_details(self):
        return f"{self.name}, ID: {self.emp_id}, Position: {self.position}, Salary: {self.salary}"

    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative!")
        self._salary = value

    def __str__(self):
        return f"{self.name}, ID: {self.emp_id}, Position: {self.position}, Salary: {self.salary}"

    def __repr__(self):
        return f"Employee('{self.name}', {self.emp_id}, {self.salary}, '{self.position}')"

class Manager (Employee):
    def __init__(self, name, emp_id, salary, position, length_of_service, age, sex, department="General"):
        super().__init__(name, emp_id, salary, position, length_of_service, age, sex, department)
        self.team = []
    
    def add_employee(self, employee):
        self.team.append(employee) 

    def list_team(self):
        for emp in self.team:
           print(emp.show_details())


    def calculate_bonus(self):
        bonus = self.salary * 0.10
        return bonus

    def show_details(self):
        return f"{self.name}, ID: {self.emp_id}, position: {self.position}, salary: {self.salary}"

    def apply_raise(self, amount):
          self.salary +=amount
          return self.salary

    def change_department(self, department):
        self.department = department 

class Developer(Employee):
    def __init__(self, name, emp_id, salary, position, length_of_service, age, sex, department="General"):
        super().__init__(name, emp_id, salary, position, length_of_service, age, sex, department)

    def calculate_bonus(self):
        return self.salary * 0.05

class Intern(Employee):
    def __init__(self, name, emp_id, salary, position, length_of_service, age, sex, department="General"):
        super().__init__(name, emp_id, salary, position, length_of_service, age, sex, department)

    def calculate_bonus(self):
        return 0

employees = []

while True:
    print("1. Add Employee")
    print("2. List All Employees")
    print("3. Search Employee")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        emp_id = int(input("Enter ID: "))
        salary = float(input("Enter salary: "))
        position = input("Enter position: ")
        length_of_service = int(input("Enter years of service: "))
        age = int(input("Enter age: "))
        sex = input("Enter sex (M/F): ")
        department = input("Enter department: ")

        new_emp = Employee(name, emp_id, salary, position, length_of_service, age, sex, department)
        employees.append(new_emp)
        print("Employee added successfully!")

    elif choice == "2":
        if not employees:
            print("No employees found.")
        else:
            for emp in employees:
                print(emp.show_details())
    elif choice == "3":
        search_id = int(input("Enter employee ID to search: "))
        found = False
        for emp in employees:
            if emp.emp_id == search_id:
                print("Employee found:")
                print(emp.show_details())
                found = True
                break

        if not found:
            print("Employee not found.")

    elif choice == "4":
        print("Goodbye!")
        break