# Write an algorithm that given the following list of integers
# a = [12,67,1,89,3,0,100,23,65,34,64,98,12,27]
# counts the number of integers below ’11’ and returns a
# sublist of those elements that are less than half of the
# average of the elements in the list.

a = [12,67,1,89,3,0,100,23,65,34,64,98,12,27]

sum_a = sum(a)
average_a = sum_a/len(a)

counter = 0

sublist = []

for value in a:
    if value < 11:
        counter += 1
    if value < average_a/2:
        sublist.append(value)

print(f'number of elements lower than 11 : {counter}\nsublist generated : {sublist}')