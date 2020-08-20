from layout import read_layout
from layout import print_layout

def main():
    print("Welcome to Maze Explorer")
    maze = read_layout()
    print_layout(maze, (3, 1)) # (3, 1) is a tuple # the value is read-only
    pass

main()
