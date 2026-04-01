import sys
import calculator

def print_menu():
    print("\n--- Python Git-Flow Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Sum (n)")
    print("7. Logarithm")
    print("8. Modulo")
    print("9. Square Root")
    print("10. Factorial")
    print("11. Absolute Value")
    print("0. Exit")

def main():
    while True:
        print_menu()
        choice = input("Select an option: ")
        
        if choice == '0':
            print("Goodbye!")
            break
        
        try:
            if choice == '1':
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print(f"Result: {calculator.add(a, b)}")
            # ... TODO: {#{12}} Member 01: Complete the menu choices for other functions
            else:
                print("Feature not yet implemented or invalid choice.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
