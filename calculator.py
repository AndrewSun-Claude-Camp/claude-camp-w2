# Calculator

def get_valid_number(prompt):
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_valid_operator():
    while True:
        operator = input("Enter operator (+ , -, *, /): ").strip()
        if operator in ["+","-","*","/"]:
            return operator
        else:
            print("Invalid operator. Please try again.")

def calculate(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2    

print("\nCalculator")
num1 = get_valid_number("Enter first number: ")
operator = get_valid_operator()
num2 = get_valid_number("Enter second number: ")

result = calculate(num1, operator, num2)
print("Result:", result)

