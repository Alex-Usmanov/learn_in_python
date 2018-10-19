def binarySearch(sortedList: list, search: int):
    """
    Searchs for an integer given in arguments and returns it's index. If an element wasn't found, returns None. Uses binary search algorithm.
    NEEDS A SORTED LIST!!!
    """
    ceiling = len(sortedList) -1
    mid = 0
    bottom = 0

    # Iterate until there is 1 element
    while bottom <= ceiling:
        mid = round((bottom + ceiling) / 2)

        print("Mid >> {}".format(mid))

        midValue = sortedList[mid]
        print("Midvalue >> ", midValue)

        if midValue == search:
            return mid

        elif midValue < search:
            bottom = mid+1

        else:
            ceiling = mid-1

    return None
