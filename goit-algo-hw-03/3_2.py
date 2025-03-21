import random

def get_numbers_ticket(min_value, max_value, quantity):
    if (min_value < 1 and max_value > 1000) or (max_value-min_value < quantity):
        return []

    lottery_numbers = sorted(random.sample(range(min_value, max_value), quantity))

    return lottery_numbers

print(get_numbers_ticket(14, 3, 4))

