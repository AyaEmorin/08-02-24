def insertion_sort(d):
    for i in range(1, len(d)):
        t = d[i]
        j = i - 1
        while j >= 0 and less_than(t, d[j]):
            d[j + 1] = d[j]
            j -= 1
        d[j + 1] = t

def less_than(a, b):
    # Assuming a and b are comparable objects (e.g., Integers)
    return a < b

def print_array(array):
    print(" ".join(map(str, array)))

if __name__ == "__main__":
    # Example array of Integers
    array = [5, 2, 8, 1, 3]

    # Print the array before sorting
    print("Before sorting:")
    print_array(array)

    # Call the insertion_sort method to sort the array
    insertion_sort(array)

    # Print the array after sorting
    print("After sorting:")
    print_array(array)
