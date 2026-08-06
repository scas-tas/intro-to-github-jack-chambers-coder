def test_cases():
    classroom1 = [[1,2,0],
                 [0,3,4],
                 [5,0,0]]
    classroom2= [[1,2],
                [3,4]]
    classroom3=[[0,0],
               [0,0]]
    classroom4=[[1,2,0],
               [0,3,4],
               [5,0,0]]
    classroom5=[[1,2,3],
               [0,0,4],
               [5,0,0]]
    classroom6=[[1,2],
               [3,4]]
    return classroom1
list_of_rows = []


def most_empty_row(classroom: list) -> int:
    best_row = 0
    best_count = -1
    empty_amount = 0
    for row_index in range(len(classroom)):
        for index in classroom[row_index]:
            if index == 0:
                empty_amount += 1
        if empty_amount > best_count:
            best_count = empty_amount
            best_row = row_index
        empty_amount = 0
    return  best_row


def count_empty(classroom: list) -> int:
    count = 0
    for row in classroom:
        for row_slot in row:
            if row_slot == 0:
                count += 1
    return count
 
print(most_empty_row(test_cases()))
#print(count_empty(test_cases()))