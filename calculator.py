# test_logic.py - 5 logic/runtime errors

# import non_existent_module  # ImportError  # REMOVED: module not found

def calculate_discount(price, discount):
    final_price = price - (price * discount / 100)  # NameError: typo in 'discount'
    return final_price


def process_user(user_dict):
    name = user_dict["name"]
    age = user_dict["age"]
    return name + str(age)  # TypeError: can't concatenate str and int


def test_addition():
    result = 2 + 2
    assert result == 4, "Math is broken"  # AssertionError


def get_item(items, index):
    return items[index]  # Potential IndexError if index out of range


# This will fail at runtime
if __name__ == "__main__":
    print(calculate_discount(100, 20))
    print(process_user({"name": "John", "age": 30}))
    test_addition()