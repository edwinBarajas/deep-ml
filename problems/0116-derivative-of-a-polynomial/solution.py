def poly_term_derivative(c: float, x: float, n: float) -> float:
    # Your code here
    der = n * c * (x ** (n-1))
    return f'{der}'