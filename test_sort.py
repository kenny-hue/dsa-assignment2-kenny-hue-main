import unittest
from sort import Sort

class TestSort(unittest.TestCase):
    def test_get_max_num_digits(self):
        lst = [55, 101, 1111, 5, 999]
        assert Sort.get_max_num_digits(lst) == 4

    def test_list_to_buckets(self):
        sort = Sort()
        lst = [5, 8, 1234, 1, 18, 0, 19, 111]
        buckets = sort.list_to_buckets(lst)
        assert buckets == [ [0], [1, 111], [], [], [1234], [5], [], [], [8, 18], [19] ]
        assert sort.moves == len(lst)

    def test_buckets_to_list(self):
        sort = Sort()
        buckets = [ [3, 5, 9], [25], [], [40], [51, 53], [], [], [88], [91] ]
        lst = sort.buckets_to_list(buckets)
        assert lst == [3, 5, 9, 25, 40, 51, 53, 88, 91]

    def test_radix_sort(self):
        sort = Sort()
        lst = [5, 8, 123, 1, 18, 0, 19, 71]
        sorted_lst = sort.radix_sort(lst)
        assert sorted_lst == [0, 1, 5, 8, 18, 19, 71, 123]
