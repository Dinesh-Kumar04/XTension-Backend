def is_anagram(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = ''.join(str1.split()).lower()
    str2 = ''.join(str2.split()).lower()
    
    # Check if string is same or not
    return sorted(str1) == sorted(str2)

# Test cases
def test_is_anagram():
    # Test case 1:
    assert is_anagram("listen", "silent") == True
    # Test case 2:
    assert is_anagram("hello", "world") == False
    # Test case 3:
    assert is_anagram("Astronomer", "Moon starer") == True
    print("All test cases passed!")

# Running test case
test_is_anagram()
