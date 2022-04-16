import re

ERROR_MESSAGE = 'ERROR: The input cannot end with a delimiter'


def stringcalculator(numbers):
    if not len(numbers):
        # empty string
        return 0

    separator, numbers = re.split('//|\n', numbers)[1:]

    if numbers.endswith(separator):
        # the input ended with a delimiter
        raise Exception(ERROR_MESSAGE)

    split_numbers = numbers.split(separator)
    # return the sum
    return sum(map(int, split_numbers))
