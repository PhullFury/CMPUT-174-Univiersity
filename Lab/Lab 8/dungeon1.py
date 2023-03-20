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
            if n == "S":
                n_index = grid[m].index(n)
                return [m,n_index]

def get_command():
    return input()

def main():
    map = load_map(MAP_FILE)
    print(map)
    print("Starting position: " + str(find_start(map)))
    command = get_command().lower()
    while not command == "escape":
        print("I do not understand")
        command = get_command().lower()

if __name__ == "__main__":
    main()