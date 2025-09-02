# Maze Runner
Maze Runner is a simple application that graphically visualizes BFS (Breadth-First Search) and DFS (Depth-First Search) algorithms. You can also reset the canvas to its initial state. Additionally, the size of the maze and the size of individual squares within it can be customized.

## How to Use
### Running the Program
To run the program, execute the `main.py` file using Python:
```bash
python main.py
```

## Required Libraries
If you are using Python's standard library, no additional libraries are required as the graphical interface is implemented using `tkinter`, which is included by default. Ensure you have Python installed on your system.

### Controls
- **D**: Visualize the DFS algorithm.
- **B**: Visualize the BFS algorithm.
- **R**: Reset the canvas to its initial state.

### Customization
- **Maze Size**: Change the size of the maze by modifying the `MAZE_WIDTH` and `MAZE_HEIGHT` variables in the `main.py` file.
- **Square Size**: Adjust the size of each square in the maze by changing the `CELL_SIZE` variable in the `config.py` file.



## Implementation

The project is implemented in Python. It uses a grid-based system to represent the maze. The BFS and DFS algorithms are visualized step-by-step, and player interactions are handled through keyboard events. The rendering of the maze and animations is done using a simple graphical library.

Enjoy exploring and learning about maze-solving algorithms!