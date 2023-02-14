# Induzione

## Def

- **Induzione**

> - $P_{1}, P_{2}, P_{3}, \ldots$ successione infinita di proposizioni $\mid P_{1}$ vera e $\forall n \ge 1 \quad P_{1}, \ldots, P_{n} \implies P_{n+1}$
> - allora $\forall n \quad P_n$ vera

## Ex

- **Hp**
  - $\left\{\begin{array}{l}F_0 = 0 \\ F_1 = 1 \\ F_n = F_{n - 1} + F_{n - 2} \quad n \ge 2\end{array}\right.$ è detta _sequenza di Fibonacci_

  - $x^2 -x -1 = 0$ ha come soluzioni $\left\{\begin{array}{l}\varphi := \dfrac{1+\sqrt{5}}{2} \\ \psi := \dfrac{1 - \sqrt{5}}{2}\end{array}\right.$
- **Th**
  - $\forall n \in \mathbb{N} \quad F_{n}=\dfrac{\varphi^{n}-\psi^{n}}{\varphi-\psi}=\dfrac{\varphi^{n}-\psi^{n}}{\sqrt{5}}$
- **Dim**
  - $n = 0 \implies F_0 = \dfrac{\varphi^0 - \psi^0}{\sqrt 5} = \dfrac{1 - 1}{\sqrt 5} = 0$
  - $n = 1 \implies F_1 = \dfrac{\varphi^1 - \psi^1}{\varphi - \psi} = 1$
  - per il passo induttivo, al posto di trovare il caso $n$ nel caso $n+ 1$, si trova il caso $n - 1$ nel caso $n$
    - $F_n = F_{n - 1} + F_{n - 2}$ per ipotesi induttiva, dunque $F_n = \dfrac{\varphi^{n - 1} - \psi^{n - 1}}{\sqrt 5} + \dfrac{\varphi ^{n - 2} - \psi ^{n - 2}}{\sqrt 5} = \dfrac{\varphi ^{n - 1} - \psi^{n - 1} + \varphi^{n - 2} - \psi^{n - 2}}{\sqrt 5} =\dfrac{(\varphi^{n - 1} + \varphi^{n - 2}) - (\psi^{n - 1} - \psi^{n - 2})}{\sqrt 5}$ $=\dfrac{\varphi^{n-2}(\varphi+1)-\psi^{n-2}(\psi+1)}{\sqrt{5}}$
    - $\left.\begin{array}{l}\varphi^{2}=\varphi+1 \\ \psi^{2}=\psi+1\end{array}\right\} \implies \dfrac{\varphi^{n-2} \cdot \varphi^{2}-\psi^{n-2} \cdot \psi^{2}}{\sqrt{5}} = \dfrac{\varphi^n - \psi^n }{\sqrt 5}$

