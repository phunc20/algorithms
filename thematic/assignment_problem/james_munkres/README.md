


## Clarifications
1. (p. 33) Step A seems unnecessary because by definition matrix $A$'s smallest element is already $0$:
   $$x_{i,j} = \max_{p,q} r_{p,q} - r_{i,j}$$
1. (p. 33) Step B.
    - How is the minimal set $S_{1}$ defined? I think, it can be defined as follows.<br>
      Since the matrix $A$ is $n$ by $n$, the set of all $2n$ lines is a set containing all the zeros of $A$.<br>
      A set $S$ is said to be minimal of all such sets if, given another such set $S'$, we have $m \le m'$,
      where $m, m'$ denotes the cardinal numbers of $S, S'$, resp.
    - Explain the statement
      > If $n_{1} = n$, there is a set of $n$ independent zeros.
      
      Explanation:<br>
      Assume that $n_{1} = n$ and that $A$ contains $m \le n$ independent zeros.
      By Kőnig's theorem (stated on p.32-33), there exists a set $S'$ of $m$ lines containing
      all the zeros. However, since $S_{1}$ is the smallest such set, we must have
      $$n_{1} = n \le m$$

