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
> - $\mathbb{K}$ campo
> - $a(x) = a_0x^0 + \ldots + a_nx^n \in \mathbb{K}[x]$
> - $\deg(a(x)):=\left\{\begin{array}{ll} n & a(x) \neq 0 \\ - \infty & a(x) = 0\end{array}\right.$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $a(x), b(x) \in \mathbb{K}[x]$
- **Th**
    - $\deg(a(x) \cdot b(x)) = \deg(a(x)) + \deg(b(x))$
- **Dim**
    - $a(x) \neq 0 \implies a(x) = a_0x^0 + \ldots + a_nb^n \implies \deg(a(x)) = n$
    - $b(x) \neq 0 \implies b(x) = b_0x^0 + \ldots + b_mx^m \implies \deg(b(x)) = m$
    - dunque $\deg(a(x)) + \deg(b(x)) = n + m$
    - $a(x) \cdot b(x) = a_0b_0\cdot x^0 + \ldots + a_nb_m\cdot x^{n + m} \implies \deg(a(x) \cdot b(x)) = n + m$
        - per dimostrazione precedente $\mathbb{K}$ campo $\implies \mathbb{K}$ dominio di integrità, e dunque in $\mathbb{K}$ vale la legge di annullamento del prodotto, per cui $a_n, b_m \neq 0 \implies a_n \cdot b_m \neq 0$
    - di conseguenza $\deg(a(x) \cdot b(x)) = n + m = \deg(a(x)) + \deg(b(x))$
    - l'equazione è verificata anche quando almeno uno dei due polinomi è nullo, in quanto $\forall n \in \mathbb{N} \quad -\infty \pm n = -\infty \land -\infty -\infty = -\infty$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $a(x) \in \mathbb{K}[x] \mid \deg(a(x)) \ge 1$
- **Th**
    - $\nexists a^{-1}(x) \in \mathbb{K}[x]$
- **Dim**
    - $\forall b(x) \neq 0 \quad \deg(a(x) \cdot b(x)) \ge \deg(a(x)) \ge 1$
    - $\deg(1 \cdot x^0) = \deg(1) = 0$
    - ipotizzando che $\exists a^{-1}(x) \in \mathbb{K}[x]$, allora $a(x) \cdot a^{-1}(x) = 1$, dunque $\deg(a(x) \cdot a^{-1}(x)) = 0$, ma $\forall b(x) \quad \deg(a(x) \cdot b(x)) \ge 1 \ \bot$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
- **Th**
    - $\mathbb{K}[x]^* = \mathbb{K}^* \subset \mathbb{K}[x]$
- **Dim**
    - $\mathbb{K}[x]^* = \mathbb{K}^*$
        - $\forall a(x) \in\mathbb{K}[x] \mid a(x) = a_0 \neq 0$ polinomio costante non nullo, il polinomio inverso sarà costituito esclusivamente dal suo coefficiente $a_0^{-1} \in \mathbb{K}$
        - per dimostrazione precedente $\mathbb{K}$ campo $\implies \forall a_0 \in \mathbb{K} - \{0\} \quad \exists a_0^{-1} \in \mathbb{K} - \{0\}$
        - dunque $\exists a^{-1}(x) \quad a(x) \cdot a^{-1}(x) = a_0 \cdot a_0^{-1} = 1$
    - $\mathbb{K}^* \subset \mathbb{K}[x]$
        - $\mathbb{K}^* \subset \mathbb{K} \subset \mathbb{K}[x]$
        - per dimostrazione precedente, gli unici elementi invertibili in $\mathbb{K}[x]$ sono i polinomi costanti, che costituiscono un sottoinsieme di $\mathbb{K}[x]$, che coincide proprio con $\mathbb{K}$ poiché i polinomi costanti si identificano con un singolo coefficiente

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $a(x), b(x) \in \mathbb{K}[x] \mid b(x) \neq 0$
- **Th**
    - $\exists ! q(x), r(x) \in \mathbb{K}[x] \mid a(x) = b(x) \cdot q(x) + r(x) \quad \deg(r(x)) \lt \deg(b(x))$, che è detto _teorema della divisione con il resto tra polinomi_

## Def

- **Radici di un polinomio**
> - $\mathbb{K}$ campo
> - $p(x) \in \mathbb{K}[x]$
> - $\{c \in \mathbb{K}\ \mid p(c) = 0\}$ è l'**insieme delle radici di $p(x)$**

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $p(x) \in \mathbb{K}[x]$
    - $c \in \mathbb{K}$
- **Th**
    - $p(c) = 0 \iff x - c \mid p(x)$
- **Hp**
    - _prima implicazione_
        - per il teorema della divisione con il resto tra polinomi, dividendo $p(x)$ per $(x - c)$ si ottiene che $\exists!q(x), r(x) \in \mathbb{K}[x] \mid p(x) = q(x) \cdot (x - c) + r(x)$
        - $r_0 := r(x)$
        - $p(c) = q(c) (c - c) + r_0 = r_0$, ma $p(c) = 0$ in ipotesi, e dunque $r_0 = 0$
        - $r_0 = 0 \implies p(x) = q(x)(x - c) \implies x- c \mid p(x)$
    - _seconda implicazione_
        - $x - c \mid p(x) \implies \exists p(x) \in \mathbb{K}[x] : p(x) = q(x)\cdot (x - c)$, allora $p(c) = q(c) \cdot (c - c) = 0 \implies c$ radice di $p(x)$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $p(x) \in \mathbb{K}[x]$
    - $n := \deg(p(x))$
- **Th**
    - $|\{c \in \mathbb{K} \mid p(c) = 0\}| \le n$
- **Dim**
    - ipotizzando $N :=|\{c \in \mathbb{K} \mid p(c) = 0\}| \gt n \implies \{c_1, \ldots, c_N\}$ sia l'insieme delle radici
    - per dimostrazione precedente $\left.\begin{array}{c} x - c_1 \mid p(x) \\ \vdots \\ x-c_N \mid p(x) \end{array}\right\} \implies (x - c_1) \cdot \ldots \cdot (x - c_N) \mid p(x)$ ⚠️  **NON SI SA PERCHÉ**, ma $\deg\left((x - c_1) \cdot \ldots \cdot (x - c_N)\right) = N$, mentre $\deg(p(x)) = n$, dove $M \gt n \ \bot$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $I \subset \mathbb{K}[x]$ ideale
- **Th**
    - $I$ ideale principale
- **Dim**
    - _unicità_
        - $I = \{0\} \implies I = I(0)$, ovvero l'ideale principale generato da $0$
        - preso $p(x) \in I - \{0\} \mid \deg(p(x))$ sia il minore possibile, allora $\forall q(x) \in I \mid \deg(q(x)) \lt \deg(p(x)) \implies q(x) \in I(0) \implies q(x) = 0$, di conseguenza è unico in quanto l'elemento minore in $I - \{0\}$ è unico
    - _esistenza_
        - $\exists p(x) \in I - \{0\} \mid I = I(p(x))$, dove $p(x)$ è il polinomio di grado minore in $I - \{0\}$
            - $I \subset I(p(x))$
                - per il teorema della divisione con il resto tra polinomi $\forall a(x) \in I \quad \exists ! q(x), r(x) \mid a(x) = p(x) \cdot q(x) + r(x) \quad \deg(r(x)) \lt \deg(p(x)) \implies r(x) = a(x) - p(x) \cdot q(x)$
                - $\left.\begin{array}{l} a(x) \in I \\ p(x) \in I - \{0\} \implies p(x) \cdot q(x) \in I \end{array}\right\} \implies r(x) \in I$
                - ma poiché $\deg(r(x)) \lt \deg(p(x))$, e $p(x)$ è stato preso con il grado minore possibile, per osservazione precedente segue necessariamente che $r(x) = 0$, e dunque $a(x) = p(x) \cdot q(x) \implies a(x) \in I(p(x)) \implies I \subset I(p(x))$
            - $I(p(x)) \subset I$
                - $p(x) \in I - \{0\}$ e $I$ è un ideale per ipotesi, dunque in particolare $\mathbb{K}[x] \cdot I \subset I$, quindi $\forall q(x) \in \mathbb{K}[x] \quad q(x) \cdot p(x) \in I$
                - $\forall a(x) \in I(p(x)) \quad \exists q(x) \in \mathbb{K}[x] \mid q(x)\cdot p(x) = a(x)$, dunque $a(x) \in I$ per osservazione precedente, allora $I(p(x)) \subset I$
