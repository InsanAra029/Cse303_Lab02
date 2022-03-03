# Find all of the words in a string that are less than 5 letters (use string above)
string = "Practice Problems to Drill List Comprehension in Your Head."
word=string.split(" ")
for i in range (1,len(word)):
    if(len(word[i])<5 ):
        print(word[i])