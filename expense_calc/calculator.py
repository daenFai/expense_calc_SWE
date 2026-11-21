"""Business logic: totals, tax and discounts for expenses."""
import csv
import math


def add_expense(expenses, name, amount, category):
    """Append an expense. Category is normalized (strip + lowercase).
    Raises ValueError for an invalid amount."""
    if isinstance(amount, bool) or not isinstance(amount, (int, float)):
        raise ValueError("amount must be a number")
    if not math.isfinite(amount) or amount < 0:
        raise ValueError("amount must be a finite number >= 0")
    category = str(category).strip().lower()
    expenses.append({"name": name, "amount": amount, "category": category})
    return expenses


def calculate_total(expenses):
    total = 0
    for e in expenses:
        total += e["amount"]
    return total


# Pricing policies ("strategies") as data: category -> multiplier.
# Adding a category or a new policy no longer means copying an if/elif chain.
TAX_RATES = {"food": 1.05, "transport": 1.10, "entertainment": 1.20}
DISCOUNT_RATES = {"food": 0.95, "transport": 0.90, "entertainment": 0.80}


def total_with_policy(expenses, rates):
    """Sum amounts after applying the per-category multiplier (default 1.0)."""
    return sum(e["amount"] * rates.get(e["category"], 1.0) for e in expenses)


def total_with_tax(expenses):
    return total_with_policy(expenses, TAX_RATES)


def total_with_discount(expenses):
    return total_with_policy(expenses, DISCOUNT_RATES)


def totals_by_category(expenses):
    result = {}
    for e in expenses:
        result[e["category"]] = result.get(e["category"], 0) + e["amount"]
    return result


def export_csv(expenses, path):
    with open(path, "w") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "amount", "category"])
        for e in expenses:
            writer.writerow([e["name"], e["amount"], e["category"]])
