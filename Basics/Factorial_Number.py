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
    # Test case 1: Factorial of 0
    assert factorial(0) == 1
    # Test case 2: Factorial of 5
    assert factorial(5) == 120
    # Test case 3: Factorial of 1
    assert factorial(1) == 1
    # Test case 4: Factorial of 10
    assert factorial(10) == 3628800
    print("All test cases passed!")

# Running test case
test_factorial()
