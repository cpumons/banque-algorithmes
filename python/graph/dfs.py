from adjacency_list import AdjacencyList

def dfs_tree(graph, start):
	"""
	Return the the traversel tree of a DFS run from the node `start`
	in the graph `graph`
	"""
	tree = AdjacencyList()
	visited = {start}
	def dfs_tree_rec(node):
		for succ in graph[node]:
			if succ not in visited:
				visited.add(succ)
				tree.add_edge(node, succ)
				dfs_tree_rec(succ)
	dfs_tree_rec(start)
	return tree

if __name__ == '__main__':
	graph = AdjacencyList()
	graph.add_edges([(0, 1), (1, 2), (0, 2)])
	tree = dfs_tree(graph, 0)
	print(tree.adj)