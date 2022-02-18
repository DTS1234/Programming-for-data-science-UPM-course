dictionary = {
                '3' : { 
                    '2' : 
                        {'1' : None }, 
                    '5' : 
                        {'4' : None, '6' : None}
                    }
            }


def shouldFinish(level, dictionary):
    for i in level:
        if dictionary[i] != None:
            return False
        elif i == level[len(level)-1]:
            return True
def getLevelList(dictionary):
    level_list = []
    new_dict = {}
    while True:
        if (len(dictionary.keys()) == 1):
            elem = list(dictionary.keys())[0]
            level_list.append(elem) #  first level
            dictionary = dictionary[elem] # new dictionary from current key
        else:
            level = []
            for i in dictionary.keys():
                level.append(i)
            level_list.append(level)
            
            if(shouldFinish(level, dictionary)):
                break

            for i in level:
                new_dict.update(dictionary[i])
            dictionary = new_dict    
    return level_list

level_list = getLevelList(dictionary)

print()

if(len(level_list[len(level_list) - 1]) % 2 != 0):
    level_list[len(level_list) - 1].insert(0, '[]') # insert one more element that will serve as '[]' if the last level is not even in number of elements

print(level_list)

print("---------------------------")

def pretty_print():
    print('        0'+ level_list[0] + '        ')
    print('     /      \     ')
    print('   0'+level_list[1][0]+'        0'+level_list[1][1]+'   ')
    print('  /  \      /  \  ')
    print(level_list[2][0]+'   0'+level_list[2][1]+'   0'+level_list[2][2]+'    0'+level_list[2][3])

    
pretty_print()
