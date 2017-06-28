string=input('Enter the string:')   #Taking input string from the user

def str_list(a):                    #Defing a function for converting string to list of charecters
    return list(a)

def str_tuple(a):                   #Defing a function for converting string to tupple of charecters
    return tuple(a)

print('List representation for the characters in the string:',str_list(string))

print('Tuple representation for the characters in the string:',str_tuple(string))
