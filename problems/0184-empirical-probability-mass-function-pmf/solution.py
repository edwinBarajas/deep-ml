def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    # TODO: Implement the function
    counts = {}
    n = len(samples)
    for sample in samples:
        if sample in counts:
            counts[sample] += 1
        else:
            counts[sample] = 1

    cs = []
    for key in counts:
        value = counts[key]
        cs.append((key, value/n))
    return cs