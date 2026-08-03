def calculate_pi(iterations):
    pi = 0.0

    for n in range(iterations):
        term = ((-1) ** n) / (2 * n + 1)
        pi += term

    return 4 * pi


result = calculate_pi(1_000_000)
print(f"Pi approximation: {result}")
