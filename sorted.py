def insertion_sort_descending(d):
    for i in range(1, len(d)):
        t = d[i]
        j = i - 1
        while j >= 0 and greater_than(t, d[j]):
            d[j + 1] = d[j]
            j -= 1
        d[j + 1] = t

def greater_than(a, b):
    return a > b

def print_array(array):
    print(" ".join(map(str, array)))

if __name__ == "__main__":
   
    score = input("Enter elements separated by space: ")
    
    array = list(map(int, score.split()))

    print("Before sorting:")
    print_array(array)

    insertion_sort_descending(array)

    print("After sorting in descending order:")
    print_array(array)
