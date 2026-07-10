#dsa problem on arrays

# Input: arr[] = [12, 35, 1, 10, 34, 1]
# Output: 34
# Explanation: The largest element of the array is 35 and the second largest element is 34.

# Input: arr[] = [10, 5, 10]
# Output: 5
# Explanation: The largest element of the array is 10 and the second largest element is 5.

# Input: arr[] = [10, 10, 10]
# Output: -1
# Explanation: The largest element of the array is 10 there is no second largest element.


# arr= [12, 35, 1, 10, 34, 1]

arr= [10,10,10]
def secondLargest(arr):
    n=len(arr)
    arr.sort()
    for i in range(n-1,-1,-1):
        if arr[i]!=arr[n-1]:
            return arr[i]
    return -1
print(secondLargest(arr))
