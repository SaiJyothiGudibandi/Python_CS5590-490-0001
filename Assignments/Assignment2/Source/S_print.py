n=int(input('Enter N:'))
print(' '+'*'*n)
for i in range(n-1):
    print('*'+' '*(n+1))
print(' '+'*'*n)
for i in range(n-1):
    print(' '*(n+1)+'*')
print('*'*(n+1))
