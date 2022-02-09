# Write a program that asks the user to enter two words. The
# program then prints out both words on one line, the length
# of both words and number of points added. The words will
# be separated by enought dots so that the total line length is 30:
#   First word : turtle
#   Second word : 153
#   turtle ....................153
#   Length first word : 6
#   Length first word : 3
#   Number of points : 21

first_word = input('First word : ')
second_word = input('Second word : ')

first_length = len(first_word)
second_length = len(second_word)
number_of_points = 30 - first_length - second_length

print(f'{first_word}{"*"*number_of_points}{second_word}')
print(f'Length first word : {first_length}')
print(f'Length second word : {second_length}')
print(f'Number of points : {number_of_points}')
