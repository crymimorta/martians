import random

def generate_cargo_location():  # Dist from spaceship to city 7 km
    return random.sample(range(1, 8), 3)

