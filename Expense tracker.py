import sqlite3
import datetime
import matplotlib.pyplot as plt

# Database setup
conn = sqlite3.connect('expenses.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS expenses
             (date TEXT, amount REAL, category TEXT)''')

# Function to add expense
def add_expense(date, amount, category):
    c.execute("INSERT INTO expenses (date, amount, category) VALUES (?, ?, ?)",
              (date, amount, category))
    conn.commit()

# Function to view spending patterns
def view_spending():
    c.execute("SELECT date, SUM(amount) FROM expenses GROUP BY date")
    data = c.fetchall()
    dates = [datetime.datetime.strptime(row[0], "%Y-%m-%d") for row in data]
    amounts = [row[1] for row in data]

    plt.plot(dates, amounts)
    plt.xlabel('Date')
    plt.ylabel('Total Expenses')
    plt.title('Spending Over Time')
    plt.show()

# Main function
def main():
    while True:
        print("\nExpense Tracking System")
        print("1. Add Expense")
        print("2. View Spending Patterns")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            add_expense(date, amount, category)
            print("Expense added successfully!")
        elif choice == '2':
            view_spending()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

    conn.close()

if __name__ == "__main__":
    main()
