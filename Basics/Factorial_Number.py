def factorial(n):
    # Check if n == 0
    if n == 0:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Test case 1
def test_factorial():
    # Test case 1:
    assert factorial(0) == 1
    # Test case 2:
    assert factorial(5) == 120
    # Test case 3:
    assert factorial(1) == 1
    print("All test cases passed!")

# Running test case
test_factorial()
