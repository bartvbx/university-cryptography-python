from math import gcd
from random import randrange


def fermat_test(n):
    a = randrange(1, n)
    if gcd(a, n) > 1: return True
    u = a ** (n - 1) % n
    return True if u != 1 else False


def perform_fermat_test():
    print("Enter odd number to be tested or enter 0 if you want to draw a random number:")
    test_value = int(input())

    if test_value == 0:
        # print("Enter the upper limit of the random number, at least 10^(9):")
        # Values greater than 10^(7) are not recommended for performance reasons
        print("Enter the upper limit of the random number:")
        upper_limit = int(input())
        # if upper_limit < 10 ** 9:
        #     raise ValueError("The specified limit is too small")
        test_value = randrange(1, upper_limit, 2)

    if test_value % 2 == 0:
        raise ValueError("The specified number is not odd")

    print("Enter the number of trials in the test:")
    n_tests = int(input())
    
    for _ in range(n_tests):
        if fermat_test(test_value):
            print(f"Tested number {test_value} is not a prime number")
            return
    
    print(f"Tested number {test_value} is a prime number with probability of {1 - 0.5 ** n_tests}")


if __name__ == "__main__":
    perform_fermat_test()
