def combine_trucks(trucks, first_truck, second_truck):
    # TODO: return the total packages in first_truck and second_truck
        return first_truck + second_truck
    

# main()

def test_cases():
    trucks = [4, 7, 2, 6, 9]
    print(combine_trucks(trucks, trucks[1], trucks[3]))  # Expected: 13
    print(combine_trucks(trucks, trucks[0], trucks[2]))  # Expected: 6

    trucks = [5,10,15,0,0]
    print(combine_trucks(trucks, trucks[0], trucks[2]))  # Expected: 20

    trucks = [0,0,0,0,1000]
    print(combine_trucks(trucks, trucks[4], trucks[4]))  # Expected: 2000

test_cases()