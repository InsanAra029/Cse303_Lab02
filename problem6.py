# Use a dictionary comprehension to count the length of each word in a sentence (use string above)
string = "Practice Problems to Drill List Comprehension in Your Head"
word = string.split()
word_len = []
for word in word:
   word_len.append(len(word))
   print(f"\"{word}\" length is {word_len}")
   word_len = []
