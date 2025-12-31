# test_multi_errors.py

def calculate(a, b):
    result = a + b
        print("Result:", result)
    return result


def divide(a, b):
    if b == 0:
        return None
     return a / b


def main():
    x = calculate(10, 5)
    y = divide(10, 2)
    print("Done")
