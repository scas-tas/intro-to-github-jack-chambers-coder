import random
counter = 0
grid = []


for row in range(5):
   row_list = []
   for col in range(5):
       row_list.append(" ")
   grid.append(row_list)

def place():
    global counter
    while counter < 15:
        for row in range(0, 5):
            if counter < 15:
                break
            column = random.randint(0, 4)
            if grid[row][column] == "X":
                continue
            else:
                grid[row][column] = ("X")
                counter += 1
place()
for list in grid:
    print(list)