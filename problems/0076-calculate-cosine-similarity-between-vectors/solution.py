import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here
	if (v1.shape != v2.shape): pass

	dot_p = v1.dot(v2)

	l2_v1 = np.sqrt(np.sum(np.power(v1, 2)))
	l2_v2 = np.sqrt(np.sum(np.power(v2, 2)))

	return dot_p / (l2_v1 * l2_v2)
	