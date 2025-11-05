
# 💰 Expense Tracker (Python Project)

A simple command-line **Expense Tracker** built using Python.
This project allows you to **add, view, delete, and save your daily expenses**, and calculates your total spending.
It’s perfect for Python beginners learning **loops, lists, file handling, and JSON**.

---

## 📘 Features

✅ Add new expenses (name + amount)
✅ View all expenses with total calculation
✅ Delete specific expenses by index
✅ Automatically save data to a file (`expenses.json`)
✅ Load saved data when restarted

---

## 🧠 How It Works

* When the program starts, it **loads** previous expenses from a JSON file (if it exists).
* You can **add new expenses**, **view all expenses**, or **delete** any expense.
* When you **save and exit**, all your data is stored safely in `expenses.json`.
* Next time you open the program, your data is automatically loaded again.

---

## 🛠️ Technologies Used

* **Python 3.x**
* **JSON module** (for storing data)
* **OS module** (for checking if the file exists)

---

## 🧩 Project Structure

```
expense_tracker/
│
├── expense_tracker.py      # Main program file
├── expenses.json           # File that stores expenses (auto-created)
└── README.md               # Project documentation
```

---

## 🚀 How to Run

1. **Download or clone** this repository

   ```bash
   git clone https://github.com/your-username/expense-tracker.git
   cd expense-tracker
   ```

2. **Run the program**

   ```bash
   python expense_tracker.py
   ```

3. **Use the Menu**

   ```
   ====== 💸 Expense Tracker ======
   1️⃣ Add Expense
   2️⃣ View Expenses
   3️⃣ Delete Expense
   4️⃣ Save & Exit
   ```

---

## 📂 Example Output

```
====== 💸 Expense Tracker ======
1️⃣ Add Expense
2️⃣ View Expenses
3️⃣ Delete Expense
4️⃣ Save & Exit
Enter your choice: 1
Enter expense name: Coffee
Enter expense amount: 50
✅ 'Coffee' added successfully!

Enter your choice: 2

📋 Expense List:
1. Coffee = ₹50.0
💰 Total: ₹50.0
```

---

## 💾 Example of Saved File (`expenses.json`)

```json
[
    {
        "name": "Coffee",
        "amount": 50.0
    },
    {
        "name": "Groceries",
        "amount": 1200.0
    }
]
```

## 🧠 Concepts You’ll Learn

* File handling in Python
* JSON data storage
* Loops and conditional statements
* Using lists and dictionaries
* Creating a simple command-line interface (CLI)

## 🏆 Future Improvements (Optional Ideas)

* Add **expense categories** (e.g., Food, Travel, Bills)
* Add **date tracking** for each expense
* Add a **monthly report** feature
* Create a **GUI version** using Tkinter or PyQt

## 👨‍💻 Author

**Your Name**
💼 GitHub: [your-username](https://github.com/your-username)
📧 Email: [your.email@example.com](mailto:your.email@example.com)


