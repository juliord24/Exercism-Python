EXPECTED_BAKE_TIME = 40  # in minutes



def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

    

def preparation_time_in_minutes(layers: int) -> int:
    """Calculate the preparation time in minutes.

    :param layers: int - number of layers in the lasagna.
    :return: int - preparation time (in minutes) derived from 'layers'.

    Function that takes the number of layers in the lasagna as an argument
    and returns how many minutes it took to prepare the lasagna based on
    a constant preparation time per layer.
    """
    return layers * 2 



def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """Calculate the total preparation time in minutes.
    
    :param number_of_layers: int - number of layers in the lasagna.
    :param elapsed_bake_time: int - number of minutes the lasagna has been baking in the oven
    :return: int - total number of minutes you have been cooking.
    
    Function that takes the number of layers in the lasagna and the elapsed baking time
    as arguments and returns the total time spent cooking the lasagna, which is the sum of
    the preparation time and the elapsed baking time.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time