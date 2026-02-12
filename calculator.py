# test_complex_indent_errors_large.py

def calculate_stats(numbers):
    if len(numbers) == 0:
        return None  # ERROR: Missing indent
    
    total = 0
    for num in numbers:
        total += num
        avg = total / len(numbers)  # ERROR: Extra indent
    
    if avg > 0:
        print("Positive average")
        print("Checked average")  # ERROR: Wrong indent
    
    return avg


def process_data(data):
    results = []
    for item in data:
        if item > 0:
            squared = item ** 2
            doubled = item * 2  # ERROR: Should be inside if
            results.append(squared + doubled)  # ERROR: Extra indent
    
    for r in results:
            print("Result:", r)  # ERROR: Extra indent
            print("Done printing")  # ERROR: Wrong indent
    
    return results


def validate_input(x, y):
    if x < 0 or y < 0:
        raise ValueError("Negative values not allowed")
    
    if x == y:
        print("Values are equal")  # ERROR: Missing indent
        return True  # ERROR: Extra indent
    
    else:
            print("Values are different")  # ERROR: Extra indent
            return False  # ERROR: Wrong indent
    
    return x + y  # ERROR: No indent


def generate_report(values):
    report = {}
    for v in values:
        if v % 2 == 0:
            report[v] = "even"
            print("Even found")  # ERROR: Wrong indent
        else:
            report[v] = "odd"  # ERROR: Missing indent
    
    for key in report:
            print(key, report[key])  # ERROR: Extra indent
            print("Report complete")  # ERROR: Wrong indent
    
    return report


class DataProcessor:
    def __init__(self, data):
            self.data = data  # ERROR: Extra indent
            self.results = []  # ERROR: Wrong indent
    
    def clean_data(self):
        for d in self.data:
            if d is not None:
                self.results.append(d)
                print("Checked:", d)  # ERROR: Should be inside if
            return self.results
    
    def summarize(self):
      total = sum(self.results)  # ERROR: Wrong indent
      count = len(self.results)
      if count == 0:
        return None  # ERROR: Missing indent
        
        average = total / count  # ERROR: Extra indent
        return average


def main():
    nums = [1, 2, 3, 4, 5]
    result = calculate_stats(nums)
    print(f"Average: {result}")  # ERROR: Extra indent
    
    data = [1, -2, 3, -4, 5]
    processed = process_data(data)
    print(f"Processed: {processed}")
    
    report = generate_report(nums)
    print(report)  # ERROR: Wrong indent
    
    processor = DataProcessor(nums)
    cleaned = processor.clean_data()
    print("Cleaned:", cleaned)  # ERROR: Extra indent
    
    summary = processor.summarize()
    print("Summary:", summary)


if __name__ == "__main__":
    main()