


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
1. (p. 33) Step D.<br>
   Let's denote by $\texttt{sum}(A)$ the sum of all elements of a matrix $A$.<br>
   Then the sequence $\texttt{sum}(A_{k})$ is a strictly decreasing (integer) sequence which is
   bounded below by $0$.<br>
   Indeed, if the procedure (of steps A,B,C,D) cannot terminate at $k$, then
   $$\texttt{sum}(A_{k+1}) = \texttt{sum}(A_{k}) - n^{2} h_{k} + n_{k} n h_{k} = \texttt{sum}(A_{k}) - n (n - n_{k}) h_{k}$$





