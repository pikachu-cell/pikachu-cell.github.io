---
date: 2026-01-22
title: When does a Unique Solution for an ODE
math: true
draft: "false"
---

# The Picard–Lindelöf Theorem

Consider an ordinary differential equation of the form

$$
y^{\prime} = f(x, y).
$$

Let us understand what each symbol means:

- $x$ is an independent variable.
- $y(x)$ is a an unknown real valued function of $x$.
- $y^{\prime}$ is $\frac{dy}{dx}$ i.e., the derivative of $y$ with respect to $x$.
- $f(x, y)$ is a given function of two variables.


The following pair

$$
\begin{cases}
y^{\prime} = f(x, y) \\
y(x_{o}) = y_{o}
\end{cases}
$$
is called an **Initial Value Problem** or an *IVP*. Given an IVP, we are interested in finding out the form of the unknown real valued function $y$, under what conditions does the solution (the function $y$ is called the solution of the ODE) even exist and if a solution exists is it unique.

**Example**: Consider the following IVP

$$
\begin{cases}
y^{\prime} = |y|^{\alpha}, \quad \alpha \in(0, 1) \\
y(0) = 0
\end{cases}
$$

>We can verify that the family of functions parameterised by $c \geq 0$ as
>$$y_{c}(x) = \begin{cases} (1 - \alpha)^{\frac{1}{(1 - \alpha)}} (x -c)^{\frac{1}{1 - \alpha}}, \quad &c \leq x < \infty, \\ 0, \quad &0 \leq x\leq c \end{cases} $$
> satisfies the given IVP.

Thus for $\alpha \in (0, 1)$ solution exists but it is not unique. We are now interested in finding what hypothesis we can impose on $f(x, y)$ which can guarantee the existence of a unique solution of the following IVP

$$
\begin{cases}
y^{\prime} = f(x, y) \\
y(x_{o}) = y_{o}.
\end{cases}
$$

## The Statement of Picard–Lindelöf Theorem

Consider the initial value problem

$$
\begin{cases}
y^{\prime} = f(x, y) \\
y(x_{o}) = y_{o}.
\end{cases}
$$

Assume the following

1. The function $f: D \to \mathbb{R}$ is defined and continuous on the set $$
D := \{ (x, y) \mid x_{o} \leq x\leq X_{M}, |y - y_{o}| \leq C \}.
$$
2. There exists a constant $K>0$ such that $$
|f(x, y_{o})| \leq K \text{ for all } x_{o} \leq x \leq X_{M}.
$$
3. There exists a constant $L> 0$ such that $$
|f(x, u) - f(x, v)| \leq L |u - v| \text{ for all } (x, u), (x, v) \in D
$$, i.e., *Lipschitz* in the second argument.
4. The constant $C$ satisfies $$
C \geq \frac{K}{L}[\exp(L(X_{M} - x_{o})) - 1].
$$

Then there exists a **unique** solution $y \in C^{1}[x_{o}, X_{M}]$ satisfying the IVP

$$
\begin{cases}
y^{\prime} = f(x, y) \\
y(x_{o}) = y_{o}.
\end{cases}
$$
Moreover the solution satisfies 

$$
|y(x) - y_{o}| \leq C \text{ for all } x_{o} \leq x\leq X_{M},
$$
i.e., the solution remains inside the set $D$.

As  we shall later see, the continuity of $f$ guarantees the existence and the Lipschitz condition guarantees the uniqueness of the solution. The bound on $C$ ensures that the solution does not leave the set where our assumptions hold.

### Proof of the Picard–Lindelöf Theorem

Consider the IVP

$$
\begin{cases}
y^{\prime} = f(x, y) \\
y(x_{o}) = y_{o}.
\end{cases}
$$

We claim that this is equivalent to the following integral equation

$$
y(x) = y_{o} + \int_{x_{o}}^{x} f(s, y(s)) \,ds.
$$

We state a couple of theorem from Real Analysis whose proof you can see here[^1].

**Theorem A**: Let $f:[a, b] \to \mathbb{R}$ be integrable. For $x \in [a, b]$ set ^5cb9d1

$$
F(x) := \int_{a}^{x} f(t) \, dt.
$$
Then $F$ is continuous on $[a, b]$; furthermore if $f$ is continuous at a point $x_{o} \in [a, b]$, then $F$ is differentiable at $x_{o}$ and $F^{\prime}(x_{o}) = f(x_{o})$.

**Theorem B** (*Fundamental Theorem of Calculus*): Let $f:[a, b] \to \mathbb{R}$ be integrable and there exists a differentiable function $F:[a, b] \to \mathbb{R}$ such that $F^{\prime} = f$ then ^a2c918

$$
\int_{a}^{b} f(x) \, dx = F(b) - F(a).
$$
Let us assume that $y \in C^{1}[x_{o}, X_{M}]$ satisfies 

$$
\begin{cases}
y^{\prime} = f(x, y) \\
y(x_{o}) = y_{o}
\end{cases}
$$
Since $f$ is continuous and $y$ is continuous the composition $x \mapsto f(x, y(x))$ is also continuous. Hence by [[picard_lindelof#^a2c918|Theorem B]] we obtain,

$$
y(x) - y(x_{o}) = \int_{x_{o}}^{x} y^{\prime}(s) \, ds = \int_{x_{o}}^{x} f(x, y(s)) \, ds.
$$
Using the initial condition $y(x_{o}) = y_{o}$ we get

$$
y(x) = y_{o} + \int_{x_{o}}^{x} f(s, y(s)) \, ds.
$$

Conversely ,  let us assume that a continuous function $y$ satisfies

$$
y(x) = y_{o} + \int_{x_{o}}^{x} f(s, y(s)) \,ds.
$$
Again since $f$ and $y$ are continuous the integrand $s \mapsto f(s, y(s))$ is continuous on $[x_{o}, X_{M}]$. Then by [[picard_lindelof#^5cb9d1|Theorem A]] the function

$$
x \mapsto \int_{x_{o}}^{x}f(s, y(s)) \, ds
$$

is differentiable on $(x_{o}, X_{M})$ and the derivative equals the integrand, thus

$$
y^{\prime}(x) = f(x, y(x)) \text{ for all } x \in [x_{o}, X_{M}].
$$

Evaluating $y(x_{o})$ gives us $y_{o}$ do the initial condition is also satisfied.

Let us now define a sequence of functions $\{ y_{n} \}$ by

$$
\begin{align}
y_{0}(x) &= y_{o}  \\
y_{n + 1}(x)  &= y_{o} + \int_{x_{o}}^{x} f(s, y_{n}(s)) \, ds, \quad n = 1, 2, \dots 
\end{align}
$$

Since $f$ and $y_{n}$ are continuous, the function $y_{n + 1}$ is also continuous. The sequence will be well defined as long as $(x, y_{n}(x)) \in D$.

Let us estimate the difference between successive Picard iterates:

$$
|y_{n  +1}(x) - y_{n} (x)| = \int_{x_{o}}^{x} [f(s, y_{n}(s)) - f(s, y_{n - 1}(s))] \, ds.
$$

We claim that  for all $n \geq 1$

$$
|y_{n  +1}(x) - y_{n} (x)| \leq \frac{K}{L} \frac{[L(x - x_{o})]^{n}}{n!}.
$$

We show this via induction.

**Base Case**: For $n = 1$,

$$
|y_{1}(x) - y_{o}| = \int_{x_{o}}^{x}f(s, y_{o}) \, ds.
$$
Using the bound $|f(x, y_{o})| \leq K$ we obtain

$$
|y_{1}(x) - y_{o}| = K(x - x_{o}).
$$

Let us assume the result holds upto $n$. From the Lipschitz condition,

$$
|f(s, y_{n}(s)) - f(s, y_{n-1}(s))| \leq L|y_{n}(s) - y_{n - 1}(s)|.
$$
Using the inductive hypothesis,

$$
|y_{n  +1}(x) - y_{n} (x)| = \int_{x_{o}}^{x} \frac{K}{L} \frac{[L(s - x_{o})]^{n}}{n!} \, ds = \frac{K}{L} \frac{[L(x - x_{o})]^{n+ 1}}{(n + 1)!}.
$$
Thus our claim is proved.

We can further prove that

$$
\begin{align}
|y_{n}(x) - y_{o}|  & \leq \sum_{k = 1}^{n} |y_{k}(x) - y_{k - 1}(x)| \\
 & \leq \sum_{k = 1}^{n} \frac{K}{L} \frac{[L(x - x_{o})]^{k}}{k!}
\end{align}
$$
As the series $\sum_{j = 1}^{\infty} \frac{a^{j}}{j!}$ converges to $\exp(a) -1$ for all $a \in \mathbb{R}$ and the constant $C$ is bounded below by $\frac{K}{L}\exp[L(X_{M} - x_{o}) - 1]$ we obtain

$$
|y_{n}(x) - y_{o}| \leq \sum_{k = 1}^{n} \frac{K}{L} \frac{[L(x - x_{o})]^{k}}{k!} < \frac{K}{L}\exp[L(X_{M} - x_{o}) - 1] < C.
$$

Thus every $(x, y_{n}(x)) \in D$ for $n = 0, 1, 2, \dots$ and ensures that our assumptions on $f$ remain valid at each iteration.

We state another theorem from real analysis whose proof can be seen here[^1].

**Theorem C** (*Weierstrass M-test*): Suppose $\{ f_{n} \}$ be a sequence of functions defined on a set $E$ satisfies the following assumptions:

1. $|f_{n}(x)| \leq M_{n}$ for all $x \in E$ and $n = 1, 2, 3, \dots$
2. and, $\sum_{n \in \mathbb{N}}M_{n}$ converges.

Then $\sum_{n \in \mathbb{N}}f_{n}$ converges uniformly.

Since 

$$
|y_{n}(x) - y_{n - 1}(x)| \leq \frac{K}{L} \frac{[L(x - x_{o})]^{j}}{j!}
$$

and the series

$$
\sum_{j = 1}^{\infty} \frac{K}{L} \frac{[L(x - x_{o})]^{j}}{j!}
$$
converges, the series 

$$
\sum_{j = 1}^{\infty} [y_{j}(x) - y_{j - 1}(x)]
$$
converges uniformly. Let $S_{n} = \sum_{j =1}^{n}[y_{j}(x) - y_{j - 1}(x)] = y_{n}(x) - y_{o}$ be the partial sums then as $S_{n}$ converges uniformly $y_{n}$ converges uniformly to some function $y$.

We state a theorem that shows us when a limit and an integral sign can be exchanged, the proof can be seen here[^1].

**Theorem D** (*Limit and Integral Exchange*): Suppose $f_{n}:[a, b] \to \mathbb{R}$ be integrable and $f_{n} \to f$ uniformly on $[a, b]$ then $f$ is integrable on $[a, b]$ and  ^c8f9f4

$$
\lim_{ n  \to \infty } \int_{a}^{b}f_{n}(x)\, dx = \int_{a}^{b}f(x)\, dx.
$$
Form the definition of $y_{n + 1}$,

$$
y_{n + 1}(x) = y_{o} + \int_{x_{o}}^{x} f(s, y_{n}(s)) \, ds.
$$
Since $y_{n} \to y$ uniformly and $f$ is continuous,

$$
f(\cdot,y_{n}(\cdot)) \to f(\cdot, y(\cdot))
$$
uniformly.

Then using [[picard_lindelof#^c8f9f4|Theorem D]] and passing through the limit we obtain

$$
y(x) = y_{o} + \int_{x_{o}}^{x} f(s, y(s)) \, ds.
$$
By the [[picard_lindelof#^a2c918|Fundamental Theorem of Calculus]] 

$$
\begin{cases}
y^{\prime}(x) = f(x, y(x))  \\
y(x_{o}) = y_{o}.
\end{cases}
$$
and $y \in C^{1}[x_{o}, X_{M}]$. Hence the existence is proved.

Suppose $y$ and $z$ be two solutions in $C^{1}[x_{o}, X_{M}]$. Then estimating their difference we obtain

$$
y(x) - z(x) = \int_{x_{o}}^{x} [f(s, y(s)) - f(s, z(s)] \, ds.
$$

Using the Lipschitz condition,

$$
|y(x) - z(x)| \leq L \int_{x_{o}}^{x} |y(s) - z(s)| \, ds.
$$

Define $m = \max_{x_{o} \leq x \leq X_{M}} |y(x) - z(x)|$.  Then $|y(x) - z(x)| \leq mL(x - x_{o})$.  Upon iteration

$$
|y(x) - z(x)| \leq L \int_{x_{o}}^{x} mL(s - x_{o}) \, ds \leq m \frac{[L(x - x_{o})]^{2}}{2!}.
$$
Extending it we observer that

$$
|y(x) - z(x)| \leq m \frac{[L(x - x_{o})]^{k}}{k!} 
$$
for all integers $k \geq 1$. As $k \to \infty$, we obtain $|y(x) - z(x)| \leq 0$ as factorial dominates exponential. Thus $y(x) = z(x)$ for all $x \in [x_{o},X_{M}]$.

## Examples 1

Consider the linear equation

$$
y^{\prime} = py + q
$$

where $p$ and $q$ are constants. Let us check the whether it satisfies the hypothesis of Picard–Lindelöf theorem:

$$
|f(x, u) - f(x, v)| = |p||u - v|,
$$

hence it satisfies the Lipschitz condition in the second argument with $L = |p|$.

$$
|f(x, y_{o})| = |py_{o} + q| \leq |py_{o}| + |q| = K,
$$

and

Since $L$ and $K$ are independent of $C$, we can choose it to sufficiently large depending upon our choice of the interval $\left[ x_{o}, X_{M} \right]$. Hence, there exists a unique solution $y\in C^{1}[x_{o}, \infty)$.

## Example 2

Consider the following IVP

$$
y^{\prime} = y^{2} \quad y(0) = 1.
$$

Let us check the whether it satisfies the hypothesis of Picard–Lindelöf theorem:

$$
|f(x, u) - f(x, v)| = |u^{2} - v^{2}| = |u + v| |u - v|,
$$

as $|u| \leq 1 + C$ and $|v| \leq 1 + C$ then

$$
|f(x, u) - f(x, v)| \leq 2(1 + C) |u - v|.
$$
Hence $f(x, y)$ is Lipschitz in the second argument over the solution set with $L = 2(1 + C)$. Also $|f(x, 0)| = 0 \leq 1$. Thus

$$
C \geq\frac{1}{2(1 + C)} (\exp{[2(1 + C)X_{M} ]} - 1)
$$
 After some computation
$$
X_{M} \leq F(C) := \frac{1}{2(1 + C)} \ln{[1 + 2C + 2C^{2}]}.
$$
From the values of $F(C)$ we can find the maximum value of $X_{M}$.

---

## References

[^1]: *Principles of Mathematical Analysis*, Rudin
