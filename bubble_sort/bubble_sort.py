def bubble_sort(unsorted_list):
    n = len(unsorted_list)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if unsorted_list[j] > unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
                swapped = True
        if not swapped:
            break
    return unsorted_list

if __name__ == "__main__":
    sample_list = [64, 34, 25, 12, 22, 11, 90]
    sorted_list = bubble_sort(sample_list)
    print("Sorted list:", sorted_list)
