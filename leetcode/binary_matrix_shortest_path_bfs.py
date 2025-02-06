from collections import deque
import math
class Solution:
    def bfs_path_search(self, grid, position):
        directions = [
        (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        visited = set()
        moves = deque([(position[0],position[1],1)])
        while len(moves) > 0:
            position = moves.popleft()
            if (position[0], position[1]) == (len(grid) -1 , len(grid) - 1):
                return position[2]
            if grid[position[0]][position[1]] == 0:
                for row, col in directions:
                    new_pos = (position[0] + row, position[1] + col, position[2] + 1)
                    if (0 <= new_pos[0] < len(grid) and
                        0 <= new_pos[1] < len(grid) and
                        grid[new_pos[0]][new_pos[1]] == 0 and
                        not (new_pos[0], new_pos[1]) in visited):
                            visited.add((new_pos[0], new_pos[1]))
                            moves.append(new_pos)

        return -1


    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        position = (0,0)
        visited = set()
        if grid[len(grid) - 1][len(grid) - 1] == 1:
            return -1
        if len(grid) == 1:
            return 1
        length = self.bfs_path_search(grid, position)
        return length