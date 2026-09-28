import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	# Your code here
	mag = 0#L2
	for g in gradient:
		mag += g * g
	mag = mag ** 0.5
	if mag == 0.0:
		direc = [0.0 for g in gradient]
		des_direc = []
	else:
		direc = [x / mag for x in gradient]
		des_direc = [-1*x for x in direc]

	return {
		"magnitude": mag,
		"direction": direc,
		"descent_direction": des_direc
	}