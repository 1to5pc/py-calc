def add(x, y):
    """Addition function"""
    return x + y

def subtract(x, y):
    """Subtraction function"""
    return x - y

def multiply(x, y):
    """Multiplication function"""
    return x * y

def divide(x, y):
    """Division function"""
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def display_menu():
    """Display menu options"""
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

def cool_calculator():
    """Main calculator function"""
    display_menu()
    while True:
        choice = input("Enter your choice (1/2/3/4): ")
        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("The result of adding {} and {} is: {}".format(num1, num2, add(num1, num2)))
            elif choice == '2':
                print("The result of subtracting {} from {} is: {}".format(num2, num1, subtract(num1, num2)))
            elif choice == '3':
                print("The result of multiplying {} by {} is: {}".format(num1, num2, multiply(num1, num2)))
            elif choice == '4':
                print("The result of dividing {} by {} is: {}".format(num1, num2, divide(num1, num2)))

            next_calculation = input("Would you like to perform another calculation? (Y/n): ").lower()
            if next_calculation == "n":
                print("Thank you for using the Cool Calculator.")
                break
        else:
            print("Invalid input. Please enter a valid choice (1/2/3/4).")

if __name__ == "__main__":
    cool_calculator()
