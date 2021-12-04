"""
This input indicates that, scanning outward from the submarine, the sonar
sweep found depths of 199, 200, 208, 210, and so on.

The first order of business is to figure out how quickly the depth increases,
just so you know what you're dealing with - you never know if the keys will get carried
into deeper water by an ocean current or a fish or something.

To do this, count the number of times a depth measurement
increases from the previous measurement.
"""

f = open('day1_input_1.txt', 'r')
input_array = [int(item) for item in f.read().split('\n')]


def find_number_of_increases(input_data):
    """
    Returns number of times a depth measurement
    in input list increases.
    :param input_data:
    :return: number_of_increases
    """
    number_of_increases = 0
    for idx, item in enumerate(input_data):
        if idx != 0:
            if item > input_data[idx - 1]:
                number_of_increases += 1
    return number_of_increases


def find_number_of_window_increases(input_data, window_size=3):
    """
    Count the number of times the window total
    increases from previous window.
    :param input_data:
    :param window_size:
    :return: number_of_window_increases
    """
    number_of_window_increases = 0
    window_totals = []
    input_size = len(input_data)
    for idx, item in enumerate(input_data):
        if idx + window_size <= input_size:
            total = 0
            for i in range(window_size):
                total += input_data[idx+i]
            window_totals.append(total)
            if idx > 0:
                if window_totals[idx] > window_totals[idx - 1]:
                    number_of_window_increases += 1
    return number_of_window_increases


if __name__ == '__main__':
    # run the first version of the function.
    # answer is 1527.
    print(find_number_of_increases(input_array))
    # generalised function that takes in window size.
    # pass in test input.
    assert find_number_of_window_increases([199, 200, 208, 210, 200, 207, 240, 269, 260, 263]) == 5
    # pass window_size=1, output should match find_number_of_increases function.
    assert find_number_of_window_increases(input_array, window_size=1) == 1527
    # pass whole input to the generalised function.
    # answer is 1575.
    print(find_number_of_window_increases(input_array))
