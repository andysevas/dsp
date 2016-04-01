[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

You don't actually need to use the files they reference in this one because they give you all the relevant information in the question.  

Average height for men = 178cm = 70.1 inches  
SD of height for men = 7.7cm = 3.03 inches  

Blue man group minimum height(inches) = 5'10" = 70 inches  
Blue man group maximum height(inches) = 6'1 = 73 inches  

Now to convert to standard units.  
Blue man group minimum height(SU) = (70-70.1)/3.03 = -0.033  
Blue man group maximum height(SU) = (73-70.1)/3.03 = 0.957  

Now to use his code.  He gives us a nice function, though it's pretty much just returning the line we need.  I'll just use the line, as seen below.  (I'm not running it yet).
```
import scipy.stats
scipy.stats.norm.cdf(x, loc=mu, scale=sigma)
```
Since it's a *cumulative* function, we have to find the probability that people will be below 6'1" and subtract the probability that someone will be below 5'10".  That gives us just 5'10" to 6'1".  

Now I do this.  
```
scipy.stats.norm.cdf(.957) - scipy.stats.norm.cdf(-.033)
```
It returns 0.344.  Considering we had about half a standard deviation of separation between the two, that sounds about right.


