num = input('Enter the number:')  #Taking nput from the user
n=int(num)
Reverse = 0
while(n > 0):   #loop to check whether the number is  > 0
    Reminder = n%10 # finding the reminder for number
    Reverse = (Reverse * 10) + Reminder
    n = n // 10

print('Reverse for the Entered number is:%d' %Reverse)




