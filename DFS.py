import time
import gc
from config import CELL_SIZE
from config import STEP_TIME

class DFS:
    def color_square(self, canvas, x, y):
        canvas.create_rectangle(CELL_SIZE*x, CELL_SIZE*y, CELL_SIZE*(x+1), CELL_SIZE*(y+1), fill="#cbebff")

    def calculate(self, maze, root, canvas, animation = True):
        gc.collect()
        visited = [[False for _ in range(maze.width)] for _ in range(maze.height)]
        parents = {}
        stack = []
        stack.append(root)


        while stack:
            actual = stack.pop()
            x, y = actual

            if not visited[y][x]:
                
                if(actual != maze.start and actual != maze.end):
                    self.color_square(canvas, x, y)
                    if animation:
                        canvas.update()
                    
                    time.sleep(STEP_TIME)

                visited[y][x] = True
                if actual == maze.end:
                    route = []
                    while actual != maze.start:
                        
                        if actual != maze.start:
                            actual = parents[actual]
                        if actual != maze.start:
                            route.append(actual)
                    del stack
                    del parents
                    del visited
                    gc.collect()
                    return route
                else:
                    #dodanie komórek do listty dzieci
                    childs = []
                    directions = [(0,1), (0,-1), (1,0), (-1,0)]
                    for dx, dy in directions:
                        if maze.maze[y+dy][x+dx] != 1:
                            childs.append((x+dx,y+dy))
                    
                    for child in childs:
                        cx, cy = child
                        #ustawienie rodzica
                        
                        if not visited[cy][cx]:
                            #dziecko na stos
                            parents[child] = actual
                            stack.append(child)

        print("brak ścieżki")