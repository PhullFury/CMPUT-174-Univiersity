import copy

def create_grid(filename):
    with open(filename, 'r') as file:
        row = int(file.readline().rstrip('\n'))  # gets the info about the number of rows
        col = int(file.readline().rstrip('\n'))  # gets the info about the number of columns
        grid = []
        for m in range(row):  # loops for the number of rows
            temp_row = []
            for n in range(col):  # loops for the number of columns
                temp_row.append(int(file.readline().rstrip('\n')))  # gets the data and puts it in a temporary list
            grid.append(temp_row)
    return grid

def display_grid(grid):
    for m in range(len(grid)):
        temp_row = ""
        for n in grid[m]:
            temp_value = "{:>8}"  # adds a 'space'
            temp_row += temp_value.format(str(n))  # adds value to the 'space' format
        print(temp_row)

def find_neighbor_values(grid, row, col):
    max_row = len(grid)-1  # max row value
    max_col = len(grid[0])-1  # max column value
    upper_row = row-1
    lower_row = row+1
    left_col = col-1
    right_col = col+1
    neighbors = []
    if (not upper_row < 0):
        if (not left_col < 0):
            neighbors.append(grid[upper_row][left_col])
        neighbors.append(grid[upper_row][col])
        if (not right_col > max_col):
            neighbors.append(grid[upper_row][right_col])
    if (not left_col < 0):
        neighbors.append(grid[row][left_col])
    if (not right_col > max_col):
        neighbors.append(grid[row][right_col])
    if (not lower_row > max_row):
        if (not left_col < 0):
            neighbors.append(grid[lower_row][left_col])
        neighbors.append(grid[lower_row][col])
        if (not right_col > max_col):
            neighbors.append(grid[lower_row][right_col])
    return neighbors

def fill_gaps(grid):
    filled_grid = copy.deepcopy(grid)  # makes a unique copy of the grid
    for m in range(len(grid)):  # loops for the number of rows
        for n in grid[m]:  # loops the loop
            if (n == 0):  # checks whether a zero entry exists
                n_index = grid[m].index(n)  # gets column index
                neighbors = find_neighbor_values(grid,m,n_index)
                number = len(neighbors)
                sum = 0
                for i in neighbors:  # calculates average value
                    sum += i
                average = round(sum/number)
                filled_grid[m][n_index] = average  # replaces zero with average
    return filled_grid

def find_max(grid):
    max = 0
    for m in grid:  # iterates over the entire grid
        for n in m:
            if (n > max):
                max = n
    return max

def find_average(grid):
    num_row = len(grid)
    num_col = len(grid[0])
    num_total = num_row * num_col
    sum = 0
    for m in grid:
        for n in m:
            sum += n
    average = round(sum/num_total)
    return average

def main():
    grid = create_grid("data_3.txt")
    print("Sim City Land Values:")
    display_grid(grid)
    print("\nCalculated Sim City land values:")
    new_grid = fill_gaps(grid)
    display_grid(new_grid)
    print("\nSTATS")
    print("Average land value in this city: " + str(find_average(new_grid)))
    print("Maximum land value in this city: " + str(find_max(new_grid)))

if __name__ == "__main__":
    main()