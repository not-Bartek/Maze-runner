import Maze
import tkinter as tk
from BFS import BFS


def paint_route(route):
    for square in route:
        j, i = square
        canvas.create_rectangle(20*j, 20*i, 20*(j+1), 20*(i+1), fill="blue")

def on_space(event):
    paint_route(route)

maze = Maze.Maze(30,30)

maze.print()
bfs = BFS()

route = bfs.calculate(maze, maze.start)


root = tk.Tk()
root.title("Maze runner")
root.attributes('-topmost', True)

canvas = tk.Canvas(root, width = maze.width * 20, height = maze.height * 20)
canvas.pack()

color_dict = {
    0: 'white',
    1: 'black',
    2: 'green',
    3: 'orange'
}

for i in range(maze.height):
    for j in range(maze.width):
        canvas.create_rectangle(20*j, 20*i, 20*(j+1), 20*(i+1), fill=color_dict[maze.maze[i][j]])
root.bind('<space>', on_space)

if __name__ == "__main__":
    root.mainloop()