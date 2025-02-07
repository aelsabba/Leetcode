class Solution:
    def __init__(self):
        self.map = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        solutions = []
        local_solution = []

        def dfs():
            if len(local_solution) == len(digits):
                solutions.append("".join(local_solution))
                return

            index = len(local_solution)
            current_digit = digits[index]

            for letter in self.map[current_digit]:
                local_solution.append(letter)
                dfs()
                local_solution.pop()

        dfs()
        return solutions