import argparse
from bubble_sort import bubble_sort
from quick_sort import quick_sort
from merge_sort import merge_sort

def parse_arguments():
    """
    Parse command line arguments.

    :return: The parsed arguments.
    """
    parser = argparse.ArgumentParser(description='Sort an array of integers using a specified algorithm.')
    parser.add_argument('algorithm', type=str, choices=['bubble', 'quick', 'merge'], help='The sorting algorithm to use.')
    parser.add_argument('data', type=int, nargs='+', help='The array of integers to sort.')
    return parser.parse_args()

def main():
    """
    The main entry point of the application.
    """
    args = parse_arguments()
    data = args.data
    algorithm = args.algorithm

    if algorithm == 'bubble':
        sorted_data = bubble_sort(data)
    elif algorithm == 'quick':
        sorted_data = quick_sort(data)
    else:  # algorithm == 'merge'
        sorted_data = merge_sort(data)

    print(f'Sorted data: {sorted_data}')

if __name__ == '__main__':
    main()
