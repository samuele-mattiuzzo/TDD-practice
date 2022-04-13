def fizzbuzz(num):    
    if not num % 3 and not num % 5:
        return 'FizzBuzz'

    if not num % 3:
        return 'Fizz'

    if not num % 5:
        return 'Buzz'

    return num
