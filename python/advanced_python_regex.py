
import csv
import collections

with open('faculty.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    
names   = [i[0] for i in data if i[0] != data[0][0]]
degrees = [i[1] for i in data if i[1] != data[0][1]]
titles  = [i[2] for i in data if i[2] != data[0][2]]
emails  = [i[3] for i in data if i[3] != data[0][3]]


#Cleaning up those damn degrees
no_dots = ([i.replace('.', '') for i in degrees])
no_whitespace = [i.strip() for i in no_dots]
flatlist = [no_whitespace[i].split(' ') for i in range(len(no_whitespace)) ]
clean_degrees = [q for i in flatlist for q in i]

#Q1
collections.Counter(clean_degrees)

#Q2
collections.Counter(titles)

#Q3
set(emails)

#Separating domain from email handle
domains = []
for i in emails[1:]:
    domains.append( i.split('@')[1])

#Q4
collections.Counter(domains)
