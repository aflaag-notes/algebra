# Polinomi

## Def

- **Polinomi**
> - $\mathbb{K}$ campo
> - $a(x) := \displaystyle{\sum_{k = 0}^na_kx^k} = a_0x^0 + \ldots + a_nx^n$ è un **polinomio**
> - $\mathbb{K}[x] := \{a_0x^0 + \ldots + a_n x^n \mid a_0, \ldots a_n \in \mathbb{K}\}$ è l'**insieme dei polinomi a coefficienti in $\mathbb{K}$**

## Oss

- **Hp**
    - ($\mathbb{K}, +, \cdot)$ anello
- **Th**
    - $(\mathbb{K}[x], +, \cdot)$ è un anello
- **Dim**
    - le operazioni $+$ e $\cdot$ sono ben definite
        - $p(x), q(x) \in \mathbb{K}[x] \mid p(x) =  \displaystyle{\sum_{i = 0}^n a_ix^i} \land q(x) = \displaystyle{\sum_{j = 0}^m b_jx^j}$
        - $p(x) + q(x) = \displaystyle{\sum_{k = 0}^{+\infty}{(a_k + b_k)}}x^k$
            - ogni termine presente in solo uno dei due polinomi, varra $0$ nell'altro, di conseguenza la sommatoria che va a $+ \infty$ ha significato
        - $p(x) \cdot q(x) = \displaystyle \sum_{i = 0}^n \left( \sum_{j = 0}^{m}{a_ib_j x^{i + j }}\right)$
    - $(\mathbb{K}[x], +)$ gruppo abeliano
        - per come $+$ è definita, è associativa
        - l'elemento neutro rispetto a $+$ è costituito dal polinomio nullo $a(x) = 0$
        - $\forall a(x) := \displaystyle{\sum_{i = 0}^{n}{a_i x^i}}\in \mathbb{K}[x] \quad \exists-a(x)= - \displaystyle {\sum_{i = 0}^n{a_i x^i}}$
        - per come $+$ è definita, è commutativa
    - $(\mathbb{K}[x], \cdot)$ monoide
        - per come $\cdot$ è definita, è associativa
        - l'elemento neutro rispetto a $\cdot$ è costituito da $a(x) = 1\cdot x^0 = 1$
    - per come $+$ e $\cdot$ sono definite $\forall a(x), b(x), c(x) \in \mathbb{K}[x] \quad a(x) \cdot (b(x) + c(x)) = a(x) \cdot b(x) + a(x) \cdot c(x)$

## Def

- **Grado del polinomio**
> - $a(x) = a_0x^0 + \ldots + a_nx^n \in \mathbb{K}[x]$
> - $\deg(a(x)):=\left\{\begin{array}{ll} n & a(x) \neq 0 \\ - \infty & a(x) = 0\end{array}\right.$

## Oss

- **Hp**
    - $a(x), b(x) \in \mathbb{K}[x]$
- **Th**
    - $\deg(a(x) \cdot b(x)) = \deg(a(x)) + \deg(b(x)))$
- **Dim**
    - $a(x) \neq 0 \implies a(x) = a_0x^0 + \ldots + a_nb^n \implies \deg(a(x)) = n$
    - $b(x) \neq 0 \implies b(x) = b_0x^0 + \ldots + b_mx^m \implies \deg(b(x)) = m$
    - dunque $\deg(a(x))\cdot \deg(b(x))$
