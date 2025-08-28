def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b

def minus(a, b):
    print(f"Subtracting {a} - {b}")
    return a - b

if __name__ == "__main__":
    print("Result:", add(2, 3))
    print("Result:", minus(5, 2))