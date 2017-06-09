num = int(input('Enter the number:'))  #Taking nput from the user

Reverse = 0
while(num > 0):   #loop to check whether the number is  > 0
    Reminder = num%10 # finding the reminder for number
    Reverse = (Reverse * 10) + Reminder
    num = num // 10

print('Reverse for the Entered number is:%d' %Reverse)




