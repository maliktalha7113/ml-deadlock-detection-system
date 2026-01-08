class DeadlockDetector:
    def __init__(self, processes, resources):
        self.processes = processes
        self.resources = resources

    def build_wait_for_graph(self):
        graph = {}

        for p in self.processes:
            if p.state == "Waiting":
                for r in self.resources:
                    if r.rid == p.requested_resource and r.allocated_to:
                        graph.setdefault(p.pid, []).append(r.allocated_to)

        return graph

    def detect_deadlock(self):
        graph = self.build_wait_for_graph()
        visited = set()
        stack = set()

        def dfs(node):
            if node in stack:
                return True
            if node in visited:
                return False

            visited.add(node)
            stack.add(node)

            for neighbour in graph.get(node, []):
                if dfs(neighbour):
                    return True

            stack.remove(node)
            return False

        for node in graph:
            if dfs(node):
                return True

        return False
