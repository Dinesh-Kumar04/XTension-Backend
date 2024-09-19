# FizzBuzz function
def fizz_buzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

# Time complexity : 
# O(n): loop runs n times. Each iteration checks conditions that take constant time (O(1)).

# Space complexity :
# O(n): The space complexity is linear because We are storing the results in a list, which grows proportionally to n.

# Test cases 1: When n=7
def test_case_1():
    n = 7
    expected_output = ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7']
    if fizz_buzz(n) == expected_output:
        print("Test case passed!")
    else:
        print("Test case failed!")
        print("Expected Output")
        print(expected_output)
        print("Your Output:")
        print(fizz_buzz(n))
        
# Test cases 2: When n=10
def test_case_2():
    n = 10
    expected_output = ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz']
    if fizz_buzz(n) == expected_output:
        print("Test case passed!")
    else:
        print("Test case failed!")
        print("Expected Output")
        print(expected_output)
        print("Your Output:")
        print(fizz_buzz(n))
        
# Test case 2: When n=15
def test_case_3():
    n = 15
    expected_output = ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
    if fizz_buzz(n) == expected_output:
        print("Test case passed!")
    else:
        print("Test case failed!")
        print("Expected Output")
        print(expected_output)
        print("Your Output:")
        print(fizz_buzz(n))

# Running test case
test_case_2()
