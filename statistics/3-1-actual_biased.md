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
