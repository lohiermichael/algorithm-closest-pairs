from utils import euclidean_distance as d


def brute_force_all(input_points):
    point_min1, point_min2, min_distance = 0, 1, d(input_points[0], input_points[1])
    for i, point1 in enumerate(input_points):
        for j, point2 in enumerate(input_points[i + 1:], i + 1):
            if d(point1, point2) < min_distance:
                point_min1, point_min2, min_distance = input_points[i], input_points[j], d(point1, point2)
    return point_min1, point_min2, min_distance


def brute_force_points(input_points):
    point_min1, point_min2, min_distance = input_points[0], input_points[1], d(
        input_points[0], input_points[1])
    for i, point1 in enumerate(input_points):
        for j, point2 in enumerate(input_points[i + 1:], i + 1):
            if d(point1, point2) < min_distance:
                point_min1, point_min2, min_distance = input_points[i], input_points[j], d(
                    point1, point2)
    return point_min1, point_min2


def brute_force_dist(input_points):
    min_distance = d(input_points[0], input_points[1])
    for i, point1 in enumerate(input_points):
        for point2 in input_points[i + 1:]:
            if d(point1, point2) < min_distance:
                min_distance = d(point1, point2)
    return min_distance
