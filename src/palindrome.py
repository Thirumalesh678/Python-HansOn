def reverseString(text):
    return "".join(reversed(text))
def ispalindrome(text):
    if(text.lower()==reverseString(text).lower()):
        return True
    else:
        return False
print(ispalindrome("madam"))