class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        indexes_to_remove = set()
        stack = []
        for iterator, character in enumerate(s):
            if character == "(":
                stack.append(iterator)
            elif character == ")" and len(stack) == 0:
                indexes_to_remove.add(iterator)
            elif character == ")":
                stack.pop()

        indexes_to_remove = indexes_to_remove.union(set(stack))

        character_array = []
        for iterator, character in enumerate(s):
            if not iterator in indexes_to_remove:
                character_array.append(character)

        return "".join(character_array)

