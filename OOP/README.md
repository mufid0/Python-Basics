# 🧩 Python Object-Oriented Programming (OOP)

This repository contains a comprehensive set of Python programs demonstrating **Object-Oriented Programming (OOP)** concepts. It covers everything from basic class creation to advanced topics like inheritance, polymorphism, encapsulation, and operator overloading.

---

## 📖 Overview

The notebook is designed to provide a structured, hands-on understanding of OOP principles in Python. Each section includes practical examples and mini-problems to reinforce learning through implementation.

---

## 🚀 Core Concepts Covered

### 🔹 1. Class & Object Fundamentals

* Defining classes and creating objects
* Instance attributes and initialization (`__init__`)
* Basic methods and object interaction

---

### 🔹 2. Methods & Attributes

* Instance methods vs class attributes
* Dynamic attribute updates
* Calculated attributes vs methods

---

### 🔹 3. Inheritance

* Single inheritance
* Using `super()` for parent class initialization
* Extending base class functionality

---

### 🔹 4. Polymorphism

* Method overriding
* Runtime polymorphism
* Duck typing

---

### 🔹 5. Encapsulation

* Private variables (`__variable`)
* Controlled access through methods
* Data hiding principles

---

### 🔹 6. Advanced OOP Concepts

* Operator overloading (`__add__`)
* Special methods (`__str__`)
* Class vs instance variables
* Function overloading alternatives (`*args`, default parameters)

---

## 📂 Implemented Examples

### ✅ Basic to Intermediate

* Book, Person, Animal, Dog classes
* Circle and Line mathematical models
* Counter with class-level tracking
* Shape hierarchy and area calculation

---

### ✅ Intermediate to Advanced

* Product & Electronics (Inheritance)
* Cylinder with dynamic scaling
* Bank Account system
* Inventory management system
* LightBulb (Encapsulation example)

---

### ✅ Polymorphism & Real-World Use Cases

* Animal sound system
* Instrument hierarchy
* Payroll system (Employee, Hourly, Salaried)
* Shape area calculation (Rectangle, Triangle)

---

## 🧠 Key Learning Outcomes

By working through this repository, you will:

* Understand core OOP principles in Python
* Write modular, reusable, and scalable code
* Apply real-world design patterns
* Implement polymorphic behavior
* Design class hierarchies effectively

---

## ▶️ How to Run

### Using Jupyter Notebook

1. Open the `.ipynb` file
2. Run cells sequentially (Shift + Enter)

### Using Python Script

```bash
python filename.py
```

---

## 💡 Example Snippet

```python
class Employee:
    def get_monthly_salary(self):
        return 4000

class SalariedEmployee(Employee):
    def __init__(self, bonus):
        self.bonus = bonus

    def get_monthly_salary(self):
        return super().get_monthly_salary() + self.bonus
```

---

## 📌 Features

* Clean and structured code
* Progressive difficulty (basic → advanced)
* Real-world inspired examples
* Strong focus on concepts + implementation

---

## 🔮 Future Enhancements

* Design patterns (Singleton, Factory, etc.)
* File handling with OOP
* Integration with real-world datasets
* Unit testing for classes

---

## 👨‍💻 Author

**Mufid Panhalkar**
Computer Engineering Student | AI/ML Enthusiast

---

## ⭐ Support

If you find this repository helpful, consider giving it a ⭐ to support the project.

