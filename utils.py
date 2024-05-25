import math

def calculate_array_size_and_hash_function_number(element_number, false_positive_rate):
    """
    :param element_number: the number of elements expected to insert
    :param false_positive_rate: range from 0 to 1
    :return: bit_array_size, hash_function_number
    """
    bit_array_size = - (element_number * math.log(false_positive_rate)) / (math.log(2) ** 2)
    hash_function_number = (bit_array_size / element_number) * math.log(2)

    return int(bit_array_size), int(hash_function_number)


def calculate_false_positive_rate(bit_array_size, hash_function_number, element_number):
    """
    :param bit_array_size: the size of bit array
    :param hash_function_number: the number of hash function
    :param element_number: the number of elements expected to insert
    :return: false_positive_rate (range from 0 to 1)
    """
    p = (1 - math.exp(-hash_function_number * element_number / bit_array_size)) ** hash_function_number
    return p