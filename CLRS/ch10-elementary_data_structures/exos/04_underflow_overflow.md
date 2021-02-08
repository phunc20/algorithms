## Enqueue with overflow check
```
ENQUEUE(Q,x)
1 if (Q.head == Q.tail + 1) or (Q.tail == Q.length and Q.head == 1)
2     error "overflow"
3 else
4     Q[Q.tail] = x
5     if Q.tail == Q.length
6         Q.tail = 1
7     else
8         Q.tail = Q.tail + 1
```


## Dequeue with underflow check
```
DEQUEUE(Q,x)
1 if Q.tail == Q.head
2     error "underflow"
3 else
4     x = Q[Q.head]
5     if Q.head == Q.length
6         Q.head = 1
7     else
8         Q.head = Q.head + 1
9     return x
```


