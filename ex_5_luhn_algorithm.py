def calculate_check_digit(value):
    digits = [int(i) for i in value]
    odd_sum = sum([sum(divmod(2 * d, 10)) for d in digits[::2]])
    even_sum = sum(digits[1::2])
    control_digit = 0 if (odd_sum + even_sum) % 10 == 0 else (10 - (odd_sum + even_sum) % 10)
    return control_digit


def luhn_algorithm():
    print("Enter '1' to calculate control digit or '0' to check if control digit is correct:")
    calculate = bool(int(input()))
    print("Enter your value:")
    value = input()

    if calculate:
        control_digit = calculate_check_digit(value)
        print('Value with control digit: ' + value + '-' + str(control_digit))
    else:
        check_control_digit = int(value[-1])
        value = value[:-2]
        control_digit = calculate_check_digit(value)
        print("Control digit is correct" if check_control_digit == control_digit else "Control digit is not correct")


if __name__ == "__main__":
    luhn_algorithm()
