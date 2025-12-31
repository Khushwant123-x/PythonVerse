#Write a python function named ComputeAverage to find average of a list of numbers.
#It should handle the exception if the list is empty and return 0 in that case.

def ComputeAverage(lst):
    try:
        return sum(lst) / len(lst)
    except ZeroDivisionError:
        return 0

print(ComputeAverage([10, 20, 30]))   # Output: 20.0
print(ComputeAverage([]))             # Output: 0
