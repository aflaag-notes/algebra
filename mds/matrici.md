# Matrici

## Def

- **Matrice**

> - $\mathbb{K}$ campo
> - $m, n \in \mathbb{N}$
> - $\textrm{Mat}_{m \times n}(\mathbb{K}):= \underbrace{\mathbb{K}^m \times \ldots \times \mathbb{K}^m}_{n \ \textrm{volte}}$ è detto **insieme delle matrici aventi $m$ righe e $n$ colonne a coefficienti in $\mathbb{K}$**

- **Vettori riga e vettori colonna**

> - $\mathbb{K}$ campo
> - $m, n \in \mathbb{N}$
> - $\forall v \in \textrm{Mat}_{1 \times n}(\mathbb{K}) \quad v = \left(x_1, \ldots, x_n\right)$ è detto **vettore riga**
> - $\forall v \in \textrm{Mat}_{m \times 1}(\mathbb{K}) \quad v = \left(\begin{array}{ccc} x_1 \\ \vdots \\ x_m \end{array}\right)$ è detto **vettore colonna**
> - $\forall A \in \textrm{Mat}_{m \times n}(\mathbb{K}) \quad \exists A^1, \ldots, A^n \in \mathbb{K}^m$ vettori colonna e $A_1, \ldots, A_m \in \mathbb{K}^n$ vettori riga $\mid A = \left(A^1, \ldots, A^n \right) = \left(\begin{array}{ccc} A_1 \\ \vdots \\ A_m\end{array}\right)$

## Def

- **$+$ tra matrici**

> - $\mathbb{K}$ campo
> - $m, n \in \mathbb{N}$
> - $\forall i \in [1, m], j \in [1, n] \quad a_{i, j}, b_{i, j} \in \mathbb{K}$
> - $A, B \in \textrm{Mat}_{m \times n}(\mathbb{K}) \mid A = \left(\begin{array}{ccc} a_{1, 1} & \cdots & a_{1, n} \\ \vdots & \ddots & \vdots \\ a_{m, 1} & \cdots & a_{m, n} \end{array}\right) \land B = \left(\begin{array}{ccc} b_{1, 1} & \cdots & b_{1, n} \\ \vdots & \ddots & \vdots \\ b_{m, 1} & \cdots & b_{m, n} \end{array}\right)$
> - $A + B = \left(\begin{array}{ccc} a_{1,1} + b_{1, 1} & \cdots & a_{1, n}+b_{1, n} \\ \vdots & \ddots & \vdots \\ a_{m,1}+b_{m, 1} & \cdots & a_{m,n}+b_{m, n} \end{array}\right)$ è detta **somma tra $A$ e $B$**
>   - in particolare, è definita solamente per matrice con stessa dimensione

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $m, n \in \mathbb{N}$
- **Th**
    - $\textrm{Mat}_{m \times n}(\mathbb{K})$ spazio vettoriale
    - $\dim(\textrm{Mat}_{m \times n}{\mathbb{K}}) = m \cdot n$

## Def

- **$\cdot$ tra matrici**

> - $\mathbb{K}$ campo
> - $l, m, n \in \mathbb{N}$
> - $A \in \textrm{Mat}_{l \times m}(\mathbb{K}) \mid A = \left(\begin{array}{ccc} a_{1, 1} & \cdots & a_{1, m} \\ \vdots & \ddots & \vdots \\ a_{l, 1} & \cdots & a_{l, m} \end{array}\right)$
> - $B \in \textrm{Mat}_{m \times n}(\mathbb{K}) \mid B = \left(\begin{array}{ccc} b_{1, 1} & \cdots & b_{1, n} \\ \vdots & \ddots & \vdots \\ b_{m, 1} & \cdots & b_{m, n} \end{array}\right)$
> - $C \in \textrm{Mat}_{l \times n}(\mathbb{K}) \mid C = AB$ è detto **prodotto tra $A$ e $B$**, ed è definito come $\left(\begin{array}{ccc}a_{1, 1}b_{1, 1} + \ldots + a_{1, m}b_{m, 1} & \cdots & a_{1, 1}b_{1, n} + \ldots + a_{1, m}b_{m,n} \\ \vdots & \ddots & \vdots \\a_{l,1}b_{1, 1} + \ldots + a_{l,m}b_{m, 1} & \cdots & a_{l,1}b_{1,n} + \ldots + a_{l, m}b_{m,n}\end{array}\right)$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $l, m, n, k \in \mathbb{N}$
    - $A \in \textrm{Mat}_{l \times m}(\mathbb{K})$
    - $B \in \textrm{Mat}_{m \times n}(\mathbb{K})$
- **Th**
    - $\forall C \in \textrm{Mat}_{n \times k}(\mathbb{K}) \quad (AB)C = A(BC)$
    - $\forall C \in \textrm{Mat}_{m \times n}(\mathbb{K}) \quad A(B+C) = AB+AC$
    - $\forall \lambda \in \mathbb{K} \quad \lambda(AB) = (\lambda A)B = A (\lambda B)$

****

# Rango

## Def

- **Moltiplicazione sinistra**

> - $\mathbb{K}$ campo
> - $m,n \in \mathbb{N}$
> - $A \in \textrm{Mat}_{m \times n}(\mathbb{K})$
> - $\mathscr{L}_A:\mathbb{K}^n \rightarrow \mathbb{K}^m: x \rightarrow Ax$ è detta **moltiplicazione sinistra di $A$**

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $m,n \in \mathbb{N}$
    - $A \in \textrm{Mat}_{m \times n}(\mathbb{K})$
- **Th**
    - $\mathscr{L}_A$ trasformazione lineare
- **Dim**
    - $\forall x, y \in \mathbb{K}^n \quad \mathscr{L}_A(x + y) = A(x + y) = Ax + Ay = \mathscr{L}_A(x) + \mathscr{L}_A(y)$
    - $\forall k \in \mathbb{K}, x \in \mathbb{K}^n \quad \mathscr{L}_A(kx) = A(kx) = k(Ax)=k\mathscr{L}_A(x)$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $m,n \in \mathbb{N}$
    - $A \in \textrm{Mat}_{m \times n}(\mathbb{K})$
- **Th**
    - $\ker(\mathscr{L}_A) = \textrm{span}(A_1, \ldots, A_m)^\bot$
    - $\textrm{im}(\mathscr{L}_A) = \textrm{span}(A^1, \ldots, A^n)$
- **Dim**
    - $\ker(\mathscr{L}_A) := \left\{x \in \mathbb{K}^n \mid \mathscr{L}_A(x) = 0_{\mathbb{K}^m} \iff A x = 0_{\mathbb{K}^m} \iff \left(\begin{array}{c}A_1\cdot x \\ \vdots \\ A_m \cdot x\end{array}\right)= \left(\begin{array}{c} 0 \\ \vdots \\ 0\end{array}\right)\right\} =: \textrm{span}(A_1, \ldots, A_m)^\bot$
    - $\textrm{im}(\mathscr{L}_A):=\left\{y \in \mathbb{K}^m \mid \exists x \in \mathbb{K}^n : y = \mathscr{L}_A(x) = A x = \left(\begin{array}{ccc} a_{1,1} & \cdots & a_{1,n}\\ \vdots & \ddots & \vdots \\ a_{m,1} & \cdots & a_{m,n}\end{array}\right) \left(\begin{array}{c} x_1 \\ \vdots \\ x_n \end{array}\right) =\right.$$\left.\left(\begin{array}{c}a_{1, 1} x_1 + \ldots + a_{1,n}x_n \\ \vdots \\ a_{m,1}x_1 + \ldots + a_{m,n} x_n \end{array}\right) =  x_1 \left(\begin{array}{c}a_{1, 1} \\ \vdots \\ a_{m, 1}\end{array}\right) + \ldots + x_n \left(\begin{array}{c}a_{1, n}\\ \vdots \\ a_{m, n}\end{array}\right) = x_1A^1 + \ldots + x_nA^n \right\}=:\textrm{span}(A^1, \ldots, A^n)$

## Oss

- **Rango di una matrice**

> - $\mathbb{K}$ campo
> - $m,n \in \mathbb{N}$
> - $A \in \textrm{Mat}_{m \times n}(\mathbb{K})$
> - $\textrm{rk}(A):=\textrm{rk}(\mathscr{L}_A)$ è detto **rango di $A$**
>   - in particolare $\textrm{rk}(A) := \textrm{rk}(\mathscr{L}_A) := \dim(\textrm{im}(\mathscr{L}_A))$
>   - inoltre, $\textrm{rk}(A) \le \min(m, n)$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $m,n \in \mathbb{N}$
    - $A \in \textrm{Mat}_{m \times n}(\mathbb{K})$
- **Th**
    - $\textrm{rk}(A) =\dim(\textrm{span}(A^1, \ldots, A^n)) = \dim(\textrm{span}(A_1, \ldots, A_n))$
- **Dim**
    - per definizione $\textrm{rk}(A) = \textrm{rk}(\mathscr{L}_A)$
    - per dimostrazione precedente $\left \{ \begin{array}{l}\ker(\mathscr{L}_A) = \textrm{span}(A_1, \ldots, A_n)^{\bot} \\ \textrm{im}(\mathscr{L}_A) = \textrm{span}(A^1, \ldots, A^n) \end{array} \right. \implies \left \{ \begin{array}{l} \dim(\ker(\mathscr{L}_A)) = \dim(\textrm{span}(A_1, \ldots, A_m)^\bot) \\ \textrm{rk}(A) := \textrm{rk}(\mathscr{L}_A) := \dim(\textrm{im}(\mathscr{L}_A)) = \dim(\textrm{span}(A^1, \ldots, A^n))\end{array} \right.$
    - per il teorema del rango $\dim(\textrm{im}(\mathscr{L}_A)) = \dim(\mathbb{K}^n) - \dim(\ker(\mathscr{L}_A)) = \dim(\mathbb{K}^n) - \dim(\textrm{span}(A_1, \ldots, A_m)^\bot)$
    - per dimostrazione precedente $\dim(\textrm{span}(A_1, \ldots, A_m)^\bot)= \dim(\mathbb{K}^n) - \dim(\textrm{span}(A_1, \ldots, A_m))$
    - allora $\textrm{rk}(A) = \dim(\textrm{span}(A^1, \ldots, A^n)) = \dim(\mathbb{K}^n) - (\dim(\mathbb{K}^n) - \dim(\textrm{span}(A_1, \ldots, A_m))) = \dim(\textrm{span}(A_1, \ldots, A_m))$

****

# Operazioni su righe e colonne

## Def

- **Scambio di righe di una matrice**

> - $\mathbb{K}$ campo
> - $m, n \in \mathbb{N}$
> - $A \in \textrm{Mat}_{m \times n}(\mathbb{K})$
> - $\forall A_1, \ldots, A_m$ righe di $A$, scambiare $A_i$ e $A_j$ lascia invariato $\ker(\mathscr{L}_A)$

- **Moltiplicazione di una riga per una costante**

> - $\mathbb{K}$ campo
> - $m, n \in \mathbb{N}$
> - $A \in \textrm{Mat}_{m \times n}(\mathbb{K})$
> - $\lambda \in \mathbb{K}^*$
> - $\forall A_1, \ldots, A_m$ righe di $A$, moltiplicare $A_i$ per $\lambda$ lascia invariato $\ker(\mathscr{L}_A)$

- **Somma di una riga con un multiplo di un'altra**

> - $\mathbb{K}$ campo
> - $m, n \in \mathbb{N}$
> - $A \in \textrm{Mat}_{m \times n}(\mathbb{K})$
> - $\lambda \in \mathbb{K}^*$
> - $\forall A_1, \ldots, A_m$ righe di $A$, sommare ad $A_i$ un certo $\lambda \cdot A_j$ lascia invariato $\ker(\mathscr{L}_A)$

- **Scambio di colonne di una matrice**

> - $\mathbb{K}$ campo
> - $m, n \in \mathbb{N}$
> - $A \in \textrm{Mat}_{m \times n}(\mathbb{K})$
> - $\forall A^1, \ldots, A^m$ colonne di $A$, scambiare $A^i$ e $A^j$ lascia invariato $\textrm{im}(\mathscr{L}_A)$

- **Moltiplicazione di una colonna per una costante**

> - $\mathbb{K}$ campo
> - $m, n \in \mathbb{N}$
> - $A \in \textrm{Mat}_{m \times n}(\mathbb{K})$
> - $\lambda \in \mathbb{K}^*$
> - $\forall A^1, \ldots, A^m$ colonne di $A$, moltiplicare $A^i$ per $\lambda$ lascia invariato $\textrm{im}(\mathscr{L}_A)$

- **Somma di una colonna con un multiplo di un'altra**

> - $\mathbb{K}$ campo
> - $m, n \in \mathbb{N}$
> - $A \in \textrm{Mat}_{m \times n}(\mathbb{K})$
> - $\lambda \in \mathbb{K}^*$
> - $\forall A^1, \ldots, A^m$ righe di $A$, sommare ad $A^i$ un certo $\lambda \cdot A^j$ lascia invariato $\textrm{im}(\mathscr{L}_A)$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $m, n \in \mathbb{N}$
    - $A, B \in \textrm{Mat}_{m \times n}(\mathbb{K})$
    - $A \equiv_R B \iff$ è possibile ricavare $B$ da $A$ eseguendo operazioni tra righe
- **Th**
    - $\equiv_R$ relazione di equivalenza
    - $A \equiv_R B \implies \left \{ \begin{array}{l}\ker(\mathscr{L}_A) = \ker(\mathscr{L}_B) \\ \textrm{rk}(A) = \textrm{rk}(B) \end{array} \right.$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $m, n \in \mathbb{N}$
    - $A, B \in \textrm{Mat}_{m \times n}(\mathbb{K})$
    - $A \equiv_C B \iff$ è possibile ricavare $B$ da $A$ eseguendo operazioni tra colonne
- **Th**
    - $\equiv_C$ una relazione di equivalenza
    - $A \equiv_C B \implies \left \{ \begin{array}{l}\textrm{im}(\mathscr{L}_A) = \textrm{im}(\mathscr{L}_B) \\ \textrm{rk}(A) = \textrm{rk}(B) \end{array}\right.$

****

# Matrici particolari

## Def

- **Vettore trasposto**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N}$
> - $v \in \textrm{Mat}_{n \times 1}(\mathbb{K}) \mid \exists x_1, \ldots, x_n \in \mathbb{K} : v = \left(\begin{array}{c}x_1 \\ \vdots \\ x_n \end{array}\right)$
> - $v^T = \left(x_1, \ldots, x_n\right)$ è detto **vettore trasposto di $v$**
>   - vicendevolmente, se $v$ è un vettore riga, il suo trasposto sarà il corrispondente vettore colonna

- **Matrice trasposta**

> - $\mathbb{K}$ campo
> - $m, n \in \mathbb{N}$
> - $A \in \textrm{Mat}_{m \times n}(\mathbb{K}) \mid A = \left(A^1, \ldots, A^n\right)$
> - $A^T = \left(\begin{array}{c} {A^1}^T \\ \vdots \\ {A^n}^T \end{array}\right)\in \textrm{Mat}_{n \times m}(\mathbb{K})$ è detta **matrice trasposta di $A$**

- **Matrice simmetrica**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N}$
> - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
> - $A$ è detta **simmetrica** $\iff A^T = A$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $m, n \in \mathbb{N}$
    - $A, B \in \textrm{Mat}_{m \times n}(\mathbb{K})$
- **Th**
    - $(A\cdot B)^T = B^T\cdot A^T$

## Def

- **Matrice identità**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N}$
> - $I_n = \left(\begin{array}{c}e_1 \\ \vdots \\ e_n \end{array}\right) = \left(e_1^T, \ldots, e_n^T\right) = \left(\begin{array}{ccccc}1 & 0 & \cdots & \cdots & 0 \\ \vdots & \ddots & & & \vdots\\ 0 & \cdots & 1 & \cdots & 0 \\ \vdots & & & \ddots & \vdots\\ 0 &\cdots & \cdots & 0 & 1\end{array}\right)$ è detta **matrice identità**
>   - in particolare $\forall A \in \textrm{Mat}_{n \times n}(\mathbb{K}) \quad A\cdot I_n = I_n \cdot A = A$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N}$
- **Th**
    - $(\textrm{Mat}_{n \times n}(\mathbb{K}), +, \cdot)$ è un anello

## Def

- **Matrice invertibile**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N}$
> - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
> - $A$ è detta **invertibile** $\iff \exists A^{-1} \in \textrm{Mat}_{n \times n}(\mathbb{K}) \mid A\cdot A^{-1} = A^{-1} \cdot A = I_n$
>   - in particolare $A$ invertibile $\iff \det(A) \neq 0$

- **Gruppo Generale Lineare**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N}$
> - $\textrm{GL}(n, \mathbb{K}) := \{A \in \textrm{Mat}_{n \times n}(\mathbb{K}) \mid A$ invertibile$\}$ è detto **gruppo generale lineare**
>   - in particolare $\textrm{GL}(n, \mathbb{K}) := \{A \in \textrm{Mat}_{n \times n}(\mathbb{K}) \mid \det(A) \neq 0\}$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N}$
- **Th**
    - $(\textrm{GL}(n, \mathbb{K}), \cdot)$ gruppo
- **Dim**
    - $\det(I_n) \neq 0 \implies I_n \in \textrm{GL}(n, \mathbb{K})$
    - $A \in \textrm{GL}(n, \mathbb{K}) \implies \det(A) \neq 0 \implies \det(A)^{-1} \neq 0$, e per il corollario del teorema di Binet $0 \neq \det(A)^{-1} = \det(A^{-1}) \implies A^{-1} \in \textrm{GL}(n, \mathbb{K})$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N}$
    - $f: \textrm{GL}(n, \mathbb{K}) \rightarrow \mathbb{K}^*$
- **Th**
    - $f$ morfismo di gruppi

## Def

- **Gruppo Speciale Lineare**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N}$
> - $\textrm{SL}(n, \mathbb{K}) := \{A \in \textrm{Mat}_{n \times n}(\mathbb{K}) \mid \det(A) = 1\}$ è detto **gruppo speciale lineare**

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N}$
- **Th**
    - $(\textrm{SL}(n, \mathbb{K}), \cdot) \trianglelefteq (\textrm{GL}(n, \mathbb{K}), \cdot)$
- **Dim**
    - $\det(I_n) = 1 \implies I_n \in \textrm{SL}(n, \mathbb{K})$
    - $A, B \in \textrm{SL}(n, \mathbb{K}) \implies \det(A) = \det(B)=1$, e per il teorema di Binet $1 = \det (A) \cdot \det(B) = \det(A \cdot B) \implies A \cdot B \in \textrm{SL}(n, \mathbb{K})$
    - $A \in \textrm{SL}(n, \mathbb{K}) \implies \det(A) = 1 \iff \det(A)^{-1} = 1$, e per il corollario del teorema di Binet $1 = \det(A)^{-1} = \det(A^{-1}) \implies A^{-1} \in \textrm{SL}(n, \mathbb{K})$
    - $G \in \textrm{GL}(n, \mathbb{K}), H \in \textrm{SL}(n, \mathbb{K}) \implies \left \{ \begin{array}{l}\det(G \cdot H \cdot G^{-1}) =\det(G) \cdot \det(H) \cdot \det(G^{-1}) = \det(G) \cdot \det(G)^{-1} = 1 \\ \det(H) = 1 \end{array} \right. \implies G \cdot H \cdot G^{-1} \in \textrm{SL}(n, \mathbb{K})$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N}$
- **Th**
    - $(\textrm{GL}(n, \mathbb{K}) / \textrm{SL}(n , \mathbb{K}), \cdot)$ è ben definito
- **Dim**
    - $\forall A, B \in \textrm{GL}(n, \mathbb{K}) \quad A \sim B \iff A^{-1}\cdot B \in \textrm{SL}(n, \mathbb{K}) \iff \det(A^{-1}\cdot B) = 1 \iff \det(A^{-1}) \cdot \det(B) = 1 \iff \det(A)^{-1} \cdot \det(B) = 1 \iff \det(B) = \det(A)$, allora le matrici in relazione tra loro saranno le matrici con stesso determinante

## Def

- **Matrice ortogonale**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N}$
> - $A \in \textrm{GL}(n, \mathbb{K})$
> - $A$ è detta **ortogonale** $\iff A \cdot A^T = A^T \cdot A = I_n$
>   - in particolare $A^{-1} = A^T$
>   - inoltre, $A_1, \ldots A_n$ e $A^1, \ldots, A^n$ base ortonormale di $\mathbb{K}^n$

- **Gruppo ortogonale**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N}$
> - $A \in \textrm{GL}(n, \mathbb{K})$
> - $\textrm{O}(n) := \{ A \in \textrm{GL}(n, \mathbb{K}) \mid A$ ortogonale$\}$ è detto **gruppo ortogonale**
>   - in particolare $\textrm{O}(n) := \{A \in \textrm{GL}(n, \mathbb{K}) \mid A^{-1} = A^T\}$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N}$
- **Th**
    - $(\textrm{O}(n), \cdot) \leqslant (\textrm{GL}(n, \mathbb{K}), \cdot)$
- **Dim**
    - $I_n = I_n^{-1} = I_n^T \implies I_n \in \textrm{O}(n)$
    - $A, B \in \textrm{O}(n) \implies \left \{ \begin{array}{l} A^{-1} = A^T \\ B^{-1} = B^T \end{array} \right. \implies (AB)^{-1} = B^{-1}A^{-1} = B^TA^T = (AB)^T \implies AB \in \textrm{O}(n)$
    - $A \in \textrm{O}(n) \implies A^{-1} = A^T \implies (A^{-1}A) = I_n = (A^{-1}A)^T \iff I_n = A^T(A^{-1})^T = A^{-1}(A^{-1})^T \iff (A^{-1})^T = A = (A^{-1})^{-1} \implies A^{-1} \in \textrm{O}(n)$
    - $p_1, \ldots, p_k \in \mathbb{P}$

## Def

- **Matrice singolare**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N}$
> - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
> - $A$ è detta **singolare** $\iff \det(A) = 0$

## Def

- **Matrici simili**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N}$
> - $A, B \in \textrm{Mat}_{n \times n}(\mathbb{K})$
> - $A$ è detta **simile a $B$** $\iff \exists C \in \textrm{GL}(n, \mathbb{K}) \mid A = C^{-1}BC$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N}$
    - $A, B \in \textrm{Mat}_{n \times n}(\mathbb{K}) \mid A$ simile a $B$
- **Th**
    - $\det(A) = \det(B)$
- **Dim**
    - $A$ simile a $B \implies \exists C \in \textrm{GL}(n, \mathbb{K}) \mid A = C^{-1}BC$
    - allora $\det(A)= \det(C^{-1}BC) = \det(C)^{-1}\cdot \det(B)\cdot \det(C) = \det(B)$

## Def

- **Traccia**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N}$
> - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
> - $\textrm{tr}(A) := a_{1,1}+ \ldots + a_{n,n}$ è detta **traccia di $A$**

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N}$
    - $A, B \in \textrm{Mat}_{n \times n}(\mathbb{K}) \mid A$ simile a $B$
- **Th**
    - $\textrm{tr}(A) = \textrm{tr}(B)$

## Def 

- **Matrice triangolare superiore**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N}$
> - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
> - $A$ è detta **triangolare superiore** $\iff \forall i, j \in [1, n], i \gt j \quad a_{i,j} = 0$

- **Matrice triangolare inferiore**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N}$
> - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
> - $A$ è detta **triangolare inferiore** $\iff \forall i, j \in [1, n], i \lt j \quad a_{i,j} = 0$

- **Matrice triangolare**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N}$
> - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
> - $A$ è detta **triangolare $\iff$** $A$ triangolare superiore o triangolare inferiore

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K}) \mid A$ triangolare
- **Th**
    - $\det(A) = a_{1,1} \cdot \ldots \cdot a_{n, n}$

## Def

- **Matrice triangolarizzabile**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N}$
> - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
> - $A$ è detta **triangolarizzabile** $\iff \exists B \in \textrm{Mat}_{n \times n}(\mathbb{K}) \mid B$ triangolare $\land \ B$ simile ad $A$

- **Matrice diagonale**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N}$
> - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
> - $A$ è detta **diagonale** $\iff \forall i, j \in [1, n], i \neq j \quad a_{i, j} = 0$
>   - in particolare, $A$ diagonale $\iff A$ triangolare superiore ed inferiore

- **Matrice diagonalizzabile**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N}$
> - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
> - $A$ è detta **diagonalizzabile** $\iff \exists B \in \textrm{Mat}_{n \times n}(\mathbb{K}) \mid B$ diagonale $\land \ B$ simile ad $A$
>   - in particolare $B$ è detta _matrice diagonalizzante_

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K}) \mid A$ diagonalizzabile
- **Th**
    - $A$ triangolarizzabile

## Def

- **Sottomatrice di una matrice**

> - $\mathbb{K}$ campo
> - $m, n \in \mathbb{N}$
> - $A \in \textrm{Mat}_{m \times n}(\mathbb{K})$
> - $A_i^j$ è detta **sottomatrice di $A$** $\iff A_i^j$ si ottiene rimuovendo $A_i$ e $A^j$ da $A$

- **Minore di una matrice**

> - $\mathbb{K}$ campo
> - $m, n \in \mathbb{N}$
> - $A \in \textrm{Mat}_{m \times n}(\mathbb{K})$
> - $M$ è detto **minore di $A$** $\iff M$ è una sottomatrice quadrata di $A$

- **Orlato di un minore**

> - $\mathbb{K}$ campo
> - $m, n, r \in \mathbb{N} \mid r \lt m \land r \lt n$
> - $A \in \textrm{Mat}_{m \times n}(\mathbb{K})$
> - $M \in \textrm{Mat}_{r \times r}(\mathbb{K})$ minore di $A$
> - $M' \in \textrm{Mat}_{(r + 1) \times (r + 1)}(\mathbb{K})$ è detto **orlato di $M$** $\iff M'$ è minore di $A$ e $M$ si ottiene rimuovendo una riga e una colonna da $M'$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $m, n, r \in \mathbb{N} \mid r \lt m \land r \lt n$
    - $A \in \textrm{Mat}_{m \times n}(\mathbb{K})$
    - $M \in \textrm{Mat}_{r \times r}(\mathbb{K})$ minore di $A$
- **Th**
    - $M$ ha $(m-r)\cdot(n-r)$ orlati in $A$
    
## Def

- **Matrice completa**

> - $\mathbb{K}$ campo
> - $m, n \in \mathbb{N}$
> - $A \in \textrm{Mat}_{m \times n}(\mathbb{K})$
> - $b \in \textrm{Mat}_{m \times 1}(\mathbb{K})$
> - $A_b:=\left(\begin{array}{cccc}a_{1, 1} & \cdots & a_{1, n} & b_1 \\ \vdots & \ddots & \vdots & \vdots \\ a_{m, 1} & \cdots & a_{m,n} & b_m\end{array}\right)$ è detta **matrice completa di $A$ e $b$**

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $m, n \in \mathbb{N}$
    - $V, W$ spazi vettoriali su $\mathbb{K} \mid \left \{ \begin{array}{l} \dim(V) = n \\ \dim(W) = m \end{array} \right.$
    - $\mathcal{B}=\{v_1, \ldots, v_n\}$ base di $V$
    - $\mathcal{C}=\{w_1, \ldots, w_m\}$ base di $W$
    - $f: V \rightarrow W$ trasformazione lineare
    - $\varphi_\mathcal{B}: \mathbb{K}^n \rightarrow V: (b_1, \ldots, b_n) \rightarrow b_1v_1 + \ldots + b_nv_n$ isomorfismo
    - $\varphi_\mathcal{C}: \mathbb{K}^m \rightarrow W: (c_1, \ldots, c_m) \rightarrow c_1w_1 + \ldots + c_mw_m$ isomorfismo
- **Th**
    - $\exists !A \in \textrm{Mat}_{m \times n}(\mathbb{K}) \mid f = \varphi_\mathcal{C}\cdot \mathscr{L}_A \cdot \varphi_\mathcal{B}^{-1}$, e prende il nome di _matrice di $f$_
- **Dim**
    - si noti che $V \cong \mathbb{K}^n$ per dimostrazione precedente, dunque esiste $\varphi_{\mathcal{B}}$, e analogamente $W \cong \mathbb{K}^m$ implica che esiste $\varphi_{\mathcal{C}}$
    - sia $e_1, \ldots, e_n$ base canonica di $\mathbb{K}^n$
    - sia $A \in \textrm{Mat}_{m \times n}(\mathbb{K})$
    - $\forall i \in [1, n] \quad \varphi_{\mathcal{B}}(e_i) = 0 \cdot v_1 + \ldots + 1 \cdot v_i + \ldots 0 \cdot v_n = v_i \iff \varphi_{\mathcal{B}}^{-1}(v_i) = e_i$
    - $\mathscr{L}_A(e_i) = \left(\begin{array}{cccc} a_{1,1} & \ldots & a_{1,n} \\ \vdots & \ddots & \vdots \\ a_{m, 1} & \ldots & a_{m, n}\end{array}\right)\left(\begin{array}{c} 0 \\ \vdots \\ 1 \\ \vdots \\ 0 \end{array}\right) = \left(\begin{array}{c} a_{1, i} \\ \vdots \\ a_{m, i}\end{array}\right) = A^i \in \mathbb{K}^m$
    - $\varphi_{\mathcal{C}}(A^i)=a_{1, i}w_1+ \ldots + a_{m, i} w_m = w_i$
    - ⚠️ **da completare**

## Def

- **Matrice di Vandermonde**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N}$
> - $b_0, \ldots, b_n \in \mathbb{K} \mid \forall i, j \in [1, n], i \neq j \quad b_i \neq b_j$
> - $V(b_0, \ldots, b_n) := \left ( \begin{array}{cccc} b_0^0 & b_0^1 & \cdots & b_0^n \\ b_1^0 & b_1^1 & \cdots & b_1^n \\ \vdots & \ddots & & \vdots \\\vdots & &\ddots  & \vdots \\ b_n^0 & b_n^1 & \cdots & b_n^n\end{array}\right)$ è detta **matrice di Vandermonde a coefficienti $b_0, \ldots, b_n$**

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N}$
    - $b_0, \ldots, b_n \in \mathbb{K} \mid \forall i, j \in [1, n], i \neq j \quad b_i \neq b_j$
- **Th**
    - $\det(V(b_0, \ldots, b_n)) = \displaystyle \prod_{0 \le i \lt j \le n}{(b_j - b_i)}$
- **Dim**
    - $\det(V(b_0, \ldots, b_n))=\det\left ( \begin{array}{cccc} b_0^0 & b_0^1 & \cdots & b_0^n \\ b_1^0 & b_1^1 & \cdots & b_1^n \\ \vdots & \ddots & & \vdots \\\vdots & &\ddots  & \vdots \\ b_n^0 & b_n^1 & \cdots & b_n^n\end{array}\right) = \det\left ( \begin{array}{cccc} 1 & b_0 & \cdots & b_0^n \\ 1 & b_1 & \cdots & b_1^n \\ \vdots & \ddots & & \vdots \\\vdots & &\ddots  & \vdots \\ 1 & b_n & \cdots & b_n^n\end{array}\right)$
    - sottraendo la prima riga a tutte le altre, si ottiene $\det\left ( \begin{array}{cccc} 1 & b_0 & \cdots & b_0^n \\ 0 & b_1 - b_0 & \cdots & b_1^n - b_0^n \\ \vdots & \ddots & & \vdots \\\vdots & &\ddots  & \vdots \\ 0 & b_n - b_0 & \cdots & b_n^n - b_0^n\end{array}\right)$
    - eseguendo lo sviluppo di Laplace sulla prima colonna, si ottiene $1 \cdot \det\left ( \begin{array}{cccc} b_1 - b_0 & b_1^2 -b_0^2 & \cdots & b_1^n - b_0^n \\ b_2 - b_0 & b_2^2-b_0^2&\cdots & b_2^n - b_0^n \\ \vdots & \ddots & &\vdots \\ \vdots &  & \ddots & \vdots \\  b_n - b_0 &  b_n^2-b_0^2 & \cdots & b_n^n - b_0^n\end{array}\right)$
    - $\forall i \in [1, n] \quad b_i^n - b_0^n = (b_i - b_0)(b_i^{n - 1} + b_i^{n - 2}b_0 + \ldots + b_ib_0^{n - 2} + b_0^{n - 1})$
    - allora si ottiene $\det\left ( \begin{array}{cccc} (b_1 - b_0) \cdot 1 & (b_1 -b_0)\cdot(b_1 + b_0) & \cdots & (b_1 - b_0)\cdot(b_1^{n - 1} + \ldots + b_0^{ n - 1}) \\ (b_2 - b_0) \cdot 1 & (b_2 - b_0)\cdot (b_2+b_0)&\cdots & (b_2 - b_0)\cdot(b_2^{n -1} + \ldots +  b_0^{n - 1}) \\ \vdots & \ddots & &\vdots \\ \vdots & & \ddots & \vdots \\  (b_n - b_0) \cdot 1 &  (b_n-b_0)\cdot (b_n + b_0) & \cdots & (b_n - b_0) \cdot (b_n^{n -1}+ \ldots + b_0^{n -1})\end{array}\right) = (b_n - b_0)\cdot \ldots \cdot(b_1 - b_0) \cdot \det\left ( \begin{array}{cccc} 1 & b_1 + b_0 & \cdots & b_1^{n - 1} + \ldots + b_0^{ n - 1} \\1 & b_2+b_0&\cdots & b_2^{n -1} + \ldots +  b_0^{n - 1} \\ \vdots & \ddots & &\vdots \\ \vdots & & \ddots & \vdots \\   1 &  b_n + b_0 & \cdots & b_n^{n -1}+ \ldots + b_0^{n -1}\end{array}\right)$ per multilinearità del determinante
    - $\left( \begin{array}{cccc} 1 & b_1 + b_0 & \cdots & b_1^{n - 1} + \ldots + b_0^{ n - 1} \\1 & b_2+b_0&\cdots & b_2^{n -1} + \ldots +  b_0^{n - 1} \\ \vdots & \ddots & &\vdots \\ \vdots & & \ddots & \vdots \\   1 &  b_n + b_0 & \cdots & b_n^{n -1}+ \ldots + b_0^{n -1}\end{array}\right)\xrightarrow{\left . \begin{subarray}{c}C^2 -= b_0 \cdot C^1 \\ C^3 -= b_0  \cdot C^1 + b_0 \cdot C^2 \\ \vdots \\ C^n -= b_0 \cdot C^1 + \ldots + b_0 \cdot C^{n - 1}\end{subarray}\right.} \left ( \begin{array}{cccc} 1 & b_1 & \cdots & b_1^{n - 1} \\1 & b_2 &\cdots & b_2^{n -1} \\ \vdots & \ddots & &\vdots \\ \vdots & & \ddots & \vdots \\   1 &  b_n  & \cdots & b_n^{n -1}\end{array}\right) = V(b_1, \ldots, b_n)$
    - allora si ha che $\det(V(b_0, \ldots, b_n)) = (b_n - b_0) \cdot \ldots \cdot(b_1 - b_0) \cdot \det(V(b_1, \ldots, b_n)) = (b_n - b_0) \cdot \ldots \cdot(b_1 - b_0) \cdot (b_n - b_1) \cdot \ldots \cdot (b_2 - b_1) \cdot \det(V(b_2, \ldots, b_n)) \implies \det(V(b_0, \ldots, b_n)) = \displaystyle \prod_{0 \le i \lt j \le n}{(b_j - b_i)}$

