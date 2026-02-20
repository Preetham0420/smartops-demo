# inventory_system.py — Warehouse Management Test File
# 15 intentional errors for comprehensive testing
# Theme: Product inventory and order processing system

import sys
import math
import datetime
from typing import List, Dict
import imaginary_warehouse_api  # ERROR 1: ImportError — non-existent module
from decimal import decmal  # ERROR 2: ImportError — typo, should be 'Decimal'


# ════════════════════════════════════════════════════════════
# SECTION 1: Syntax & Indentation Errors
# ════════════════════════════════════════════════════════════

def validate_stock_level(product_id, quantity):
    """Check if stock level is sufficient."""
    min_threshold = 10
    if quantity < min_threshold:
print(f"Warning: Low stock for {product_id}")  # ERROR 3: IndentationError — needs indent
        return False
    return True

def generate_report(items):
    """Generate inventory report."""
    report = []
    for item in items:
            report.append(f"{item['id']}: {item['count']}")  # ERROR 4: IndentationError — over-indented
    return "\n".join(report)


# ════════════════════════════════════════════════════════════
# SECTION 2: Name Errors (undefined variables)
# ════════════════════════════════════════════════════════════

def calculate_shipping_cost(weight, distance):
    """Calculate shipping cost based on weight and distance."""
    base_rate = 5.50
    weight_charge = weight * 0.75
    distance_charge = distance * 0.30
    total_cost = base_rate + weight_charge + distanc_charge  # ERROR 5: NameError — typo 'distanc_charge'
    return total_cost

def create_product_label(sku, description, price):
    """Create a formatted product label."""
    label = f"SKU: {sku}\n"
    label += f"Description: {description}\n"
    label += f"Price: ${priice:.2f}"  # ERROR 6: NameError — typo 'priice' should be 'price'
    return label


# ════════════════════════════════════════════════════════════
# SECTION 3: Type Errors
# ════════════════════════════════════════════════════════════

def merge_order_info(order_id, customer_name):
    """Merge order information into a single string."""
    return order_id + " - " + customer_name  # ERROR 7: TypeError — order_id is int, can't concatenate with str

def calculate_bulk_discount(quantity, unit_price):
    """Calculate price with bulk discount."""
    discount_rate = 0.15 if quantity > 100 else 0
    discounted_price = unit_price * (1 - discount_rate)
    return quantity * discounted_price + " items"  # ERROR 8: TypeError — float + str


# ════════════════════════════════════════════════════════════
# SECTION 4: Assertion Errors
# ════════════════════════════════════════════════════════════

def test_price_calculation():
    """Test that price calculation is correct."""
    items = [{"price": 10, "qty": 3}, {"price": 20, "qty": 2}]
    total = sum(item["price"] * item["qty"] for item in items)
    assert total == 80, "Price calculation failed"  # ERROR 9: AssertionError — actual is 70 (30+40)

def test_inventory_update():
    """Test inventory update logic."""
    current_stock = 50
    sold = 15
    restocked = 25
    final_stock = current_stock - sold + restocked
    assert final_stock == 65, "Inventory update incorrect"  # ERROR 10: AssertionError — actual is 60


# ════════════════════════════════════════════════════════════
# SECTION 5: Attribute / Index / Key Errors
# ════════════════════════════════════════════════════════════

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    
    def get_tax_amount(self):
        tax_rate = 0.07
        return self.cost * tax_rate  # ERROR 11: AttributeError — should be self.price
    
    def get_discounted_price(self, discount_percent):
        discount_amount = self.price * discount_percent / 100
        return self.price - discount_amount


class Warehouse:
    def __init__(self, location):
        self.location = location
        self.inventory = []
    
    def get_most_expensive_item(self):
        if not self.inventory:
            return None
        sorted_items = sorted(self.inventory, key=lambda x: x.price, reverse=True)
        return sorted_items[0].description  # ERROR 12: AttributeError — Product has 'name' not 'description'


def extract_postal_code(address):
    """Extract postal code from address string."""
    parts = address.split(",")
    # Expects format: "123 Main St, City, State, 12345"
    return parts[4].strip()  # ERROR 13: IndexError — only 4 parts (indices 0-3), not 5


def get_supplier_email(suppliers_dict, supplier_id):
    """Get email for a specific supplier."""
    supplier = suppliers_dict[supplier_id]
    return supplier["email_address"]  # ERROR 14: KeyError — key is 'email' not 'email_address'


# ════════════════════════════════════════════════════════════
# SECTION 6: Value & Logic Errors
# ════════════════════════════════════════════════════════════

def parse_quantity(qty_string):
    """Parse quantity from string input."""
    # ERROR 15: ValueError when qty_string="twenty" or other non-numeric
    return int(qty_string)  # No validation for non-numeric strings


def calculate_profit_margin(revenue, costs):
    """Calculate profit margin percentage."""
    profit = revenue - costs
    margin = (profit / costs) * 100  # ERROR 16: ZeroDivisionError when costs=0
    return margin


# ════════════════════════════════════════════════════════════
# MAIN — Test runner
# ════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 60)
    print("WAREHOUSE INVENTORY SYSTEM - ERROR TEST SUITE")
    print("=" * 60)
    
    # Section 1: Syntax errors prevent compilation
    print("\n[Testing Stock Validation]")
    validate_stock_level("PROD-001", 5)
    
    print("\n[Testing Report Generation]")
    items = [{"id": "A1", "count": 50}, {"id": "B2", "count": 30}]
    print(generate_report(items))
    
    # Section 2: Name errors
    print("\n[Testing Shipping Cost]")
    print(f"Shipping: ${calculate_shipping_cost(10, 250):.2f}")
    
    print("\n[Testing Product Label]")
    print(create_product_label("SKU-12345", "Widget Pro", 29.99))
    
    # Section 3: Type errors
    print("\n[Testing Order Info Merge]")
    print(merge_order_info(1001, "Jane Smith"))
    
    print("\n[Testing Bulk Discount]")
    print(calculate_bulk_discount(150, 12.99))
    
    # Section 4: Assertion errors
    print("\n[Running Unit Tests]")
    test_price_calculation()
    test_inventory_update()
    
    # Section 5: Attribute/Index/Key errors
    print("\n[Testing Product Class]")
    product = Product("Laptop", 999.99, "Electronics")
    print(f"Tax: ${product.get_tax_amount():.2f}")
    
    warehouse = Warehouse("Building A")
    warehouse.inventory = [
        Product("Mouse", 25.00, "Accessories"),
        Product("Keyboard", 75.00, "Accessories")
    ]
    print(f"Most expensive: {warehouse.get_most_expensive_item()}")
    
    print("\n[Testing Address Parsing]")
    address = "456 Oak Ave, Springfield, IL, 62701"
    print(f"Postal code: {extract_postal_code(address)}")
    
    print("\n[Testing Supplier Lookup]")
    suppliers = {
        "SUP-001": {"name": "Acme Corp", "email": "contact@acme.com"}
    }
    print(get_supplier_email(suppliers, "SUP-001"))
    
    # Section 6: Value/Logic errors
    print("\n[Testing Quantity Parsing]")
    print(f"Quantity: {parse_quantity('fifty')}")
    
    print("\n[Testing Profit Margin]")
    print(f"Margin: {calculate_profit_margin(1000, 0):.2f}%")
    
    print("\n" + "=" * 60)
    print("TEST SUITE COMPLETE")
    print("=" * 60)
