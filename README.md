# Veda Technology Internship — Task 5: Number Statistics

**Track:** AI & ML  
**Level:** 1 — Day 5

## Project Overview

This project is part of the Veda Technology AI & ML internship. The task is to create a Python program that processes a manually created list of numbers.

The program:
- Separates numbers into even and odd lists.
- Finds the largest number.
- Finds the smallest number.
- Demonstrates loops, conditions, the modulo operator, `max()`, and `min()`.

## Objective

Practice basic Python programming and numerical data processing concepts that are useful as a foundation for AI/ML and data science.

## Tools Used

- Python 3
- Jupyter Notebook

No external Python libraries are required.

## Dataset

A manually created numerical list is used:

```text
[12, 7, 25, 4, 18, 31, 9, 42, 16, 3]
```

## Project Structure

```text
Veda_Technology_Task_5_Number_Statistics/
├── README.md
├── number_statistics.py
├── requirements.txt
├── .gitignore
└── notebooks/
    └── Task_5_Number_Statistics.ipynb
```

## How to Run

### Option 1 — Python file

Make sure Python 3 is installed, then run:

```bash
python number_statistics.py
```

### Option 2 — Jupyter Notebook

Start Jupyter Notebook:

```bash
jupyter notebook
```

Open:

```text
notebooks/Task_5_Number_Statistics.ipynb
```

Run all cells.

## Expected Output

```text
Number Statistics
------------------------------
Original list : [12, 7, 25, 4, 18, 31, 9, 42, 16, 3]
Even numbers  : [12, 4, 18, 42, 16]
Odd numbers   : [7, 25, 31, 9, 3]
Largest value : 42
Smallest value: 3
```

## Concepts Demonstrated

### 1. Modulo Operator

The expression:

```python
number % 2 == 0
```

checks whether a number is divisible by 2. A remainder of zero means the number is even.

### 2. For Loop

The `for` loop processes every number in the list one at a time.

### 3. Conditional Statement

An `if-else` statement separates the numbers into even and odd categories.

### 4. max() and min()

Python's built-in `max()` function returns the largest value, while `min()` returns the smallest value.

## Interview Questions

**Q1. How do you check whether a number is even?**

Use `number % 2 == 0`. If the remainder is zero, the number is even.

**Q2. What does the modulo operator do?**

The `%` operator returns the remainder after division.

**Q3. How can loops be used for data processing?**

Loops process each item in a collection one by one, allowing the same operation or condition to be applied to every item.

## Outcome

The task successfully identifies even and odd numbers and calculates the largest and smallest values from the given numerical list.

## Submission Checklist

- [x] Python program
- [x] Jupyter Notebook
- [x] Separate even and odd lists
- [x] Largest and smallest values
- [x] README.md
- [x] requirements.txt
- [x] .gitignore

