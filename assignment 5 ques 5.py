def print_pattern(num_rows):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    index = 0
    for i in range(1, num_rows + 1):
        for j in range(i):
            print(alphabet[index], end="")
            index += 1
            if index == 26:
                index = 0
        print()

num_rows = int(input("Enter the number of rows: "))
print_pattern(num_rows)
