---

# ![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge) Python Learning Repository

![GitHub Repo Size](https://img.shields.io/github/repo-size/yourusername/python-learning?style=for-the-badge) ![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

> A **comprehensive Python learning repository** for beginners and intermediates.
> Covers **basic coding**, **functions (lambda, map, filter)**, and **advanced OOP concepts** with detailed explanations and examples.

---

## 📌 Table of Contents

1. [Introduction](#introduction)
2. [Basic Python Coding](#basic-python-coding)

   * [Printing & Variables](#printing--variables)
   * [Data Types](#data-types)
   * [Conditional Statements](#conditional-statements)
   * [Loops](#loops)
3. [Functions in Python](#functions-in-python)

   * [Defining Functions](#defining-functions)
   * [Lambda Functions](#lambda-functions)
   * [Map Function](#map-function)
   * [Filter Function](#filter-function)
4. [Object-Oriented Programming (OOP)](#object-oriented-programming-oop)

   <details>
   <summary>Click to expand OOP Sections</summary>
   - [Classes and Objects]  
   - [Attributes and Methods]  
   - [Multiple Instances]  
   - [Inheritance]  
     - [Single Inheritance]  
     - [Multiple Inheritance]  
   - [Super Function]  
   - [Polymorphism]  
     - [Method Overriding]  
   </details>
5. [Conclusion](#conclusion)

---

## Introduction

Python is a **high-level, interpreted programming language** that focuses on **readability, simplicity, and productivity**. It is widely used in:

* **Web Development** – Django, Flask
* **Data Science & Analysis** – Pandas, NumPy
* **Machine Learning & AI** – scikit-learn, TensorFlow
* **Automation & Scripting** – Automate repetitive tasks
* **Game Development** – Pygame

💡 **Why Python?**

* Easy syntax for beginners
* Large standard library and third-party modules
* Supports multiple programming paradigms: Procedural, Functional, OOP

---

## Basic Python Coding

### Printing & Variables

Variables are containers to store data. Python does **not require explicit type declaration**.

```python
# Print text
print("Hello, Python!")

# Variables
name = "Mufid"
age = 19

# Using f-string for formatted output
print(f"My name is {name}, I am {age} years old")
```

**Output:**

```text
My name is Mufid, I am 21 years old.
```

---

### Data Types

Python has several built-in data types:

| Data Type  | Example                               | Description                 |
| ---------- | ------------------------------------- | --------------------------- |
| Integer    | `x = 10`                              | Whole numbers               |
| Float      | `y = 3.14`                            | Decimal numbers             |
| String     | `name = "Python"`                     | Sequence of characters      |
| Boolean    | `is_student = True`                   | True/False                  |
| List       | `numbers = [1,2,3]`                   | Ordered collection of items |
| Dictionary | `person = {"name":"Mufid", "age":21}` | Key-value pairs             |

**Tip:** Use `type(variable)` to check the data type.

```python
x = 10
print(type(x))  # Output: <class 'int'>
```

---

### Conditional Statements

Conditional statements allow **decision-making** in programs.

```python
num = 15

if num % 2 == 0:
    print("Even Number")
elif num % 3 == 0:
    print("Divisible by 3")
else:
    print("Odd Number")
```

**Output:**

```text
Divisible by 3
```

**Note:** Python uses **indentation** (spaces/tabs) instead of braces `{}`.

---

### Loops

Loops allow **repetition of tasks**.

#### For Loop

```python
for i in range(1, 6):
    print(i)
```

**Output:**

```text
1
2
3
4
5
```

#### While Loop

```python
count = 1
while count <= 5:
    print(count)
    count += 1
```

---

## Functions in Python

Functions allow **code reuse** and **modular programming**.

### Defining Functions

```python
def greet(name):
    """Function to greet a person"""
    return f"Hello, {name}!"

print(greet("Mufid"))
```

**Output:**

```text
Hello, Mufid!
```

---

### Lambda Functions

* Anonymous, **single-line functions**
* Useful for **short operations**

```python
# Lambda to add two numbers
add = lambda a, b: a + b
print(add(5, 3))  # Output: 8
```

**Tip:** Use `lambda` in combination with `map()` and `filter()`.

---

### Map Function

`map()` applies a function to each item of an iterable (like a list).

```python
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16]
```

---

### Filter Function

`filter()` selects elements from an iterable **based on a condition**.

```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]
```

**Tip:** Both `map()` and `filter()` return **iterators**, so we often convert them to a list.

---

## Object-Oriented Programming (OOP)

OOP allows you to **organize code as objects**, combining **data (attributes)** and **functions (methods)**.

<details>
<summary>Click to expand OOP Examples</summary>

---

### Classes and Objects

```python
class Person:
    def __init__(self, name, age):
        self.name = name   # Attribute
        self.age = age     # Attribute

    def greet(self):
        return f"Hello, my name is {self.name}, age {self.age}"

# Creating an object
person1 = Person("Mufid", 21)
print(person1.greet())
```

**Output:**

```text
Hello, my name is Mufid, age 21
```

---

### Attributes & Methods

| Concept   | Description                        |
| --------- | ---------------------------------- |
| Attribute | A variable belonging to the object |
| Method    | A function belonging to the object |

---

### Multiple Instances

```python
person2 = Person("Alice", 25)
print(person2.greet())
```

**Tip:** Each object **stores its own attributes** independently.

---

### Inheritance

Inheritance allows a class (child) to **reuse code from another class (parent)**.

#### Single Inheritance

```python
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display(self):
        return f"{self.name}, ID: {self.student_id}"

student1 = Student("Bob", 20, "S123")
print(student1.greet())
print(student1.display())
```

---

#### Multiple Inheritance

```python
class Teacher:
    def __init__(self, subject):
        self.subject = subject

class TeachingAssistant(Student, Teacher):
    def __init__(self, name, age, student_id, subject):
        Student.__init__(self, name, age, student_id)
        Teacher.__init__(self, subject)

ta1 = TeachingAssistant("Charlie", 22, "S456", "Math")
print(ta1.greet())
print(ta1.subject)
```

---

### Super Function

`super()` is used to **call parent class methods or attributes**.

```python
class Employee(Person):
    def __init__(self, name, age, role):
        super().__init__(name, age)
        self.role = role

emp = Employee("Diana", 30, "Developer")
print(emp.greet())
print(emp.role)
```

---

### Polymorphism

Polymorphism allows **same method name to behave differently** depending on the object.

#### Method Overriding

```python
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Bark"

print(Animal().speak())  # Some sound
print(Dog().speak())     # Bark
```

---

</details>

---

## ✅ Conclusion

This repository covers:

* **Python Basics**: Variables, loops, data types, conditional statements
* **Functions**: Regular, Lambda, Map, Filter
* **OOP Concepts**: Classes, Attributes, Methods, Multiple Instances, Inheritance, Polymorphism

