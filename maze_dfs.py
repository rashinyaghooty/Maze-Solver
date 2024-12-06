from collections import deque
import tkinter as tk

def dfs(maze, start, goal):
    stack = [(start, [start])]
    visited = set()
    visited.add(start)

    while stack:
        (x, y), path = stack.pop()
        if (x, y) == goal:
            return path

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            i, j = x + dx, y + dy
            if 0 <= i < len(maze) and 0 <= j < len(maze[0]) and maze[i][j] == 0 and (i, j) not in visited:
                visited.add((i, j))
                stack.append(((i, j), path + [(i, j)]))

    return None

def create_maze():
    return [
    [0, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 1],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0]
    ]

#def print_maze(maze, path):
 #   for i, row in enumerate(maze):
  #      for j, cell in enumerate(row):
   #         if (i, j) in path:
    #            print("P", end=" ")
     #       else:
      #          print("." if cell == 0 else "#", end=" ")
       # print()

def draw_maze(canvas, maze, path):
    cell_size = 50
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            color = 'white' if cell == 0 else 'black'
            canvas.create_rectangle(j * cell_size, i * cell_size, (j + 1) * cell_size, (i + 1) * cell_size, fill=color,
                                    outline='black')

        if path:
            for (i, j) in path:
                canvas.create_rectangle(j * cell_size, i * cell_size, (j + 1) * cell_size, (i + 1) * cell_size,
                                        fill='blue')


def main():
    maze = create_maze()
    start = (0, 0)
    goal = (5, 3)
    test = dfs(maze, start, goal)
    if test:
        print("Path found:", test)
    else:
        print("No path found")

    root = tk.Tk()
    root.title("Maze Solver")
    canvas = tk.Canvas(root, width=len(maze) * 50, height=len(maze[0]) * 50)
    canvas.pack()

    draw_maze(canvas, maze, test)

    root.mainloop()

main()