from collections import deque
import gc
import time
class BFS:
    def color_square(self, canvas, x, y):
        canvas.create_rectangle(20*x, 20*y, 20*(x+1), 20*(y+1), fill="#f6ccff")

    def calculate(self, maze, actual, canvas):
        gc.collect()
        visited = [[False for _ in range(maze.width)] for _ in range(maze.height)]
        parents = {}
        queue = deque()
        queue.append(actual)

        x, y = actual
        visited[y][x] = True
        while queue:
            actual = queue.popleft()
            x, y = actual

            if(actual != maze.start and actual != maze.end):
                self.color_square(canvas, x, y)
                canvas.update()
                time.sleep(0.001)

            childs = []
            directions = [(0,1), (0,-1), (1,0), (-1,0)]
            for dx, dy in directions:
                if maze.maze[y+dy][x+dx] != 1:
                    childs.append((x+dx,y+dy))

            for child in childs:
                cx, cy = child
                if not visited[cy][cx]:

                    parents[child] = cx - x, cy - y


                    #dodanie rodziców danych węzłów
                    visited[cy][cx] = True
                    queue.append(child)
                    if maze.end == child:
                        new_x, new_y = child
                        route = []
                        while (new_x, new_y) != maze.start:
                            dx, dy = parents[(new_x,new_y)]
                            new_x, new_y = new_x - dx, new_y - dy
                            if (new_x, new_y) != maze.start:
                                route.append((new_x, new_y))
                        del queue
                        del visited
                        del parents
                        gc.collect()
                        return route
        print("brak ścieżki")   

