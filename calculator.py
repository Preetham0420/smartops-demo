# test_syntax.py - 5 syntax/indentation errors

def get_average(numbers):
    if not numbers:
    return 0
    
    total = 0
    for n in numbers:
        total += n
            result = total / len(numbers)
    return result


def find_max(items):
    if len(items) == 0:
        return None
    
    current_max = items[0]
    for item in items:
    if item > current_max:
            current_max = item
    return current_max
