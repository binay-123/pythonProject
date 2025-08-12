# You are tasked with developing a simple program for the Human Resources (HR) department to store and display basic employee information, including each employee’s name, salary, and job title.
# to_do list
# 1.Create at least two Employee objects with different data.
# 2.Call the display_info() method to show each employee’s details.
# 3.Call the give_raise() method to increase an employee’s salary and display the updated amount.
#endregion

class Employee:
    def __init__(self):
        self.employee_list = []

    def enter_employee_details(self):
        employee_info = print("!!!Detailed information of Company Employee!!!")
        no_of_employees = int(input("Enter the number of employees: "))
        for i in range(no_of_employees):
            self.employee_list.append(input("Enter the employee's name:\n "))
            self.employee_list.append(input("Enter the employee's salary:\n "))
            self.employee_list.append(input("Enter the employee's job tile:\n "))

    def display_info(self):
        print("Employee Information After entering their Basic Data: ")
        count = 2

        for index, item in enumerate(self.employee_list):
            print(item, end="\n")
            if index == count:
                count += 3
                print("\n")

    def give_raiser(self):
        count = 1
        increment = int(input(f"\nEnter the increase percentage amount for an employee's salary: "))
        for index, item in enumerate(self.employee_list):
            if index == count:
                self.employee_list[index] = int(self.employee_list[index]) + (increment / 100)
                count += 3


if __name__ == "__main__":
    obCandidate = Employee()

    obCandidate.enter_employee_details()
    obCandidate.display_info()
    obCandidate.give_raiser()
    obCandidate.display_info()
