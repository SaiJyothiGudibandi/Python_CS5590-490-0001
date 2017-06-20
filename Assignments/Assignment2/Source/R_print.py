n=int(input('Enter the N value:'))  #Taking the input from the user
s=1
print('*'*n)    #Printing *'s in first line
for i in range(n-1):    #loop for n-1 lines
    print('*' + ' ' * (n-1) + '*')
print('*' * n)
for j in range(n,2*n):  #loop for 2*n lines
    print('*' + ' ' * (s) + '*')
    s=s+1


