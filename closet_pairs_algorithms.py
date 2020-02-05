from time import sleep
from utils import euclidean_distance as d
from inputs import InputListPointsXY as Points
from ast import literal_eval
import matplotlib.pyplot as plt

def brute_force_all(input_points):
    point_min1, point_min2, min_distance = 0, 1, d(
        input_points[0], input_points[1])
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


def divide_to_conquer(P):
    Px = sorted(P, key=lambda x: x[0])
    Py = sorted(P, key=lambda x: x[1])
    return closest_pair(Px, Py)


def closest_pair(Px, Py):
    # Call the brute force algorithm for the terminal case
    if len(Px) <= 3:
        return brute_force_all(Px)
    mid = len(Px) // 2
    # Split in function of the x-axis
    Qx = Px[:mid]
    Rx = Px[mid:]
    # Determine midpoint on x-axis
    midpoint = Px[mid][0]
    Qy = list()
    Ry = list()
    for x in Py:  # split ay into 2 arrays using midpoint
        if x[0] <= midpoint:
            Qy.append(x)
        else:
            Ry.append(x)
    # The syntax looks is more brief but it might take long as we pass through Py twice
    # Qyp = list(filter(lambda point: point[0] <= midpoint, Py))
    # Ryp = list(filter(lambda point: point[0] > midpoint, Py))
    (p1, q1, mi1) = closest_pair(Qx, Qy)
    (p2, q2, mi2) = closest_pair(Rx, Ry)
    # Save the pair with distance between left and right
    best_pair_dist = min((p1, q1, mi1), (p2, q2, mi2), key=lambda res: res[2])
    (p3, q3, mi3) = closest_split_pair(Px, Py, best_pair_dist)
    return min(best_pair_dist, (p3, q3, mi3), key=lambda res: res[2])


def closest_split_pair(Px, Py, pair_dist):
    best_pair = pair_dist[0], pair_dist[1]
    delta = pair_dist[2]
    xm = Px[len(Px) // 2][0]
    Sy = [x for x in Py if xm - delta <= x[0] <= xm + delta]
    best = delta
    for i, point1 in enumerate(Sy):
        for point2 in Sy[i+1: i+8]:
            dist = d(point1, point2)
            if dist < best:
                best_pair = point1, point2
                best = dist
    return best_pair[0], best_pair[1], best


def count_percentage_err(algorithm=divide_to_conquer, nb_tests: int = 1000, l_length: int = 10):
    bad = 0
    for i in range(nb_tests):
        P = Points(l_length=l_length)
        p1, q1, d1 = algorithm(P)
        p2, q2, d2 = brute_force_all(P)
        if d1 != d2:
            bad += 1
    return round(bad / nb_tests * 100, 3)


def save_err_points(algorithm=divide_to_conquer, l_length: int = 100):
    is_err = False
    while not is_err:
        P = Points(l_length=l_length)
        p1, q1, d1 = algorithm(P)
        p2, q2, d2 = brute_force_all(P)
        if d(p1, q1) != d(p2, q2):
            with open('input.txt', 'w') as f:
                f.write(str(P))
            is_err = True
            print('Error list saved in "input.txt"')


def test_saved_err_list(algorithm=divide_to_conquer):
    with open('input.txt', 'r') as f:
        P = literal_eval(f.read())
    return P, algorithm(P)


if __name__ == "__main__":
    P = Points(l_length=10)
    p, q, dist = divide_to_conquer(P)
    print(p, q)
    P.plot_line_between(p,q, annotate=True)
    plt.show()

