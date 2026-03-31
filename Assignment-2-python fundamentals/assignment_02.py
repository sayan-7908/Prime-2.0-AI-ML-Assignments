# # Q1.

# salary = int(input("Enter salary: "))

# if salary < 30000:
#     print("Tax rate is 5%")
# elif salary <= 70000:
#     print("Tax rate is 15%")
# else:
#     print("Tax rate is 25%")

# #Q2.

# def even(a,b):
#     print("Even number's are: ")
#     for i in range(a,b + 1):
#         if (i % 2 == 0):
#             print(i)
       
# a = int(input("Enter 1st number: "))
# b = int(input("Enter 2nd number: "))
# even(a,b)

# #Q3.

# def digit(num):
#     if num == 0:
#         return
#     digit(num // 10)
#     print(num % 10)

# num = int(input("Enter a number: "))
# digit(num)

# #Q4.

# def digit(num):
#     if num == 0:
#         return 0
#     return 1 + digit(num // 10)

# num = int(input("Enter a number: "))
# print("Total digits:", digit(num))

# #Q5.

# def sumOfDigit(num):
#     if num == 0:
#         return 0
#     return (num % 10) + sumOfDigit(num // 10)

# num = int(input("Enter a number: "))
# print("Sum of digits:", sumOfDigit(num))

# #Q6.

# for i in range(1,101):
#     if (i % 3 == 0 and i % 5 == 0):
#         print(i)

# #Q7.

# while True:
#     n = input("Enter number or Quit: ")

#     if n == "Quit":
#         break

#     try:
#         num = int(n)

#         if num > 0:
#             print("Positive")
#         elif num < 0:
#             print("Negative")
#         else:
#             print("Zero")

#     except:
#         print("Invalid input")

# #Q8.

# def calculator(a, b, operation):
#     if operation == "add":
#         print("Result:", a + b)
#     elif operation == "sub":
#         print("Result:", a - b)
#     elif operation == "mul":
#         print("Result:", a * b)
#     elif operation == "div":
#         if b != 0:
#             print("Result:", a / b)
#         else:
#             print("Division by zero not allowed")
#     else:
#         print("Invalid operation")


# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# operation = input("Enter operation (add/sub/mul/div): ")

# calculator(a, b, operation)

# #Q9.

# def is_prime(n):
#     if n < 2:
#         return False

#     for i in range(2, n):
#         if n % i == 0:
#             return False

#     return True


# num = int(input("Enter a number: "))

# if is_prime(num):
#     print("Prime number")
# else:
#     print("Not a prime number")

#Q10.

secret = 7

while True:
    guess = int(input("Enter your guess: "))

    if guess > secret:
        print("Too high")
    elif guess < secret:
        print("Too low")
    else:
        print("Correct!")
        break