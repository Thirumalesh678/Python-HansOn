#vowels a,e,i,o,u

#The quick brown fox jump over a lazy dog

def countVowels(text):
	
	vowels = "aeiou"
	count = 0

	for letter in text.lower():
		if letter in vowels:
			count += 1
	return count


print(countVowels("The quick brown fox jump over a lazy dog"))
#print(countVowels("thirumalesh"))