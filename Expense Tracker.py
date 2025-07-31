import csv
import os

filename = "expenses.csv"

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    item = input("Enter expense item: ")
    amount = float(input("Enter amount: "))

    with open(filename, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, item, amount])
    print("Expense added successfully!\n")

def view_expenses():
    if not os.path.exists(filename):
        print("No expenses recorded yet.\n")
        return

    with open(filename, mode="r") as file:
        reader = csv.reader(file)
        total = 0
        print("\n--- Expense List ---")
        for row in reader:
            print(f"Date: {row[0]}, Item: {row[1]}, Amount: ₹{row[2]}")
            total += float(row[2])
        print(f"Total Spent: ₹{total}\n")

def delete_all():
    if os.path.exists(filename):
        os.remove(filename)
        print("All expenses deleted.\n")
    else:
        print("No expense file found.\n")

while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete All")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        delete_all()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Try again.\n")
