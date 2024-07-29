def isPalindrome(word):
    dict = {}
    for char in word:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1

    total = 0
    for count in dict.values():
        
        if count%2 != 0:
            total += 1
    
    if total>1:
        return False
    return True

