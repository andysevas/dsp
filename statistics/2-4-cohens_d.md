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
