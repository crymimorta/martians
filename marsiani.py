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

def main():
    total_weight = 713
    weights = []
    while True:
        cargo_location = generate_cargo_location()  # array of locations of 3 boxes
        print(cargo_location)
        kilometers = []  # array of distances from martians
        for i in range(3):
            klm_of_box = int(input(f'Enter the kilometer mark for box {i + 1}, number from 1 to 7: '))
            kilometers.append(klm_of_box)
        cargo_found = (cargo_location, kilometers)
        if cargo_found:
            print("Congratulations! You found all the cargo locations! Now let's find their weights")
            for i in range(3):
                weight = int(input(f'Enter the weight for box {i + 1}: '))
                weights.append(weight)
            cargo_weight = check_total_weight(total_weight, weights)
            if cargo_weight:
                print("Congratulations! You found all the cargo!")
                break
            else:
                print('Fail, you entered wrong weight.')
        else:
            cargo_location = generate_cargo_location()
            print('Fail, the cargoes were not found. Cargoes have changed their location,enter new kilometer marks.')

main()