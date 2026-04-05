# Generated from: practice-set-2.ipynb
# Converted at: 2026-04-05T11:18:32.095Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

# **1. Positive, Negative, or Zero**


num = float(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# 2. FizzBuzz (Number Game)


num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)

# 3. Movie Ticket Price Checker


age = int(input("Enter your age: "))

if age < 5:
    print("Free")
elif age <= 12:
    print("100")
elif age <= 60:
    print("150")
else:
    print("120")

print("Thank you for visiting!")

# 4. Multiplication Table


num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# 5. Print Stars Pattern


n = int(input("Enter number of lines: "))

for i in range(1, n + 1):
    print("*" * i)

# 6. Add It Up (1 to 100)


total = 0

for i in range(1, 101):
    total += i

print("Total =", total)

# 7. Countdown Time


num = int(input("Enter a number: "))

for i in range(num, 0, -1):
    print(i)

print("Liftoff!")

# Final Challenge: Secret Code Detector


password = input("Enter password: ")

if password == "python123":
    print("Access Granted")
else:
    print("Wrong password! Try again")