
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

