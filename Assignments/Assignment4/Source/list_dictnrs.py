from collections import defaultdict

def final_sum(l):
    f = defaultdict(int)
    for item in l:
        f[item['Emp']] += item['Salary']
    print(f)

list=[{'Emp': 'Raghu', 'Salary':100},
      {'Emp': 'Saijo', 'Salary':200},
      {'Emp': 'Saijo', 'Salary':300},
      {'Emp': 'Raghu', 'Salary':200},
      {'Emp': 'Vihari', 'Salary':200}]
final_sum(list)

