import re


def generator_numbers(text):
    pattern = r'\b\d+\.\d+\b'
    for number in re.findall(pattern, text):
        yield number


def sum_profit(text, func):
    return sum(map(float, func(text)))
