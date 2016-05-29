from util.xor import *
import unittest


class TestChallengeTwo(unittest.TestCase):
    def test_challenge(self):
        first = "1c0111001f010100061a024b53535009181c"
        second = "686974207468652062756c6c277320657965"
        expected_result = "746865206b696420646f6e277420706c6179"
        self.assertEquals(xor_hex(first, second), expected_result)
