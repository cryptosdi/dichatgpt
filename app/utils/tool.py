import random
import string

def generate_random_string(length):
        digits = string.digits
        result = ''.join(random.choices(digits, k=length))
        return result