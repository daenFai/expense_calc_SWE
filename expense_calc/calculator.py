"""Business logic: totals, tax and discounts for expenses."""
import csv


def add_expense(expenses, name, amount, category):
    expenses.append({"name": name, "amount": amount, "category": category})
    return expenses


def calculate_total(expenses):
    total = 0
    for e in expenses:
        total += e["amount"]
    return total


def total_with_tax(expenses):
    total = 0
    for e in expenses:
        if e["category"] == "food":
            total += e["amount"] * 1.05
        elif e["category"] == "transport":
            total += e["amount"] * 1.10
        elif e["category"] == "entertainment":
            total += e["amount"] * 1.20
        else:
            total += e["amount"] * 1.00
    return total


def total_with_discount(expenses):
    total = 0
    for e in expenses:
        if e["category"] == "food":
            total += e["amount"] * 0.95
        elif e["category"] == "transport":
            total += e["amount"] * 0.90
        elif e["category"] == "entertainment":
            total += e["amount"] * 0.80
        else:
            total += e["amount"]
    return total


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
