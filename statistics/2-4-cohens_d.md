[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

I started with Mr. Downey's dataframe.

```python
import nsfg
df = nsfg.ReadFemPreg()
df
```

I followed his examples and used his ccode for first borns and non-first borns.  He also calculates how many there are of each.

```python
firsts = df[df.birthord==1]
others = df[df.birthord>1]
len(firsts), len(others)
```

He calculates the Cohen effect size as follows:

```python
def CohenEffectSize(group1, group2):
    diff = group1.mean() - group2.mean() #the numerator

    var1 = group1.var()    
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)

    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)  #the denominator, but as variance instead of SD
    d = diff / math.sqrt(pooled_var)
    return d
```

Then I simply use his function with the babies' weights, which is the column indicated in the problem.
```python
CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)  #First babies weights vs. Non-first weights
```
