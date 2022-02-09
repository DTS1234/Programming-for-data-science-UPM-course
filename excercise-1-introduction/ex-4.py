# Write an algorithm that asks the users how many numbers
# he/she wants to type. Then read these numbers and print
# out the smallest number, the sum, the average and the
# largest number (watch for possible errors).

from msilib.schema import Error

def read_number(message):
    value = 0
    while True:
        try:
            value = int(input(message))
            break
        except:
            print('wrong input, enter integer value')
    return value

numbers_to_read = read_number("Enter the value of the numbers to read: ")
numbers = []

for i in range (numbers_to_read):
    numbers.append(read_number('Enter the value of the number: '))

sum = sum(numbers)
average = sum/len(numbers)
min = min(numbers)
max = max(numbers)

print(f"sum : {sum}\naverage : {average}\nmin : {min}\nmax : {max}")