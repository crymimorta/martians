import random

def generate_cargo_location():  # Dist from spaceship to city 7 km
    return random.sample(range(1, 8), 3)

def check_cargo_location(locations, kilometers):
    if len(locations) != len(kilometers):
        return False
    for i in range(3):
        if locations[i] != kilometers[i]:
            return False
    return True

def check_total_weight(total_weight, weights):  # Function, that calculates the total weight of the cargo.
    sum_weights = sum(weights[i] for i in range(3))
    return total_weight == sum_weights
