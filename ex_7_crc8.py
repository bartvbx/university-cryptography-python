def crc8():
    print("Enter a bit string:")
    input_value = input()
    polynomial_value = [int(i) for i in input_value]
    print("Enter a divider bit string of length 8:")
    input_divider = input()
    divider_crc = [int(i) for i in input_divider]

    crc = [0] * 7
    polynomial_value_crc = polynomial_value + crc

    while 1 in polynomial_value_crc[:-7]:
        start_index = polynomial_value_crc.index(1)
        for i in range(8):
            polynomial_value_crc[start_index + i] = polynomial_value_crc[start_index + i] ^ divider_crc[i]
        print(polynomial_value_crc)

    print("CRC is:", polynomial_value_crc[-7:])


if __name__ == "__main__":
    crc8()
