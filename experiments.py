import random
from sort import Sort

# maximum value to be generated in a list
MAX_VAL = 65536

# construct a random list of size n
def random_list(n):
    lst = []
    for i in range(n):
       lst.append(random.randint(0, MAX_VAL))
    return lst

# construct an almost sorted list of size n
def almost_sorted_list(n):
    # first get a random list of size n
    lst = random_list(n)

    # use Python's built-in list sorting algorithm
    lst.sort()

    # move one quarter of the elements out of
    # place by between 1 and 5 places
    for i in range(n // 8):
        j = random.randint(0, n - 1)
        displace = -5 + random.randint(0, 10)
        k = j + displace;
        if k < 0:
            k = 0;
        elif k > n - 1:
            k = n - 1
 
        temp = lst[j]
        lst[j] = lst[k]
        lst[k] = temp

    return lst

if __name__ == "__main__":
    sort = Sort()

    # sort a random list of length 1000
    # print("testing mystery sort on a random list")
    # lst = random_list(1000) 
    # sort.mystery_sort(lst)
    # comps = sort.get_comps()
    # moves = sort.get_moves()
    # print("  comps: %s; moves: %s" % (str(comps), str(moves)))
    # sort.reset_stats()

    # # sort an almost-sorted list of length 1000
    # print("testing mystery sort on an almost sorted list")
    # lst = almost_sorted_list(1000)
    # sort.mystery_sort(lst)
    # comps = sort.get_comps()
    # moves = sort.get_moves()
    # print("  comps: %s; moves: %s" % (str(comps), str(moves)))
    # sort.reset_stats()

    # sort a random list of length 1000
    print("testing mystery sort on a random list")
    lst = random_list(1000) 
    sort.mystery_sort(lst)
    comps = sort.get_comps()
    moves = sort.get_moves()
    print(Sort.get_max_num_digits(lst))
    print(sort.radix_sort(lst))
    print("  comps: %s; moves: %s" % (str(comps), str(moves)))
    sort.reset_stats()