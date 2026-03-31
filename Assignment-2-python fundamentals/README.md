# Python Fundamentals – Assignment 2 (README)

## Overview

This assignment is designed to build basic programming logic using Python.
The problems cover conditional statements, loops, functions, recursion, and basic number logic such as prime numbers, digits, and arithmetic operations.

---

## Assignment Questions

### Q1. Salary Tax Calculator

Write a program that takes salary as input and calculates the final tax rate using conditional statements based on the following rules:

- If salary < 30,000 → 5%
- If salary is between 30,000 and 70,000 → 15%
- If salary > 70,000 → 25%

---

### Q2. Even Numbers Between Two Numbers

Write a function that takes two integers **a** and **b** and prints all even numbers between them (inclusive).

---

### Q3. Print Digits of a Number

Write a function that prints the digits of a number **n**.

**Example:**
If n = 312, then digits are: 3, 1, 2

**Hint:**

- Rightmost digit of a number N is `N % 10`
- To remove the rightmost digit: `N = N // 10`

---

### Q4. Count Number of Digits

Write a function to return the number of digits in a number **n**.

---

### Q5. Sum of Digits

Write a function to return the sum of digits of a number **n**.

---

### Q6. Numbers Divisible by 3 and 5

Write a program to print all numbers from 1 to 100 that are divisible by both 3 and 5.

---

### Q7. Positive or Negative Until Quit

Design a program to continuously input a number **n** from the user and print whether it is positive or negative until the user enters **"Quit"**.

---

### Q8. Simple Calculator Function

Create a simple calculator function:

```
calculator(a, b, operation)
```

The function should perform:

- Addition (+)
- Subtraction (-)
- Multiplication (\*)
- Division (/)

---

### Q9. Prime Number Function

Write a function:

```
is_prime(n)
```

The function should:

- Return **True** if n is a prime number
- Return **False** otherwise
- Use a loop to check divisibility from range [2, n-1]

**Hint:**

- 2 is the smallest prime number
- A non-prime number will always be divisible by at least one number in the range [2, n-1]

---

### Q10. Number Guessing Game

Create a number guessing game:

- A secret number is already decided
- The user keeps guessing the number
- Program prints:
  - "Too high" if the guess is above the number
  - "Too low" if the guess is below the number
  - "Correct!" if the guess matches the number

---

## Topics Covered

This assignment covers:

- Conditional Statements
- Loops (for, while)
- Functions
- Recursion
- Input Validation
- Number Logic
- Prime Numbers
- Arithmetic Operations

---

## End of Assignment

**Python Fundamentals – Assignment 2**
