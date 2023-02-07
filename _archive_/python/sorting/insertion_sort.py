def insertion_sort(l):
	for i in range(1, len(l)):
		temp = l[i]
		j = i
		while j > 0 and temp < l[j-1]:
			l[j] = l[j-1]
			j -= 1
		l[j] = temp
	return l