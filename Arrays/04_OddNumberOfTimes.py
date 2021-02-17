# Given an array of positive integers. All numbers occur even number of times except one
# number which occurs odd number of times. Find the number in O(n) time & constant space.


# NOTE: This will only work when there is only one number with odd number of occurences.

def printOddOccurences(array):
    odd = 0

    for element in array:

        odd = odd ^ element

    return odd

if __name__ == '__main__':
    myArray = [3, 4, 1, 2, 4, 1, 2, 5, 6, 4, 6, 5, 3]
    print(printOddOccurences(myArray))
