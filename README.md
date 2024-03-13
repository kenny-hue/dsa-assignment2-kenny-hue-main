# Sorting Analysis

In this assignment, you will derive the time complexity of sorting algorithms *empirically* -- by running multiple trials of the algorithms and measuring the number of comparisons and moves. From those measurements, you will then conduct a quantitative analysis of the running time of the algorithms.

## Your Task

You have two high-level tasks:

Task 1 will consist of generating lists of various sizes and sorting them using an unnamed sorting algorithm to find the number of comparisons and moves that are performed. You will then infer the time efficiency of the algorithm based on how the number of comparisons and moves change as the size of the list changes.

Task 2 will consist of implementing radix sort and also evaluating its running time empircally.

## Starter Code

You are given the file `sort.py`, which includes the implementation of an unnamed sorting algorithm, `mystery_sort()`. It is in a Python class called `Sort`, which has two fields: `comps` and `moves`. These variables track the number of comparisons and moves made by the sorting algorithm, respectively. On creating an instance of the `Sort` class, `comps` and `moves` are initialized to zero.

`mystery_sort()` uses the `compare()` method to compare two elements of a list while incrementing the `comps` field. For example, instead of:

```python
if lst[j] < lst[j - 1]:
```

The method instead uses:

```python
if self.compare(lst[j] < lst[j - 1]):
```

This method returns the result of the comparison (either `True` or `False`), and increments the count of comparisons that the class maintains. The `swap()` method has also been modified to increment the `moves` field by three, since each swap consists of three moves of data in memory.

You are also given `experiments.py`, in which you will write all of the code to perform your experiments to count the operations of the algorithms. It contains a few important pieces:

- A `random_list()` function that generates a random integer list of length `n`.
- An `almost_sorted_list()` function that generates an integer list of length `n` that is almost sorted. *You do not need to understand how this function works.*
- Code in the main part of the script that generates random and almost-sorted lists, sorts them, and reports the number of comparisons and moves for each.

Finally, you are given `analysis.md`. This is a plain-text file that you will fill with your experimental results. You should open it with a text editor (such as VS Code), add your results and analysis to it, and submit it along with your source code.

## General Guidelines

* You may only use programming concepts and constructs covered in this course and previous Kibo courses. In particular, you may not use built-in library functions that have not been discussed.
* Use the unit tests after completing each task. Note: unit tests for tasks not you have not yet completed will fail.
* You don't need to write a program to fill in the results for `analysis.md` automatically. You can just manually edit the file to add the experimental results and analysis.

## Steps to Complete

### Task 1: Derive the time complexity of a sorting algorithm

Your first task is to write code to experimentally find the time complexity of a sorting algorithm for random lists and almost-sorted lists.

1. Modify the code in `experiments.py` to test how many comparisons and moves `mystery_sort()` makes on *random* lists of various lengths. You should run the algorithm on lists of at least three different sizes (e.g., 1000, 2000, and 4000). Record the number of comparisons and moves for each trial in `analysis.md`.

    Be sure to do the following before each call to the `mystery_sort()` function:
      - Generate a new list. You don't want to pass the list you just sorted back to the algorithm.
      - Call the `reset_stats()` method of the `Sort` object to reset the comparisons and moves to zero. If you don't, the number of comparisons and moves will continue to increment for each invocation of the algorithm.

2. Modify the code in `experiments.py` to test how many comparisons and moves `mystery_sort()` makes on *almost sorted* lists of various sizes. The same guidelines as (1) apply here. Record the number of comparisons and moves for each trial in `analysis.md`.

3. Using the experimental data, calculate the big-O time complexity for `mystery_sort()`. For both types of input (random lists and almost sorted lists), show the time complexity for moves, the time complexity for comparisons, and the overall time complexity.

### Task 2: Implement radix sort

Radix sort is a non-comparative sorting algorithm that repeatedly distributes values into buckets in order to sort them. When sorting numbers, radix sort starts by assigning the numbers of the input list to buckets that are indexed by the least significant digit (the ones digit) of the numbers:

![A list of numbers transitioning into the first pass of radix sort, where the numbers are bucketed according to their ones digit.](/images/assignment-2-radix-1.svg)

Once the ordering of the numbers by their least significant digit is complete, the algorithm performs another iteration where it distributes the numbers by their *next* significant digit (the tens digit):

![The second iteration of radix sort, in which the numbers are placed into buckets according to their tens digit.](/images/assignment-2-radix-2.svg)

Single digit numbers have a tens digit of 0, so they are all placed in bucket `0`.

Since the maximum number of digits among all of the numbers is three (for 123), we need to perform a third iteration to distribute the numbers by the hundreds digit:

![The third iteration of radix sort, in which the numbers are placed into buckets according to their hundreds digit.](/images/assignment-2-radix-3.svg)

The buckets can then be reformatted into a single list and returned:

![The sorted version of the original list.](/images/assignment-2-radix-4.svg)

You will now implement radix sort by following the steps below. Along the way, you should test your implementation by executing (and adding to) the set of unit tests in `test_sort.py`.

1. In order for radix sort to know how many iterations to perform, it needs to know how many digits the largest number in the list has. To do this, implement the `get_max_num_digits()` function. This function should accept a list of numbers as input, and return the maximum number of digits among any number in the list. For example, `get_max_num_digits([55, 101, 1111, 5, 999])` should return `4`, since the maximum number of digits among any of the numbers is four (1111).

2. Implement the `list_to_buckets()` function. This function should accept a one-dimensional list of numbers as input, and return a list of buckets, where each bucket represents one of the ten decimal digits (0-9). The numbers from the input list should be assigned to a bucket according to their *least significant digits*. For example, `list_to_buckets([5, 8, 1234, 1, 18, 0, 19, 111])` should return:

    ```python
    [ [0], [1, 111], [], [], [1234], [5], [], [], [8, 18], [19] ]
    ```

    * This will serve as the first iteration of the radix sort algorithm, which has the dual purpose of formatting the list of numbers into a list of buckets, _and_ also sorting the numbers by the least significant digit.
    * To get a list of ten empty buckets, you should call `Sort.get_new_buckets(10)`, which has been provided for you.
    * To get the least significant digit (index 0) for some number `num`, you should call `Sort.digit(num, 0)`.
    * Note that the return value is a two-dimensional list.

3. When the algorithm is complete, we will need to reformat the list of buckets back into a one-dimensional list. To do so, implement the `buckets_to_list()` function, which accepts a list of buckets and converts it into a simple list of numbers. For example, `buckets_to_list([ [3, 5, 9], [25], [], [40], [51, 53], [], [], [88], [91] ])` should return:

    ```python
    [3, 5, 9, 25, 40, 51, 53, 88, 91]
    ```
4. Implement the radix sort algorithm as described above in the `radix_sort()` method. This method should invoke each of the three functions you just wrote, in addition to other logic to make the algorithm work.

    Other notes:

    * A new set of buckets should be created for each iteration of the algorithm.
    * You should track the number of moves that radix sort makes during its execution, since that measurement will be the basis of your algorithmic analysis. Whenever an value is added to a bucket, you should increment `self.moves`.
    * Since radix sort is a non-comparitive algorithm, you don't need to count the number of comparisons.
    * Before the algorithm is over, you will need to convert the list of buckets back to a one-dimensional list of numbers.
    * Since radix sort is not performed *in-place*, i.e. the list that was passed in as input is not itself sorted, you will need to return the sorted list that is created during the algorithm.

5. Redo your complexity analysis from Task 1, but this time base it on `radix_sort()`. Modify `experiments.py` to test `radix_sort()` and get the number of moves when sorting both random and almost-sorted lists of various sizes. For both types of lists, show the overall time complexity (which is equivalent to the time complexity for just moves).

## Testing

In addition to the experimental trials that find the number of comparisons and moves for each sort, you should be making use of the unit tests in `test_sort.py` to evaluate the correctness of the functions you implement in Task 2. You are given a basic set of tests to begin with, but you should add more tests to evaluate other cases.

When you upload your submission to Gradescope, you will see the results for some tests, but there may be other edge cases we test during grading that you are not able to see when you submit. So be sure to test thoroughly!

## Conclusion

Now that we've completed running time analyses of these two algorithms, let's quickly check in on how long they take to run in terms of wall time.

Try sorting lists of increasing sizes using mystery sort and radix sort: 5000 items, 10,000 items, 50,000 items, or even more. Warning: you might find that you need to halt the program's execution once the lists reach a certain size for one of the algorithms, because it will take far too long to finish!

Do the actual execution times you observed seem to correspond with the time complexities you derived in the assignment? (This is a rhetorical question -- just something to think about!)
