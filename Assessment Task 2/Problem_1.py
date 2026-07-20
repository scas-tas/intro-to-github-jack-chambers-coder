def combine_trucks(trucks, first_truck, second_truck):
    # TODO: return the total packages in first_truck and second_truck
    return first_truck + second_truck


def main():
    trucks = [4, 7, 2, 6, 9]
    print(combine_trucks(trucks, trucks[1], trucks[3]))  # Expected: 13
    print(combine_trucks(trucks, trucks[0], trucks[2]))  # Expected: 6


main()
