import re

def afunction():
    print("This is the installed function")

def clean_string(str_word):
    """
    INPUTS:
    str_word     string string contining several words to clean
    RETURNS:
    string       the string after removal of extra spaces, punctuation and lowercasing
    """
    str_word = re.sub(r'\W+', ' ', str_word)
    assert isinstance(str_word, str), "String expected but recieved type {} instead".format(type(str_word))

    return str_word.strip()

import re
def space_compress(stocomp):
    assert isinstance(stocomp, str), "Expected str but got {} instead".format(type(stocomp))
    comp = re.sub(r'\s+', ' ', stocomp)
    return comp.strip()

def square_func(value):
    """
    INPUTS:
    value   int value to be squared
    RETURNS:
    square squared int value
    """
    assert isinstance(value, int), "Expected int but got {} instead".format(type(value))
    return value ** 2
