def check_pesel():
    print("Enter your PESEL:")
    pesel = input()

    if len(pesel) != 11:
        raise ValueError("The PESEL should consist of 11 digits")

    pesel_weights = (1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1)

    multiplied_digits = [int(n) * w for n, w in zip(pesel, pesel_weights)]
    multiplied_digits_sum = sum(i if len(str(i)) == 1 else int(str(i)[1]) for i in multiplied_digits)

    print("The PESEL is correct" if multiplied_digits_sum % 10 == 0 else "The PESEL is not correct")


if __name__ == "__main__":
    check_pesel()
