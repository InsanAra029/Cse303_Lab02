# Remove all of the vowels in a string (use string above)
string = "Practice Problems to Drill List Comprehension in Your Head."
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
newstr = ""
for i in range(len(string)):
    if string[i] not in vowels:
        newstr = newstr + string[i]

print("String after removing Vowels: ")
string = newstr
print(string)