from collections import deque


def return_adj_lis(nodes_available, connected_nodes, B):
    adj_arr = [[]for j in range(nodes_available+1)]
    for i in range(len(connected_nodes)):
        adj_arr[connected_nodes[i][0]].append(connected_nodes[i][1])
        adj_arr[connected_nodes[i][1]].append(connected_nodes[i][0])
    return adj_arr


def BFS(adj_arr, traversed_nodes, curr_node, B):
    cost = 0
    q = deque([])
    for i in adj_arr[curr_node]:
        q.append(i)
    cost += B[curr_node-1]
    while q:
        result = q.popleft()
        if result not in traversed_nodes:
            traversed_nodes.add(result)
            cost += B[result-1]
            for i in adj_arr[result]:
                if i not in traversed_nodes:
                    q.append(i)
    return cost


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B, C, D):
        adj_arr = return_adj_lis(A, C, B)
        ans = 0
        traversed_nodes = {0}
        for i in range(1, A+1):
            if i not in traversed_nodes:
                traversed_nodes.add(i)
                strength = BFS(adj_arr, traversed_nodes, i, B)
                if strength >= D:
                    ans += 1
        return ans
