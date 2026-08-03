from decimal import Decimal, getcontext
import math

def compute_pi_chudnovsky(digits):
    """
    Compute Pi using the Chudnovsky algorithm.
    :param digits: Number of decimal places to compute
    :return: Decimal value of Pi
    """
    if not isinstance(digits, int) or digits <= 0:
        raise ValueError("Digits must be a positive integer.")

    # Increase precision to avoid rounding errors during computation
    getcontext().prec = digits + 5

    # Constants in the Chudnovsky formula
    C = 426880 * Decimal(10005).sqrt()
    K = Decimal(6)
    M = Decimal(1)
    X = Decimal(1)
    L = Decimal(13591409)
    S = L

    k = 1
    while True:
        # Update variables according to the Chudnovsky series
        M = (K**3 - 16*K) * M // (k**3)
        L += 545140134
        X *= -262537412640768000
        term = (M * L) / X
        S += term

        # Break when term is smaller than desired precision
        if abs(term) < Decimal(1) / (10 ** (digits + 2)):
            break

        K += 12
        k += 1

    pi = C / S
    # Round to the requested number of digits
    getcontext().prec = digits
    return +pi  # Unary plus applies the precision

if __name__ == "__main__":
    try:
        n = int(input("Enter number of decimal places for π: "))
        pi_value = compute_pi_chudnovsky(n)
        print(f"π to {n} decimal places:\n{pi_value}")
    except ValueError as e:
        print(f"Error: {e}")
