# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b

def display_menu():
    print("\n📌 Simple Calculator Menu:")
    print("1. ➕ Addition")
    print("2. ➖ Subtraction")
    print("3. ✖️ Multiplication")
    print("4. ➗ Division")
    print("5. ❌ Exit")

def get_numbers():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2
    except ValueError:
        print("⚠️ Invalid input. Please enter numbers only.")
        return get_numbers()

def main():
    while True:
        display_menu()
        choice = input("Choose an operation (1-5): ")

        if choice == '5':
            print(" Exiting calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            num1, num2 = get_numbers()

            if choice == '1':
                result = add(num1, num2)
            elif choice == '2':
                result = subtract(num1, num2)
            elif choice == '3':
                result = multiply(num1, num2)
            elif choice == '4':
                result = divide(num1, num2)

            print(f"✅ Result: {result}")
        else:
            print("⚠️ Invalid choice. Please select from 1 to 5.")

if __name__ == "__main__":
    main()
