[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

I start by using his data, with the data labeled "resp".
```
%matplotlib inline

import chap01soln
import thinkstats2
resp = chap01soln.ReadFemResp()
```

I make a pmf of the number of kids in the household

```
actualchart = thinkstats2.Pmf(resp['numkdhh'], label='actual')
```

Then I use his bias pmf function.  He defines it as follows in his ipynb.

```
def BiasPmf(pmf, label):
  new_pmf = pmf.Copy(label=label)
    for x, p in pmf.Items():
  new_pmf.Mult(x, x)
        
  new_pmf.Normalize()
  return new_pmf
```

I run the function on my data
```biasedpmf = BiasPmf(actualchart, 'observed')```

Then I import the right modules and make the chart.  This code below will do it but I can't make the chart show in here.

```
import thinkplot
thinkplot.PrePlot(2)
thinkplot.Pmfs([actualchart, biasedpmf])
thinkplot.Show(xlabel='Num kids in HH', ylabel='PMF')
```

Then I calculate the means.

```
print ('Actual mean: ' + str(actualchart.Mean()))
print ('Observed mean: ' + str(biasedpmf.Mean()))
```

Actual mean is 1.024.  Observed mean is 2.404.
