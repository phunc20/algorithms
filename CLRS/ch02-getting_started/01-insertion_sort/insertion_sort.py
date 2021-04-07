def insertion_sort(A):
    """
    A: list or tuple of numbers
    """
    for j in range(1, len(A)):
        key = A[j]
        # insert A[j] into the sorted seq. A[:j]
        # i.e. into A[0..j-1]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key

if __name__ == "__main__":
    import numpy as np
    L = np.random.randn(7)
    print("Before")
    print("L = {}".format(L))
    print("After")
    insertion_sort(L)
    print("L = {}".format(L))


