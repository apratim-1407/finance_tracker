import datetime

print("===FINANCE TRACKER===")

# Step 1: User name input
user_name = input("Enter your name: ")
print(f"Welcome to the Finance Tracker, {user_name}!")

# Data Storage
salary = 0
expenses = []
monthly_budget = 0
categories = ["Food", "Travel", "Bills", "Shopping", "Entertainment", "Misc"]
category_limits = {}

# Program loop
while True:
    print("\nEnter:" 
        "\n1  -  Current Status"
        "\n2  -  Transactions" 
        "\n3  -  Budgeting" 
        "\n4  -  Analysis"
        "\n5  -  Filter / Search / Delete"
        "\n6  -  Reset Month"
        "\n7  -  Exit")

    choice = input("Please enter your choice: ")

    if choice == "1":
        print("\n=== CURRENT STATUS ===")
        if salary == 0:
            salary = float(input("Enter your monthly salary (₹): "))
        total_expense = sum(item["amount"] for item in expenses)
        print(f"Monthly Salary: ₹{salary}")
        print(f"Total Expenses: ₹{total_expense}")
        print(f"Remaining Balance: ₹{salary - total_expense}")

    elif choice == "2":
        print("\n=== TRANSACTIONS ===")
        while True:
            print("\n1 - Add Expense")
            print("2 - View All Transactions")
            print("3 - View Today's Expenses")
            print("4 - Go Back")
            sub_choice = input("Choose an option: ")

            if sub_choice == "1":
                description = input("Enter expense description: ")
                amount = float(input("Enter amount (₹): "))

                print("\nChoose a category:")
                for index, cat in enumerate(categories):
                    print(f"{index + 1}. {cat}")
                print(f"{len(categories)+1}. Create New Category")

                cat_choice = input("Enter category number: ")

                if cat_choice == str(len(categories)+1):
                    new_cat = input("Enter new category name: ").capitalize()
                    if new_cat not in categories:
                        categories.append(new_cat)
                        category = new_cat
                    else:
                        category = new_cat
                elif cat_choice.isdigit() and 1 <= int(cat_choice) <= len(categories):
                    category = categories[int(cat_choice) - 1]
                else:
                    print("Invalid choice, using 'Misc'")
                    category = "Misc"

                note = input("Add a note (optional): ")
                date = datetime.date.today().strftime("%Y-%m-%d")
                confirm = input(f"Confirm adding ₹{amount} in {category}? (yes/no): ").lower()
                if confirm == "yes":
                    expense = {
                        "description": description,
                        "amount": amount,
                        "category": category,
                        "date": date,
                        "note": note
                    }
                    expenses.append(expense)
                    print("✅ Expense added.")

                    if category in category_limits:
                        if sum(item["amount"] for item in expenses if item["category"] == category) > category_limits[category]:
                            print(f"⚠️ You've crossed your budget for {category}!")

            elif sub_choice == "2":
                if expenses:
                    print("\nYour Transactions:")
                    for i, item in enumerate(expenses):
                        print(f"{i+1}. {item['date']} | {item['category']} | {item['description']} | ₹{item['amount']} | Note: {item['note']}")
                else:
                    print("No transactions yet.")

            elif sub_choice == "3":
                today = datetime.date.today().strftime("%Y-%m-%d")
                today_expenses = [e for e in expenses if e["date"] == today]
                if today_expenses:
                    print(f"\nToday's Expenses ({today}):")
                    for item in today_expenses:
                        print(f"- {item['category']} | {item['description']} | ₹{item['amount']} | Note: {item['note']}")
                else:
                    print("No expenses today.")

            elif sub_choice == "4":
                break
            else:
                print("Invalid choice. Try again.")

    elif choice == "3":
        print("\n=== BUDGETING ===")
        if monthly_budget == 0:
            monthly_budget = float(input("Set your total monthly budget (₹): "))
            print("✅ Monthly budget set.")
        else:
            print(f"Your Monthly Budget: ₹{monthly_budget}")
            total_expense = sum(item["amount"] for item in expenses)
            print(f"Total Spent: ₹{total_expense}")
            print(f"Remaining: ₹{monthly_budget - total_expense}")

        change = input("Do you want to update your total budget? (yes/no): ").lower()
        if change == "yes":
            monthly_budget = float(input("Enter new budget: ₹"))
            print("✅ Updated.")

        print("\n--- Category Budgeting ---")
        for cat in categories:
            if cat in category_limits:
                print(f"{cat}: ₹{category_limits[cat]}")
        set_cat = input("Do you want to set/update category limits? (yes/no): ").lower()
        if set_cat == "yes":
            for cat in categories:
                limit = input(f"Set limit for {cat} (press enter to skip): ")
                if limit:
                    category_limits[cat] = float(limit)
            print("✅ Category limits updated.")

    elif choice == "4":
        print("\n=== ANALYSIS ===")
        if expenses:
            total_expense = sum(e["amount"] for e in expenses)
            avg = total_expense / len(expenses)
            highest = max(e["amount"] for e in expenses)
            lowest = min(e["amount"] for e in expenses)

            print(f"Total Spent: ₹{total_expense}")
            print(f"Average Expense: ₹{round(avg, 2)}")
            print(f"Highest Expense: ₹{highest}")
            print(f"Lowest Expense: ₹{lowest}")

            print("\n--- Category-wise Breakdown ---")
            category_totals = {}
            for e in expenses:
                cat = e["category"]
                category_totals[cat] = category_totals.get(cat, 0) + e["amount"]
            for cat, amt in category_totals.items():
                print(f"{cat}: ₹{amt}")
        else:
            print("No data yet.")

    elif choice == "5":
        print("\n=== FILTER / SEARCH / DELETE ===")
        while True:
            print("\n1 - Filter by Category")
            print("2 - Search by Keyword")
            print("3 - Delete a Transaction")
            print("4 - Go Back")
            sub = input("Choose: ")

            if sub == "1":
                for i, cat in enumerate(categories):
                    print(f"{i+1}. {cat}")
                pick = int(input("Pick category number: "))
                if 1 <= pick <= len(categories):
                    cat = categories[pick-1]
                    filtered = [e for e in expenses if e["category"] == cat]
                    if filtered:
                        for item in filtered:
                            print(f"- {item['date']} | {item['description']} | ₹{item['amount']}")
                    else:
                        print("No expenses in this category.")
                else:
                    print("Invalid selection.")

            elif sub == "2":
                keyword = input("Enter keyword to search: ").lower()
                results = [e for e in expenses if keyword in e["description"].lower() or keyword in e["note"].lower()]
                if results:
                    for item in results:
                        print(f"- {item['date']} | {item['category']} | {item['description']} | ₹{item['amount']}")
                else:
                    print("No matching expenses found.")

            elif sub == "3":
                if not expenses:
                    print("No transactions to delete.")
                else:
                    print("\nExpenses:")
                    for i, e in enumerate(expenses):
                        print(f"{i+1}. {e['date']} | {e['category']} | {e['description']} | ₹{e['amount']}")
                    idx = int(input("Enter the number to delete: "))
                    if 1 <= idx <= len(expenses):
                        confirm = input(f"Delete '{expenses[idx-1]['description']}' for ₹{expenses[idx-1]['amount']}? (yes/no): ")
                        if confirm.lower() == "yes":
                            expenses.pop(idx-1)
                            print("✅ Deleted.")
                    else:
                        print("Invalid number.")

            elif sub == "4":
                break
            else:
                print("Invalid option.")

    elif choice == "6":
        print("\n⚠️ This will clear all your current month’s data.")
        confirm = input("Are you sure you want to reset everything? (yes/no): ")
        if confirm.lower() == "yes":
            expenses = []
            salary = 0
            monthly_budget = 0
            category_limits = {}
            print("✅ All data cleared for new month.")

    elif choice == "7":
        print("\nSaving data...")

        with open("finance_summary.txt", "w", encoding="utf-8") as f:
            f.write(f"Finance Report for {user_name}\n")
            f.write(f"Total Expenses: ₹{sum(e['amount'] for e in expenses)}\n\n")
            for item in expenses:
                f.write(f"{item['date']} | {item['category']} | {item['description']} | ₹{item['amount']} | Note: {item['note']}\n")

        print("✅ Data saved to 'finance_summary.txt'")
        print("Exiting Finance Tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
