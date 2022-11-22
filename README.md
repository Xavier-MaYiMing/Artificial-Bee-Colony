### Artificial Bee Colony

##### Reference: Karaboga D. An idea based on honey bee swarm for numerical optimization[J]. Technical Report-TR06, Kayseri, Turkey: Erciyes University; 2005.

| Variables   | Meaning                                                      |
| ----------- | ------------------------------------------------------------ |
| pop         | The number of bees                                           |
| iter        | The iteration number                                         |
| lb          | The lower bound (list)                                       |
| ub          | The upper bound (list)                                       |
| pos         | The set of bees (list)                                       |
| score       | The score of bees (list)                                     |
| dim         | Dimension (list)                                             |
| trail       | The non-improvement number of each solution (list)           |
| trail_limit | The maximum non-improvement number. Once exceed this number, the scout bee procedure is triggered. |
| gbest       | The score of the global best score                           |
| gbest_pos   | The position of the global best (list)                       |
| iter_best   | The global best score of each iteration (list)               |
| con_iter    | The last iteration number when "gbest" is updated            |

#### Test problem: Pressure vessel design

![](https://github.com/Xavier-MaYiMing/Artificial-Bee-Colony/blob/main/Pressure%20vessel%20design.png)

$$
\begin{align}
&\text{min}\ f(x)=0.6224x_1x_3x_4+1.7781x_2x_3^2+3.1661x_1^2x_4+19.84x_1^2x_3,\\
&\text{s.t.} \\
&-x_1+0.0193x_3\leq0,\\
&-x_3+0.0095x_3\leq0,\\
&-\pi x_3^2x_4-\frac{4}{3}\pi x_3^3+1296000\leq0,\\
&x_4-240\leq0,\\
&0\leq x_1\leq99,\\
&0\leq x_2 \leq99,\\
&10\leq x_3 \leq 200,\\
&10\leq x_4 \leq 200.
\end{align}
$$


#### Example

```python
if __name__ == '__main__':
    # Parameter settings
    pop = 50
    iter = 300
    lb = [0, 0, 10, 10]
    ub = [99, 99, 200, 200]
    print(main(pop, iter, lb, ub))
```

##### Output:

![](https://github.com/Xavier-MaYiMing/Artificial-Bee-Colony/blob/main/convergence%20curve.png)

The ABC converges at its 203-th iteration, and the global best value is 8050.913534658795. 

```python
{
    'best score': 8050.913534658795, 
    'best solution': [1.3005502034963052, 0.6428626394484327, 67.3860209065443, 10.000000000000002], 
    'convergence iteration': 203
}
```

