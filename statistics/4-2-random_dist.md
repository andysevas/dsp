[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

I started like this.  Essentially I imported everything I needed and made a pmf of 1000 random numbers from 0 to 1.  What I got was a crazy chart that just looked like a mess of blue.  Since every number is equally likely, it was expected that it would come out ugly like that.  See code below.  

```
import thinkstats2
import thinkplot
import random
x = [random.random() for i in range(1000)]
randompmf = thinkstats2.Pmf(x, label='random nums')
thinkplot.Pmf(randompmf)
thinkplot.Show(xlabel='randoms', ylabel='PMF')
```

After that, I ran the cdf.  Because it is cumulative, it ended up making much more sense, since it is showing me the odds of getting a number at least that large.  

```
randomcdf = thinkstats2.Cdf(x, label='random nums')
thinkplot.Cdf(randomcdf)
thinkplot.Show(xlabel='randoms', ylabel='CDF')
```

The cdf was a (basically) straight diagonal line that ran from bottom left to upper right.  Because it was straight, it implies there is no number that was more or less likely to be chosen than any other.
