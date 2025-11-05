# Import necessary modules
import json  # for saving and loading data in JSON format
import os    # for checking if a file exists

# File where we’ll store all expenses
FILENAME = "expenses.json"

# -----------------------------
# Function to load expenses from the file
# -----------------------------
def load_expenses():
    if os.path.exists(FILENAME):  # Check if file exists
        with open(FILENAME, "r") as file:
            return json.load(file)  # Read JSON data and return as Python list
    return []  # If file doesn’t exist, return an empty list

# -----------------------------
# Function to save expenses to the file
# -----------------------------
def save_expenses(expenses):
    with open(FILENAME, "w") as file:
        json.dump(expenses, file, indent=4)  # Save expenses in readable JSON format

# -----------------------------
# Function to add a new expense
# -----------------------------
def add_expense(expenses):
    name = input("Enter expense name: ")  # Example: "Coffee"
    try:
        amount = float(input("Enter expense amount: "))  # Example: 50.0
    except ValueError:
        print("❌ Invalid amount. Please enter a number.")
        return  # Stop function if invalid input
    
    # Append the expense to the list as a dictionary
    expenses.append({"name": name, "amount": amount})
    print(f"✅ '{name}' added successfully!")

# -----------------------------
# Function to view all expenses
# -----------------------------
def view_expenses(expenses):
    if not expenses:  # Check if list is empty
        print("No expenses recorded yet.")
        return
    
    total = 0  # Initialize total variable
    print("\n📋 Expense List:")
    print("-" * 30)
    
    # Loop through expenses list and print each expense
    for idx, exp in enumerate(expenses, 1):
        print(f"{idx}. {exp['name']} = ₹{exp['amount']}")
        total += exp['amount']  # Add amount to total
    
    # Display total expense at the end
    print("-" * 30)
    print(f"💰 Total: ₹{total}\n")

# -----------------------------
# Function to delete an expense by index
# -----------------------------
def delete_expense(expenses):
    view_expenses(expenses)  # Show all expenses before deleting
    try:
        idx = int(input("Enter expense index to delete: ")) - 1  # Get index from user
        if 0 <= idx < len(expenses):  # Check if index is valid
            deleted = expenses.pop(idx)  # Remove the expense
            print(f"❌ Deleted '{deleted['name']}' successfully!")
        else:
            print("⚠️ Invalid index.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

# -----------------------------
# Main function – menu system
# -----------------------------
def main():
    # Load previous data if available
    expenses = load_expenses()
    
    # Infinite loop until user exits
    while True:
        # Display menu options
        print("\n====== 💸 Expense Tracker ======")
        print("1️⃣. Add Expense")
        print("2️⃣. View Expenses")
        print("3️⃣. Delete Expense")
        print("4️⃣. Save & Exit")
        choice = input("Enter your choice: ")

        # Perform action based on user choice
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            delete_expense(expenses)
        elif choice == "4":
            save_expenses(expenses)  # Save data before exiting
            print("💾 Data saved.\nHave A Goodday!")
            break
        else:
            print("⚠️ Invalid choice. Try again!")

# -----------------------------
# Run the program
# -----------------------------
if __name__ == "__main__":
    main()
