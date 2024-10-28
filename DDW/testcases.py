from test2.py import heapsort

def test_heapsort():
    # Test case 1: Sorting an already sorted array
    array = [1, 2, 3, 4, 5]
    heapsort(array)
    assert array == [1, 2, 3, 4, 5]

    # Test case 2: Sorting a reverse sorted array
    array = [5, 4, 3, 2, 1]
    heapsort(array)
    assert array == [1, 2, 3, 4, 5]

    # Test case 3: Sorting an array with duplicate elements
    array = [4, 1, 3, 2, 4, 1]
    heapsort(array)
    assert array == [1, 1, 2, 3, 4, 4]

    # Test case 4: Sorting an array with negative elements
    array = [3, -1, 2, -5, 4]
    heapsort(array)
    assert array == [-5, -1, 2, 3, 4]

    # Test case 5: Sorting an empty array
    array = []
    heapsort(array)
    assert array == []

    # Test case 6: Sorting an array with one element
    array = [1]
    heapsort(array)
    assert array == [1]

    # Test case 7: Sorting an array with all identical elements
    array = [2, 2, 2, 2, 2]
    heapsort(array)
    assert array == [2, 2, 2, 2, 2]

test_heapsort()