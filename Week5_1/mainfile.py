from database import create_table
from user_info import students, lecturers

def menu():
    print("\n==== User Information ====")
    print("1. Name of Student")
    print("2. Name of Course")
    print("3. Name of Class")
    print("4. Name of Lecturer")
    print("5. Exit")

def main():
    create_table()
    while True:
        menu()
        choice = input("Select an option (1-5): ")
        if choice == '1':
            name = input("Enter name: ")
            course = input("Enter course: ")
            add_user(name, course)
        elif choice == '2':
            users = view_users()
            for user in users:
                print(user)
        elif choice == '3':
            name = input("Enter name of class: ")
            users = search_user(name)
            for user in users:
                print(user)
        elif choice == '4':
            user_id = int(input("Enter the name of lecturer: "))
            user = user_id(name)
            print(user)

        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
