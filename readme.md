
---

# Lab 5: Static Code Analysis

## 🎯 Objective

[cite_start]This project demonstrates the use of static analysis tools to enhance Python code quality, security, and style[cite: 7]. [cite_start]The goal is to identify and fix common programming issues in a provided `inventory_system.py` file[cite: 8, 36].

## 🛠️ Tools Used

* [cite_start]**Pylint**: A "strict code reviewer" used to check for code quality, logical errors, and poor practices[cite: 29, 30].
* [cite_start]**Bandit**: An "app's security guard" used to identify common security vulnerabilities in Python code[cite: 33].
* [cite_start]**Flake8**: A "grammar checker" that enforces PEP 8 style guidelines, checking for formatting, whitespace, and syntax issues[cite: 31, 32].

## ⚙️ Process

1.  [cite_start]**Setup**: A GitHub Codespace was initialized, and the required tools (`pylint`, `bandit`, `flake8`) were installed using pip[cite: 43, 58].
2.  **Analysis**: Each tool was run against the `inventory_system.py` file, and the results were saved to report files:
    * [cite_start]`pylint inventory_system.py > pylint_report.txt` [cite: 69]
    * [cite_start]`bandit -r inventory_system.py > bandit_report.txt` [cite: 70]
    * `flake8 inventory_system.py > flake8_report.txt`
3.  **Identification**: The generated reports were reviewed to identify critical, high, and medium-severity issues.
4.  [cite_start]**Fixing**: At least four major issues were documented and fixed in the source code[cite: 39, 77].
5.  [cite_start]**Reflection**: A `reflection.md` file was created to answer questions about the process and learnings[cite: 89, 90].

## 📋 Identified Issues Table

[cite_start]The following table documents the primary issues identified and the approach taken to fix them[cite: 40].

| Issue | Type | Line(s) | Description | Fix Approach |
| :--- | :--- | :--- | :--- | :--- |
| **Dangerous Default Value** | Bug | 8 | [cite_start]The `logs=[]` argument in the `addItem` function is a mutable default value[cite: 1]. This list will be shared and grow with every call to the function. | Change the default argument to `logs=None`. Inside the function, add a check: `if logs is None: logs = []`. |
| **Use of `eval`** | Security | 59 | [cite_start]`eval()` is used, which is a significant security risk as it can execute arbitrary code[cite: 3, 98]. [cite_start]Bandit flags this as a medium-severity issue[cite: 98]. | Remove the entire line: `eval("print('eval used')")`. |
| **Bare `except`** | Bug | 19 | [cite_start]The `removeItem` function uses a bare `except:`[cite: 1, 4], which catches all possible errors, including system-exit signals. This can hide bugs. | Replace `except:` with `except KeyError:`, which is the specific error that would happen if the item is not in `stock_data`. |
| **No `with` for File I/O** | Bug / Resource | 26, 32 | [cite_start]The `loadData` and `saveData` functions open files but don't use a `with` statement[cite: 2]. If an error occurs, the file may not be closed properly. | Refactor both functions to use a `with open(...) as f:` block to automatically manage file resources. |
| **Unused Import** | Cleanliness | 2 | [cite_start]The `logging` module is imported but never used in the code[cite: 3, 4]. | Remove the line `import logging`. |

## 📂 Files in This Repository

* `inventory_system.py`: The original Python file with known issues. (This would be updated to the "cleaned" version).
* `pylint_report.txt`: The full analysis report from Pylint.
* `bandit_report.txt`: The full security report from Bandit.
* `flake8_report.txt`: The full style report from Flake8.
* `reflection.md`: Answers to the lab's reflection questions.
* `readme.md`: This file.