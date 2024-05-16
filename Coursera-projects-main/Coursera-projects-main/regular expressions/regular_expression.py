import re

#fh = open('regex_sum_42.txt')
fh = open('regex_sum_1922014.txt')

total = 0
count = 0
for line in fh:
    split_line = line.split()
    num = re.findall('[0-9+]+', line)
    for number in num:
        try:
            converted = int(number)
            count += 1
            total = total + converted
        except:
            continue
    #print(num)
print(total)       
print('count:', count)
