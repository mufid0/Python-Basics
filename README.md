# 🐍 Python Fundamentals, Functional Programming & OOP

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge)
![Repo Size](https://img.shields.io/github/repo-size/yourusername/python-fundamentals?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

> A **comprehensive and structured Python learning repository** designed to build strong programming fundamentals, master functional programming, and understand object-oriented design — with a **real-world project implementation**.

---

# 📌 Table of Contents

* [📁 Repository Structure](#-repository-structure)
* [📚 Modules Overview](#-modules-overview)
* [🧠 Concepts Covered](#-concepts-covered)
* [🧮 Project: Calculator](#-project-calculator)
* [⚙️ Setup & Usage](#️-setup--usage)
* [📈 Learning Outcomes](#-learning-outcomes)
* [🚀 Future Enhancements](#-future-enhancements)
* [🤝 Contribution](#-contribution)

---

# 📁 Repository Structure

```
python-fundamentals/
│
├── 📂 01_python_basics/
│   ├── basics_part1.ipynb
│   ├── basics_part2.ipynb
│   └── README.md
│
├── 📂 02_functions/
│   ├── lambda_map_filter.ipynb
│   └── README.md
│
├── 📂 03_oop/
│   ├── polymorphism.ipynb
│   └── README.md
│
├── 📂 04_projects/
│   ├── calculator.py
│   └── README.md
│
├── 📂 assets/              # Images / diagrams (optional)
│
├── requirements.txt       # Dependencies (optional)
└── README.md
```

---

# 📚 Modules Overview

---

## 🔹 01. Python Basics

This module builds the **foundation of Python programming**.

### 📘 Topics Covered

* Variables & Data Types
* Input / Output Handling
* Conditional Statements (`if-else`)
* Loops (`for`, `while`)
* Data Structures:

  * Lists
  * Tuples
  * Sets
  * Dictionaries

### 🎯 Goal

Understand syntax and logic building for problem-solving.

---

## 🔹 02. Functions & Functional Programming

Focuses on writing **clean, reusable, and optimized code**.

### 📘 Topics Covered

* Function Definition & Scope
* Lambda Functions
* Higher-Order Functions
* `map()` and `filter()` usage

### 💡 Example

```python
square = lambda x: x * x
print(list(map(square, [1, 2, 3, 4])))
```

### 🎯 Goal

Adopt functional programming techniques for efficient coding.

---

## 🔹 03. Object-Oriented Programming (OOP)

Introduces **modular and scalable code design**.

<details>
<summary>📘 Click to expand detailed concepts</summary>

### 🔸 Classes & Objects

Blueprints for creating reusable code structures.

### 🔸 Inheritance

Promotes code reusability by deriving new classes.

### 🔸 Polymorphism

Same method behaving differently based on object.

```python
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"
```

</details>

### 🎯 Goal

Write structured, reusable, and scalable programs.

---

## 🔹 04. Project: Calculator 🧮

A **command-line calculator application** demonstrating real-world usage of Python fundamentals.

---

# 🧮 Project: Advanced Calculator (High-Performance CLI)

## ✨ Features

* Basic arithmetic operations:

  * Addition
  * Subtraction
  * Multiplication
  * Division
* Continuous execution using loops
* Input validation
* Error handling (division by zero)

---

## 💻 Implementation

```python
import math
from datetime import datetime


class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def power(self, a, b):
        return a ** b

    def sqrt(self, a):
        if a < 0:
            raise ValueError("Cannot take sqrt of negative number")
        return math.sqrt(a)

    def modulus(self, a, b):
        return a % b

    def evaluate_expression(self, expr):
        try:
            result = eval(expr)
            return result
        except Exception:
            raise ValueError("Invalid expression")

    def save_history(self, expression, result):
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.history.append(f"[{timestamp}] {expression} = {result}")

    def show_history(self):
        if not self.history:
            print("No history yet.")
        else:
            print("\n📜 Calculation History:")
            for item in self.history:
                print(item)


def main():
    calc = Calculator()

    while True:
        print("\n====== Advanced Calculator ======")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Square Root")
        print("7. Modulus")
        print("8. Evaluate Expression")
        print("9. Show History")
        print("0. Exit")

        choice = input("Enter choice: ")

        try:
            if choice == '0':
                print("Exiting Calculator...")
                break

            elif choice == '8':
                expr = input("Enter expression (e.g., 2+3*5): ")
                result = calc.evaluate_expression(expr)
                calc.save_history(expr, result)
                print("Result:", result)

            elif choice == '9':
                calc.show_history()

            elif choice in ['1', '2', '3', '4', '5', '7']:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))

                operations = {
                    '1': calc.add,
                    '2': calc.subtract,
                    '3': calc.multiply,
                    '4': calc.divide,
                    '5': calc.power,
                    '7': calc.modulus
                }

                result = operations[choice](a, b)
                calc.save_history(f"{a} op {b}", result)
                print("Result:", result)

            elif choice == '6':
                a = float(input("Enter number: "))
                result = calc.sqrt(a)
                calc.save_history(f"sqrt({a})", result)
                print("Result:", result)

            else:
                print("Invalid choice")

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()

```

---

# 🧠 Concepts Covered

| Category         | Concepts                           |
| ---------------- | ---------------------------------- |
| Core Python      | Variables, Data Types, Loops       |
| Functional       | Lambda, map, filter                |
| OOP              | Classes, Inheritance, Polymorphism |
| Problem Solving  | Logic building                     |
| Project Building | CLI application                    |

---

# ⚙️ Setup & Usage

## 🔧 Prerequisites

* Python 3.8+

## ▶️ Run Locally

```bash
git clone https://github.com/yourusername/python-fundamentals.git
cd python-fundamentals
```

### Run Calculator

```bash
python 04_projects/calculator.py
```

### Run Notebooks

```bash
jupyter notebook
```

---

# 📈 Learning Outcomes

After completing this repository, you will:

* ✔ Build strong Python fundamentals
* ✔ Write clean and reusable functions
* ✔ Understand OOP concepts deeply
* ✔ Apply knowledge to real-world projects
* ✔ Be prepared for coding interviews & AI/ML learning

---

# 🚀 Future Enhancements

* 🔹 Add File Handling module
* 🔹 Add NumPy & Pandas notebooks
* 🔹 Add Data Structures & Algorithms
* 🔹 Add Mini AI/ML Projects
* 🔹 Add GUI-based calculator

---

# 🤝 Contribution

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Submit a Pull Request

---

# ⭐ Support

If you find this repository helpful, consider giving it a ⭐ on GitHub!
