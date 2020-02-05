from closest_pair_algorithms.brute_force import brute_force_all
from utils import euclidean_distance as d


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
        for point2 in Sy[i + 1: i + 8]:
            current_dist = d(point1, point2)
            if current_dist < best:
                best_pair = point1, point2
                best = current_dist
    return best_pair[0], best_pair[1], best
