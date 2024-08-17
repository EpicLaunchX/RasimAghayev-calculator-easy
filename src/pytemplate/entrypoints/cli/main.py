from src.pytemplate.domain.models import operands_factory
from src.pytemplate.service.calculator import Calculator


def main():
    # Get input values from the user
    first_operand = int(input("Enter the first operand: "))
    second_operand = int(input("Enter the second operand: "))
    action = input("Enter the action (add, subtract, multiply, divide): ").strip().lower()

    # Create Operands object
    operands = operands_factory(first_operand, second_operand)

    # Initialize Calculator
    calculator = Calculator()

    # Perform the calculation based on the action
    if action == "add":
        result = calculator.add(operands)
    elif action == "subtract":
        result = calculator.subtract(operands)
    elif action == "multiply":
        result = calculator.multiply(operands)
    elif action == "divide":
        result = calculator.divide(operands)
    else:
        print("Invalid action")
        return

    # Display the result
    print(f"The result is: {result}")


if __name__ == "__main__":
    main()
