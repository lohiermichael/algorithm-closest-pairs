from closet_pairs_algorithms import divide_to_conquer
from closet_pairs_algorithms import brute_force_points
from inputs import InputListPointsXY as Points
from utils import euclidean_distance as d
import random


def closest_split_pair(p_x, p_y, delta, best_pair):  # <- a parameter
    ln_x = len(p_x)
    mx_x = p_x[ln_x // 2][0]
    s_y = [x for x in p_y if mx_x - delta <= x[0] <= mx_x + delta]
    best = delta
    for i in range(len(s_y) - 1):
        for j in range(1, min(i + 7, (len(s_y) - i))):
            p, q = s_y[i], s_y[i + j]
            dst = d(p, q)
            if dst < best:
                best_pair = p, q
                best = dst
    return best_pair


def closestPair(Px, Py):
    if len(Px) <= 3:
        return brute_force_points(Px)
    mid = len(Px) // 2
    # get left and right half of Px
    q, r = Px[:mid], Px[mid:]
    # sorted versions of q and r by their x and y coordinates
    Qx, Qy = [x for x in q if Py and x[0] <= Px[-1][0]], [x for x in q if x[1] <= Py[-1][1]]
    Rx, Ry = [x for x in r if Py and x[0] <= Px[-1][0]], [x for x in r if x[1] <= Py[-1][1]]
    (p1, q1) = closestPair(Qx, Qy)
    (p2, q2) = closestPair(Rx, Ry)
    dist = min(d(p1, p2), d(p2, q2))
    mn = min((p1, q1), (p2, q2), key=lambda x: d(x[0], x[1]))
    (p3, q3) = closest_split_pair(Px, Py, dist, mn)
    return min(mn, (p3, q3), key=lambda x: d(x[0], x[1]))


if __name__ == "__main__":
    nb_pbs = 0
    for i in range(10000):
        P = Points(l_length=10)
        Px = sorted(P, key=lambda x: x[0])
        Py = sorted(P, key=lambda x: x[1])
        p1, p2 = closestPair(Px, Py)
        pp1, pp2 = brute_force_points(P)
        if d(p1, p2) != d(pp1, pp2):
            nb_pbs += 1
    print(nb_pbs)
