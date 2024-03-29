# Dynamic programming Python implementation
# of LIS problem


# lis returns length of the longest
# increasing subsequence in arr of size n
def LongestIncresingSequence(arr):
    n = len(arr)

    # Declare the list (array) for LIS and
    # initialize LIS values for all indexes
    lis = [1] * n

    # Compute optimized LIS values in bottom up manner
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    # Initialize maximum to 0 to get
    # the maximum of all LIS
    maximum = 0

    # Pick maximum of all LIS values
    for i in range(n):
        maximum = max(maximum, lis[i])

    return maximum


# end of lis function


# Driver program to test above function
def LongestIncresingSequenceReader():
    lines = []
    for i in range(1, 11):
        file1 = open("../ProblemD/" + str(i) + ".txt", 'r')
        for line in file1:
            items = line.rstrip('\r\n').split('\t')
            items = [item.strip() for item in items
                     ]  # strip extra whitespace off data items
            lines.append(items)

    return lines


def Calculate(lines):

    LongestIncresingSequence(lines)
