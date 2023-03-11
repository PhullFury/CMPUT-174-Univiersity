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

def main():
    grid = create_grid("data_3.txt")
    print("Sim City Land Values:")
    display_grid(grid)

if __name__ == "__main__":
    main()