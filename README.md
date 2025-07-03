Features Used in the project 
## 📌 1. **Python Basics**

* `print()` – For displaying text and UI prompts
* `input()` – For taking user input from the terminal
* `variables` – To store data like salary, budgets, categories, and user name
* `comments` – For explaining sections of code (`# comment`)

---

## 🔁 2. **Control Flow**

* `if`, `elif`, `else` – Conditional logic based on user choices
* `while True:` – Infinite loop to keep the program running until the user exits
* `break` – To exit inner loops (e.g. go back to main menu)
* `continue` (indirectly via loop structure) – Skip or retry invalid inputs


## 📦 3. **Data Structures**

### ✅ Lists:

* Used for:

  * `categories` (list of strings)
  * `expenses` (list of dictionaries)
  * `today_expenses`, `filtered`, etc. (filtered lists)

### ✅ Dictionaries:

* Each `expense` is a dictionary:

```python
{
  "description": ...,
  "amount": ...,
  "category": ...,
  "date": ...,
  "note": ...
}
```

* `category_limits` – Dictionary to store per-category budgets


## 🧮 4. **Built-in Functions**

* `sum()` – To calculate total expenses
* `max()` / `min()` – For highest and lowest expenses
* `round()` – To format average values
* `enumerate()` – To display indexed categories or transactions
* `isdigit()` – To validate numeric category selection


## 📅 5. **Date Handling**

* `import datetime` – Used to record today’s date with:

```python
datetime.date.today().strftime("%Y-%m-%d")
```

* Allows daily filtering of transactions

---

## 📄 6. **File Handling**

* Writing to a text file with:

```python
with open("finance_summary.txt", "w", encoding="utf-8") as f:
    f.write(...)
```

* Saves the user’s transaction history in a readable `.txt` file


## 💡 7. **User-Friendly Features**

* Dynamic UI with menus and submenus
* Confirmation prompts before deletion or adding expenses
* Custom category creation
* Keyword search in descriptions and notes
* Optional notes per transaction
* Reset feature to clear monthly data


## 📚 8. **Data Validation**

* Checks for:

  * Valid category selection
  * Correct numeric input for amounts and budgets
  * Confirmation before deleting or modifying data
  * Fallback defaults (like "Misc" for invalid categories)



| Concept              | Usage                               |
| -------------------- | ----------------------------------- |
| `print`, `input`     | User interaction                    |
| `if`, `elif`, `else` | Menu logic                          |
| `while`, `break`     | Looping through program             |
| `list`, `dict`       | Data storage (expenses, categories) |
| `datetime` module    | Automatically logging date          |
| `file handling`      | Save report in `.txt` file on exit  |
| `sum`, `max`, `min`  | Analysis and calculations           |
| `validation`         | Ensures proper user inputs and flow |

