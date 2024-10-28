def insertionsortv1(array):
    n = len(array)
    for outer_index in range (1,n):
        inner_index = outer_index
        while inner_index > 0 and array[inner_index] < array[inner_index-1]:
            array[inner_index-1], array[inner_index] = array[inner_index], array[inner_index-1]
            inner_index = inner_index -1
    return array
        
        
# Python Code
numbers = [16, 14, 10, 8, 7, 8, 3, 2, 4, 1]

print(insertionsortv1(numbers))

def insertionsortv2(array):
    n = len(array)
    for outer_index in range (1,n):
        inner_index = outer_index
        temporary = array[inner_index]
        while inner_index > 0 and temporary < array[inner_index-1]:
            array[inner_index] = array[inner_index-1]
            inner_index = inner_index-1
        array[inner_index] = temporary
    return array

print(insertionsortv2(numbers))


