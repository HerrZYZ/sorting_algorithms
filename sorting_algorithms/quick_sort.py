def quick_sort(arr: list) -> list:
    """
    Implement the Quick Sort algorithm.

    :param arr: The array to be sorted.
    :return: The sorted array.
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
