from collections import defaultdict

class Graph:
    def __init__(self,index):
        self.graph = defaultdict(list)
        for col,t in index.items():
            for i in range(len(t)):
                for j in range(i + 1, len(t)):
                    self.add_edge(t[i], t[j], col)
    def add_edge(self,t1,t2,col):
        self.graph[t1].append((t2,col))
        self.graph[t2].append((t1,col))
    def display(self):
        for table, neighbors in self.graph.items():
            print(f"{table} -> {[(n, c) for n, c in neighbors]}")
    def find_join_path(self, tables):
        # 存储已访问的表
        visited = set()
        def dfs(current_table, target_tables, path):
            if visited >= target_tables:
                return path
            # 遍历当前表的邻居
            for neighbor,primary_key in self.graph.get(current_table, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    new_path = path + [(current_table, neighbor, primary_key)]
                    # 如果目标表都已经访问过，返回当前路径
                    result = dfs(neighbor, target_tables, new_path)
                    if result:
                        return result
                    visited.remove(neighbor)
            return None
        # 从任意一个表开始遍历
        for start_table in tables:
            visited.add(start_table)
            result = dfs(start_table, tables, [])
            if result:
                return result
            visited.remove(start_table)
        return None  # 如果找不到有效路径，返回 None