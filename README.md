---

# ![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge) Python Learning Repository

> A **comprehensive Python learning repository** covering fundamentals, functional programming, OOP, and a **real-world calculator project**.

---

## 📌 Table of Contents

1. [Introduction](#introduction)
2. [Basic Python Coding](#basic-python-coding)
3. [Functions in Python](#functions-in-python)
4. [Object-Oriented Programming (OOP)](#object-oriented-programming-oop)
5. [Calculator Project](#calculator-project)
6. [Conclusion](#conclusion)

---

## Introduction

Python is a **beginner-friendly, powerful programming language** used in web development, AI, automation, and more.

---

## Basic Python Coding

### Variables & Printing

```python
name = "Mufid"
print(f"Hello {name}")
```

---

## Functions in Python

### Lambda Example

```python
square = lambda x: x*x
print(square(5))
```

---

## Object-Oriented Programming (OOP)

<details>
<summary>Click to expand OOP Concepts</summary>

### Class Example

```python
class Person:
    def __init__(self, name):
        self.name = name
```

### Inheritance

```python
class Student(Person):
    pass
```

### Polymorphism

```python
class Dog:
    def sound(self):
        return "Bark"
```

</details>

---

# 🧮 Calculator Project

This repository also includes a **basic calculator project**, which demonstrates real-world application of Python concepts.

---

## 📌 Features

* Addition
* Subtraction
* Multiplication
* Division
* User input handling
* Loop-based continuous execution

---

## 💻 Calculator Code

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

## 📊 Concepts Used

| Concept        | Usage                                     |
| -------------- | ----------------------------------------- |
| Functions      | Separate operations (add, subtract, etc.) |
| Conditionals   | Menu selection                            |
| Loops          | Continuous execution                      |
| Error Handling | Division by zero                          |
| User Input     | Interactive CLI                           |

---

## 🚀 How to Run

```bash
python calculator.py
```

---

## ✅ Conclusion

This repository covers:

✔ Python Basics
✔ Functions (Lambda, Map, Filter)
✔ OOP Concepts
✔ Real-world Project (Calculator)
