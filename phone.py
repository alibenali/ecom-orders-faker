import random


def generate_random_phone():
    prefixes = ['06', '05', '07']
    prefix = random.choice(prefixes)
    suffix = ''.join(random.choices('0123456789', k=8))  # Generate 8 random digits
    return prefix + suffix