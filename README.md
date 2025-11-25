# Expense Tracker

A Flask web application for tracking personal expenses with category filtering and spending summaries.

## Features

- ✅ Add expenses with amount, category, and notes
- ✅ View all expenses in a clean layout
- ✅ Filter expenses by category (Food, Transport, Bills, Entertainment, Other)
- ✅ Calculate and display total spending
- ✅ Delete expenses
- ✅ Persistent data storage (JSON)

## Tech Stack

- Python 3
- Flask
- HTML/CSS
- JSON (data storage)

## Live Demo

[Expense Tracker Live](https://expense-tracker-xxxxx.onrender.com)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/drewdavis816/ExpenseTracker.git
cd ExpenseTracker
```

2. Create a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the app:
```bash
python3 main.py
```

5. Open your browser and go to `http://127.0.0.1:5000`

## How to Use

1. Enter the expense amount (e.g., 12.50)
2. Select a category from the dropdown
3. Add an optional note (e.g., "Lunch with friends")
4. Click "Add Expense" to save
5. Use category filter buttons to view specific expenses
6. Click "All" to see all expenses
7. Total spending updates automatically based on filter
8. Click "Delete" to remove an expense

## Project Structure
```
ExpenseTracker/
├── main.py              # Flask app and routes
├── templates/
│   └── index.html       # Expense tracker UI
├── static/
│   └── style.css        # Styling
├── expenses.json        # Data storage
└── requirements.txt     # Dependencies
```

## What I Learned

- Flask form handling and data validation
- Array filtering and aggregation
- Dynamic total calculation
- Category-based organization
- Money formatting in Python
- Building financial tracking applications

## Future Improvements

- Monthly budget limits
- Spending graphs and charts
- Export to CSV
- Recurring expenses
- User authentication
- Database integration
