import math
import string

decimal_chars = [str(i) for i in range(10)]
hex_chars =  decimal_chars + ['a','b', 'c','d','e', 'f']
base64_chars = list(string.ascii_uppercase) + list(string.ascii_lowercase) + [str(i) for i in range(10)] + ['+','/']


def reverse(str):
    return str[::-1]

# 16 -> 10
def convert_hex_to_decimal(hex):
    return sum([int(hex_chars.index(c.lower()) * math.pow(16, idx)) for idx, c in enumerate(reverse(hex))])

# 10 -> 2
def convert_decimal_to_binary_inner(decimal):
    if decimal == 0:
        return ""
    else:
        return convert_decimal_to_binary_inner(decimal / 2) + str(decimal % 2)
      
    
def convert_decimal_to_binary(decimal):
    result = convert_decimal_to_binary_inner(decimal)
    while len(result) % 8 != 0:
        result = "0" + result
    return result
        
# 2 -> 10
def convert_binary_to_decimal(binary):
    return sum([int(int(c) * math.pow(2, idx)) for idx, c in enumerate(reverse(binary))])

# 16 -> 2
def convert_hex_to_binary(hex):
    decimal = convert_hex_to_decimal(hex)
    return convert_decimal_to_binary(decimal)

# 2 -> 64
def convert_binary_to_base64(binary):
    decimals = [convert_binary_to_decimal(binary[i:i+6]) for i in range(0, len(binary), 6)]
    return ''.join([base64_chars[decimal] for decimal in decimals])

# 16 -> 64
def convert_hex_to_base64(hex):
    binary = convert_hex_to_binary(hex)
    return convert_binary_to_base64(binary)

if __name__ == "__main__":
    hex = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    expected_base64 = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    print convert_hex_to_base64(hex) == expected_base64
