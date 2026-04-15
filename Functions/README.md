
# ⚙️ Python Functions & Functional Programming

This notebook demonstrates the use of **functions**, **lambda expressions**, and functional programming tools like `map()` and `filter()` in Python. It focuses on writing reusable, concise, and efficient code for data processing tasks.

---

## 📖 Overview

The notebook introduces core concepts of functional programming in Python, including:

* Function definition and usage
* Variable-length arguments (`*args`)
* Lambda (anonymous) functions
* Built-in higher-order functions (`map`, `filter`)
* Combining multiple operations for data transformation

---

## 🚀 Topics Covered

### 🔹 1. Functions

* Basic function definition
* Returning values
* Reusable logic implementation

Examples:

* Addition of two numbers
* Addition using multiple arguments (`*args`)
* Even number checking

---

### 🔹 2. Lambda Functions

* Writing concise, one-line functions
* Using lambda with `map()` and `filter()`

---

### 🔹 3. `filter()` Function

Used to extract elements based on a condition.

Examples:

* Filtering even numbers
* Selecting words starting with vowels
* Removing empty strings
* Filtering alphabetic values

---

### 🔹 4. `map()` Function

Used to transform elements in a sequence.

Examples:

* Squaring numbers
* Finding length of strings
* Converting strings to uppercase
* Generating boolean lists

---

### 🔹 5. Combined Usage (`map + filter`)

* Squaring only even numbers
* Processing strings with multiple conditions
* Efficient data pipelines

---

### 🔹 6. List Comprehension

* Alternative to `map()` and `filter()`
* Cleaner and more Pythonic syntax

Example:

```python
[x * x for x in nums if x % 2 != 0]
```

---

## 🧠 Key Concepts

* Functional programming paradigm
* Higher-order functions
* Code reusability and readability
* Efficient data processing techniques

---

## ▶️ How to Run

### Using Jupyter Notebook

1. Open the notebook (`.ipynb`)
2. Run cells sequentially (Shift + Enter)

### Using Python Script

```bash
python filename.py
```

---

## 💡 Sample Use Case

```python
# Remove empty strings, keep only alphabets, convert to uppercase
data = ["apple", "", "123", "banana", "456", ""]

data = list(filter(lambda x: x != "", data))
data = list(filter(lambda x: x.isalpha(), data))
data = list(map(lambda x: x.upper(), data))

print(data)  # Output: ['APPLE', 'BANANA']
```

---

## 🎯 Learning Outcomes

By completing this notebook, you will:

* Understand functional programming in Python
* Write concise code using lambda functions
* Use `map()` and `filter()` effectively
* Combine multiple operations for real-world data processing
* Improve code readability and efficiency

---

## 📌 Future Enhancements

* Add `reduce()` function examples
* Performance comparison with loops
* Real-world datasets for practice
* Advanced functional programming patterns

---

## 👨‍💻 Author

**Mufid Panhalkar**
Computer Engineering Student | AI/ML Enthusiast

---

⭐ *If you found this useful, consider starring the repository!*

