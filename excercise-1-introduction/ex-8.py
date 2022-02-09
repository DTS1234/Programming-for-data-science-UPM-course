# Create a program for printing
#     *
#    ***
#   *****
#  *******
# *********

def print_pyramid(level = 5):
    for i in range(1, level*2, 2):
        print_row(level*2, i)
        print('', end='')
        
def print_row(width, points):
    
    mid = width/2
    indexes = [mid]
    
    for i in range(1, points):
        if(i % 2 == 0):
            indexes.append(max(indexes)+1)
        else:
            indexes.append(min(indexes)-1)

    s = width*' '

    for i in range(len(s)):
        if(i in indexes):
            s = s[:i] + "*" + s[i+1:]

    print(s)
    
print_pyramid()