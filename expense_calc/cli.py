"""Command line interface (mixes input handling, printing and logic)."""
import sys
from expense_calc import calculator


def main(argv=None):
    expenses = []
    print("Expense calculator. Commands: add, total, tax, discount, bycat, export, quit")
    while True:
        cmd = input("> ").strip().lower()
        if cmd == "add":
            name = input("name: ")
            raw_amount = input("amount: ")
            category = input("category: ")
            try:
                calculator.add_expense(expenses, name, float(raw_amount), category)
            except ValueError as err:
                print("Invalid expense:", err)
        elif cmd == "total":
            print("Total:", calculator.calculate_total(expenses))
        elif cmd == "tax":
            print("Total with tax:", calculator.total_with_tax(expenses))
        elif cmd == "discount":
            print("Total with discount:", calculator.total_with_discount(expenses))
        elif cmd == "bycat":
            for k, v in calculator.totals_by_category(expenses).items():
                print(k, v)
        elif cmd == "export":
            calculator.export_csv(expenses, input("path: "))
        elif cmd == "quit":
            return 0
        else:
            print("unknown command")


if __name__ == "__main__":
    sys.exit(main())
