def merge(array: list, p: int, q: int, r: int) -> None:
    # Create left and right subarrays
    left = array[p:q+1]
    right = array[q+1:r+1]

    # Initialize pointers for left (i), right (j), and merged array (k)
    i = j = 0
    k = p

    # Merge the temp arrays back into the original array
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    # Copy the remaining elements of left, if any
    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    # Copy the remaining elements of right, if any
    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1

def mergesort_recursive(array: list, p: int, r: int) -> None:
    if p < r:
        q = (p + r) // 2
        mergesort_recursive(array, p, q)
        mergesort_recursive(array, q + 1, r)
        merge(array, p, q, r)

def mergesort(array: list) -> None:
    if array:
        mergesort_recursive(array, 0, len(array) - 1)
        
        
list = [5, 2, 4, 7, 1, 3, 2, 6]
mergesort(list)
print(list)