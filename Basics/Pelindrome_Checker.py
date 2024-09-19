def isPelindrome(str):
    # To check if string has only letter
    if len(str)==1:
        return True
    
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True

# Input from user
userStr = input("Enter any string: ")

result = isPelindrome(userStr)

# Check if string is pelindrome or not
if result:
    print("Pelindrome")
else:
    print("Not a pelindrome")
