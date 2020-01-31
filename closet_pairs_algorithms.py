from utils import euclidean_distance as d
from inputs import InputListPointsXY as Points
from ast import literal_eval
import matplotlib.pyplot as plt


def brute_force_all(input_points):
    point_min1, point_min2, min_distance = 0, 1, d(input_points[0], input_points[1])
    for i, point1 in enumerate(input_points):
        for j, point2 in enumerate(input_points[i + 1:], i + 1):
            if d(point1, point2) < min_distance:
                point_min1, point_min2, min_distance = i, j, d(point1, point2)
    return point_min1, point_min2, min_distance


def brute_force_points(input_points):
    point_min1, point_min2, min_distance = input_points[0], input_points[1], d(input_points[0], input_points[1])
    for i, point1 in enumerate(input_points):
        for j, point2 in enumerate(input_points[i + 1:], i + 1):
            if d(point1, point2) < min_distance:
                point_min1, point_min2, min_distance = input_points[i], input_points[j], d(point1, point2)
    return point_min1, point_min2


def brute_force_dist(input_points):
    min_distance = d(input_points[0], input_points[1])
    for i, point1 in enumerate(input_points):
        for point2 in input_points[i + 1:]:
            if d(point1, point2) < min_distance:
                min_distance = d(point1, point2)
    return min_distance


def pre_process(P):
    Px = sorted(P, key=lambda x: x[0])
    Py = sorted(P, key=lambda x: x[1])
    return Px, Py


def divide_to_conquer(P):
    Px, Py = pre_process(P)
    return closest_pair(Px, Py)


def closest_pair(Px, Py):
    if len(Px) <= 3:
        return brute_force_points(Px)
    mid = len(Px) // 2
    Q, R = Px[:mid], Px[mid:]
    Qx, Qy = pre_process(Q)
    Rx, Ry = pre_process(R)
    (p1, q1) = closest_pair(Qx, Qy)
    (p2, q2) = closest_pair(Rx, Ry)
    min_d = min(d(p1, p2), d(p2, q2))
    mn = min((p1, q1), (p2, q2), key=lambda x: d(x[0], x[1]))
    (p3, q3) = closest_split_pair(Px, Py, min_d, mn)
    return min(mn, (p3, q3), key=lambda x: d(x[0], x[1]))


def closest_split_pair(Px, Py, delta, best_pair):
    xm = Px[len(Px) // 2][0]
    Sy = [x for x in Py if xm - delta <= x[0] <= xm + delta]
    best = delta
    for i, point1 in enumerate(Sy):
        for point2 in Sy[i+1: i+8]:
            dist = d(point1, point2)
            if dist < best:
                best_pair = point1, point2
                best = dist
    return best_pair


if __name__ == "__main__":
    with open('input.txt', 'r') as input_file:
        P = literal_eval(input_file.read())
    print(divide_to_conquer(P))
    print(brute_force_points(P))
