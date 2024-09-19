def find_missing(arr, n):
    # Calculate the expected sum using formula: sum = n * (n + 1) // 2
    expected_sum = n * (n + 1) // 2
    
    # Calculate the actual sum
    actual_sum = sum(arr)
    
    # Finding missing number
    return expected_sum - actual_sum

# Test case
def test_find_missing():
    # Test case 1:
    assert find_missing([1, 2, 4, 5], 5) == 3
    # Test case 2:
    assert find_missing([1, 2, 3, 4], 5) == 5
    # Test case 4:
    assert find_missing([1, 2, 3, 4, 5, 6, 7, 9, 10], 10) == 8
    print("All test cases passed!")

# Running test case
test_find_missing()
