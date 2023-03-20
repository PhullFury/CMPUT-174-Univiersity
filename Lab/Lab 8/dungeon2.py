import copy

MAP_FILE = 'cave_map.txt'

def load_map(map_file):
    with open(map_file,'r') as file:
        str = file.readline().rstrip('\n')
        map = []
        while not str == "":
            temp = []
            for i in str:
                temp.append(i)
            map.append(temp)
            str = file.readline().rstrip('\n')
    return map

def find_start(grid):
    for m in range(len(grid)):
        for n in grid[m]:
            if (n == "S"):
                n_index = grid[m].index(n)
                return [m,n_index]

def get_command():
    return input("What's your command: ")

def display_map(grid, player_position):
    map = copy.deepcopy(grid)
    m = player_position[0]
    n = player_position[1]
    map[m][n] = "@"
    for row in map:
        temp_row = ""
        for col in row:
            temp_row += col
        print(temp_row)

def get_grid_size(grid):
    row = len(grid)
    col = len(grid[0])
    return [row, col]

def is_inside_grid(grid, player_position):
    grid_rows, grid_cols = get_grid_size(grid)
    row = player_position[0]
    col = player_position[1]
    if (not row < 0 and not row >= grid_rows and not col < 0 and not col >= grid_cols):
        return True
    else:
        return False

def look_around(grid, player_position):
    allowed_objects = ('S', 'F', '*')
    row = player_position[0]
    col = player_position[1]
    directions = []
    if (is_inside_grid(grid, [row - 1, col]) and grid[row - 1][col] in allowed_objects):
        directions.append('north')
    if (is_inside_grid(grid, [row, col - 1]) and grid[row][col - 1] in allowed_objects):
        directions.append('west')
    if (is_inside_grid(grid, [row + 1, col]) and grid[row + 1][col] in allowed_objects):
        directions.append('south')
    if (is_inside_grid(grid, [row, col + 1]) and grid[row][col + 1] in allowed_objects):
        directions.append('east')
    return directions

def display_directions(directions):
    for i in directions:
        print("You can go " + i)

def main():
    map = load_map(MAP_FILE)
    position = find_start(map)
    display_map(map, position)
    display_directions(look_around(map, position))
    command = get_command().lower()
    while not command == "escape":
        if (command == "show map"):
            display_map(map, position)
            print()
        else:
            print("I do not understand\n")
        display_directions(look_around(map, position))
        command = get_command().lower()

if __name__ == "__main__":
    main()