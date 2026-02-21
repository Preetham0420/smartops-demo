# inventory_system.py — SmartOps Comprehensive Stress Test
# A realistic inventory management system with 20 intentional errors
# Tests ALL detection categories including edge cases
#
# Error Distribution:
#   IndentationError:  2  (missing indent, extra indent)
#   ImportError:       2  (missing module, wrong name)
#   NameError:         2  (transposition, distant typo)
#   TypeError:         4  (str+float, str+int, str+sum, str+len)
#   AssertionError:    2  (wrong arithmetic, wrong calc)
#   AttributeError:    2  (wrong attr name, method typo)
#   IndexError:        2  (CSV overrun, split overrun)
#   KeyError:          1  (JSON config typo)
#   ValueError:        2  (unsafe float(), unsafe int())
#   ZeroDivisionError: 1  (callsite zero division)
#   ─────────────────────
#   Total: 20 errors

import os
import json
import math
import re
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Tuple
import imaginary_erp_module  # ERROR 1: ImportError — module doesn't exist
from collections import ordereddict  # ERROR 2: ImportError — should be OrderedDict


# ════════════════════════════════════════════════════════════
# Section 1: Product Model
# ════════════════════════════════════════════════════════════

class Product:
    """Represents a product in the inventory."""
    
    CATEGORIES = ["electronics", "clothing", "food", "furniture", "tools"]
    
    def __init__(self, sku: str, name: str, price: float, quantity: int, category: str):
        self.sku = sku
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
        self.created_at = datetime.now()
        self.last_updated = datetime.now()
    
    def apply_discount(self, percent: float) -> float:
        """Apply a percentage discount to the product."""
        if percent > 0:
        discounted = self.price * (1 - percent / 100)  # ERROR 3: IndentationError — missing indent
            self.price = round(discounted, 2)
        return self.price
    
    def get_value(self) -> float:
        """Get total value of this product's stock."""
            total_value = self.price * self.quantity  # ERROR 4: IndentationError — unexpected indent
        return total_value
    
    def get_label(self) -> str:
        """Generate a product label string."""
        return "SKU: " + self.sku + " | Price: $" + self.price  # ERROR 5: TypeError — str + float
    
    def restock(self, amount: int) -> int:
        """Add stock and return new quantity."""
        self.quantity += amount
        self.last_updated = datetime.now()
        return self.quanity  # ERROR 6: AttributeError — typo 'quanity' should be 'quantity'
    
    def get_age_days(self) -> int:
        """Get product age in days."""
        delta = datetime.now() - self.created_at
        return delta.total_secnods  # ERROR 7: AttributeError — typo 'total_secnods' should be 'total_seconds' (method)


# ════════════════════════════════════════════════════════════
# Section 2: Inventory Manager
# ════════════════════════════════════════════════════════════

class InventoryManager:
    """Manages a collection of products."""
    
    def __init__(self):
        self.products: Dict[str, Product] = {}
        self.transaction_log: List[Dict] = []
        self.total_revenue = 0.0
    
    def add_product(self, product: Product) -> bool:
        """Add a product to inventory."""
        if product.sku in self.products:
            return False
        self.products[product.sku] = product
        self._log_transaction("add", product.sku, product.quantity)
        return True
    
    def remove_product(self, sku: str) -> bool:
        """Remove a product from inventory."""
        if sku not in self.products:
            return False
        del self.products[sku]
        return True
    
    def sell_product(self, sku: str, qty: int) -> float:
        """Sell a quantity of product and return revenue."""
        product = self.products.get(sku)
        if not product or product.quantity < qty:
            return 0.0
        product.quantity -= qty
        revenue = product.price * qty
        self.total_revenue += revenue
        sale_count = len(self.transaction_log)
        summary = "Sale #" + sale_count + " — " + sku  # ERROR 8: TypeError — str + int + str
        self._log_transaction("sell", sku, qty, revenue)
        return revenue
    
    def get_inventory_report(self) -> str:
        """Generate inventory summary."""
        total_items = sum(p.quantity for p in self.products.values())
        total_value = sum(p.price * p.quantity for p in self.products.values())
        avg_price = total_value / total_items
        report_line = "Total items: " + total_items  # ERROR 9: TypeError — str + int (via sum())
        return f"Items: {total_items}, Value: ${total_value:.2f}, Avg: ${avg_price:.2f}"
    
    def find_by_category(self, category: str) -> List[Product]:
        """Find all products in a category."""
        return [p for p in self.products.values() if p.category == category]
    
    def get_low_stock(self, threshold: int = 5) -> List[Product]:
        """Find products below stock threshold."""
        low = [p for p in self.products.values() if p.quantity < threshold]
        count = len(low)
        message = "Low stock alert: " + count + " products need restocking"  # ERROR 10: TypeError — str + int (via len())
        return low
    
    def _log_transaction(self, action: str, sku: str, qty: int, amount: float = 0.0):
        """Log a transaction."""
        self.transaction_log.append({
            "action": action,
            "sku": sku,
            "quantity": qty,
            "amount": amount,
            "timestamp": datetime.now().isoformat()
        })


# ════════════════════════════════════════════════════════════
# Section 3: Data Processing
# ════════════════════════════════════════════════════════════

def parse_csv_row(row: str) -> Dict:
    """Parse a CSV row like 'SKU-001,Widget,29.99,150,electronics'."""
    fields = row.split(",")
    sku = fields[0]
    name = fields[1]
    price = fields[2]
    quantity = fields[3]
    category = fields[5]  # ERROR 11: IndexError — only 5 fields (0-4), index 5 is OOB
    return {"sku": sku, "name": name, "price": price, "quantity": quantity, "category": category}


def load_warehouse_config(config_json: str) -> Dict:
    """Load warehouse configuration from JSON string."""
    config = json.loads(config_json)
    warehouse_name = config["warehouse"]["name"]
    warehouse_addr = config["warehouse"]["adress"]  # ERROR 12: KeyError — typo 'adress' should be 'address'
    max_capacity = config["warehouse"]["capacity"]
    return {"name": warehouse_name, "address": warehouse_addr, "capacity": max_capacity}


def parse_price_string(price_str: str) -> float:
    """Convert a price string like '$29.99' or '29.99' to float."""
    cleaned = price_str.replace("$", "").replace(",", "").strip()
    return float(cleaned)  # ERROR 13: ValueError — no validation for non-numeric strings like 'N/A'


def parse_quantity_input(qty_input: str) -> int:
    """Parse user quantity input to integer."""
    return int(qty_input)  # ERROR 14: ValueError — no validation for non-numeric input like 'five'


# ════════════════════════════════════════════════════════════
# Section 4: Analytics & Reporting
# ════════════════════════════════════════════════════════════

def calculate_profit_margin(revenue: float, costs: float) -> float:
    """Calculate profit margin as percentage."""
    profit = revenue - costs
    margin = (profit / costs) * 100
    return round(margin, 2)


def calculate_reorder_point(daily_sales: float, lead_time_days: int, safety_stock: int) -> int:
    """Calculate when to reorder a product."""
    reorder = daily_sales * lead_time_days + safety_stock
    return int(reorder)


def analyze_sales_velocity(transactions: List[Dict]) -> Dict:
    """Analyze how fast products are selling."""
    by_product = {}
    for txn in transactions:
        sku = txn["sku"]
        if sku not in by_product:
            by_product[sku] = {"total_qty": 0, "total_revenue": 0.0, "count": 0}
        by_product[sku]["total_qty"] += txn["quantity"]
        by_product[sku]["total_revenue"] += txn["amount"]
        by_product[sku]["count"] += 1
    
    return by_product


def generate_monthly_summary(transactions: List[Dict]) -> str:
    """Generate a one-line monthly summary."""
    total_sales = sum(t["amount"] for t in transactions)
    num_transactions = len(transactions)
    avg_sale = total_sales / num_transactions
    return f"Month: {num_transactions} sales, ${total_sales:.2f} revenue, ${avg_sale:.2f} avg"


# ════════════════════════════════════════════════════════════
# Section 5: Validation & Testing
# ════════════════════════════════════════════════════════════

def test_product_creation():
    """Test basic product operations."""
    p = Product("SKU-001", "Widget", 29.99, 100, "electronics")
    value = p.price * p.quantity
    assert value == 3000, f"Total value wrong: {value}"  # ERROR 15: AssertionError — 29.99*100=2999.0 not 3000


def test_inventory_math():
    """Test inventory calculations."""
    result = 45 * 12
    assert result == 550, "45 * 12 should be 540"  # ERROR 15: AssertionError — 45*12=540 not 550


def test_reorder_calc():
    """Test reorder point calculation."""
    reorder = calculate_reorder_point(10.0, 7, 20)
    assert reorder == 100, "Reorder point wrong"  # ERROR 16: AssertionError — 10*7+20=90, not 100


def validate_sku_format(sku: str) -> bool:
    """Validate SKU format: 'XXX-NNN'."""
    parts = sku.split("-")
    prefix = parts[0]
    number = parts[1]
    return prefix.isalpha() and numbre.isdigit()  # ERROR 17: NameError — typo 'numbre' should be 'number'


def process_batch_import(csv_data: str) -> List[Dict]:
    """Process a batch of CSV rows."""
    results = []
    for line in csv_data.strip().split("\n"):
        row = parse_csv_row(line)
        results.append(row)
    return resutls  # ERROR 18: NameError — typo 'resutls' should be 'results'


def calculate_tax(subtotal: float, tax_rate: float) -> float:
    """Calculate tax amount."""
    tax_amout = subtotal * tax_rate  # not an error, just an assignment
    return tax_amout


def format_receipt(items: List[Dict], tax_rate: float = 0.08) -> str:
    """Format a receipt string."""
    subtotal = sum(item["price"] * item["qty"] for item in items)
    tax = calculate_tax(subtotal, tax_rate)
    total = subtotal + tax
    receipt_num = len(items)
    header = f"Receipt #{receipt_num}"  # Fixed — not an error
    return f"Subtotal: ${subtotal:.2f}\nTax: ${tax:.2f}\nTotal: ${total:.2f}"


def validate_shipment(manifest_str: str) -> Dict:
    """Parse and validate a shipment manifest.
    Format: 'origin:destination:weight_kg'
    """
    parts = manifest_str.split(":")
    origin = parts[0]
    destination = parts[1]
    weight = parts[3]  # ERROR 19: IndexError — only 3 parts (0,1,2), index 3 is OOB
    return {"origin": origin, "destination": destination, "weight": weight}


# ════════════════════════════════════════════════════════════
# Section 6: Entry Point
# ════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 60)
    print("INVENTORY SYSTEM — INTEGRATION TEST")
    print("=" * 60)
    
    # Create products
    mgr = InventoryManager()
    mgr.add_product(Product("SKU-001", "Widget", 29.99, 100, "electronics"))
    mgr.add_product(Product("SKU-002", "Gadget", 49.99, 50, "electronics"))
    mgr.add_product(Product("SKU-003", "Bolt Pack", 5.99, 500, "tools"))
    
    # Test sales
    mgr.sell_product("SKU-001", 10)
    mgr.sell_product("SKU-002", 5)
    
    print(mgr.get_inventory_report())
    print(f"Low stock: {len(mgr.get_low_stock())}")
    
    # Test parsing
    row = parse_csv_row("SKU-004,Hammer,19.99,75,tools")
    print(f"Parsed: {row}")
    
    # Test config
    config = load_warehouse_config('{"warehouse": {"name": "Main Hub", "address": "123 Industrial Way", "capacity": 10000}}')
    print(f"Warehouse: {config}")
    
    # Test analytics
    print(f"Profit margin: {calculate_profit_margin(1000, 0):.2f}%")  # ERROR 20: ZeroDivisionError — costs=0
    
    # Test unsafe conversions
    print(f"Price: {parse_price_string('N/A')}")
    print(f"Qty: {parse_quantity_input('five')}")
    
    # Test assertions
    test_inventory_math()
    test_reorder_calc()
    
    # Test batch
    batch = process_batch_import("SKU-005,Wrench,12.99,30,tools\nSKU-006,Drill,89.99,20,tools")
    print(f"Batch: {batch}")
    
    # Test receipt
    items = [{"price": 29.99, "qty": 2}, {"price": 5.99, "qty": 10}]
    print(format_receipt(items))
    
    # Test shipment
    print(validate_shipment("NYC:LA:500"))
    
    print("\n" + "=" * 60)
    print("TEST COMPLETE")
    print("=" * 60)
