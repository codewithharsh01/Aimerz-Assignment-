 def show_menu():
    print("\n==== Simple Calculator ====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Power (^)")
    print("7. Exit the program")

def calculator():
    while True:
        show_menu()
        choice = input("Choose an operation (1-7): ")

        if choice == '7':
            print("Exiting the program. Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5', '6']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print("Result:", num1 + num2)
                elif choice == '2':
                    print("Result:", num1 - num2)
                elif choice == '3':
                    print("Result:", num1 * num2)
                elif choice == '4':
                    if num2 == 0:
                        print("Error: Cannot divide by zero.")
                    else:
                        print("Result:", num1 / num2)
                elif choice == '5':
                    print("Result:", num1 % num2)
                elif choice == '6':
                    print("Result:", num1 ** num2)
            except ValueError:
                print("Invalid input. Please enter numeric values.")
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")

        # Ask if user wants to continue
        cont = input("Do you want to perform another calculation? (yes/no): ").lower()
        if cont not in ['yes', 'y']:
            print("Thank you for using the calculator. Goodbye!")
            break

# Run the calculator
calculator()

