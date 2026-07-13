DATA_FILE = "expenses.txt"

categories = ["Food", "Transport", "Shopping", "Bills", "Other"]

expenses = []

next_id = 1


def add_expense():
    global next_id

    print("\n--- ADD NEW EXPENSE ---")
    description = input("Description: ")

    # keep asking until a valid, positive amount is entered
    while True:
        try:
            amount = float(input("Amount (PKR): "))
            if amount <= 0:
                print("Amount must be greater than 0!")
                continue
            break
        except ValueError:
            print("Please enter a valid number!")

    print("\nCategories:")
    for i in range(len(categories)):
        print(f"  {i + 1}. {categories[i]}")

    # keep asking until a valid category number is entered
    while True:
        choice = input("Select category (1-5): ")
        if choice.isdigit() and 1 <= int(choice) <= 5:
            category = categories[int(choice) - 1]
            break
        print("Please enter a number from 1 to 5!")

    expense = {
        "id": next_id,
        "description": description,
        "amount": amount,
        "category": category
    }
    expenses.append(expense)
    print(f"\nExpense added! ID: {next_id}")
    next_id = next_id + 1


def view_expenses():
    if len(expenses) == 0:
        print("\nNo expenses yet. Add some first!")
        return

    print("\n--- ALL EXPENSES ---")
    print(f"{'ID':<5}{'Description':<20}{'Category':<12}{'Amount':>10}")
    print("-" * 50)

    total = 0
    for exp in expenses:
        print(f"{exp['id']:<5}{exp['description']:<20}"
              f"{exp['category']:<12}PKR {exp['amount']:>8.2f}")
        total = total + exp["amount"]

    print("-" * 50)
    print(f"Total: PKR {total:.2f}")


def category_summary():
    if len(expenses) == 0:
        print("\nNo expenses to summarize!")
        return

    # add up total spent per category
    totals = {}
    for exp in expenses:
        cat = exp["category"]
        if cat in totals:
            totals[cat] = totals[cat] + exp["amount"]
        else:
            totals[cat] = exp["amount"]

    grand_total = 0
    for exp in expenses:
        grand_total = grand_total + exp["amount"]

    print("\n--- CATEGORY SUMMARY ---")
    for cat in totals:
        percent = (totals[cat] / grand_total) * 100
        print(f"{cat:<12}: PKR {totals[cat]:>8.2f} ({percent:.1f}%)")


def filter_by_category():
    if len(expenses) == 0:
        print("\nNo expenses to filter!")
        return

    print("\nCategories:")
    for i in range(len(categories)):
        print(f"  {i + 1}. {categories[i]}")

    choice = input("Select category (1-5): ")
    if choice.isdigit() and 1 <= int(choice) <= 5:
        target = categories[int(choice) - 1]
    else:
        print("Invalid choice!")
        return

    print(f"\n--- {target} EXPENSES ---")
    found = False
    total = 0
    for exp in expenses:
        if exp["category"] == target:
            print(f"{exp['id']:<5}{exp['description']:<20}"
                  f"PKR {exp['amount']:>8.2f}")
            total = total + exp["amount"]
            found = True

    if not found:
        print("No expenses found in this category.")
    else:
        print(f"\nTotal for {target}: PKR {total:.2f}")


def delete_expense():
    if len(expenses) == 0:
        print("\nNo expenses to delete!")
        return

    view_expenses()
    choice = input("\nEnter ID of expense to delete: ")

    if not choice.isdigit():
        print("Please enter a valid ID!")
        return

    target_id = int(choice)

    for exp in expenses:
        if exp["id"] == target_id:
            confirm = input(f"Delete '{exp['description']}' "
                             f"(PKR {exp['amount']:.2f})? (y/n): ")
            if confirm.lower() == "y":
                expenses.remove(exp)
                print("Expense deleted!")
            else:
                print("Deletion cancelled.")
            return

    print(f"No expense found with ID {target_id}.")


def save_expenses():
    # write each expense as one line, fields separated by "|"
    with open(DATA_FILE, "w") as f:
        for exp in expenses:
            line = f"{exp['id']}|{exp['description']}|{exp['amount']}|{exp['category']}\n"
            f.write(line)
    print("Expenses saved!")


def load_expenses():
    global next_id
    try:
        f = open(DATA_FILE, "r")
    except FileNotFoundError:
        # first run, no file yet - nothing to load
        return

    for line in f:
        line = line.strip()
        if line == "":
            continue
        parts = line.split("|")
        expense = {
            "id": int(parts[0]),
            "description": parts[1],
            "amount": float(parts[2]),
            "category": parts[3]
        }
        expenses.append(expense)
        next_id = int(parts[0]) + 1

    f.close()


def show_menu():
    print("\n========================================")
    print("   CLOUDEXIFY EXPENSE TRACKER")
    print("========================================")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Category Summary")
    print("4. Filter by Category")
    print("5. Delete Expense")
    print("6. Save Expenses")
    print("7. Save & Exit")
    print("========================================")


def main():
    print("Loading saved expenses...")
    load_expenses()
    print(f"Loaded {len(expenses)} expenses.")

    while True:
        show_menu()
        choice = input("Select option (1-7): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            category_summary()
        elif choice == "4":
            filter_by_category()
        elif choice == "5":
            delete_expense()
        elif choice == "6":
            save_expenses()
        elif choice == "7":
            save_expenses()
            print("\nGoodbye! Expenses saved.")
            break
        else:
            print("Invalid choice! Please enter 1-7.")


if __name__ == "__main__":
    main()
