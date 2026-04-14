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

# 🧮 Project: Calculator

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
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


while True:
    print("\nCalculator Menu")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '5':
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid choice")
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

✔ Build strong Python fundamentals
✔ Write clean and reusable functions
✔ Understand OOP concepts deeply
✔ Apply knowledge to real-world projects
✔ Be prepared for coding interviews & AI/ML learning

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

---
