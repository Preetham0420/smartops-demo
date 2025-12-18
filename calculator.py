def add_numbers(a, b):
    return a + b

def test_add():
    assert add_numbers(2, 3) == 5
    assert add_numbers(0, 0) == 0
    assert add_numbers(-1, 1) == 0
    assert add_numbers(10, 5) == 99  # THIS WILL FAIL!
    print("All tests passed!")

if __name__ == "__main__":
    test_add()

# [SmartOps Auto-Fix] AI Suggested Remediation:
# $ sed -i '12,13d' smartops-demo/calculator.py && echo "assert add_numbers(10, 5) == 15" >> smartops-demo/calculator.py

# [SmartOps Auto-Fix] AI Suggested Remediation:
# $ cat logs/error.log