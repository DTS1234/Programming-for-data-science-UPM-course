
# gene_copy_numbers = [32,3,5,12,45,23,88,1,8,5,10,0,32,0,88]

# gene_names = ['has-let-7a','has-mir-9' ,'has-mir-121' ,'has-mir-23',
# 'has-mir-19', 'has-mir-221', 'has-mir-89' , 'has-mir-1034', 'has-mir-12',
# 'has-mir-2088', 'has-mir-56' , 'has-mir-55a' , 'has-mir-55b' ,
# 'has-mir-127', 'has-mir-17']

#   Write an algorithm that:

#   1. Prints the names of the miRNAs (-mir-) with gene copy
#   number values exceeding the average copy number value for all the genes.
#   2. Prints the names of the miRNA genes with 0 copy numbers
#   3. Prints what is the value of the highest copy number for all the genes
#   4. Constructs a dictionary gene_name -> gene_copy_number

gene_copy_numbers = [32,3,5,12,45,23,88,1,8,5,10,0,32,0,88]

gene_names = ['has-let-7a','has-mir-9' ,'has-mir-121' ,'has-mir-23',
'has-mir-19', 'has-mir-221', 'has-mir-89' , 'has-mir-1034', 'has-mir-12',
'has-mir-2088', 'has-mir-56' , 'has-mir-55a' , 'has-mir-55b' ,
'has-mir-127', 'has-mir-17']

def create_dictionary(names, numbers):
    hash_map_number_name = {}

    for i in range(0, len(numbers)):
        hash_map_number_name[names[i]] = numbers[i]
    
    return hash_map_number_name

dictionary =  create_dictionary(gene_names, gene_copy_numbers)
avg = sum(gene_copy_numbers)/len(gene_copy_numbers)
names_with_codes_over_average = []
names_with_codes_equal_to_zero = []
highest_copy_value = max(gene_copy_numbers)

for name in dictionary.keys():

    current = dictionary[name]

    if(current > avg and name.find('mir') != -1):
        names_with_codes_over_average.append(name)
    if(current == 0):
        names_with_codes_equal_to_zero.append(name)


print('############ 1 ####################')

print(f'names_with_codes_equal_to_zero : {names_with_codes_equal_to_zero}')

print('############ 2 ####################')

print(f'namers with codes over average {names_with_codes_over_average}')

print('############ 3 ####################')

print(f'max value {str(max(gene_copy_numbers))}')

print('############ 4 ####################')

print(f'dictionary created : {dictionary}')
