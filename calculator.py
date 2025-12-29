def calculate_discount(price, discount_percent):
    if discount_percent > 100:
        raise ValueError("Discount cannot exceed 100%")
    return price * (1 - discount_percent / 100)

def test_discount_calculation():
    result = calculate_discount(100, 20)
    assert result == 70  # Wrong! Should be 80
    
    result2 = calculate_discount(50, 10)
    assert result2 == 45
    
if __name__ == "__main__":
    test_discount_calculation()
    print("All tests passed!")
