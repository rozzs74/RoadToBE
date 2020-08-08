# base start of inseration is alwasy 2
def insertion_sort(list_a):
    indexing_length = range(1, len(list_a))
    for i in indexing_length:
        value_to_sort = list_a[i]
        print(f"v={value_to_sort} l={list_a[i-1]} l={list_a[i]}")
        # In need > 0 as python allowed negative indexing
        while list_a[i-1] > value_to_sort and i > 0:
            list_a[i], list_a[i-1] = list_a[i-1], list_a[i] # switch
            i = i -1 # continue comparison
    return list_a

a = [5, 2, 4, 6, 1, 3]
insertion_sort(a)
print(a)
# https://www.youtube.com/watch?v=byHi41L9vTM