from util.converter import Converter
import unittest


class TestChallengeOne(unittest.TestCase):
    def test_challenge(self):
        hex = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
        expected_base64 = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
        self.assertEquals(Converter.convert_hex_to_base64(hex), expected_base64)
