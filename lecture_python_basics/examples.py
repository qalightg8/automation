from typing import Union

digits = [1, 2, 3, 4, 5]
strings = ['a', 'b', 'c']

summ_of_digits = sum(digits)
print(summ_of_digits)

summ_of_strings = ''.join(strings)
print(summ_of_strings)

digits2 = [1, 1, 2, 3, 4, 4]
summ_of_unique_values = sum(set(digits2))
print(summ_of_unique_values)

employee = {'name': 'Vasya', 'salary': 1000.0}
# employee['salary'] = employee['salary'] * 1.5
employee['salary'] *= 1.5
print(employee)
