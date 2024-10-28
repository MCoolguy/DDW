
# Python Code
numbers = [16, 14, 10, 8, 7, 8, 3, 2, 4, 1] #length of 10


def bubblesort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

print(bubblesort(numbers))


def bubblesortv1(lst):
    n = len(lst)
    for i in range(1,n-1):
        for j in range (1,n-1):
            first_number = lst[j-1]
            second_number = lst[j]
            if first_number > second_number:
                lst[first_number], lst[second_number] = lst[second_number],lst[first_number]
    return lst

print(bubblesortv1(numbers))

def bubblesortv2(lst):
    n = len(lst)
    swapped = True
    while swapped == True:
        swapped = False
        for i in range (1,n-1):
            first_number = lst[i-1]
            second_number = lst[i]
            if first_number > second_number:
                lst[first_number], lst[second_number] = lst[second_number],lst[first_number]
                swapped = True
    return lst

def bubblesortv3(lst):
    n = len(lst)
    swapped = True
    while swapped == True:
        swapped = False
        for i in range (1,n-1):
            first_number = lst[i-1]
            second_number = lst[i]
            if first_number > second_number:
                lst[first_number], lst[second_number] = lst[second_number],lst[first_number]
                swapped = True
        n = n-1
    return lst

def bubblesortv4(lst):
    n = len(lst)
    swapped = True
    while swapped == True:
        swapped = False
        new_n = 0
        for i in range (1,n-1):
            first_number = lst[i-1]
            second_number = lst[i]
            if first_number > second_number:
                lst[first_number], lst[second_number] = lst[second_number],lst[first_number]
                swapped = True
                new_n = i
        n = n-1
    return lst