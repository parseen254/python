import random


class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def is_in_unit_circle(self) -> bool:
        """
        True, if the point lies in the unit circle
        False, otherwise
        """
        return (self.x ** 2 + self.y ** 2) <= 1

    @classmethod
    def random_unit_square(cls):
        """
        Generates a point randomly drawn from the unit square [0, 1) x [0, 1).
        """
        return cls(x=random.random(), y=random.random())


def estimate_pi(number_of_simulations: int) -> float:
    """
    Generates an estimate of the mathematical constant PI.
    See https://en.wikipedia.org/wiki/Monte_Carlo_method#Overview

    The estimate is generated by Monte Carlo simulations. Let U be uniformly drawn from
    the unit square [0, 1) x [0, 1). The probability that U lies in the unit circle is:

        P[U in unit circle] = 1/4 PI

    and therefore

        PI = 4 * P[U in unit circle]

    We can get an estimate of the probability P[U in unit circle].
    See https://en.wikipedia.org/wiki/Empirical_probability by:

        1. Draw a point uniformly from the unit square.
        2. Repeat the first step n times and count the number of points in the unit
            circle, which is called m.
        3. An estimate of P[U in unit circle] is m/n
    """
    if number_of_simulations < 1:
        raise ValueError("At least one simulation is necessary to estimate PI.")

    number_in_unit_circle = 0
    for simulation_index in range(number_of_simulations):
        random_point = Point.random_unit_square()

        if random_point.is_in_unit_circle():
            number_in_unit_circle += 1

    return 4 * number_in_unit_circle / number_of_simulations


if __name__ == "__main__":
    # import doctest

    # doctest.testmod()
    from math import pi

    prompt = "Please enter the desired number of Monte Carlo simulations: "
    my_pi = estimate_pi(int(input(prompt).strip()))
    print(f"An estimate of PI is {my_pi} with an error of {abs(my_pi - pi)}")
