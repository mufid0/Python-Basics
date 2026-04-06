---

# ![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge) Python Learning Repository

![GitHub Repo Size](https://img.shields.io/github/repo-size/yourusername/python-learning?style=for-the-badge) ![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

> A **comprehensive Python learning repository** for beginners and intermediates.
> Covers **basic coding**, **functions (lambda, map, filter)**, and **advanced OOP concepts** like inheritance, polymorphism, and method overriding.

---

## 📌 Table of Contents

1. [Introduction](#introduction)
2. [Basic Python Coding](#basic-python-coding)
3. [Functions in Python](#functions-in-python)

   * [Lambda Functions](#lambda-functions)
   * [Map Function](#map-function)
   * [Filter Function](#filter-function)
4. [Object-Oriented Programming (OOP)](#object-oriented-programming-oop)

   <details>
   <summary>Click to expand OOP Sections</summary>
   - [Classes and Objects](#classes-and-objects)  
   - [Attributes and Methods](#attributes-and-methods)  
   - [Multiple Instances](#multiple-instances)  
   - [Inheritance](#inheritance)  
     - [Single Inheritance](#single-inheritance)  
     - [Multiple Inheritance](#multiple-inheritance)  
   - [Super Function](#super-function)  
   - [Polymorphism](#polymorphism)  
     - [Method Overriding](#method-overriding)  
   </details>
5. [Conclusion](#conclusion)

---

## Introduction

Python is a **high-level, interpreted language** known for **simplicity and readability**.

💡 *Use Cases*: Web development, Data Science, Machine Learning, Automation, and more.

---

## Basic Python Coding

### 1️⃣ Printing & Variables

```python
# Printing
print("Hello, Python!")

# Variables
name = "Mufid"
age = 21
height = 5.9

print(f"Name: {name}, Age: {age}, Height: {height}")
```

**Output:**

```text
Name: Mufid, Age: 21, Height: 5.9
```

---

### 2️⃣ Data Types

| Type       | Example                               |
| ---------- | ------------------------------------- |
| Integer    | `x = 10`                              |
| Float      | `y = 3.14`                            |
| String     | `name = "Python"`                     |
| Boolean    | `is_student = True`                   |
| List       | `numbers = [1, 2, 3]`                 |
| Dictionary | `person = {"name":"Mufid", "age":21}` |

---

### 3️⃣ Loops & Conditionals

```python
# For loop
for i in range(1, 6):
    print(i)

# If-Else
num = 10
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

---

## Functions in Python

Functions are blocks of reusable code.

### Basic Function

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Mufid"))
```

---

### Lambda Functions

* **Anonymous, short functions**

```python
add = lambda a, b: a + b
print(add(5, 3))  # Output: 8
```

---

### Map Function

Applies a function to all items in an iterable.

```python
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16]
```

---

### Filter Function

Selects items based on a condition.

```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4, 6]
```

---

## Object-Oriented Programming (OOP)

OOP organizes code into **objects** that have **attributes** and **methods**.

<details>
<summary>Click to expand OOP Sections</summary>

---

### Classes and Objects

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name}, age {self.age}"

person1 = Person("Mufid", 21)
print(person1.greet())
```

---

### Attributes & Methods

| Concept   | Description                      |
| --------- | -------------------------------- |
| Attribute | Variables associated with object |
| Method    | Functions associated with object |

---

### Multiple Instances

```python
person2 = Person("Alice", 25)
print(person2.greet())
```

---

### Inheritance

Allows child class to **reuse parent class methods/attributes**.

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

`super()` calls **parent class methods**.

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

Allows **same method name with different behavior**.

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

</details>

---

## ✅ Conclusion

This repository covers:

* **Python Basics**: Variables, loops, data types
* **Functions**: Regular, Lambda, Map, Filter
* **OOP Concepts**: Classes, Attributes, Methods, Inheritance, Polymorphism

It’s ideal for **beginners to intermediates**, providing a strong foundation for Python development.

