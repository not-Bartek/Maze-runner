import Maze
import tkinter as tk
maze = Maze.Maze(41,41)

maze.print()

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

if __name__ == "__main__":
    root.mainloop()