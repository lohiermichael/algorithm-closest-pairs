# algorithmic-closest-pairs

This exercise follows the idea of improvement of algorithm thanks to the **Divide to Conquer paradigm**.

This is an application of the notions developed in the following videos by Tim Roughgarden:
1. [On log n Algorithm for Closest Pair I Advanced](https://www.youtube.com/watch?v=3pUOv_ocJyA&list=PLXFMmlk03Dt7Q0xr1PIAriY5623cKiH7V&index=18)
2. [On log n Algorithm for Closest Pair II Advanced](https://www.youtube.com/watch?v=7tiafUFrlBw&list=PLXFMmlk03Dt7Q0xr1PIAriY5623cKiH7V&index=18)

# Introduction to the problem

This problem is an important problem of computational geometry. This type of algorithms are used in fields like **robotic**, **computer vision**, or **computer graphics**.

## Inputs

Given n points in the plan: 
```P = {p1, ..., pn}```
```For i in [1, n] pi(xi, yi)```

## Goal

we want to figure out which pair of point are closest to each other.
i.e. Find pi and pj so that 
```d(pi, pj) = sqrt((xi-xj)**2 + (yi-yj)**2)```
is minimal

## Assumption

All pi points have distinct x coordinates
All pi points have distinct y coordinates

# Solutions

## Brute force approach

You iterates over all pairs of points. The complexity is in O(n2)

## Divide to conquer

### Observation

Given n points having only x-coordinate, the way to go would be:
1. Sort the points by their coordinate **O(n*log(n))**
2. Scan through the points and keep the minimum distance between two adjacent points in the sorted list **(O(n))**

The algorithm will have an overall complexity of O(n*log(n)).

The objective is to keep the same complexity in 2-dimensions.

### Steps

*Note:*

For a list of points Points sorted by :
    * x-coordinate: Points_x
    * y-coordinate: Points_y
As we couldn't do best than O(n log(n)), any sort of list of size k*n is "for free"

Given P
1. Form Px and Py  **O(n*log(n))**

**DIVIDE**

*ClosetPair(Px,Py)*
2. Make the split <br>
Let Q = left half of P<br> 
Let R = right half of  P<br>  **O(n*log(n))**

3. Form Qx, Qy, Rx, Ry  **O(n*log(n))**

**CONQUER**

4. (p1, q1) = ClosetPair(Qx, Qy)
5. (p2, q2) = ClosetPair(Rx, Ry)

**COMBINE**

6. Let delta = min {d(p1, q1), d(p2, q2)}
In the lucky cases, the closest pair either lays on the right or on the left half of P. But if it is split, we need **delta**: <br>
(p3, q3) = ClosestPair(Px, Py, delta)

7. Let x_m = biggest x-coordinate in left of P  **O(1)** <br>
We can get it from Px









