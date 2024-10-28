def min_heap(arr, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left

    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        min_heap(arr, n, smallest)

def build_min_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        min_heap(arr, n, i)

def heapsort(arr):
    n = len(arr)
    build_min_heap(arr)
    sorted_arr = []
    for i in range(n):
        arr[0], arr[n - 1 - i] = arr[n - 1 - i], arr[0]
        sorted_arr.append(arr.pop())
        min_heap(arr, n - 1 - i, 0)
    return sorted_arr

# Example usage
if __name__ == "__main__":
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_arr = heapsort(arr)
    print("Sorted array is:", sorted_arr)