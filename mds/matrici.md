# Matrici

## Def

- **Matrici**

> - $\mathbb{K}$ campo
> - $m, n \in \mathbb{N} - \{0\}$
> - $\textrm{Mat}_{m \times n}(\mathbb{K})$ è l'**insieme delle matrici aventi $m$ righe e $n$ colonne a coefficienti in $\mathbb{K}$**

- **Vettori riga e vettori colonna**

> - $\mathbb{K}$ campo
> - $m, n \in \mathbb{N} - \{0\}$
> - $\forall A \in \textrm{Mat}_{1 \times n}(\mathbb{K}) \quad A = \left(x_1, \ldots, x_n\right)$ è detto **vettore riga**
> - $\forall A \in \textrm{Mat}_{m \times 1}(\mathbb{K}) \quad A = \left(\begin{array}{ccc} x_1 \\ \vdots \\ x_m \end{array}\right)$ è detto **vettore colonna**
> - $\forall A \in \textrm{Mat}_{m \times n}(\mathbb{K}) \quad \exists A^1, \ldots, A^n \in \mathbb{K}^m$ vettori colonna e $A_1, \ldots, A_m \in \mathbb{K}^n$ vettori riga $\mid A = \left(A^1, \ldots, A^n \right) = \left(\begin{array}{ccc} A_1 \\ \vdots \\ A_m\end{array}\right)$

## Def

- **Somma tra matrici**

> - $\mathbb{K}$ campo
> - $m, n \in \mathbb{N} - \{0\}$
> - $\forall i \in [1, m], j \in [1, n] \quad a_{i, j}, b_{i, j} \in \mathbb{K}$
> - $A, B \in \textrm{Mat}_{m \times n}(\mathbb{K}) \mid A = \left(\begin{array}{ccc} \ddots & & \\ & a_{i, j} & \\ & & \ddots \end{array}\right) \land B = \left(\begin{array}{ccc}\ddots & & \\ & b_{i, j} & \\ & & \ddots\end{array}\right)$
> - $A + B = \left(\begin{array}{ccc}\ddots & & \\ & a_{i, j} + b_{i, j} & \\ & & \ddots\end{array}\right)$ è la **somma tra $A$ e $B$**

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $m, n \in \mathbb{N} - \{0\}$
- **Th**
    - $\textrm{Mat}_{m \times n}(\mathbb{K})$ è uno spazio vettoriale
- **Dim**
    - **⚠️ TODO**

## Def

- **Prodotto scalare**

> - $\mathbb{K}$ campo
> - $m, n \in \mathbb{N} - \{0\}$
> - $A \in \textrm{Mat}_{1 \times n}(\mathbb{K})$
> - $B \in \textrm{Mat}_{m \times 1}(\mathbb{K})$
> - $A \cdot B := \displaystyle \sum_{i = 1}^n{a_i \cdot b_i}$ è il **prodotto scalare tra $A$ e $B$**


## Oss

- **⚠️  WIP**

## Def

- **Prodotto tra matrici**

> - **⚠️  WIP**

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $\lambda \in \mathbb{K}$
    - $l, m, n \in \mathbb{N} - \{0\}$
    - $A \in \textrm{Mat}_{l \times m}(\mathbb{K})$
    - $B \in \textrm{Mat}_{m \times n}(\mathbb{K})$
- **Th**
    - $(AB)C = A(BC)$
    - $A(B+C) = AB+AC$
    - $(A+B)C = AC+BC$
    - $\lambda(AB) = (\lambda A)B = A (\lambda B)$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $\lambda \in \mathbb{K}$
    - $n \in \mathbb{N} - \{0\}$
- **Th**
    - $(\textrm{Mat}_{n \times n}(\mathbb{K}), +, \cdot)$ è un anello
- **Dim**
    - **⚠️  TODO**

****

# Rango

## Def

- **Sottospazio ortogonale**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N} - \{0\}$
> - $V \subset \mathbb{K}^n$ sottospazio vettoriale
> - $V^{\perp} := \{w \in \mathbb{K}^n \mid \forall v \in V \quad w \cdot v = 0\}$ è detto **sottospazio ortogonale di $V$**

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N} - \{0\}$
    - $V \subset \mathbb{K}^n$ sottospazio vettoriale
- **Th**
    - $V^{\bot}$ è sottospazio vettoriale di $\mathbb{K}^n$
- **Dim**
    - **⚠️  TODO**

## Def

- **Moltiplicazione sinistra**

> - $\mathbb{K}$ campo
> - $m,n \in \mathbb{N} - \{0\}$
> - $x \in \textrm{Mat}_{n \times 1}(\mathbb{K})$
> - $\forall A \in \textrm{Mat}_{m \times n}(\mathbb{K}) \quad L_A:\mathbb{K}^n \rightarrow \mathbb{K}^m: x \rightarrow A\cdot x$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $m,n \in \mathbb{N} - \{0\}$
    - $x \in \textrm{Mat}_{n \times 1}(\mathbb{K})$
- **Th**
    - $\forall A \in \textrm{Mat}_{m \times n}(\mathbb{K}) \quad L_A$ è una trasformazione lineare
- **Dim**
    - **⚠️  TODO**

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $m,n \in \mathbb{N} - \{0\}$
    - $x \in \textrm{Mat}_{n \times 1}(\mathbb{K})$
- **Th**
    - $\forall A \in \textrm{Mat}_{m \times n}(\mathbb{K}) \quad \ker(L_A) = \textrm{span}(A_1, \ldots, A_n) \land \textrm{im}(L_A) = \textrm{span}(A^1, \ldots, A^n)$
- **Dim**
    - $\forall A \in \textrm{Mat}_{m \times n}(\mathbb{K}) \quad L_A(x) = A \cdot x$ per definizione di $L_A$
    - $A \cdot x = \left(\begin{array}{ccc} a_{1,1} & \cdots & a_{1,n}\\ \vdots & \ddots & \vdots \\ a_{m,1} & \cdots & a_{m,n}\end{array}\right) \cdot \left(\begin{array}{c} x_1 \\ \vdots \\ x_n \end{array}\right) = \left(\begin{array}{c}a_{1, 1} x_1 + \ldots + a_{1,n}x_n \\ \vdots \\ a_{m,1}x_1 + \ldots + a_{m,n} x_n \end{array}\right) = \left(\begin{array}{c}A_1 \cdot x \\ \vdots \\ A_m \cdot x\end{array}\right) = x_1 \left(\begin{array}{c}a_{1, 1} \\ \vdots \\ a_{m, 1}\end{array}\right) + \ldots + x_n \left(\begin{array}{c}a_{1, n}\\ \vdots \\ a_{m, n}\end{array}\right) = x_1A^1 + \ldots + x_nA^n$, e poiché $x_1, \ldots x_n \in \mathbb{K} \implies x_1A^1+ \ldots + x_nA^n \in \textrm{span}(A^1, \ldots, A^n)$
    - **⚠️  TODO**

## Oss

- **Rango di una matrice**

> - $\mathbb{K}$ campo
> - $m,n \in \mathbb{N} - \{0\}$
> - $A \in \textrm{Mat}_{m \times n}(\mathbb{K})$
> - $x \in \textrm{Mat}_{n \times 1}(\mathbb{K})$
> - $\textrm{rk}(A):=\textrm{rk}(L_A)$ è il **rango di $A$**

## Oss

- **Hp**
