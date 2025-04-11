from collections import defaultdict, deque


class Graph:
    def __init__(self):
        self.graph = {}



    # Exemplo de uso
if __name__ == "__main__":

    A = [[0, 1],[1, 3], [0, 2], [2,3], [1, 2]]
    M = []

    D = defaultdict(list)

    print(D)

    for u, v in A:
        D[u].append(v)

    print("------------------------")

    print(D)

   
    #DFS RECURSIVE ----------------
    # def dfs_recursive(node):
    #     print(node)
    #     for nei_node in D[node]:
    #         if nei_node not in seen:
    #             seen.add(nei_node)
    #             dfs_recursive(nei_node)


    
    # source = 0
    # seen = set()
    # seen.add(source)
    # dfs_recursive(source)



    #DFS WITH STACK ----------------
    # source = 0
    # seen = set()
    # seen.add(source)
    # stack = [source]


    # while stack:
    #     node = stack.pop()
    #     print("popped node", node)
    #     for nei_node in D[node]:
    #         if nei_node not in seen:
    #             seen.add(nei_node)
    #             stack.append(nei_node)







    



    


        

