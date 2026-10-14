def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:

	means = []
	if (mode == "column"):
		collen = len(matrix)
		length = len(matrix[0])
		for i in range(length):
			su = 0
			for j in range(len(matrix)):
				su += matrix[j][i]
		
			means.append(su / collen)


	else:
		for row in matrix:
			length = len(row)
			s = 0
			for n in row:
				s+= n
			means.append(s / length)


	return means