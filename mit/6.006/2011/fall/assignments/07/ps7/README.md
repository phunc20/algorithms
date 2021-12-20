## Problem Set Sheet
1. On p.1, the **Relation.** part, it says
  ```
  dp[i,j] = min(dp[i-1,j-1], dp[i,j-1], dp[i+1,j-1]) + energy(i, j)
  ```
  The reason why this might look weird to some of us is because, contrary
  to convention, here `i` represents column index, `j` row index. To justify
  this, note that in `imagematrix.py`, the class `ImageMatrix`'s `self` is
  also defined as
  ```python
  self.width, self.height = image.size
  pixels = iter(image.getdata())
  for j in range(self.height):
      for i in range(self.width):
          self[i,j] = pixels.next()
  ```
  where `j` iterates through the rows and `i` through the columns.


## Python Version
By the look of

```python
print 'You do not have PIL (the Python Imaging Library) installed.'
```
in `imagematrix.py`, we could infer that these Python scripts were
written for Python2.7.

