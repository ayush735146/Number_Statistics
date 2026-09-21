"""
Project: Number Statistics

This program:
1. Identifies even and odd numbers from a given list.
2. Finds the largest and smallest numbers.
3. Demonstrates loops, conditions, modulo operator, max(), and min().
"""

numbers = [12, 7, 25, 4, 18, 31, 9, 42, 16, 3]

even_numbers = []
odd_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

largest_number = max(numbers)
smallest_number = min(numbers)

print("Number Statistics")
print("-" * 30)
print("Original list :", numbers)
print("Even numbers  :", even_numbers)
print("Odd numbers   :", odd_numbers)
print("Largest value :", largest_number)
print("Smallest value:", smallest_number)
