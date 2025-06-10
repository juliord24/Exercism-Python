def square(number):
    """Calculate the number of grains on a specific square of a chessboard.

    :param number: int - the square number (1 to 64).
    :return: int - number of grains on the given square.
    :raises ValueError: if number is not between 1 and 64.
    """
    if number < 1 or number > 64: 
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)


def total():
    """
    Calculate the total number of grains on a chessboard.

    :return: int - total number of grains on all 64 squares.
    """
    return 2 ** 64 - 1
