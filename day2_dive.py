"""
forward 5
down 5
forward 8
up 3
down 8
forward 2

Your horizontal position and depth both start at 0. The steps above would then modify them as follows:

    forward 5 adds 5 to your horizontal position, a total of 5.
    down 5 adds 5 to your depth, resulting in a value of 5.
    forward 8 adds 8 to your horizontal position, a total of 13.
    up 3 decreases your depth by 3, resulting in a value of 2.
    down 8 adds 8 to your depth, resulting in a value of 10.
    forward 2 adds 2 to your horizontal position, a total of 15.

After following these instructions,
you would have a horizontal position of 15 and a depth of 10.
(Multiplying these together produces 150.)
Calculate the horizontal position and depth
you would have after following the planned course.
What do you get if you multiply your final horizontal position by your final depth?
"""

TEST_INPUT_ARRAY = '''forward 5
down 5
forward 8
up 3
down 8
forward 2'''.split('\n')

INPUT_ARRAY = open('day2_input_2.txt', 'r').read().split('\n')


class Command:
    FORWARD = 'forward'
    DOWN = 'down'
    UP = 'up'


def get_position(input_array):
    """
    Calculate the position based on the input array of commands and values.
    :param input_array:
    :return: x, y
    """
    # initial position
    x, y = (0, 0)
    for item in input_array:
        command, value = item.split(' ')
        value = int(value.strip())
        if command == Command.FORWARD:
            x += value
        elif command == Command.DOWN:
            y += value
        elif command == Command.UP:
            y -= value
    return x, y


def get_position_2(input_array):
    """
    In addition to horizontal position and depth,
    you'll also need to track a third value, aim, which also starts at 0.
    The commands also mean something entirely different than you first thought:
    - down X increases your aim by X units.
    - up X decreases your aim by X units.
    - forward X does two things:
        * It increases your horizontal position by X units.
        * It increases your depth by your aim multiplied by X.
    :param input_array:
    :return: x, y
    """
    # initial position
    x, y = (0, 0)
    aim = 0
    for item in input_array:
        command, value = item.split(' ')
        value = int(value.strip())
        if command == Command.FORWARD:
            x += value
            y += aim*value
        elif command == Command.DOWN:
            aim += value
        elif command == Command.UP:
            aim -= value
    return x, y


if __name__ == '__main__':
    # part 1
    # first run the verify with test input.
    assert get_position(TEST_INPUT_ARRAY) == (15, 10)
    # run with the actual input and print the desire result.
    x, y = get_position(INPUT_ARRAY)
    print("Answer to part 1: {}".format(x*y))
    # part 2
    # first run the verify with test input.
    assert get_position_2(TEST_INPUT_ARRAY) == (15, 60)
    x, y = get_position_2(INPUT_ARRAY)
    print("Answer to part 2: {}".format(x * y))
