def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return fib_sequence

# Test case
def test_fibonacci():
    # Test case 1:
    assert fibonacci(0) == []
    # Test case 2:
    assert fibonacci(1) == [0]
    # Test case 3:
    assert fibonacci(5) == [0, 1, 1, 2, 3, 5]
    print("All test cases passed!")

# Running test case
test_fibonacci()