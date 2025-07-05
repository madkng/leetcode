# Number of Islands: BFS and DFS Solutions Explained

This document provides a detailed explanation of two classic approaches—**Breadth-First Search (BFS)** and **Depth-First Search (DFS)**—to solve the "Number of Islands" problem.

---

## Problem Statement

Given an `m x n` 2D binary grid representing a map of `'1'`s (land) and `'0'`s (water), return the number of islands.  
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.  
You may assume all four edges of the grid are surrounded by water.

---

## Approach 1: Breadth-First Search (BFS)

### How BFS Works

BFS explores the grid level by level, starting from a land cell (`'1'`) and visiting all its adjacent land cells before moving deeper. It uses a queue to keep track of the cells to visit next.

### Steps

1. **Initialization**:
    - Check if the grid is empty.
    - Initialize a `visited` set to keep track of visited cells.
    - Initialize `island_count` to zero.

2. **BFS Traversal**:
    - For each cell in the grid:
        - If the cell is land (`'1'`) and not visited:
            - Start a BFS from this cell.
            - Mark all reachable land cells as visited (these form one island).
            - Increment `island_count`.

3. **BFS Helper Function**:
    - Use a queue to process cells.
    - For each cell dequeued, check its four neighbors (up, down, left, right).
    - If a neighbor is land and not visited, add it to the queue and mark as visited.

### Code Snippet

```python
def numIslands_bfs(grid: List[List[str]]) -> int:
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    visited = set()
    island_count = 0

    def bfs(ridx, cidx):
        q = collections.deque()
        visited.add((ridx, cidx))
        q.append((ridx, cidx))
        while q:
            row, col = q.popleft()
            directions = [[1, 0], [-1, 0], [0,1], [0,-1]]
            for dridx, dcidx in directions:
                r, c = row + dridx, col + dcidx
                if (r in range(rows) and c in range(cols) and
                    grid[r][c] == "1" and (r, c) not in visited):
                    q.append((r, c))
                    visited.add((r, c))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                bfs(r, c)
                island_count += 1
    return island_count
```

### Pros and Cons

- **Pros**: Avoids stack overflow, good for wide/deep islands.
- **Cons**: Slightly more memory usage due to the queue.

---

## Approach 2: Depth-First Search (DFS)

### How DFS Works

DFS explores as far as possible along each branch before backtracking. It can be implemented recursively or with a stack. Here, recursion is used.

### Steps

1. **Initialization**:
    - Check if the grid is empty.
    - Initialize a `visited` set.
    - Initialize `island_count` to zero.

2. **DFS Traversal**:
    - For each cell in the grid:
        - If the cell is land (`'1'`) and not visited:
            - Start a DFS from this cell.
            - Mark all reachable land cells as visited (these form one island).
            - Increment `island_count`.

3. **DFS Helper Function**:
    - For the current cell, recursively visit all four neighbors (up, down, left, right) if they are land and not visited.

### Code Snippet

```python
def numIslands_dfs(grid: List[List[str]]) -> int:
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    visited = set()
    island_count = 0

    def dfs(ridx, cidx):
        if (ridx < 0 or ridx >= rows or
            cidx < 0 or cidx >= cols or
            grid[ridx][cidx] != "1" or
            (ridx, cidx) in visited):
            return
        visited.add((ridx, cidx))
        dfs(ridx + 1, cidx)
        dfs(ridx - 1, cidx)
        dfs(ridx, cidx + 1)
        dfs(ridx, cidx - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                dfs(r, c)
                island_count += 1
    return island_count
```

### Pros and Cons

- **Pros**: Simple and elegant, easy to implement.
- **Cons**: Risk of stack overflow for very large grids/islands due to recursion depth.

---

## Key Points

- Both BFS and DFS mark all cells of an island as visited to avoid counting them again.
- The main difference is in the order of traversal: BFS uses a queue (level-order), DFS uses recursion (depth-first).
- Both approaches have the same time complexity: **O(m × n)**, where `m` is the number of rows and `n` is the number of columns.

---

## Example

Given the grid:

```
[
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
```

Both BFS and DFS will return `3` as there are three distinct islands.

---

## Conclusion

Both BFS and DFS are effective for solving the "Number of Islands" problem, with their own advantages and considerations. Choose based on the specific requirements and constraints of your application, such as grid size and available memory.
