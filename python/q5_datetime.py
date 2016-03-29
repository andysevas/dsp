# Hint:  use Google to find python function

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

import datetime
a = '01-02-2013'
b = '07-28-2015'
c=datetime.datetime.strptime(a, "%m-%d-%Y").date()
d=datetime.datetime.strptime(b, "%m-%d-%Y").date()
(d-c).days  
938 is the answer.


####b)  
date_start = '12312013'  
date_stop = '05282015'  
e=datetime.datetime.strptime(date_start, "%m%d%Y").date()
f=datetime.datetime.strptime(date_stop, "%m%d%Y").date()
(f-e).days
513 is the answer.


####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  
g=datetime.datetime.strptime(date_start, "%d-%b-%Y").date()
h=datetime.datetime.strptime(date_stop, "%d-%b-%Y").date()
(h-g).days
7850 is the answer.
