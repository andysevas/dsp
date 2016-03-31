
import csv
import collections

with open('faculty.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    

emails  = [i[3] for i in data if i[3] != data[0][3]]

emailfile = open('emails.csv', 'wb')
writer = csv.writer(emailfile)
for i in emails:
    writer.writerow([i])
emailfile.close()
