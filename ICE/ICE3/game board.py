size=int(input('What is the size of the game board:'))

def print_horiz_line():
    print(' --- '*size)
def print_vert_line():
    print('|    '*(size+1))

for i in range(size):
    print_horiz_line()
    print_vert_line()
print_horiz_line()



