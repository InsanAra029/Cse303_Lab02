# Count the number of spaces in a string (use string above)
str="Practice Problems to Drill List Comprehension in Your Head."
s=0
for i in range(0,len(str)):
  if(str[i]==' '):
    s=s+1
print("Count the spaces: ",s)