def toupper(text):
    return text.upper()

def replacetext(text, replacetext, keyword):
    return text.replace(replacetext,keyword)

def reverseString():
	strV = "The Text"
	rev =strV+"="+"".join(reversed(strV))
	print(rev)

reverseString()

print(replacetext("The quick brown fox jump over a lazy dog","dog","cat"))

print(toupper("The quick brown fox jump over a lazy dog"))