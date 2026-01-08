# test_complex_errors.py

def calculate_stats(numbers):
    if len(numbers) == 0:
        return None
    
    total = 0
        for num in numbers:
        total += num
    avg = total / len(numbers)  # Calculate average
    
    return avg

def process_data(data):
    results = []
    for item in data:
        if item > 0:
            squared = item ** 2
        doubled = item * 2  # ERROR: Wrong indent (should be 12 spaces to be inside if)
    results.append(squared + doubled)
    
    return results

def validate_input(x, y):
    if x < 0 or y < 0:
        raise ValueError("Negative values not allowed")
    
    if x == y:
        print("Values are equal")
        return True  # ERROR: Extra indent (should be 8 spaces, not 12)
    
return x + y  # ERROR: No indent (should be 4 spaces)

def main():
    nums = [1, 2, 3, 4, 5]
    result = calculate_stats(nums)
    print(f"Average: {result}")
    
    data = [1, -2, 3, -4, 5]
    processed = process_data(data)
    print(f"Processed: {processed}")
    
    val = validate_input(10, 20)
    print(f"Sum: {val}")