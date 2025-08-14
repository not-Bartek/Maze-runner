import Maze
import tkinter as tk
from BFS import BFS
from DFS import DFS
import time

#TODO Implement deleting canva instead of rewriting with new object (speed loss)

MAZE_WIDTH = 30
MAZE_HEIGHT = 30
def paint_route(algorithm, canvas, debug=False):
    if algorithm == 'bfs':
        bfs = BFS()
        start = time.time()
        route = bfs.calculate(maze, maze.start, canvas)
        end = time.time()
        if debug:
            print(f'Czas wykonania bfs {end - start:.4f}, wielkość canvy: {len(canvas.find_all())}')
        for square in route:
            j, i = square
            canvas.create_rectangle(20*j, 20*i, 20*(j+1), 20*(i+1), fill="#f2ffa0")
    elif algorithm == 'dfs':
        dfs = DFS()
        start = time.time()
        route = dfs.calculate(maze, maze.start, canvas)
        end = time.time()
        if debug:
            print(f'Czas wykonania dfs {end - start:.4f}, wielkość canvy: {len(canvas.find_all())}')
        for square in route:
            j, i = square
            canvas.create_rectangle(20*j, 20*i, 20*(j+1), 20*(i+1), fill="#76e6ff")
def reset_canva(maze, canvas):
    canvas.delete("all")  # Usuwa wszystkie elementy z kanwy
    for i in range(maze.height):
        for j in range(maze.width):
            canvas.create_rectangle(20*j, 20*i, 20*(j+1), 20*(i+1), fill=color_dict[maze.maze[i][j]])
    canvas.update()

def on_b(event):
    paint_route('bfs', canvas, debug=True)
def on_d(event):
    paint_route('dfs', canvas)
def on_r(event):
    reset_canva(maze, canvas)
maze = Maze.Maze(MAZE_WIDTH, MAZE_HEIGHT)




root = tk.Tk()
root.title("Maze runner")
root.attributes('-topmost', True)
canvas = tk.Canvas(root, width = maze.width * 20, height = maze.height * 20)
canvas.pack()

color_dict = {
    0: 'white',
    1: "#484848",
    2: "#38d526",
    3: '#ffd500'
}
# Maze in window
for i in range(maze.height):
    for j in range(maze.width):
        canvas.create_rectangle(20*j, 20*i, 20*(j+1), 20*(i+1), fill=color_dict[maze.maze[i][j]])
root.bind('<b>', on_b)
root.bind('<d>', on_d)
root.bind('<r>', on_r)
if __name__ == "__main__":
    root.mainloop()