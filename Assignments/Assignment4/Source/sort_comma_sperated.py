def sort_split(l):          #function to split by comma seperated elements and sort those elements
    x=l.split(',')          #split by ' , '
    print(sorted(x))        #sort and print the list

def sort_split_space(l):          #function to split by comma seperated elements and sort those elements
    x=l.split(' ')          #split by 'space'
    print(sorted(x))        #sort and print the list



words=input('Enter some word seperated by comma:')          #taking the , seperated elemets from the user
#sort_split(words)                                           #calling the sort_split function by giving the words as input to that function.
sort_split_space(words)                                           #calling the sort_split_space function by giving the words as input to that function.