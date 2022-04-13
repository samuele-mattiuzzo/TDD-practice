import re


def stringcalculator(numbers):
    if not len(numbers):
        # empty string
        return 0

    split_input = re.split(',|\n', numbers)
    if split_input[-1] == '':
        # the input ended with a delimiter
        raise Exception('The input cannot end with a delimiter')

    # return the sum
    return sum(map(int, split_input))

