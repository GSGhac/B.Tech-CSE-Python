for num_pieces in range(1, 200):
    if num_pieces % 5 == 2 and num_pieces % 6 == 3 and num_pieces % 7 == 2:
        print(f"The number of pieces in the bowl is: {num_pieces}")
        break
