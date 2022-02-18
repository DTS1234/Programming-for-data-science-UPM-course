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
print("")

stringsToPrint = []

# for i in range(len(level_list)-1, -1, -1):
#     current = level_list[i]

#     if (i == len(level_list)-1): # lowest level
#         lowest_level = ""

#         for j in range(0, len(current)):
#             if(int(current[j])<9):
#                 lowest_level += "0" + str(current[j])
#             else:
#                 lowest_level += str(current[j])
            
#             if((j+1)%2 != 0): 
#                 lowest_level += " "*4            
#             elif(j != len(current)-1):
#                 lowest_level += " "*2
#         stringsToPrint.append(lowest_level)
    
#     if(len(stringsToPrint) != 0):
#         pass

# print('        01        ')
# print('     /      \     ')
# print('   02        03   ')
# print('  /  \      /  \  ')
# print('04    05  06    07')
