class AdjacencyList(dict):
	def add_node(self, node):
		if node not in self:
			self[node] = {}
	
	def add_nodes(self, nodes):
		for node in nodes:
			self.add_node(node)
	
	def add_edge(self, node1, node2, **attributes):
		self.add_node(node1)
		self.add_node(node2)
		self[node1][node2] = attributes
	
	def add_edges(self, edges):
		for edge in edges:
			attributes = {} if len(edge) <= 2 else edge[2]
			self.add_edge(edge[0], edge[1], **attributes)
	
	def nodes(self):
		return self.keys()
	
	def data(self, node, attribute):
		return [(succ, attrs[attribute]) for succ, attrs in self[node].items()]

if __name__ == '__main__':
	g = AdjacencyList()
	g.add_edge(1, 2, weight=5)
	g.add_edges([(1, 2), (1, 3, {'weight': 2})])
	print(g)