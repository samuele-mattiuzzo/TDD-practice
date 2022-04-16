import re

DELIMITER_ERROR_MESSAGE = 'The input cannot end with a delimiter'
NEGATIVE_NUMBER_ERROR_MESSAGE = 'No negative numbers allowed'


def stringcalculator(ipt):
    if not len(ipt):
        # empty string
        return 0

    separator, numbers = re.split('//|\n', ipt)[1:]

    if numbers.endswith(separator):
        # the input ended with a delimiter
        raise Exception(DELIMITER_ERROR_MESSAGE)

    split_numbers = numbers.split(separator)
    str_to_int = [i for i in map(int, split_numbers)]

    if not all([x >= 0 for x in str_to_int]):
        raise Exception(NEGATIVE_NUMBER_ERROR_MESSAGE)

    # return the sum
    return sum(str_to_int)
