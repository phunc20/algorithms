## Environment
To run `comparison.py`, I used Python3.10. Nevertheless, I think that all
Python3.8+ will work as well.

The required Python packages are listed in `requirements.txt` and could be installed in the command line by
```bash
$ pip install -r requirements.txt
```

As usual, better install them in a virtual environment instead of in the system Python of your machine.


## PuLP
PuLP seems to provide usage of different solvers. However, it seems that one cannot
just use whichever solver. Instead, if one desires to use a non-default solver, one
needs to install that solver to their system.

For example, the [GLPK (GNU Linear Programming Kit)](https://www.gnu.org/software/glpk/)
could be installed as follows:
- Linux: Use your Linux distro's package manager, e.g.
  ```sh
  # Arch Linux
  $ sudo pacman -S glpk
  # Debian
  $ sudo apt install glpk glpk-utils
  ```
- MacOS
  ```sh
  # Homebrew
  $ brew install glpk
  ```
- Windows: I'm not a Windows user, but it seems that one may download and install
  from
    - Either <https://winglpk.sourceforge.net/>
    - Or <https://sourceforge.net/projects/winglpk/>
- Conda users: This seems to be particularly good in that this is platform-independent.
  ```sh
  $ conda install -c conda-forge glpk
  ```

Read more about solvers and their installation in
[this blog post](https://realpython.com/linear-programming-python/)


## How to Use This Directory
- `comparison.py`: This script compares performances of different algorithms/solutions of linear
  assignment problem. Here are a few ways to run it:
  ```
  # Run default 10x10 rating matrix
  $ python comparison.py
  # Run some rectangular rating matrices
  $ python comparison.py --rows 5 --cols 7
  # Or equiv.
  $ python comparison.py -m 5 -n 7
  ```


## TODO
`comparison.py`
1. [x] Add flag to max/min the problem
1. [x] Add solution using PuLP
1. [ ] [NetworkX's bipartite graph](https://networkx.org/documentation/stable/reference/algorithms/bipartite.html#module-networkx.algorithms.bipartite.matching)
    - <https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.bipartite.matching.minimum_weight_full_matching.html#networkx.algorithms.bipartite.matching.minimum_weight_full_matching>
    - defers to SciPY: <https://networkx.org/documentation/stable/_modules/networkx/algorithms/bipartite/matching.html#minimum_weight_full_matching>
    - <https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csgraph.maximum_bipartite_matching.html>


## Q&A
1. The Hungarian algorithm feels sophisticated. Is there anything which assured Mr. Kuhn of its success, before his
   diving into designing such complex algorithm? I mean, it will be a huge waste if, after much struggling and
   effort, we end up with a solution with the same worst-case complexity of $O(n!)$.


## Refs
1. Jacobi
    - <http://www.lix.polytechnique.fr/~ollivier/JACOBI/bibliographie.html>
    - <http://www.lix.polytechnique.fr/~ollivier/Borne_Jacobi_I/>
2. Optimal Control
    - [POT](https://github.com/PythonOT/POT)
        - <https://pythonot.github.io/auto_examples/plot_OT_2D_samples.html#sphx-glr-auto-examples-plot-ot-2d-samples-py>
        - <https://pythonot.github.io/auto_examples/plot_Intro_OT.html#sphx-glr-auto-examples-plot-intro-ot-py>
3. Integer Programming
    - <https://realpython.com/linear-programming-python/>
    - <https://math.mit.edu/~goemans/18433S09/matching-notes.pdf>
