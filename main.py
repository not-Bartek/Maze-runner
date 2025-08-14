import Maze
import tkinter as tk
from BFS import BFS
from DFS import DFS
import time
from config import CELL_SIZE

#TODO Implement deleting canva instead of rewriting with new object (speed loss)

MAZE_WIDTH = 270
MAZE_HEIGHT = 270
 # Rozmiar jednej kratki w pikselach

def paint_route(algorithm, canvas, debug=False, animation=True):
    if algorithm == 'bfs':
        bfs = BFS()
        start = time.time()
        route = bfs.calculate(maze, maze.start, canvas, animation)
        end = time.time()
        if debug:
            print(f'Czas wykonania bfs {end - start:.4f}, wielkość canvy: {len(canvas.find_all())}')
        for square in route:
            j, i = square
            canvas.create_rectangle(CELL_SIZE*j, CELL_SIZE*i, CELL_SIZE*(j+1), CELL_SIZE*(i+1), fill="#b7ff00")
    elif algorithm == 'dfs':
        dfs = DFS()
        start = time.time()
        route = dfs.calculate(maze, maze.start, canvas, animation)
        end = time.time()
        if debug:
            print(f'Czas wykonania dfs {end - start:.4f}, wielkość canvy: {len(canvas.find_all())}')
        for square in route:
            j, i = square
            canvas.create_rectangle(CELL_SIZE*j, CELL_SIZE*i, CELL_SIZE*(j+1), CELL_SIZE*(i+1), fill="#1100ff")
def reset_canva(maze, canvas):
    canvas.delete("all")  # Usuwa wszystkie elementy z kanwy
    for i in range(maze.height):
        for j in range(maze.width):
            canvas.create_rectangle(CELL_SIZE*j, CELL_SIZE*i, CELL_SIZE*(j+1), CELL_SIZE*(i+1), fill=color_dict[maze.maze[i][j]])
    canvas.update()

def on_b(event):
    animation = True
    if MAZE_HEIGHT * MAZE_WIDTH > 5000:
        animation = False
    paint_route('bfs', canvas, debug=False, animation=animation)
def on_d(event):
    animation = True
    if MAZE_HEIGHT * MAZE_WIDTH > 5000:
        animation = False
    paint_route('dfs', canvas, debug = False, animation=animation)
def on_r(event):
    reset_canva(maze, canvas)
maze = Maze.Maze(MAZE_WIDTH, MAZE_HEIGHT)




root = tk.Tk()
root.title("Maze runner")
root.attributes('-topmost', True)
canvas = tk.Canvas(root, width=maze.width * CELL_SIZE, height=maze.height * CELL_SIZE)
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
        canvas.create_rectangle(CELL_SIZE*j, CELL_SIZE*i, CELL_SIZE*(j+1), CELL_SIZE*(i+1), fill=color_dict[maze.maze[i][j]])
root.bind('<b>', on_b)
root.bind('<d>', on_d)
root.bind('<r>', on_r)
if __name__ == "__main__":
    root.mainloop()