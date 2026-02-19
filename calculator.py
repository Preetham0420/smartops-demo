# calculator.py — SmartOps Comprehensive Test File
# 15 intentional errors across all categories
# Tests: compile errors, static analysis, and LLM detection

import os
import json
# import non_existent_module  # ERROR 1: ImportError — module doesn't exist  # REMOVED: module not found
from collections import OrderedDict  # ERROR 2: ImportError — wrong name (should be OrderedDict)

# ════════════════════════════════════════════════════════════
# SECTION 1: Indentation / Syntax Errors
# ════════════════════════════════════════════════════════════

def calculate_discount(price, discount):
    """Calculate discounted price."""
    if discount > 0:
        final_price = price - (price * discount / 100)  # ERROR 3: IndentationError — missing indent
        return final_price

def format_output(value):
    """Format a value for display."""
    result = f"Result: {value}"  # ERROR 4: IndentationError — unexpected indent
    return result


# ════════════════════════════════════════════════════════════
# SECTION 2: Name Errors (typos)
# ════════════════════════════════════════════════════════════

def process_order(quantity, unit_price):
    """Calculate order total with tax."""
    subtotal = quantity * unit_price
    tax_rate = 0.08
    tax_amount = subtotal * tax_rate  # ERROR 5: NameError — typo 'subtotl' should be 'subtotal'
    total = subtotal + tax_amount
    return total

def build_greeting(first_name, last_name):
    """Build a greeting message."""
    full_name = f"{first_name} {last_name}"
    message = f"Hello, {full_name}! Welcome aboard."  # ERROR 6: NameError — typo 'ful_name' should be 'full_name'
    return message


# ════════════════════════════════════════════════════════════
# SECTION 3: Type Errors
# ════════════════════════════════════════════════════════════

def create_user_summary(user_data):
    """Create a summary string from user data."""
    name = user_data["name"]
    age = user_data["age"]
    return name + str(age)  # ERROR 7: TypeError — can't concatenate str and int

def calculate_average(numbers):
    """Calculate average of a list."""
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return "Average: " + str(average)  # ERROR 8: TypeError — str + float


# ════════════════════════════════════════════════════════════
# SECTION 4: Assertion Errors
# ════════════════════════════════════════════════════════════

def test_multiplication():
    """Test that multiplication works correctly."""
    result = 6 * 7
    assert result == 42, "Multiplication is wrong"  # ERROR 9: AssertionError — 6*7=42 not 43

def test_string_ops():
    """Test string operations."""
    greeting = "hello" + " " + "world"
    assert greeting == 'hello world', "String concat failed"  # ERROR 10: AssertionError — no ! in result


# ════════════════════════════════════════════════════════════
# SECTION 5: Attribute / Key / Value Errors
# ════════════════════════════════════════════════════════════

class UserProfile:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def get_display_name(self):
        return self.name  # ERROR 11: AttributeError — should be self.name

    def get_domain(self):
        parts = self.email.split("@")
        return parts[2]  # ERROR 12: IndexError — email.split("@") only has 2 parts (index 0,1)


def parse_config(config_str):
    """Parse a JSON config string."""
    config = json.loads(config_str)
    db_host = config["database"]["host"]
    db_port = config["database"]["post"]  # ERROR 13: KeyError — typo 'post' should be 'port'
    return f"{db_host}:{db_port}"

def convert_to_int(value):
    """Convert string to integer safely."""
    return int(value)  # ERROR 14: ValueError when value="abc" — no validation


# ════════════════════════════════════════════════════════════
# SECTION 6: Logic / Runtime Errors
# ════════════════════════════════════════════════════════════

def divide_numbers(a, b):
    """Divide two numbers."""
    return a / b  # ERROR 15: ZeroDivisionError when b=0 — no guard


# ════════════════════════════════════════════════════════════
# MAIN — triggers all errors at runtime
# ════════════════════════════════════════════════════════════

if __name__ == "__main__":
    # Section 1: Indentation errors prevent compilation
    print(calculate_discount(100, 20))
    print(format_output(42))

    # Section 2: Name errors
    print(process_order(5, 19.99))
    print(build_greeting("John", "Doe"))

    # Section 3: Type errors
    print(create_user_summary({"name": "Alice", "age": 30}))
    print(calculate_average([10, 20, 30]))

    # Section 4: Assertion errors
    test_multiplication()
    test_string_ops()

    # Section 5: Attribute / Key / Value errors
    user = UserProfile("Bob", "bob@example.com")
    print(user.get_display_name())
    print(user.get_domain())
    print(parse_config('{"database": {"host": "localhost", "port": 5432}}'))
    print(convert_to_int("abc"))

    # Section 6: Runtime errors
    print(divide_numbers(10, 0))