Recall the standard, increasing-order insertion sort:
```julia
function textbook_insertion_sort(A::Array)
  for j in 2:length(A)
    key = A[j]
    i = j - 1
    while i > 0 && A[i] > key
      A[i+1] = A[i]
      i -= 1
    end
    A[i+1] = key
  end
end
```

It is quite easy to modify this code to
make it into a decreasing-order insertion sort:
```julia
# Decreasing order: the sorted subarray
# should always be in decreasing order.
function insertion_sort_decr(A::Array)
  for j in 2:length(A)
    key = A[j]
    i = j - 1
    while i > 0 && A[i] < key
      A[i+1] = A[i]
      i -= 1
    end
    A[i+1] = key
  end
end
```
**Rmk**. The only modification is at the `while`'s condition:
- `A[i] > key` for increasing-order insertion sort
- `A[i] < key` for decreasing-order insertion sort

If we test this in Julia's REPL, we'd get sth similar to the following.
```julia
julia> A = rand(1:100, 10)
10-element Array{Int32,1}:
 96
 53
 76
 91
 45
 51
  9
 33
 65
 12

julia> insertion_sort_decr(A); A
10-element Array{Int32,1}:
 96
 91
 76
 65
 53
 51
 45
 33
 12
  9

```

