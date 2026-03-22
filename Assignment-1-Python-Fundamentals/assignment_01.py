# Q1.

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Hello", name + ",", "you are", age, "years old!")

# Q2.

num_1 = int(input("Enter 1st number: "))
num_2 = int(input("Enter 2nd number: "))

sum = num_1 + num_2
difference = num_1 - num_2
product = num_1 * num_2
quotient = num_1 / num_2

print("sum is:", sum)
print("difference is:", difference)
print("product is:", product)
print("quotient is:", quotient)

# Q3.

num_1 = float(input("Enter first integer: "))
num_2 = float(input("Enter second integer: "))
num_3 = float(input("Enter float number: "))

average = (num_1 + num_2 + num_3)/3

print(average)

# Q4.

num = input("Enter a number: ")

print("Original:", num, type(num))

i_num = int(num)
f_num = float(num)
s_num = str(num)

print("Integer:", i_num, type(i_num))
print("Float:", f_num, type(f_num))
print("String:", s_num, type(s_num))

# Q5.

x = 10 + 3 * 2 ** 2

print(x)

# The output is 22 because Python follows operator precedence rules.
# First exponentiation is performed (2 ** 2 = 4), then multiplication (3 * 4 = 12), and finally addition (10 + 12 = 22).
# Therefore, the final result is 22.

# Q6.

num_1 = input("Enter num 1: ")
num_2 = input("Enter num 2: ")

x = num_1
num_1 = num_2
num_2 = x

print("After swapping num 1 is: ", num_1)
print("After swapping num 2 is: ", num_2)

# Q7.

celsius_temp = float(input("Enter temperature in celsius: "))

fahrenheit_temp = (celsius_temp * (9/5) + 32)

print(fahrenheit_temp)

# Q8.

pi = 3.14
radius = float(input("Enter the redius: "))

area = pi * radius * radius

print(area)

# Q9.

p = float(input("Enter Principal: "))
r = float(input("Enter Rate: "))
t = float(input("Enter Time: "))

si = (p * r * t) / 100

print(f"Simple Interest = {si:.2f}")

# Q10.

decimal = float(input("Enter a decimal number: "))

integer = int(decimal)
fraction = decimal - integer

print("Integer part:", integer)
print("Fractional part:", f"{fraction:.2f}")