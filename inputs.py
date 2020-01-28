import random
import matplotlib.pyplot as plt


class InputList(list):
    def __init__(self, l_length: int = 100, min_value: int = 0, max_value: int = 10000, distinct_elements: bool = True):
        """
        Object of input list for algorithms
        Parameters
        ----------
        l_length (int): Length of the input list
        min_value (int): Minimal value of the elements of the list
        max_value (int): Maximal value of the elements of the list
        distinct_elements (bool): distinct elements in the list
        """
        self.l_length = l_length
        self.min_value = min_value
        self.max_value = max_value
        self.distinct_elements = distinct_elements
        self._construct()

    def _find_element_not_in_set(self, already_used: set) -> int:
        """
        This function returns an element not present in a set
        Parameters
        ----------
        already_used (set): a set of int

        Returns
        -------
        int: int not in set
        """
        new_element = random.randint(a=self.min_value, b=self.max_value)
        while new_element in already_used:
            new_element = random.randint(a=self.min_value, b=self.max_value)
        return new_element

    def _construct(self):
        """
        This function will build the object by append elements to the initial empty list
        Returns
        -------
        """
        if self.distinct_elements:
            assert self.l_length <= self.max_value - self.min_value + 1, "The range of values chosen " \
                                                                         "doesn't allow to have distinct values"
            already_used = set()
            for index in range(self.l_length):
                # Find an element not present in already_used
                new_element = self._find_element_not_in_set(already_used)
                # Add the element to already used
                already_used.add(new_element)
                # Add the element to the list
                self.append(new_element)
        else:
            for index in range(self.l_length):
                self.append(random.randint(a=self.min_value, b=self.max_value))


class InputListPairs(list):
    def __init__(self, l_length: int = 100, min_value: int = 0, max_value: int = 10000, distinct_elements: bool = True):
        """
        Object of list of pairs of points of the graph
        Parameters
        ----------
        l_length (int): Number of pairs (points of the graph
        min_value (int): Minimum value of the x and y axes
        max_value (int): Maximum value of the x and y axes
        distinct_elements (bool): whether the points have distinct values of both x and y
        """
        self.l_length = l_length
        self.min_value = min_value
        self.max_value = max_value
        self.distinct_elements = distinct_elements
        self._construct()

    def _construct(self):
        """
        This function will build the object by append elements to the initial empty list
        Returns
        -------
        fig_
        """
        x_values = InputList(l_length=self.l_length,
                             min_value=self.min_value,
                             max_value=self.max_value,
                             distinct_elements=self.distinct_elements)
        y_values = InputList(l_length=self.l_length,
                             min_value=self.min_value,
                             max_value=self.max_value,
                             distinct_elements=self.distinct_elements)

        for x, y in zip(x_values, y_values):
            self.append((x, y))

    def plot(self) -> None:
        """
        Function to plot the points on a graph
        Returns
        -------
        fig, ax
        """
        fig, ax = plt.subplots()
        fig.set_size_inches(18.5, 10.5)

        ax.scatter(*zip(*self))
        for i, pair  in enumerate(self):
            ax.annotate(i, (pair[0], pair[1]),fontsize=15)
        plt.show()
        return fig, ax 
        
    def plot_line_between(self, i, j) -> None:
        """
        Function that plot a line between to pairs of points of interest
        Parameters
        ----------
        i(int): pair numbered i of the list
        j(int): pair numbered j of the list
        
        Returns
        -------
        

        """
        fig, ax = self.plot()
        ax.plot(self[i], self[j])
        plt.show()