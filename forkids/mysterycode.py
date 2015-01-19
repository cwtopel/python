#Python For Kids Chapter 9 Programming Puzzles
#Challenge2 Mystery Code

original_string = "this if is you not are a reading very this good then way you to have hide done a it message wrong"

#str.split() parses sentence into a list of individual words and preserves the order

words = str.split(original_string)


print(words)

print(len(words))

print(dir(words))
new_string = ""
for x in range(0, len(words), 2):
	print(x)
	print(words[x])

	new_string = new_string + words[x] + " "

print(new_string)