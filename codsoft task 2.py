def simple_calculator():
    print("=== Simple Calculator ===")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))


        print("Choose an operation:")
        print("1. Add (+)")
        print("2. Subract (-)")
        print("3.Multiply (*)")
        print("4. Divide (/)")
        operation = input("Enter the operation symbol (+,-,*,/): ")


        if operation == '+':
            result = num1 + num2
            op_name = "Addition"
        elif operation == '-':
            result = num1 - num2
            op_name = "Subtraction"
        elif operation == '*':
            result = num1 * num2
            op_name = "Multiplication"
        elif operation == '/':
            if num2 == 0:
                print("Error: Cannot divide by zero.")
                return
            result = num1/num2
            op_name = "Division"
        else:
            print("Invalid operation. Please choose +,-,*, or /.")
            return
        print(f"{op_name} result: {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

simple_calculator()        
