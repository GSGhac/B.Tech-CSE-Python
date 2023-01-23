def find_numbers():
    for i in range(1, 501):
        if i % 7 == 0 and i % 11 == 0:
            print(i)

find_numbers()
