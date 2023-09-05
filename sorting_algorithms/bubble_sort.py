def bubble_sort(arr: list) -> list:
    """
    Implement the Bubble Sort algorithm.

    :param arr: The array to be sorted.
    :return: The sorted array.
    """
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr
