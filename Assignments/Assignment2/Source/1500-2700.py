n=0
print('The numbers divided by 5 and 7 in between 1500 and 2700 are:')
for i in range(1500,2700):      #loop between 1500 to 2700
    if (i%5)==0 and (i%7)==0:   #condition:should the number divided by both 5 and 7
        print(i)                #Printing the numbers which are divided by both 5 and 7 in between 1500 and 2700
        n=n+1
print('Total:',n)               #Pring the total n umber of numbers