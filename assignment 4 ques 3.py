import random

num_questions = 10
num_correct = 0

for i in range(num_questions):
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    product = a * b
    answer = int(input(f"Question {i + 1}: {a} x {b} = "))
    if answer == product:
        print("Right!")
        num_correct += 1
    else:
        print(f"Wrong. The answer is {product}.")

print(f"You got {num_correct} out of {num_questions} correct.")
