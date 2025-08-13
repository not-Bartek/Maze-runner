import time
import gc

class DFS:
    def color_square(self, canvas, x, y):
        canvas.create_rectangle(20*x, 20*y, 20*(x+1), 20*(y+1), fill="#a7bdff")

    def calculate(self, maze, root, canvas):
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
                    canvas.update()
                    time.sleep(0.001)

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