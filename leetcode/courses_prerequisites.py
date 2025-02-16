from collections import defaultdict
from collections import deque


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not prerequisites:
            return True

        graph = defaultdict(lambda: {"in": set(), "out": set()})
        for course, prereq in prerequisites:
            graph[course]["in"].add(prereq)
            graph[prereq]["out"].add(course)

        frontier = deque([])

        for node in range(numCourses):
            if len(graph[node]["in"]) == 0:
                frontier.append(node)

        visited = set()

        while len(frontier) > 0:
            node = frontier.popleft()
            visited.add(node)
            for neighbor in graph[node]["out"]:
                if neighbor not in visited:
                    can_visit_neighbor = True
                    for neighbor_prereqs in graph[neighbor]["in"]:
                        if neighbor_prereqs not in visited:
                            can_visit_neighbor = False
                    if can_visit_neighbor:
                        frontier.append(neighbor)

        return len(visited) >= numCourses