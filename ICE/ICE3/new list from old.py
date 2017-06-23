def fun():
    list = []
    num = int(input("Size of the list:"))
    for x in range(0,num):
        var = int(input())
        list.append(var)
    return list

list = fun() #Using the function
print (list)   #printing the list
list2=[list[0],list[-1]]
print("new list is", list2) #Printing the first and last elements f the list