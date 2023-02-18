`scipy` adapts different algorithms for the function `linear_sum_assignment()` through the years.
At the time when I notice linear assignment problem (i.e. July 2022), `scipy` has shifted from
**Hungarian method** to **Jonker-Volgenant algorithm**.

- For its Hungarian method implementation, cf.
    - <https://github.com/scipy/scipy/blob/v0.18.1/scipy/optimize/_hungarian.py#L13-L107> (For convenience, I have also downloaded this file to `$PWD`)
    - <https://docs.scipy.org/doc/scipy-0.18.1/reference/generated/scipy.optimize.linear_sum_assignment.html>
- For its Jonker-Volgenant algorithm implementation, I haven't been able to track down the exact code.
  Indeed, if one uses conda, then one could only find in `site-packages/scipy/optimize/`
  the two following related files:
  ```bash
  _lsap_module.cpython-310-x86_64-linux-gnu.so
  _lsap.py
  ```
  In `_lsap.py`, it simply imports and uses `_lsap_module.calculate_assignment()`. One needs to dig deeper into
  where this module's code is.
