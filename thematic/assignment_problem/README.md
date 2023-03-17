## Environment
To run `comparison.py`, I used Python3.10.

The required Python packages are listed in `requirements.txt` and could be installed in the command line by
```bash
$ pip install -r requirements.txt
```

As usual, better install them in a virtual environment instead of in the system Python of your machine.


## How to Use This Directory
- `comparison.py`: This script compares performances of different algorithms/solutions of linear
  assignment problem. Here are a few ways to run it:
  ```
  # Run default 10x10 rating matrix
  $ python comparison.py
  # Run some random 3x3, 5x5, 7x7 rating matrices
  $ python comparison.py 3 5 7 9
  ```


## TODO
`comparison.py`
1. [ ] Add flag to max/min the problem
1. [x] Add solution using PuLP
1. [ ] [NetworkX's bipartite graph](https://networkx.org/documentation/stable/reference/algorithms/bipartite.html#module-networkx.algorithms.bipartite.matching)
    - <https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.bipartite.matching.minimum_weight_full_matching.html#networkx.algorithms.bipartite.matching.minimum_weight_full_matching>
    - defers to SciPY: <https://networkx.org/documentation/stable/_modules/networkx/algorithms/bipartite/matching.html#minimum_weight_full_matching>


## Q&A
1. The Hungarian algorithm feels sophisticated. Is there anything which assured Mr. Kuhn of its success, before his
   diving into designing such complex algorithm? I mean, it will be a huge waste if, after much struggling and
   effort, we end up with a solution with the same worst-case complexity of $O(n!)$.


## Refs
1. <https://math.mit.edu/~goemans/18433S09/matching-notes.pdf>
    - <http://www.lix.polytechnique.fr/~ollivier/JACOBI/bibliographie.html>
    - <http://www.lix.polytechnique.fr/~ollivier/Borne_Jacobi_I/>



