def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b

def minus(a, b):
    print(f"Subtracting {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"Multiplying {a} * {b}")
    return a * b

def divide(a, b):
    print(f"Dividing {a} / {b}")
    return a / b

if __name__ == "__main__":
    print("Result:", add(2, 3))
    print("Result:", minus(5, 2))
    print("Result:", multiply(3, 4))
    print("Result:", divide(10, 2))