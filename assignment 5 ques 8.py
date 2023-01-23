def print_numbers_info():
    numbers = []
    for i in range(10):
        number = int(input("Enter an integer: "))
        numbers.append(number)
        
    positive_numbers = [x for x in numbers if x > 0]
    negative_numbers = [x for x in numbers if x < 0]
    odd_numbers = [x for x in numbers if x % 2 != 0]
    even_numbers = [x for x in numbers if x % 2 == 0]
    occurrences = {}
    for number in numbers:
        if number in occurrences:
            occurrences[number] += 1
        else:
            occurrences[number] = 1
    print("Positive numbers:", positive_numbers)
    print("Negative numbers:", negative_numbers)
    print("Odd numbers:", odd_numbers)
    print("Even numbers:", even_numbers)
    print("Number of occurrences:", occurrences)

print_numbers_info()
