list=['apple','bag','saijyothi']
count=0
for i in list:
    if len(i)> count:
        count=len(i)
        word=i
print(word,count)
