
#The value 'data' is from the last problem.  It's the faculty.csv data.
faculty_dict = {}
for i in data:
        fullname = i[0].split()
        lastname = fullname[-1]
        faculty_dict[lastname] = row[1:]

#Question 6
first3pairs = {k: faculty_dict[k] for k in faculty_dict.keys()[:3]}

#Building the dictionary for question 7
professor_dict = {}
for i in data:
    fullname = i[0].split()
    fullname = tuple(fullname)
    professor_dict[fullname] = i[1:]
    
    
first3pairs = {k: professor_dict[k] for k in professor_dict.keys()[:3]}


#Sorting for question 8
last_name_sort = sorted(professor_dict, key=lambda x: x[-1]) 

#Just taking the first 3 
for i in last_name_sort[:3]:
    print i, ":", professor_dict[i]

