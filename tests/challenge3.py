from util.xor import *
from util.text import *
import unittest

class TestChallengeThree(unittest.TestCase):
    def test_challenge(self):
        input = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
        xor_hex = "X".encode("hex")

        decrypt_hex = xor_hex_digit(input, xor_hex) 
        text = hex_to_text(decrypt_hex)
        self.assertEquals(text, "Cooking MC's like a pound of bacon")
