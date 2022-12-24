# Determinante

## Def

- **Applicazione multilineare**

> - $\mathbb{K}$ campo
> - $k \in \mathbb{N}$
> - $V_1, \ldots, V_k, W$ spazi vettoriali
> - $f: V_1 \times \ldots \times V_k \rightarrow W:(v_1, \ldots, v_k) \rightarrow w$
    > - $f$ **multilineare** $\iff \forall i \in [1, k], \ \forall v_1 \in V_1, \ldots, v_i', v_i'' \in V_i, \ldots, v_k \in V_k, \ \forall \lambda, \mu \in \mathbb{K} \quad f(v_1, \ldots, \lambda v_i'+\mu v_i'', \ldots, v_k) = \lambda f(v_1, \ldots, v_i', \ldots, v_k) + \mu f(v_1, \ldots, v_i'', \ldots, v_k)$

- **Determinante**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N} - \{0\}$
> - $\det : \textrm{Mat}_{n \times n}(\mathbb{K}) \rightarrow \mathbb{K}$
> - 1. $\forall A \in \textrm{Mat}_{n \times n}(\mathbb{K}) \quad \det$ multilineare su $A_1, \ldots A_n$ e $A^1, \ldots, A^n$
> - 2. $\forall A \in \textrm{Mat}_{n \times n}(\mathbb{K}) \quad A_1, \ldots A_n$ e $A^1, \ldots, A^n$ basi di $\mathbb{K}^n \iff \det(A) \neq 0$
> - 3. $\det(I_n) = 1$
> - 4. per $\mathbb{K} \mid 1 \neq -1 \quad$ **⚠️  SCRIVI DETERMINANTE ALTERNANTE**
> - $\det$ è il **determinante** $\iff \det$ verifica 1, 2 e 3, oppure 1, 3 e 4
>   - poiché è possibile dimostrare che la funzione che verifica tali condizioni esiste ed è unica, allora il $\det$ è totalmente determinato da tali caratteristiche

## Oss

- **Hp**
    - $\mathbb{K}$ campo $\mid 1 \neq -1$
    - $n \in \mathbb{N} - \{0\}$
    - $f : \textrm{Mat}_{n \times n}(\mathbb{K}) \rightarrow \mathbb{K}$
    4. **⚠️  SCRIVI**
- **Th**
    - **⚠️  DETERMINANTE ALTERNANTE**

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N} - \{0\}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
    1. $A$ invertibile
    2. $A_1, \ldots, A_n$ base di $\mathbb{K}^n$
    3. $A^1, \ldots, A^n$ base di $\mathbb{K}^n$
    4. $\textrm{rk}(A)=n$
    5. $\det(A) \neq 0$
    6. $A \equiv I_n$ tramite la relazione di equivalenza delle operazioni sulle righe
    7. **⚠️  NON ANCHE PER COLONNE? CEH PENSO DE SI**
- **Th**
    - le proposizioni sono equivalenti
- **Dim**
    - **⚠️  alcune le ha fatte**

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N} - \{0\}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K}) \mid \exists i \in [1, n] : A_i = 0_{\mathbb{K}^n} \lor \exists j \in [1, n] : A^j = 0_{\mathbb{K}^n}$, ovvero in $A$ è presente o una riga, o una colonna nulla
- **Th**
    - $\det(A) = 0$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N} - \{0\}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
- **Th**
    - $\det(A) = \det(A^T)$

## Formula di Leibniz

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N} - \{0\}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
- **Th**
    - $\displaystyle{\det(A) = \sum_{\sigma \in S_n} \textrm{sgn}(\sigma) \cdot \prod_{i=1}^n{a_{i, \sigma_i}}}$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $A \in \textrm{Mat}_{2 \times 2}(\mathbb{K})$
    - $A = \left(\begin{array}{cc}a_{1,1} & a_{1, 2} \\ a_{2, 1} & a_{2, 2}\end{array}\right)$
- **Th**
    - $\det(A) = a_{1,1}a_{2,2}-a_{1,2}a_{2,1}$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $A \in \textrm{Mat}_{3 \times 3}(\mathbb{K})$
    - $A = \left(\begin{array}{ccc}a_{1,1} & a_{1, 2} & a_{1,3}\\ a_{2, 1} & a_{2, 2} & a_{2,3} \\ a_{3,1} & a_{3,2} & a_{3,3}\end{array}\right)$
- **Th**
    - $\det(A) = a_{1,1}a_{2,2}a_{3,3}+a_{1,3}a_{2,1}a_{3,2}+a_{1,2}a_{2,3}a_{3,1} - a_{1,3}a_{2,2}a_{3,1}-a_{1,1}a_{2,3}a_{3,2}-a_{1,2}a_{2,1}a_{3,3}$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N} - \{0\}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K}) \mid A$ triangolare
- **Th**
    - $\det(A) = a_{1,1} \cdot \ldots \cdot a_{n, n}$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N} - \{0\}$
    - $\lambda \in \mathbb{K}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
    - $A' = \left(\begin{array}{c}A_1 \\ \vdots \\ \lambda A_i \\ \vdots \\ A_n \end{array}\right)$
- **Th**
    - $\det(A')=\lambda \cdot \det(A)$
- **Dim**
    - **⚠️  credo abbia a che fare con la multilinearità, inoltre aggiungi anche il terzo tipo di operazione che non cambia un cazzo**

## Formula di Laplace

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N} - \{0\}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
- **Th**
    - $\forall 1 \le i, j \le n \quad \det(A) = \displaystyle \sum_{k = 1}^{n}{(-1)^{i + k}\cdot a_{i, k} \cdot \det(A_i^k)} = \sum_{h = 1}^n{(-1)^{h + j}\cdot a_{h, j} \cdot \det(A_h^j)}$

## Def

- **Aggiunta di una matrice**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N} - \{0\}$
> - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
> - $A^*$ è detta **aggiunta di $A$** $\iff \forall i, j \in [1, n] \quad a^*_{i, j} = (-1)^{i + j}\cdot \det(A_i^j)$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N} - \{0\}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K}) \mid \det(A) \neq 0$
- **Th**
    - $A^{-1}=\dfrac{(A^*)^T}{\det(A)}$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $A \in \textrm{Mat}_{2 \times 2}(\mathbb{K}) \mid \det(A) \neq 0$
    - $A = \left(\begin{array}{cc}a & b \\ c & d\end{array}\right)$
- **Th**
    - $A^{-1}=\dfrac{1}{ad - bc} \left(\begin{array}{cc}d & -b \\ -c & a\end{array}\right)$

****

# Polinomio caratteristico

## Def

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N} - \{0\}$
> - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
> - $p_A(x) := \det(x\cdot I_n - A)$ è detto **polinomio caratteristico di $A$**

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N} - \{0\}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
- **Th**
    - $p_A(x) = x^n - \textrm{tr}(A)\cdot x^{n -1} + \ldots + (-1)^n \cdot \det(A)$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N} - \{0\}$
    - $A, B \in \textrm{Mat}_{n \times n}(\mathbb{K}) \mid A$ simile a $B$
- **Th**
    - $p_A(x) = p_B(x)$

## Def

- **Autovalore**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N} - \{0\}$
> - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
> - $\lambda \in \mathbb{K} \mid p_A(\lambda) = 0$ è detto **autovalore di $A$**

- **Spettro**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N} - \{0\}$
> - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
> - $\textrm{sp}(A) := \{\lambda \in \mathbb{K} \mid p_A(\lambda) = 0\}$ è detto **spettro di $A$**

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N} - \{0\}$
    - $A, B \in \textrm{Mat}_{n \times n}(\mathbb{K}) \mid A$ simile a $B$
- **Th**
    - $\textrm{sp}(A) = \textrm{sp}(B)$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N} - \{0\}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
    - $\lambda \in \mathbb{K}$
- **Th**
    - $\lambda$ autovalore $\iff \exists v \in \mathbb{K}^n - \{0\} \mid A \cdot v = \lambda \cdot v$
- **Dim**
    - $\exists v \in \mathbb{K}^n - \{0\} \mid A \cdot v = \lambda \cdot v = \lambda \cdot I_n \cdot v \iff \exists v \in \mathbb{K}^n - \{0\} \mid (A - \lambda \cdot I_n)\cdot v = 0 \iff v \in \ker(L_{A - \lambda \cdot I_n})$
    - di conseguenza $\ker(L_{A - \lambda \cdot I_n}) \neq \{0\} \implies \dim(\ker(L_{A - \lambda \cdot I_n})) \gt 0$
    - per il teorema del rango $\textrm{rk}(L_{A - \lambda \cdot I_n}) = \dim(\mathbb{K}^n) - \dim(\ker(L_{A - \lambda \cdot I_n})) = n - \dim(\ker(L_{A - \lambda \cdot I_n})) \lt n$, in particolare $\textrm{rk}(L_{A-\lambda \cdot I_n}) \neq n$
    - $\textrm{rk}(L_{A- \lambda \cdot I_n}) \neq n \iff \det(A - \lambda \cdot I_n) = 0$ per dimostrazione precedente, e $\det(A - \lambda \cdot I_n) = p_A(\lambda) = 0 \iff \lambda$ autovalore

## Def

- **Autovettore**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N} - \{0\}$
> - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
> - $\lambda \in \textrm{sp}(A)$
> - $v \in \mathbb{K}^n - \{0\}$ è detto **autovettore di $A$ relativo a $\lambda$** $\iff (A- \lambda \cdot I_n) \cdot v = 0$

- **Autospazio**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N} - \{0\}$
> - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
> - $\lambda \in \textrm{sp}(A)$
> - $\textrm{E}_\lambda(A) := \{v \in \mathbb{K}^n \mid A \cdot v = \lambda \cdot v\}$ è detto **autospazio di $A$ relativo a $\lambda$**

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N} - \{0\}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
    - $\lambda \in \textrm{sp}(A)$
- **Th**
    - $\textrm{E}_\lambda(A) \subset \mathbb{K}$ sottospazio vettoriale

