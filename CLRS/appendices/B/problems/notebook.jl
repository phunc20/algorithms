### A Pluto.jl notebook ###
# v0.16.1

using Markdown
using InteractiveUtils

# ╔═╡ 7f005754-26bb-11ec-2d0c-2dfd971bc6e2
md"""
## B-1 Graph Coloring
**Def.**$(HTML("<br>"))
Given an undirected graph ``G = (V, E)``, a _**``k``-coloring**_ is a function ``c: V \to \{0,1,\ldots,k-1\}`` s.t. ``c(u) \ne c(v)`` for every edge ``\{u, v\} \in E``.

**Rmk.**
01. The map coloring problem that many of us have heard of is a concret question of which the above definition forms an abstraction: The countries are the vertices. Those which share borders constitute the edges in ``E``. 
02. For any graphs with finite vertices, there always exists a ``k``-coloring, e.g. simply taking ``k = |V|``, coloring each vertex with a different color will do. As a result, we are usually interested in discussing ``k``-coloring of a graph with ``k`` as small as possible.

"""

# ╔═╡ Cell order:
# ╠═7f005754-26bb-11ec-2d0c-2dfd971bc6e2
