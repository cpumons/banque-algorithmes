def bubble_sort(l):
	permutation = True
	passage = 0
	while permutation == True:
		permutation = False
		passage = passage + 1
		for en_cours in range(0, len(l) - passage):
			if l[en_cours] > l[en_cours + 1]:
				permutation = True
				# On echange les deux elements
				l[en_cours], l[en_cours + 1] = \
				l[en_cours + 1],l[en_cours]
	return l