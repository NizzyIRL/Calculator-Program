


print("Simple Calculator")
print("Operator choices:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

num_1 = float(input("Enter first digit: "))
num_2 = float(input("Enter second digit: "))
choice = input("What operation would you like to do? (1,2,3,4): ")

if choice == "1":
    result = num_1 + num_2
    print(f"Adding {num_1} and {num_2},the result is {round(result, 2)}.")

elif choice == "2":
    result = num_1 - num_2
    print(f"Subtracting {num_1} and {num_2},the result is {round(result, 2)}.")

elif choice == "3":
    result = num_1 * num_2
    print(f"Multiplying {num_1} and {num_2},the result is {round(result, 2)}.")

elif choice == "4":
    if num_2 != 0:
        result = num_1 / num_2
        print(f"Dividing {num_1} and {num_2},the result is {round(result, 2)}.")
    else:
        print("Division by zero is not allowed.")
else:
    print("Invalid choice. Please select 1,2,3 or 4.")