class User:
    def personal_details(self):
        users_info = print("Personal Details of users!!!")
        Name = input("Enter the User's Name:")
        Age = int(input("Enter the User's Age:"))
        Address = input("Enter the User's Address:")
        self.list = [Name, Age, Address]

    def added_age(self):
        year_to_add = int(input("\nEnter number of years to add to your current age: "))
        self.list[1] += year_to_add
        print (self.list)
        return self.list

if __name__ == "__main__":
    objusr = User()
    objusr.personal_details()
    objusr.added_age()