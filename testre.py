import re
datafile = open('sample_data.txt', 'r')
data = datafile.read()
string_numbers = re.findall('[0-9]+', data)
numbers = map(int, string_numbers)
sum_oflist = sum(i for i in numbers)
print sum_oflist
    
