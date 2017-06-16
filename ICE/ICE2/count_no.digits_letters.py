str=input('Enter string:')
digit=0
letter=0
for i in str:
    if i.isalpha():
        letter=letter+1
    elif i.isnumeric():
        digit=digit+1

print("digits:",digit,"letters:",letter)


