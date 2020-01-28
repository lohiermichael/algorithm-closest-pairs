
def euclidean_distance(a, b):
    """
    Perform the Euclidean distance between two points in the plan
    Args:
        a: First point
        b: Second point

    Returns:
        The distance between the two points

    """

    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** (1 / 2)
