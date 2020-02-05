from inputs import InputListPointsXY as Points
from closest_pair_algorithms.brute_force import brute_force_all
from closest_pair_algorithms.divide_to_conquer import divide_to_conquer
from ast import literal_eval
import matplotlib.pyplot as plt


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
            with open('error_input.txt', 'w') as f:
                f.write(str(P))
            is_err = True
            print('Error list saved in "error_input.txt"')


def test_saved_err_list(algorithm=divide_to_conquer):
    with open('error_input.txt', 'r') as f:
        P = literal_eval(f.read())
    return P, algorithm(P)


if __name__ == "__main__":
    print(f'There is {count_percentage_err(algorithm=divide_to_conquer)} % of error on {str(divide_to_conquer.__name__)}')
