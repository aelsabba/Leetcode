from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(set)
        email_to_user = {}
        for account in accounts:
            for email in account[1:]:
                graph[email].add(account[1])
                graph[account[1]].add(email)
                email_to_user[email] = account[0]

        visited = set()
        results = []
        for node in graph:
            if node not in visited:
                stack = [node]
                visited.add(node)
                group = []
                while len(stack) > 0:
                    neighbor = stack.pop()
                    group.append(neighbor)
                    for neighbor in graph[neighbor]:
                        if neighbor not in visited:
                            stack.append(neighbor)
                            visited.add(neighbor)

                results.append([email_to_user[node]] + sorted(group))
        return results
