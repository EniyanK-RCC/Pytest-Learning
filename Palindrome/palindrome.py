def isPalindrome(word):
    dict = {}
    for i in word:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    list = [None for _ in range(len(word))]
    index = 0
    for i in dict.keys():
        
        while dict[i]>1:
            list[index] = i
            list[(index+1)*(-1)] = i
            dict[i] -= 2
            
        index += 1
    
    dict = {k: v for k, v in dict.items() if v != 0}
    if len(dict)>1:
        return False
    return True

print(isPalindrome("word"))