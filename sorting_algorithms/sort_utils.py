## sort_utils.py

def swap(arr: list, i: int, j: int) -> None:
    """
    Swap two elements in an array.

    :param arr: The array.
    :param i: The index of the first element.
    :param j: The index of the second element.
    """
    arr[i], arr[j] = arr[j], arr[i]


def partition(arr: list, low: int, high: int) -> int:
    """
    Partition an array around a pivot element.

    :param arr: The array.
    :param low: The lower bound of the partition.
    :param high: The upper bound of the partition.
    :return: The index of the pivot element.
    """
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            swap(arr, i, j)

    swap(arr, i + 1, high)
    return i + 1
