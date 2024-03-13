class Sort:
    def __init__(self):
        self.reset_stats()

    def reset_stats(self):
        self.comps = 0
        self.moves = 0

    def get_comps(self):
        return self.comps

    def get_moves(self):
        return self.moves

    def compare(self, comparison):
        self.comps += 1
        return comparison

    def swap(self, lst, i, j):
        temp = lst[i]
        lst[i] = lst[j]
        lst[j] = temp
        self.moves += 3

    #
    # Task 1
    #

    def mystery_sort(self, lst):
        for i in range(len(lst) - 1, 0, -1):
            for j in range(len(lst) - 1, len(lst) - 1 - i, -1):
                if self.compare(lst[j] < lst[j - 1]):
                    self.swap(lst, j, j - 1)

    #
    # Task 2
    #

    # returns the nth digit of num,
    # where digit 0 is the least significant digit
    # e.g.: digit(1234, 0) -> 4
    def digit(self, num, n):
        return int(num // 10 ** n % 10)

    # returns a list of buckets of order radix
    # e.g.: get_new_buckets(10) will return a
    # 2D list of 10 empty lists: [ [], [], [], ... ]
    @staticmethod
    def get_new_buckets(radix):
        buckets = []
        for i in range(radix):
            buckets.append([])
        return buckets

    # get the maximum number of digits
    # among any number in the input list
    def get_max_num_digits(self, lst):
        # Task 2, Step 1
        max_digits = 0
        for num in lst:
            num_digits = 1
            while num >= 10:
                num //= 10
                num_digits += 1
            if num_digits > max_digits:
                max_digits = num_digits
        return max_digits

    # converts a list of numbers to a list
    # of buckets, with entries sorted by
    # their least significant digit
    def list_to_buckets(self, lst):
        # Task 2, Step 2
        buckets = self.get_new_buckets(10)
        for num in lst:
            digit_val = self.digit(num, 0)  # Check if 'num' is correctly an integer
            buckets[digit_val].append(num)
            self.moves += 1  # Increment moves counter for each appended element
        return buckets

    # converts a list of buckets
    # into a one-dimensional list
    def buckets_to_list(self, buckets):
        # Task 2, Step 3
        lst = []
        for bucket in buckets:
            lst.extend(bucket)
        return lst

    # sort a list of numbers by distributing
    # them to buckets according to their digits
    def radix_sort(self, lst):
        # Task 2, Step 4
        max_digits = self.get_max_num_digits(lst)
        
        for digit_place in range(max_digits):
            buckets = self.list_to_buckets(lst)  # Remove the second argument
            lst = self.buckets_to_list(buckets)
        
        return lst  # Return the sorted list
