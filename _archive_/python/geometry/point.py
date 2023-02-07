import math

class Point:
	def __init__(self, x, y):
		self.x, self.y = x, y
	
	def norm(self):
		return math.sqrt(self.x * self.x + self.y * self.y)
	
	def distance(self, p):
		return Point(self.x - p.x, self.y - p.y).norm()
	
	def dot(self, p):
		return self.x * p.x + self.y * p.y