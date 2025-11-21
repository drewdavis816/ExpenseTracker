from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)

EXPENSES_FILE = "expenses.json"


# Load expenses from file
def load_expenses():
    if os.path.exists(EXPENSES_FILE):
        with open(EXPENSES_FILE, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []


# Save expenses to file
def save_expenses(expenses):
    with open(EXPENSES_FILE, "w") as file:
        json.dump(expenses, file, indent=4)


@app.route('/')
def index():
    expenses = load_expenses()
    total = sum(exp["amount"] for exp in expenses)
    return render_template('index.html', expenses=expenses, total=total)


@app.route('/add', methods=['POST'])
def add_expense():
    amount = float(request.form.get('amount'))
    category = request.form.get('category').lower() or 'misc'
    note = request.form.get('note')

    expenses = load_expenses()
    expenses.append({"amount": amount, "category": category, "note": note})
    save_expenses(expenses)

    return redirect('/')

@app.route('/delete/<int:index>', methods=['POST'])
def delete_expense(index):
    expenses = load_expenses()
    if 0 <= index < len(expenses):
        expenses.pop(index)
        save_expenses(expenses)
    return redirect('/')

@app.route('/filter/<category>')
def filter_expenses(category):
    expenses = load_expenses()
    filtered = [exp for exp in expenses if exp["category"] == category]
    total = sum(exp["amount"] for exp in filtered)
    return render_template('index.html', expenses=filtered, total=total, current_filter=category)

@app.route('/all')
def all_expenses():
    expenses = load_expenses()
    total = sum(exp["amount"] for exp in expenses)
    return render_template('index.html', expenses=expenses, total=total, current_filter=None)


if __name__ == "__main__":
    app.run(debug=True)