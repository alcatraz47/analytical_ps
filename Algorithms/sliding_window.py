"""
the problem is to find out the maximum sum among the k elements
of an array with the size of n.

example:

arr = [1, 2, 3, 4] and k=2
then the maximum sum calculation will be:
a. 1+2 = 3
then slide the window to next element.
b. 2+3 = 5
c. 3+4 = 7

so, the maximum sum = 7

from the look of it, there will be two loops, one for taking each index
until n-1. and another one will start from the array element of selected
index and then will sum up the elements up to k sized window. so, the
complexity will be n-1 * k-1 ~ n*k. which is about O(n^2).

firstly, I will use the above approach to find out the sum of k elements
"""
import sys

def sliding_window_sum(arr, k) -> str:
    """
        Calculates the maximum sum given the window size.

        Parameters:
            arr: int -> given array
            k: int -> window size

        Returns:
            str: message or maximum sum.
    """
    if k > len(arr):
        return "Array size cannot be smaller than the window size"

    max_sum = -sys.maxsize - 1
    for i in range(len(arr) - k + 1):
        total = 0
        for j in range(0, k):
            total += arr[i + j]
        if total > max_sum:
            max_sum = total

    return str(max_sum)

def optimized_sliding_window_sum(arr, k) -> str:
    """
        Calculates the maximum sum given the window size.

        Parameters:
            arr: int -> given array
            k: int -> window size

        Returns:
            str: message or maximum sum.
    """
    if k > len(arr):
        return "Array size cannot be smaller than the window size"

    max_sum = -sys.maxsize - 1
    window_sum = 0
    for i in range(len(arr)):
        if i < k:
            window_sum += arr[i]
            max_sum = window_sum
        else:
            window_sum = window_sum - arr[i-k] + arr[i]
            if window_sum > max_sum:
                max_sum = window_sum
        
    return str(max_sum)

if __name__ == "__main__":
    arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]#[1, 2, 3, 4, 5]
    k = 4#2
    max_sum = optimized_sliding_window_sum(arr, k)
    print(max_sum)