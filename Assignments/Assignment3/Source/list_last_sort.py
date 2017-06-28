def tuple_last(a):                              #function for getting last element in tupple
    return a[-1]                                #using last index


def last_sort(b):                               #function t sort the elements
    return sorted(b, key=tuple_last)


list1 = input("Enter a 1st elements in tuples:")
list2 = input('Enter a 2nd elements in tuples:')

list = zip(list1, list2)                        #merig the two list into list of tuples

#print(list)

print('Sorted list:', last_sort(list))          #printin the sorted list of tuples based on the last element in the tiples
