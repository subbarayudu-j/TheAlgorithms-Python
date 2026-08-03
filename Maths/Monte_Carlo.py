import random


def calculate_pi(samples):
    inside_circle = 0

    for _ in range(samples):
        x = random.random()
        y = random.random()

        if x * x + y * y <= 1:
            inside_circle += 1

    return 4 * inside_circle / samples


result = calculate_pi(1_000_000)
print(f"Pi approximation: {result}")
