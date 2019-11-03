# 狄克斯特拉算法演示，计算带权重的DAG最少消耗cost的路径

# graph用来描述原始图
graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['a'] =3
graph['b']['fin'] = 5
graph['fin'] = {}

# costs用来记录经过计算的开销
infinity = float("inf")
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

# parents用来记录父节点，散列表，更新此散列表用来记录更新过costs的对应路径
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

# processed用来记录处理过的节点
processed = []

def find_lowest_cost_node(costs):
    lowest_cost = infinity
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

# 在未处理的节点中找出开销最小的节点
node = find_lowest_cost_node(costs)
# 此while循环在所有节点都被处理过后结束
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    # 遍历当前所有邻居
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        # 如果经当前节点前往该邻居最近
        if costs[n] > new_cost:
            # 就更新该邻居的开销
            costs[n] = new_cost
            # 同时将该邻居的父节点设置为当前节点
            parents[n] = node
    # 将当前节点标记为处理过
    processed.append(node)
    # 找出接下来要处理的节点，并循环
    node = find_lowest_cost_node(costs)

print(graph)
print(costs)
print(parents)
