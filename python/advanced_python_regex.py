
import csv
import collections

with open('faculty.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    
names   = [i[0] for i in data if i[0] != data[0][0]]
degrees = [i[1] for i in data if i[1] != data[0][1]]
titles  = [i[2] for i in data if i[2] != data[0][2]]
emails  = [i[3] for i in data if i[3] != data[0][3]]

domains = []
for i in emails[1:]:
    domains.append( i.split('@')[1])

collections.Counter(domains)
