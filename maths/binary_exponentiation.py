"""Binary Exponentiation."""

# Author : Junth Basnet
# Time Complexity : O(logn)


def binary_exponentiation(a: int, n: int) -> int:
    """
    >>> binary_exponentiation(3, 5)
    243
    >>> binary_exponentiation(10, 3)
    1000
    """
    if n == 0:
        return 1

    elif n % 2 == 1:
        return binary_exponentiation(a, n - 1) * a

    else:
        b = binary_exponentiation(a, n // 2)
        return b * b


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    try:
        BASE = int(input("Enter Base : ").strip())
        POWER = int(input("Enter Power : ").strip())
    except ValueError:
        print("Invalid literal for integer")

    RESULT = binary_exponentiation(BASE, POWER)
    print(f"{BASE}^({POWER}) : {RESULT}")
