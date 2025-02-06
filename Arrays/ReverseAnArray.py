#  Reverse an Array: Write a function to reverse the elements of an array in place.


def reverse_array(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr


array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f'{array} this is orignal array and after reversing it becomes {reverse_array(array)}')
