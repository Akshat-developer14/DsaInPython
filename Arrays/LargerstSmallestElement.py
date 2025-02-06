# Find the Largest and Smallest Elements in an Array: Write a function that returns the largest and smallest elements from an array.

def find_largest_and_smallest_element(arr):
    if not arr:
        return None, None
    
    largest = arr[0] # at start it will be 1
    smallest = arr[0] # at start it will also be 1
    
    for num in arr: # python for loop which runs until arr complete and select each element in num
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num

    return largest, smallest


array = [95, 995, 590, 926, 856, 78, 98 ,52 , 46 , 256, 88, 95]

largest, smallest = find_largest_and_smallest_element(array)

print(f'{largest} is the largest number and {smallest} is the smallest number in the array')