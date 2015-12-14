#! /usr/bin/env python3

import unittest
from naughty_nice_strings import disallowed, three_vowels, double_letter


class NaughtyNiceTestCase(unittest.TestCase):
    def test_not_disallowed(self):
        s = 'azza'
        self.assertFalse(disallowed(s))

    def test_double_letter_beginning(self):
        s = 'aaza'
        self.assertTrue(double_letter(s))

    def test_double_letter_middle(self):
        s = 'azza'
        self.assertTrue(double_letter(s))

    def test_double_letter_end(self):
        s = 'aczz'
        self.assertTrue(double_letter(s))
