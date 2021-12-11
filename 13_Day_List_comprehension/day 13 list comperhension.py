numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered_numbers = [i for i in numbers if i <= 0]
print(filtered_numbers)

# 2
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
print(list_of_lists[0])
flattened_list = [number for row in list_of_lists for list in row for number in list]
print(flattened_list)

# 3
output = [(i, pow(i, 0), pow(i, 1), pow(i, 2), pow(i, 3), pow(i, 4), pow(i, 5)) for i in range(11)]
print(output)

# 4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output = [[country[0].upper(), country[0][:3].upper(), country[1].upper()] for item in countries for country in item]
print(output)

# 5
output = [{'country': country[0], 'city':country[1]} for item in countries for country in item]
print(output)

# 6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Duck')], [('Bill', 'Gates')]]
output = [name[0] + ' ' + name[1] for lst in names for name in lst]
print(output)