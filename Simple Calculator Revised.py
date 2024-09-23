def add(numbers):
    return sum(numbers)

def subtract(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def divide(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        if num == 0:
            return "Error! Division by zero."
        result /= num
    return result

print("Simple Calculator (multiple digits)")
print("Operator choices:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Input numbers
numbers = input("Enter numbers separated by spaces: ")
numbers = list(map(float, numbers.split()))

# Choose operation
choice = input("What operation would you like to do? (1, 2, 3, 4): ")

if choice == "1":
    result = add(numbers)
    print(f"Adding {numbers}, the result is {round(result, 2)}.")

elif choice == "2":
    result = subtract(numbers)
    print(f"Subtracting {numbers}, the result is {round(result, 2)}.")

elif choice == "3":
    result = multiply(numbers)
    print(f"Multiplying {numbers}, the result is {round(result, 2)}.")

elif choice == "4":
    result = divide(numbers)
    if isinstance(result, str):  # Check if there's an error message
        print(result)
    else:
        print(f"Dividing {numbers}, the result is {round(result, 2)}.")
else:
    print("Invalid choice. Please select 1, 2, 3, or 4.")