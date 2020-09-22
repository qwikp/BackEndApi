import re
from random import randint


def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


def bd_number_match(phone_number):
    regex_str = "^(?:\+?88)?01[13-9]\d{8}$"
    if re.search(regex_str, phone_number):
        return True
    else:
        return False


def swedish_phone_no_formatter(phone_no):
    if phone_no[0] == '0':
        phone_no = phone_no[1:]
    if phone_no[0] != '+':
        phone_no = '+46' + phone_no
    return phone_no
