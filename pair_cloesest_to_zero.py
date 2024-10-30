def closest_to_zero(arr):
  
    # Sorting the array in ascending order
    arr.sort()

    i, j = 0, len(arr) - 1

    # Initializing sum with the first and last elements
    sum_val = arr[i] + arr[j]

    # Initializing the result with the absolute value
    # of the initial sum
    diff = abs(sum_val)

    while i < j:
      
        # If we have zero sum, there's no result
        # better. Hence, we return 0.
        if arr[i] + arr[j] == 0:
            return 0

        # If we get a better result, we update the
        # difference
        if abs(arr[i] + arr[j]) < abs(diff):
            diff = arr[i] + arr[j]
            sum_val = arr[i] + arr[j]
        elif abs(arr[i] + arr[j]) == abs(diff):
          
            # If there are multiple pairs with the same
            # minimum absolute difference, return the
            # pair with the larger sum
            sum_val = max(sum_val, arr[i] + arr[j])

        # If the current sum is greater than zero, we
        # search for a smaller sum
        if arr[i] + arr[j] > 0:
            j -= 1
        # Else, we search for a larger sum
        else:
            i += 1

    return sum_val


# Driver Code
arr = [1, 60, -10, 70, -80, 85]
print(closest_to_zero(arr))
