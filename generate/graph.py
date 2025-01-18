from collections import defaultdict

class Graph:
    def __init__(self,index):
        self.graph = defaultdict(list)
        for col,l in index.items():
            for i in range(len(l)):
                for j in range(i + 1, len(l)):
                    self.add_edge(l[i], l[j], col)
    def add_edge(self,t1,t2,col):
        self.graph[t1].append((t2,col))
        self.graph[t2].append((t1,col))
    def find_join_path(self, tables):
        visited = set()
        def dfs(current_table, target_tables, path):
            if visited >= target_tables:
                return path
            for neighbor,primary_key in self.graph.get(current_table, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    new_path = path + [(current_table, neighbor, primary_key)]
                    result = dfs(neighbor, target_tables, new_path)
                    if result:
                        return result
                    visited.remove(neighbor)
            return None
        
        for start_table in tables:
            visited.add(start_table)
            result = dfs(start_table, tables, [])
            if result:
                return result
            visited.remove(start_table)
        return None  