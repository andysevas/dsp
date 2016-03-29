# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

Both are "list-like" aggregations/collections of values.  Lists are muteable (changeable) however and tuples are not.  Tuples will work as keys in dictionaries due to that fact.  

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

A set is like a list with duplicates removed.  They don't have an order like a list and you can't use an index on them.  Sets must be hashable and lists do not have to be.  That makes them much quicker to search when you're looking for an element contained within one of them.  A set would be better used for finding all the people who did something, like made a purchase from a company.  If they just want to know how big their user base is, they'd want to know how many individuals made at least one purchase.  That's well stored in a set.  A list could store all the purchases and have multiple mentions of the same person making more than one transaction.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

Lambda is used to make functions that don't have to be named first.  Some people call it an "anonymous function".  It's useful to call it if you need a function while in the midst of solving another issue.  

So in the case of "sorted", you can use it to decide what you're going to sort.  Let's say you want to sort a list of words, but first you need to make sure that the sort doesn't get all messed up because some of them are uppercase and some are lowercase.  You can write the sorted function like this...

```python
sorted(list_of_words, key=lambda x: x.lower())
```

x represents your words in the list that the function will operate on.  Also, I'm kind of impressed that I was able to do that formatting so nicely.  It's the little things :)

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

List comprehensions are a quick way to make new lists, often from old lists.  You can change and filter them without having to run a function on them.  For example, if you had a list of numbers from 1 to 10 called "numbers", you could make the list of only even numbers in the list as follows.

```python
evens = [n for n in numbers if n%2==0]
```
This comprehension says "Give me a list where you put in "n" every time you have an item "n" in the list "numbers", but only if it fits the criteria n%2==0."  You can actually get the same result with the filter function.

```python
filter(lambda n: n%2==0, numbers)
```

If instead of reducing the list, I was changing it, like squaring each number, I could have used "map" in the same way.  From what I understand, calling functions is more resource-intensive than list comprehensions.  The same effect can be achieved on sets, except the result will be a set and it uses {braces like this}.  Dictionary comprehensions largely manipulate the keys and values so that they can combine or rearrange values as necessary.




---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

937 is the answer.

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

513 is the answer.

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

7,850 is the answer.

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





