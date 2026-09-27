def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	if len(b) != len(a[0]):
		return -1

	c = [0 for _ in a]

	for i in range(len(c)):
		dp = 0
		for j in range(len(a[i])):
			dp += a[i][j] * b[j]
		c[i] = dp
	
	return c