#LeetCode 2658 Number of Fish

validMotions = [(1,0),(-1,0),(0,1),(0,-1)]
class Solution:
    def findMaxFishHelper(self,visited,grid,cell,numberOfFish):
        if (cell[0] >= len(grid) or
                        cell[0] < 0 or
                            cell[1] >= len(grid[0]) or
                             cell[1] < 0):
            return numberOfFish
        elif visited[cell[0]][cell[1]] == 1:
            return numberOfFish
        elif grid[cell[0]][cell[1]] == 0:
            visited[cell[0]][cell[1]] = 1
            return numberOfFish
        else:
            visited[cell[0]][cell[1]] = 1
            numberOfFish += grid[cell[0]][cell[1]]
            for move in validMotions:
                numberOfFish = self.findMaxFishHelper(visited,grid,(cell[0] + move[0], cell[1] + move[1]),
                                            numberOfFish)
            return numberOfFish

    def findMaxFish(self, grid: List[List[int]]) -> int:
        visited = [[0] * len(grid[0]) for _ in range(len(grid))]
        maxFish = 0
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if visited[row][column] == 0:
                    potentialMaxFish = self.findMaxFishHelper(visited,grid,(row,column),0)
                    if potentialMaxFish > maxFish:
                        maxFish = potentialMaxFish
        return maxFish