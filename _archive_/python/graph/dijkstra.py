from adjacency_list import AdjacencyList
import heapq
import math

def dijkstra_distances(graph, start):
	"""
	Return the minimum distance from `start` to each node
	in the positively weighted graph `graph`
	"""
	distances = {node: math.inf for node in graph.nodes()}
	distances[start] = 0
	visited = set()
	heap = [(0, start)]
	while heap:
		cost, node = heapq.heappop(heap)
		if node in visited:
			continue		
		visited.add(node)
		for succ, weight in graph.data(node, 'weight'):
			new_dist = cost + weight
			if new_dist < distances[succ]:
				distances[succ] = new_dist
				heapq.heappush(heap, (new_dist, succ))
	return distances

if __name__ == '__main__':
	graph = AdjacencyList()
	graph.add_edge(0, 1, weight=1)
	graph.add_edge(1, 2, weight=2)
	graph.add_edge(0, 2, weight=4)
	print(dijkstra_distances(graph, 0))