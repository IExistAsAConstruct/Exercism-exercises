def is_armstrong_number(number):
    number_length = len(str(number))
    number_sum = sum(int(digit) ** number_length for digit in str(number))
    if number_sum == number:
        return True
    return False