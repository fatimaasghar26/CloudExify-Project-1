# Personal Expense Tracker

Project Report, CloudExify Python Internship, Month 1, Project 1

| | |
|---|---|
| **Name** | Fatima Asghar |
| **Registration No.** | CX-INT-2026-PY-0063|
| **Program** | CloudExify Summer Internship 2026 |
| **Module** | Python Programming, Month 1 |
| **Project** | Project 1: Personal Expense Tracker |
| **Type** | Command Line Interface (CLI) Application |
| **Language** | Python 3.x |
| **Submission** | End of Week 2 |

---

## 1. Project Description

This project is a command-line expense tracker built in Python. It allows a user to log daily expenses, view them in a formatted table, break down spending by category, filter expenses by category, delete entries, and persist data between sessions using a plain text file.

## 2. Objective

The goal was to apply core Python concepts (variables, functions, loops, conditionals, lists, dictionaries, file handling, and error handling) in a single working command-line application, while practicing clean program structure through a menu-driven design.

## 3. How to Run

1. Make sure Python 3 is installed.
2. Open a terminal in the project folder.
3. Run:
   ```
   python expense_tracker.py
   ```
4. Use the on-screen menu (options 1 to 7) to interact with the program.

## 4. Features Implemented

- Add expense (description, amount, category) with input validation
- View all expenses in a formatted table with running total
- Category-wise spending summary with percentage breakdown
- Filter expenses by category
- Delete an expense by ID, with confirmation prompt
- Save expenses to `expenses.txt`
- Automatically load saved expenses on startup
- Input validation for invalid numbers, empty fields, and out-of-range menu choices

## 5. Data Storage

Expenses are saved to `expenses.txt`, created automatically in the same folder as the script on first save. Each line represents one expense, with fields separated by a pipe character:

```
id|description|amount|category
```

The pipe separator was used instead of a comma, so a description containing a comma doesn't break the file when it's read back in.

## 6. Project Structure

```
expense_tracker/
├── expense_tracker.py
├── expenses.txt
├── README.md
└── screenshots/
    ├── main_menu.png
    └── expense_list.png
```

## 7. Concepts Applied

| Concept | Where It's Used |
|---|---|
| Variables & data types | Storing expense amount, description, category |
| Loops (`while`, `for`) | Main menu loop, input retry loops, iterating over expenses |
| Conditionals (`if`/`elif`/`else`) | Menu routing, validation checks |
| Functions | Each feature isolated into its own function |
| Lists & dictionaries | Expenses stored as a list of dictionaries |
| File handling | Reading and writing `expenses.txt` |
| Try/except | Handling invalid numeric input |
| String formatting | Aligned table output using f-strings |

## 8. Testing

Manually tested: valid and invalid amounts, negative amounts, out-of-range category choices, viewing an empty list versus a populated list, category summary accuracy, filtering by existing and non-existing categories, deleting an existing and a non-existent ID, and confirming data persists correctly after saving and restarting the program.

## 9. Screenshots

See the `screenshots/` folder for:

1. `main_menu.png`, the main menu on startup
2. `expense_list.png`, the expense list view with 5+ entries

## 10. Conclusion

This project reinforced foundational Python skills, particularly structuring a program around functions, validating user input defensively, and persisting state to disk, and produced a working command-line tool suitable for a development portfolio.
