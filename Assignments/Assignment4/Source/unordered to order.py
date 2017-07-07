import collections #importing collection lib

unordict = {'Raghu':120,'Saijyothi':100,'Vihari':105,'Nandan':115} # declaring a dictnoary
print(unordict)                                         #printing it

ordered_dict = collections.OrderedDict(sorted(unordict.items())) # orderdinng them with sorted by its key
print(ordered_dict)