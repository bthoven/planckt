# plancktables

Provide a Python interface for the current Planck results for cosmological parameters.

> NOTE: The current version supports only the Planck 2018 results for the base LCDM model provided by table 2 of [1807.06209](https://arxiv.org/abs/1807.06209).


## Simple Usage

```python
>>> from plancktables import lcdm
>>>
>>> H0 = lcdm.Planck18Param("H_0", "TT,TE,EE+lowE+lensing+BAO")
>>> print(H0.value)
67.66
>>> print(H0.limit68)
0.42
>>> print(H0.units)
'km/s/Mpc'
```


## The Variables

The following table shows the mapping between the names of the variables in that paper and in `plancktables`:

| name in the paper                                                                 | name in `plancktables`  |
|:---------------------------------------------------------------------------------:|:-----------------------:|
| <img src="https://latex.codecogs.com/gif.latex?\Omega_\text{b}h^2" />             | `Omega_b__h2`           |
| <img src="https://latex.codecogs.com/gif.latex?\Omega_\text{c}h^2" />             | `Omega_c__h2`           |
| <img src="https://latex.codecogs.com/gif.latex?100\theta_\text{MC}" />            | `100theta_MC`           |
| <img src="https://latex.codecogs.com/gif.latex?\tau" />                           | `tau`                   |
| <img src="https://latex.codecogs.com/gif.latex?\ln{(10^{10}A_\text{s})}" />       | `ln(10^10A_s)`          |
| <img src="https://latex.codecogs.com/gif.latex?n_\text{s}" />                     | `n_s`                   |
| <img src="https://latex.codecogs.com/gif.latex?H_0" />                            | `H_0`                   |
| <img src="https://latex.codecogs.com/gif.latex?\Omega_\Lambda" />                 | `Omega_Lambda`          |
| <img src="https://latex.codecogs.com/gif.latex?\Omega_\text{m}" />                | `Omega_m`               |
| <img src="https://latex.codecogs.com/gif.latex?\Omega_\text{m}h^2" />             | `Omega_m__h2`           |
| <img src="https://latex.codecogs.com/gif.latex?\Omega_\text{m}h^3" />             | `Omega_m__h3`           |
| <img src="https://latex.codecogs.com/gif.latex?\sigma_8" />                       | `sigma_8`               |
| <img src="https://latex.codecogs.com/gif.latex?S_8" />                            | `S_8`                   |
| <img src="https://latex.codecogs.com/gif.latex?\sigma_8\Omega_\text{m}^{0.25}" /> | `sigma_8__Omega_m^0.25` |
| <img src="https://latex.codecogs.com/gif.latex?z_\text{re}" />                    | `z_re`                  |
| <img src="https://latex.codecogs.com/gif.latex?10^9A_\text{s}" />                 | `10^9A_s`               |
| <img src="https://latex.codecogs.com/gif.latex?10^9A_\text{s}e^{-2\tau}" />       | `10^9A_s__e^-2tau`      |
| <img src="https://latex.codecogs.com/gif.latex?\text{Age}" />                     | `Age`                   |
| <img src="https://latex.codecogs.com/gif.latex?z_*" />                            | `z_*`                   |
| <img src="https://latex.codecogs.com/gif.latex?r_*" />                            | `r_*`                   |
| <img src="https://latex.codecogs.com/gif.latex?100\theta_*" />                    | `100theta_*`            |
| <img src="https://latex.codecogs.com/gif.latex?z_\text{drag}" />                  | `z_drag`                |
| <img src="https://latex.codecogs.com/gif.latex?r_\text{drag}" />                  | `r_drag`                |
| <img src="https://latex.codecogs.com/gif.latex?k_\text{D}" />                     | `k_D`                   |
| <img src="https://latex.codecogs.com/gif.latex?z_\text{eq}" />                    | `z_eq`                  |
| <img src="https://latex.codecogs.com/gif.latex?k_\text{eq}" />                    | `k_eq`                  |
| <img src="https://latex.codecogs.com/gif.latex?100\theta_\text{s,eq}" />          | `100theta_s,eq`         |
| <img src="https://latex.codecogs.com/gif.latex?f_{2000}^{143}" />                 | `f_2000^143`            |
| <img src="https://latex.codecogs.com/gif.latex?f_{2000}^{143\times217}" />        | `f_2000^143x217`        |
| <img src="https://latex.codecogs.com/gif.latex?f_{2000}^{217}" />                 | `f_2000^217`            |
