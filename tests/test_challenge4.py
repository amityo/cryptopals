import string
from collections import Counter
import re

from util.xor import *
from util.text import *
import unittest


# Answer:
# 7b5a4215415d544115415d5015455447414c155c46155f4058455c5b523f
# Now that the party is jumping
# the char -  5

class TestChallengeFour(unittest.TestCase):

    def test_challenge_by_most_common_char(self):
        """
        Step 1: Get all the lines with the most common char (two hex) appear more than four times.
        Step 2: The most common character in a long string will probably be space " ".
        Step 3: Find the xor char -
            xor between the most common char and every char in [0-9|a-z]
            decode the xor and see if it equals to the most common char (from Step 1)
        Step 4: Use hex_xor_digit to xor each char in word and print the decoded word
        Step 5: Search for english sentence (or use regex)

        """
        words = self.read_lined_from_file()

        words_with_common_chars = self.get_possible_words_with_common_chars(words)

        common_chars = [" "]

        options = []
        for possibility in words_with_common_chars:
            option = self.find_decryption_option(common_chars, possibility)
            if option:
                options.append(option)
        self.assertTrue("Now that the party is jumping\n" in options)

    def _test_challenge_brute_force(self):
        # letters, whitepace, digits, special charecters
        regex = re.compile("^(\s+|\d+|\w+|[!?.,]+)+$")
        words = self.read_lined_from_file()
        for word in words:
            self.brute_force(word, regex)

    def find_decryption_option(self, common_chars, possibility):
        most_common_char = self.get_most_common(possibility)
        for encoded in [d.encode("hex") for d in string.digits + string.ascii_lowercase]:
            if xor_hex(most_common_char, encoded).decode("hex") in common_chars:
                decrypt_hex = xor_hex_digit(possibility, encoded)
                return hex_to_text(decrypt_hex)

    def read_lined_from_file(self):
        f = open("4.txt", 'r')
        words = f.read().split('\n')
        return words

    def get_possible_words_with_common_chars(self, words):
        return [word for word in words if self.get_most_common(word)[1] > 4]

    def get_most_common(seff, word):
        r = [word[i:i + 2] for i in range(0, len(word), 2)]
        c = Counter(r)
        return c.most_common(1)[0][0]

    def brute_force(self, word, regex):
        encoded_letters = [letter.encode("hex") for letter in string.printable]
        for encoded in encoded_letters:
            decrypt_hex = xor_hex_digit(word, encoded)
            text = hex_to_text(decrypt_hex)
            result = regex.search(text)
            if result:
                print word, encoded, encoded.decode("hex")
                print text
