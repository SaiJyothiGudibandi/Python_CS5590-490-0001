string=input('Enter string:')
set={}
for char in string:
    set[char]=string.count(char)
print(set)