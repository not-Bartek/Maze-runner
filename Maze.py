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
        self.start = (2* random.randint(1, width//2) - 1, 2 * random.randint(1, height//2) - 1)
        x, y = self.start
        self.maze[y][x] = 2
        self.end = None
        
    
    def print(self):
        chars = {0: ' ', 1: '#', 2: 'S', 3: 'E'}
        for row in self.maze:
            print(''.join(chars.get(cell, '?') for cell in row))

    