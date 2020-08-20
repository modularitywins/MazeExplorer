def read_layout(filename="layout/maze.txt"):
    maze = [] # a list of {list of locations/letters}s, e,g. [["a", "b"], ["1", "2"]]
    with open(filename, "r") as file: # good practice to open a file
        for line in file:
            maze.append([])
            line = line.strip() # removing any heading and trailing white space " " "\s" "\t" "\n"
            for letter in line:
                maze[-1].append(letter)
    return maze

# print the maze in a user-friendly way
def print_layout(maze, user_location=(None, None)):
    for i in range(len(maze)):
        row_list = maze[i]
        row_string = ""
        for j in range(len(row_list)):
            letter = row_list[j]
            if (i, j) == user_location:
                letter = "X"
            row_string += letter # row_string = row_string + letter
        print(row_string)
