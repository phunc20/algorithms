### A Pluto.jl notebook ###
# v0.16.1

using Markdown
using InteractiveUtils

# ╔═╡ d8aa0d5c-273f-11ec-3d4e-d9c3dbb94278
md"""
# B.5 Trees
By definition, a _**free tree**_ is an undirected, connected, acyclic graph. At first glance, this seems to be
an object with many (`3` to be precise) adjectives. But, once we started to have a deeper understanding, we
might come to realize that a free tree is just an undirected graph that is
```math
\newcommand{\norm}[1]{\lVert{#1}\rVert}
\newcommand{\abs}[1]{\lvert{#1}\rvert}
```

- connected
  - (Exercise B.4-3) If ``G = (V, E)`` is an undirected, connected graph then ``\abs{E} \ge \abs{V} - 1``.
  - In day-to-day English, this simply says,
    > "For an undirected graph to be connected, there cannot be too few edges; there must exist at least ``\abs{V} - 1`` edges."
- acyclic
  - We prove an analogous result: If ``G = (V, E)`` is an undirected, acyclic graph then ``\abs{E} \le \abs{V} - 1``.
  - This simply says analogously,
    > "For an undirected graph to remain acyclic, there cannot be too many edges. Too many edges create cycles. There can be at most ``\abs{V} - 1`` edges."

_Proof._$(HTML("<br>"))
We show that for any acyclic undirected graph ``G = (V, E)``, we have ``\abs{E} \le \abs{V} - 1``.

Note that this is not saying that cyclic graphs tend to have many more edges than acyclic graphs do. Indeed, three edges btw three distinct vertices suffice to make a graph cyclic. I find it useful to picture in our head like this:
> We are given the vertex set ``V`` and an empty edge set ``E``.
> We search to add as many edges to ``E`` as possible in keeping ``G`` acyclic.

Again, we shall prove this by mathematical induction on ``\abs{V}``. It is easy to
verify the validity of the statement when ``\abs{V} = 1, 2``. When ``\abs{V} = 3``, assume that ``G`` is acyclic. If ``\abs{E} = 3``, then ``G`` contains a cycle; in fact, in this case, ``G`` is itself a cycle. So we can conclude ``\abs{E} \le 2 = \abs{V} - 1.`` (Three vertices admit at most ``\begin{pmatrix} 3 \\ 2\end{pmatrix} = 3`` edges, and,  since ``3`` is excluded, we must have ``\abs{E} \le 2``.)

Now, assume that the statement holds for ``\abs{V} = 1, 2, 3, \ldots, k``. Let ``G = (V, E)`` be an acyclic undirected graph with ``\abs{V} = k+1``. (To be continued...)
"""

# ╔═╡ 638c65ab-3eb4-416b-8adf-110649dac5c4
md"""
Since a tree (i.e. a free tree. It seems that we often drop the adjective and speak of trees as free trees) is at the same time connected and acyclic, from the above relation btw number of edges and number of vertices, we should have
```math
\abs{E} = \abs{V} - 1.
```

**Theorem B.2 (Properties of free trees)**$(HTML("<br>"))
The followings are equiv:
"""

# ╔═╡ Cell order:
# ╠═d8aa0d5c-273f-11ec-3d4e-d9c3dbb94278
# ╠═638c65ab-3eb4-416b-8adf-110649dac5c4
