import heapq as hp


def return_adj_lis(nodes_available, connected_nodes):
    adj_arr = [[]for j in range(nodes_available+1)]
    for i in connected_nodes:
        if i[0] != i[1]:
            adj_arr[i[0]].append([i[2], i[1]])
            adj_arr[i[1]].append([i[2], i[0]])
    return adj_arr


def return_min_cost_of_MST(adj_arr):
    traversed_nodes = {1}
    cost = 0
    min_hp = []
    hp.heapify(min_hp)
    for i in adj_arr[1]:
        hp.heappush(min_hp, i)
    while min_hp:
        result = hp.heappop(min_hp)
        if result[1] not in traversed_nodes:
            traversed_nodes.add(result[1])
            cost += result[0]
            for i in adj_arr[result[1]]:
                if i[1] not in traversed_nodes:
                    hp.heappush(min_hp, i)
    return cost


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        adj_arr = return_adj_lis(A, B)
        return return_min_cost_of_MST(adj_arr)
