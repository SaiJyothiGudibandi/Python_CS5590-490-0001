#Symetric difference is nothin but printing the new set of values which either persent in list1 or list2, but not in both the lists
from pip.backwardcompat import raw_input


'''list1=[]
len1 = int(input('Enter length of list1:'))
length1=0
while length1<len1:
    element = int(raw_input('Enter the list1 elements:'))
    list1.append(element)
    length1=length1+1
print(list1)

list2=[]
len2 = int(input('Enter length of list2:'))
length2=0
while length2<len2:
    element = int(raw_input('Enter the list1 elements:'))
    list2.append(element)
    length2=length2+1
print(list2)'''

list1=set(['1','2','3','4'])
list2=set(['2','3','8'])

final= list1^list2
print(final)