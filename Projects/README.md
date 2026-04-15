# 🧮 Advanced Python Calculator

A feature-rich command-line calculator built using Python that supports both basic and advanced mathematical operations. This project demonstrates strong use of **Object-Oriented Programming (OOP)**, error handling, and user interaction through a menu-driven interface.

---

## 📖 Overview

The Advanced Calculator is designed to perform a wide range of mathematical operations while maintaining a history of calculations. It provides a clean and interactive CLI experience, making it suitable for learning and practical usage.

---

## 🚀 Features

* ➕ Basic arithmetic operations (Addition, Subtraction, Multiplication, Division)
* 🔢 Advanced operations (Power, Square Root, Modulus)
* 🧠 Expression evaluation (e.g., `2 + 3 * 5`)
* 📜 Calculation history with timestamps
* ⚠️ Robust error handling (e.g., division by zero, invalid inputs)
* 🔄 Menu-driven interactive interface

---

## 🏗️ Project Structure

```bash id="0ae7qp"
advanced-calculator/
│
├── calculator.py    # Main application file
└── README.md        # Project documentation
```

---

## 🧠 Concepts Used

* Object-Oriented Programming (Classes & Methods)
* Exception Handling (`try-except`)
* Python Standard Libraries:

  * `math` (for advanced calculations)
  * `datetime` (for timestamped history)
* Dynamic function mapping (dictionary-based operations)
* CLI-based user interaction

---

## ⚙️ How It Works

1. The program displays a menu of operations
2. User selects an operation
3. Inputs are taken from the user
4. The corresponding method is executed
5. Result is displayed and stored in history

---

## ▶️ Getting Started

### Prerequisites

* Python 3.x installed

### Run the Application

```bash id="k5xs9c"
python calculator.py
```

---

## 💡 Example Usage

```
====== Advanced Calculator ======
1. Add
2. Subtract
3. Multiply
4. Divide
5. Power
6. Square Root
7. Modulus
8. Evaluate Expression
9. Show History
0. Exit
```

---

## 📜 Sample History Output

```
📜 Calculation History:
[12:30:15] 2 + 3 = 5
[12:31:10] sqrt(16) = 4.0
```

---

## ⚠️ Error Handling

* Prevents division by zero
* Handles invalid mathematical expressions
* Validates square root for negative numbers
* Displays user-friendly error messages

---

## 🔐 Note on `eval()`

The calculator uses Python’s built-in `eval()` for expression evaluation.

> ⚠️ For production-level applications, avoid using `eval()` with untrusted input due to security risks. Consider safer alternatives like parsing libraries.

---

## 📌 Future Enhancements

* GUI version using Tkinter or PyQt
* Scientific calculator features (log, sin, cos, etc.)
* Save history to file
* Unit testing for all operations
* Web-based version using Flask/Django

---

## 👨‍💻 Author

**Mufid Panhalkar**
Computer Engineering Student | AI/ML Enthusiast

---

## ⭐ Support

If you find this project useful, consider giving it a ⭐ on GitHub to support the work!

