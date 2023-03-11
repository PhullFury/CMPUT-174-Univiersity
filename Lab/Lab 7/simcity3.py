import copy

def create_grid(filename):
    with open(filename, 'r') as file:
        row = int(file.readline().rstrip('\n'))
        col = int(file.readline().rstrip('\n'))
        grid = []
        for m in range(row):
            temp_row = []
            for n in range(col):
                temp_row.append(int(file.readline().rstrip('\n')))
            grid.append(temp_row)
    return grid

def display_grid(grid):
    for m in range(len(grid)):
        temp_row = ""
        for n in grid[m]:
            temp_value = "{:>8}"
            temp_row += temp_value.format(str(n))
        print(temp_row)

def find_neighbor_values(grid, row, col):
    max_row = len(grid) - 1
    max_col = len(grid[0]) - 1
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
    filled_grid = copy.deepcopy(grid)
    for m in range(len(grid)):
        for n in grid[m]:
            if (n == 0):
                n_index = grid[m].index(n)
                neighbors = find_neighbor_values(grid,m,n_index)
                number = len(neighbors)
                sum = 0
                for i in neighbors:
                    sum += i
                average = round(sum/number)
                filled_grid[m][n_index] = average
    return filled_grid

def main():
    grid = create_grid("data_1.txt")
    print("Sim City Land Values:")
    display_grid(grid)
    print("\nCalculated Sim City land values:")
    new_grid = fill_gaps(grid)
    display_grid(new_grid)

if __name__ == "__main__":
    main()