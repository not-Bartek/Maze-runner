from collections import deque
from Maze import Maze

Maze = Maze()

class BFS:
    def calculate(self, maze, actual):
        visited = [[False for _ in range(maze.width)] for _ in range(maze.height)]
        parents = {}
        queue = deque()
        queue.append(actual)

        x, y = actual
        visited[y][x] = True
        parents = {}
        i=0
        while queue:
            print(f" -=-=-= {i} =-=-=-= ")
            actual = queue.popleft()
            x, y = actual
            print(actual)
            #dodanie możliwych dzieci

            childs = []
            directions = [(0,1), (0,-1), (1,0), (-1,0)]
            for dx, dy in directions:
                print((x+dx,y+dy))
                if maze.maze[y+dy][x+dx] != 1:
                    childs.append((x+dx,y+dy))

            for child in childs:
                print('child: ')
                print(child)
                cx, cy = child
                if not visited[cy][cx]:

                    parents[child] = cx - x, cy - y


                    #dodanie rodziców danych węzłów
                    visited[cy][cx] = True
                    queue.append(child)
                    if maze.end == child:
                        print("zwróć ścieżke")
                        new_x, new_y = child
                        route = []
                        while (new_x, new_y) != maze.start:
                            dx, dy = parents[(new_x,new_y)]
                            new_x, new_y = new_x - dx, new_y - dy
                            if (new_x, new_y) != maze.start:
                                route.append((new_x, new_y))
                        return route
            print(list(queue))
            i+=1
        print("brak ścieżki")   

