import calculator

def print_menu():
    print("\n=== 🧮 Python Calculator ===")
    print(" 1. Add         2. Subtract")
    print(" 3. Multiply    4. Divide")
    print(" 5. Power       6. Sum (n)")
    print(" 7. Logarithm   8. Modulo")
    print(" 9. Square Root 10. Factorial")
    print("11. Absolute    0. Exit")

def _ab():
    return float(input('a: ')), float(input('b: '))

def main():
    while True:
        print_menu()
        choice = input("Select: ")
        if choice == '0': print("Goodbye!"); break
        try:
            if   choice == '1':  a,b = _ab(); print(calculator.add(a,b))
            elif choice == '2':  a,b = _ab(); print(calculator.subtract(a,b))
            elif choice == '3':  a,b = _ab(); print(calculator.multiply(a,b))
            elif choice == '4':  a,b = _ab(); print(calculator.divide(a,b))
            elif choice == '5':  a,b = _ab(); print(calculator.power(a,b))
            elif choice == '6':  nums=list(map(float,input('numbers: ').split())); print(calculator.sum_n(*nums))
            elif choice == '7':  a=float(input('a: ')); print(calculator.logarithm(a))
            elif choice == '8':  a,b = _ab(); print(calculator.modulo(a,b))
            elif choice == '9':  a=float(input('a: ')); print(calculator.sq_root(a))
            elif choice == '10': n=int(input('n: ')); print(calculator.factorial(n))
            elif choice == '11': a=float(input('a: ')); print(calculator.absolute(a))
            else: print('Invalid option')
        except Exception as e:
            print(f'Error: {e}')

if __name__ == '__main__':
    main()