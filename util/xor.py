from converter import Converter


def xor(first_digit, second_digit):
    if first_digit == second_digit:
        return 0
    return 1


def xor_str(first_digit, second_digit):
    return str(xor(first_digit, second_digit))


def xor_hex(first, second):
    first_binary = Converter.convert_hex_to_binary(first)
    second_binary = Converter.convert_hex_to_binary(second)
    result_binary = ''.join([xor_str(f, s) for f, s in zip(first_binary, second_binary)])
    return Converter.convert_binary_to_hex(result_binary)


def xor_hex_digit(input, xor):
    return ''.join([xor_hex(input[i:i + 2], xor) for i in range(0, len(input), 2)])
