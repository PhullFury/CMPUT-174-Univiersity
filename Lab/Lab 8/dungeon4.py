import copy
MAP_FILE = 'midgaard_map.txt'

def load_map(map_file):
    with open(map_file,'r') as file:  # opens the file
        str = file.readline().rstrip('\n')  # strips the new line formatting
        map = []
        while not str == "":  # loops until the file is finished
            temp = []
            for i in str:
                temp.append(i)
            map.append(temp)
            str = file.readline().rstrip('\n')
    return map

def find_start(grid):
    for m in range(len(grid)):  # loops the rows
        for n in grid[m]:  # loops the columns
            if (n == "S"):
                n_index = grid[m].index(n)
                return [m,n_index]  # returns position as a list

def find_end(grid):
    for m in range(len(grid)):
        for n in grid[m]:
            if (n == "F"):
                n_index = grid[m].index(n)
                return [m,n_index]

def get_command():
    return input("What's your command: ")

def display_map(grid, player_position):
    map = copy.deepcopy(grid)  # makes a copy that's independent of the original grid
    m = player_position[0]  # gets the row position
    n = player_position[1]  # gets the column position
    map[m][n] = "@"  # adds the 'player'
    for row in map:
        temp_row = ""
        for col in row:
            if col == "S":
                temp_row += "🏠"
            elif col == "F":
                temp_row += "🏺"
            elif col == "-":
                temp_row += "🧱"
            elif col == "*":
                temp_row += "🟢"
            elif col == "@":
                temp_row += "🧝"
        print(temp_row)

def get_grid_size(grid):
    row = len(grid)  # gets the number of rows
    col = len(grid[0])  # gets the number of columns
    return [row, col]

def is_inside_grid(grid, player_position):
    grid_rows, grid_cols = get_grid_size(grid)
    row = player_position[0]
    col = player_position[1]
    if (not row < 0 and not row >= grid_rows and not col < 0 and not col >= grid_cols):  # checks if the position is outside the grid or not
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
    # these if statements check whether the position is in the grid and whether it's an allowed object
    return directions

def display_directions(directions):
    for i in directions:
        print("You can go " + i)

def move(direction, player_position, grid):
    if (direction in look_around(grid, player_position)):  # checks if the direction inputted is valid
        if (direction == "north"):
            player_position[0] -= 1  # updates the row index
        if (direction == "south"):
            player_position[0] += 1
        if (direction == "west"):
            player_position[1] -= 1  # updates the column index
        if (direction == "east"):
            player_position[1] += 1
        return True
    else:
        return False

def check_finish(grid, player_position):
    end_position = find_end(grid)
    if (player_position == end_position):
        return True
    else:
        return False

def display_help():
    with open('help.txt','r') as file:
        str = file.readline().rstrip('\n')
        while not str == "":
            print(str)
            str = file.readline().rstrip('\n')
        print()

def main():
    map = load_map(MAP_FILE)
    position = find_start(map)
    display_map(map, position)
    display_directions(look_around(map, position))
    command = get_command().lower()  # lowers the inputted string to make it easy to compare
    finished = check_finish(map, position)
    while not command == "escape" and not finished:  # runs until the user inputs 'escape' or the user reaches the finish position
        if (command == "show map"):
            display_map(map, position)
            print()
        elif (command == "go north" or command == "go south" or command == "go west" or command == "go east"):
            if (move(command[3:], position, map)):
                print("You moved " + command[3:] + "\n")
                finished = check_finish(map, position)
            else:
                print("There is no way there\n")
        elif (command == "help"):
            display_help()
        else:
            print("I do not understand\n")
        if (not finished):
            display_directions(look_around(map, position))
            command = get_command().lower()
        elif (finished):
            print("Congratulations! You have reached the exit!")
            display_map(map, position)

if __name__ == "__main__":
    main()