num = int(input("Enter a number: "))

if num < 0:
    print("Error: Factorial is not defined for negative numbers.")
else:
    factorial = 1
    i = 1

    while i <= num:
        factorial *= i
        i += 1

    print(f"The factorial of {num} is {factorial}")