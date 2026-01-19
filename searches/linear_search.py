from __future__ import print_function
"""
Linear Search Algorithm

Linear search is a simple searching technique that checks each element
of a list one by one until the target element is found or the list ends.

Input:
- arr (list): A list of elements to search through
- target: The element to be searched for in the list

Output:
- int: The index of the target element if found
- -1: If the target element is not present in the list
"""
"""
This is pure python implementation of linear search algorithm

For doctests run following command:
python -m doctest -v linear_search.py
or
python3 -m doctest -v linear_search.py

For manual testing run:
python linear_search.py
"""
try:
    raw_input          # Python 2
except NameError:
    raw_input = input  # Python 3

def linear_search(sequence, target):
    """Pure implementation of linear search algorithm in Python

    :param sequence: some sorted collection with comparable items
    :param target: item value to search
    :return: index of found item or None if item is not found

    Examples:
    >>> linear_search([0, 5, 7, 10, 15], 0)
    0

    >>> linear_search([0, 5, 7, 10, 15], 15)
    4

    >>> linear_search([0, 5, 7, 10, 15], 5)
    1

    >>> linear_search([0, 5, 7, 10, 15], 6)

    """
    for index, item in enumerate(sequence):
        if item == target:
            return index
    return None


if __name__ == '__main__':
    user_input = raw_input('Enter numbers separated by comma:\n').strip()
    sequence = [int(item) for item in user_input.split(',')]

    target_input = raw_input('Enter a single number to be found in the list:\n')
    target = int(target_input)
    result = linear_search(sequence, target)
    if result is not None:
        print('{} found at positions: {}'.format(target, result))
    else:
        print('Not found')