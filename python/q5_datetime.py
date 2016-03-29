# Hint:  use Google to find python function

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

a = '01-02-2013'
b = '07-28-2015'
c=datetime.datetime.strptime(a, "%m-%d-%Y").date()
d=datetime.datetime.strptime(b, "%m-%d-%Y").date()
(d-c).days


####b)  
date_start = '12312013'  
date_stop = '05282015'  




####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  
