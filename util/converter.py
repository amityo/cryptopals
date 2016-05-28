import math
import string

decimal_chars = [str(i) for i in range(10)]
hex_chars =  decimal_chars + ['a','b', 'c','d','e', 'f']
base64_chars = list(string.ascii_uppercase) + list(string.ascii_lowercase) + [str(i) for i in range(10)] + ['+','/']


def reverse(str):
    return str[::-1]

class Converter(object):
    # 16 -> 10
    @staticmethod
    def convert_hex_to_decimal(hex):
        return sum([int(hex_chars.index(c.lower()) * math.pow(16, idx)) for idx, c in enumerate(reverse(hex))])

    # 10 -> 2
    @staticmethod
    def convert_decimal_to_binary_inner(decimal):
        if decimal == 0:
            return ""
        else:
            return Converter.convert_decimal_to_binary_inner(decimal / 2) + str(decimal % 2)
          
    @staticmethod        
    def convert_decimal_to_binary(decimal):
        result = Converter.convert_decimal_to_binary_inner(decimal)
        while len(result) % 8 != 0:
            result = "0" + result
        return result
            
    # 2 -> 10
    @staticmethod
    def convert_binary_to_decimal(binary):
        return sum([int(int(c) * math.pow(2, idx)) for idx, c in enumerate(reverse(binary))])

    # 16 -> 2
    @staticmethod
    def convert_hex_to_binary(hex):
        decimal = Converter.convert_hex_to_decimal(hex)
        return Converter.convert_decimal_to_binary(decimal)

    # 2 -> 64
    @staticmethod
    def convert_binary_to_base64(binary):
        decimals = [Converter.convert_binary_to_decimal(binary[i:i+6]) for i in range(0, len(binary), 6)]
        return ''.join([base64_chars[decimal] for decimal in decimals])

    # 16 -> 64
    @staticmethod
    def convert_hex_to_base64(hex):
        binary = Converter.convert_hex_to_binary(hex)
        return Converter.convert_binary_to_base64(binary)

    @staticmethod
    def convert_binary_to_hex(binary):
        decimals = [Converter.convert_binary_to_decimal(binary[i:i+4]) for i in range(0, len(binary), 4)]
        return ''.join([hex_chars[decimal] for decimal in decimals])
