def sum(list):                                  #function to get the sum of the values in the dictionary

    for i in list:
        f1 = i.pop('Prev-fee')                  #pop the Prev-fee key value and assign that to f1
        f2 = i.pop('Present-fee')
        i['Total-fee'] = (f1 + f2)/2            #pop the Present-fee key value and assign that to f2
    return list

fee= [{'Student_Name' : 'Bavish',  'Prev-fee' : 1000, 'Present-fee' : 2000},            #List of three dictonories
      {'Student_Name' : 'Sai',  'Prev-fee' : 95, 'Present-fee' : 85},
      {'Student_Name' : 'Raghu',  'Prev-fee' : 100, 'Present-fee' : 100}]
print(sum(fee))