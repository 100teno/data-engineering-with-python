# Pythonic is the code that makes Python code more readable and idiomatic.

# Non-Pythonic way
doubled_numbers =  []

for i in range(len(numbers)):
    doubled_numbers.append(numbers[i] * 2)

# Pythonic way
doubled_numbers = [x * 2 for x in numbers]