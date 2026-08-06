def combine_trucks(trucks, first_truck, second_truck):
    # TODO: return the total packages in first_truck and second_truck
    if first_truck != second_truck:
        return trucks[first_truck-1] + trucks[second_truck - 1]
    else:
        return f"{trucks[first_truck-1] + trucks[second_truck - 1]} Note: Boundary case, real value: {trucks[first_truck-1]}"
    

# main()

def test_cases():
    trucks = [4, 7, 2, 6, 9]
    print(combine_trucks(trucks, 2, 4))  # Expected: 13

    trucks = [5,10,15,0,0]
    print(combine_trucks(trucks, 1, 3))  # Expected: 20

    trucks = [0,0,0,0,1000]
    print(combine_trucks(trucks, 5, 5))  # Expected: 2000

test_cases()