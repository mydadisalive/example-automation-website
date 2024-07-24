class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

def main():
    calc = Calculator()
    print("Addition: 1 + 2 =", calc.add(1, 2))
    print("Subtraction: 10 - 5 =", calc.subtract(10, 5))
    print("Multiplication: 3 * 7 =", calc.multiply(3, 7))
    print("Division: 10 / 2 =", calc.divide(10, 2))

if __name__ == "__main__":
    main()
