#! /usr/bin/env python3
import re

#  matches a double letter
double = re.compile(r'([a-z])\1')


def disallowed(s):
    return any(string in s for string in ('ab', 'cd', 'pq', 'xy'))


def three_vowels(s):
    vowel_count = 0
    for char in s:
        if char.upper() in 'AEIOU':
            vowel_count += 1
    return vowel_count >= 3


def double_letter(s):
    return double.match(s) is not None


def is_nice(s):
    return (not disallowed(s)) and three_vowels(s) and double_letter(s)

num_nice = 0
with open("input.txt", "r") as fin:
    for line in fin:
        if is_nice(line.strip()):
            num_nice += 1

print(num_nice)
