def dice_statistics(n: int) -> tuple[float, float]:
	"""
	Compute the expected value and variance of a fair n-sided die roll.

	Args:
		n (int): Number of sides of the die

	Returns:
		tuple: (expected_value, variance)
	"""
	# Your code here
	n_pos = n

	pos = [x for x in range(1, n+1)]
	ex = 0
	ex2 = 0
	for num in pos:
		ex += num/n_pos
		ex2 += (num*num)/n_pos
	
	var = ex2 - (ex * ex)
	
	return [ex, var]