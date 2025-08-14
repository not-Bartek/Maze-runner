import random

class Maze:
    def __init__(self, width=10, height=10):
        if(width % 2 == 0):
            width += 1
        if(height % 2 == 0):
            height += 1
        self.width = width
        self.height = height
        self.maze = [[1 for _ in range(width)] for _ in range(height)]
        
       
        self.start = None
        self.end = None
        self._generate()

    def _generate(self):
        self.start = (2* random.randint(1, self.width//2) - 1, 2 * random.randint(1, self.height//2) - 1)
        x,y = self.start

        self.maze[y][x] = 0
        self._carve(x, y)

        self.maze[y][x] = 2
        
        while True:
            point = (2* random.randint(1, self.width//2) - 1, 2 * random.randint(1, self.height//2) - 1)
            ex, ey = point
            if self.maze[ey][ex] == 0 and (ex != x or ex):
                self.maze[ey][ex] = 3
                self.end = (ex, ey)
                break



    def _carve(self, x, y):
        stack = [(x, y)]
        while stack:
            cx, cy = stack.pop()
            directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
            random.shuffle(directions)
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 1 <= nx < self.width-1 and 1 <= ny < self.height-1:
                    if self.maze[ny][nx] == 1:
                        self.maze[ny-dy//2][nx-dx//2] = 0
                        self.maze[ny][nx] = 0
                        stack.append((nx, ny))


    def print(self):
        chars = {0: ' ', 1: '#', 2: 'S', 3: 'E'}
        for row in self.maze:
            print(''.join(chars.get(cell, '?') for cell in row))

    