```python
In [14]: A = [5,4,3,2,1]                                        

In [15]: for i in A: 
    ...:     if i == 3: 
    ...:         A.append(0) 
    ...:                                                        

In [16]: A                                                      
Out[16]: [5, 4, 3, 2, 1, 0]

In [17]: for i in A: 
    ...:     if i == 3: 
    ...:         A.remove(i) 
    ...:                                                        

In [18]: A                                                      
Out[18]: [5, 4, 2, 1, 0]
# No problem so far, but read on!

In [19]: for i in A: 
    ...:     A.remove(i) 
    ...:                                                        

In [20]: A                                                      
Out[20]: [4, 1]

In [21]: A = [5,4,3,2,1,0]                                      

In [22]: for i in A: 
    ...:     print("i = {}".format(i)) 
    ...:     A.remove(i) 
    ...:                                                        
i = 5
i = 3
i = 1

In [23]: A                                                      
Out[23]: [4, 2, 0]

```


### What happened?
What happened under the hood was that the `for i in A` internally iterates through the
indices of `A`, and the `.remove()` (or any `.insert()`)
method changes `A` in place, resulting in a new `A`
with diff indexing and diff elements.

For example, in `[21]`, we have `A = [5,4,3,2,1,0]`. When running `[22]`, we first remove the
element of index `0` of `A`, resulting in `[4,3,2,1,0]`; then at next iteration, we need to
remove the element of index `1`, resulting in `[4,2,1,0]` this time; next up, we need to
remove the element of index `2`, producing `[4,2,0]`; next up we are supposed to remove the
element of index `3`, but there are only 3 elements in the remaining `[4,2,0]`, so we are done.


### Remedy
Several possible workarounds exist:
1. Use loop via indices or `while` loop instead, which have
clearer syntax and more control. -- And generally,
`while` is safer than `for`. (cf. example below.)
2. make a copy of `A` and iterate on one while mutating on
the other.

```python
# Example in which while triumphs over for
my_list = [1,2,3,4,5,6,7,8,9]
for i in range(len(my_list)):
    if my_list[i] == 8:
        del my_list[i]
    print("i = {}".format(i))


# To see more easily why this happened
In [25]: my_list = [1,2,3,4,5,6,7,8,9] 
    ...: for i in range(len(my_list)): 
    ...:     print("i = {}".format(i)) 
    ...:     if my_list[i] == 8: 
    ...:         del my_list[i] 
    ...:                                                        
i = 0
i = 1
i = 2
i = 3
i = 4
i = 5
i = 6
i = 7
i = 8
----------------------------------------------------------------
IndexError                     Traceback (most recent call last)
<ipython-input-25-b8a664389eec> in <module>
      2 for i in range(len(my_list)):
      3     print("i = {}".format(i))
----> 4     if my_list[i] == 8:
      5         del my_list[i]

IndexError: list index out of range

# Maybe, let us explain this a little bit:
# When my_list[i] == 8, we have i == 7 and then
# we delete the element 8 in my_list in place.
# Next we enter into the for loop again, this time with i == 8;
# but now len(my_list) == 8 meaning the largest index
# in my_list was 7, and then when we tried to access
# my_list[i] with i == 8, we encountered
# the IndexError: list index out of range.

# At this point, you might ask, "Why while may
# perform better in such cases?"
# Well,

while index < len(my_list):
	# Do something to my_list[index]
	index += 1

# Since len(my_list) is **recalculated** each time,
# we are guaranteed not to bump into any
# IndexError: list index out of range

# Besides, you know why in the first examples, we didn't
# encounter IndexError?
```
