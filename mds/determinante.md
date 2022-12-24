# Determinante

## Def

- **Applicazione multilineare**

> - $k \in \mathbb{N}$
> - $V_1, \ldots, V_k, W$ spazi vettoriali
> - $f: V_1 \times \ldots \times V_k \rightarrow W:(v_1, \ldots, v_k) \rightarrow w$
    > - $f$ **multilineare** $\iff \forall i \in [1, k], \ \forall v_1 \in V_1, \ldots, v_i', v_i'' \in V_i, \ldots, v_k \in V_k, \ \forall \lambda, \mu \in \mathbb{K} \quad f(v_1, \ldots, \lambda v_i'+\mu v_i'', \ldots, v_k) = \lambda f(v_1, \ldots, v_i', \ldots, v_k) + \mu f(v_1, \ldots, v_i'', \ldots, v_k)$

- **Determinante**

> - $n \in \mathbb{N} - \{0\}$
> - $\mathbb{K}$ campo
> - $\det : \textrm{Mat}_{n \times n}(\mathbb{K}) \rightarrow \mathbb{K}$
> - 1. $\forall A \in \textrm{Mat}_{n \times n}(\mathbb{K}) \quad \det$ multilineare su $A_1, \ldots A_n$ e $A^1, \ldots, A^n$
> - 2. $\forall A \in \textrm{Mat}_{n \times n}(\mathbb{K}) \quad A_1, \ldots A_n$ e $A^1, \ldots, A^n$ basi di $\mathbb{K}^n \iff \det(A) \neq 0$
> - 3. $\det(I_n) = 1$
> - 4. per $\mathbb{K} \mid 1 \neq -1 \quad$ **⚠️  SCRIVI DETERMINANTE ALTERNANTE**
> - $\exists ! \det: \textrm{Mat}_{n \times n}(\mathbb{K}) \rightarrow \mathbb{K} \mid$ sono verificate 1, 2 e 3, oppure 1, 3 e 4


## Oss

- **Hp**
    - $n \in \mathbb{N} - \{0\}$
    - $\mathbb{K}$ campo $\mid 1 \neq -1$
    - $f : \textrm{Mat}_{n \times n}(\mathbb{K}) \rightarrow \mathbb{K}$
    4. **⚠️  SCRIVI**
- **Th**
    - **⚠️  DETERMINANTE ALTERNANTE**

## Formula di Leibniz

- **Hp**
    - $n \in \mathbb{N} - \{0\}$
    - $\mathbb{K}$ campo
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
- **Th**
    - $\displaystyle{\det(A) = \sum_{\sigma \in S_n} \textrm{sgn}(\sigma) \cdot \prod_{i=1}^n{a_{i, \sigma_i}}}$

## Oss

- **Hp**
    - $A \in \textrm{Mat}_{2 \times 2}(\mathbb{K})$
    - $A = \left(\begin{array}{cc}a_{1,1} & a_{1, 2} \\ a_{2, 1} & a_{2, 2}\end{array}\right)$
- **Th**
    - $\det(A) = a_{1,1}a_{2,2}-a_{1,2}a_{2,1}$

## Oss

- **Hp**
    - $A \in \textrm{Mat}_{3 \times 3}(\mathbb{K})$
    - $A = \left(\begin{array}{cc}a_{1,1} & a_{1, 2} & a_{1,3}\\ a_{2, 1} & a_{2, 2} & a_{2,3} \\ a_{3,1} & a_{3,2} & a_{3,3}\end{array}\right)$
- **Th**
    - $\det(A) = a_{1,1}a_{2,2}a_{3,3}+a_{1,3}a_{2,1}a_{3,2}+a_{1,2}a_{2,3}a_{3,1} - a_{1,3}a_{2,2}a_{3,1}-a_{1,1}a_{2,3}a_{3,2}-a_{1,2}a_{2,1}a_{3,3}$
