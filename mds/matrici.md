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

> - $\mathbb{K}$ campo
> - $l, m, n \in \mathbb{N} - \{0\}$
> - $A \in \textrm{Mat}_{l \times m}(\mathbb{K}) \mid A = \left(\begin{array}{ccc} a_{1, 1} & \cdots & a_{1, m} \\ \vdots & \ddots & \vdots \\ a_{l, 1} & \cdots & a_{l, m} \end{array}\right)$
> - $B \in \textrm{Mat}_{m \times n}(\mathbb{K}) \mid B = \left(\begin{array}{ccc} b_{1, 1} & \cdots & b_{1, n} \\ \vdots & \ddots & \vdots \\ b_{m, 1} & \cdots & b_{m, n} \end{array}\right)$
> - $C \in \textrm{Mat}_{l \times n}(\mathbb{K}) \mid C = A \cdot B$ è il **prodotto tra $A$ e $B$**, ed è definito come $\left(\begin{array}{ccc}a_{1, 1}b_{1, 1} + \ldots + a_{1, m}b_{m, 1} & \cdots & a_{1, 1}b_{1, n} + \ldots + a_{1, m}b_{m,n} \\ \vdots & \ddots & \vdots \\a_{l,1}b_{1, 1} + \ldots + a_{l,m}b_{m, 1} & \cdots & a_{l,1}b_{1,n} + \ldots + a_{l, m}b_{m,n}\end{array}\right)$

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

# Matrici particolari

## Def

- **Vettore trasposto**

> - $n \in \mathbb{N}$
> - $\mathbb{K}$ campo
> - $v \in \textrm{Mat}_{n \times 1}(\mathbb{K}) \mid v = \left(\begin{array}$

- **Matrice trasposta**

> - $m, n \in \mathbb{N} - \{0\}$
> - $\mathbb{K}$ campo
> - $A \in \textrm{Mat}_{m \times n}(\mathbb{K}) \mid A = \left(A^1, \ldots, A^n\right)$
> - $A^T = \left(\begin{array}{c} {A^1}^T \\ \vdots \\ {A^n}^T \end{array}\right)$

## Def

- **Matrice identità**

> - $n \in \mathbb{N} - \{0\}$
> - $\mathbb{K}$ campo
> - $I_n = \left(\begin{array}{c}e_1 \\ \vdots \\ e_n \end{array}\right) = \left(e_1^T, \ldots, e_n^T\right) = \left(\begin{array}{cccc}1 & 0 & \cdots & \cdots & 0 \\ \vdots & \ddots & & & \vdots\\ 0 & \cdots & 1 & \cdots & 0 \\ \vdots & & & \ddots & \vdots\\ 0 &\cdots & \cdots & 0 & 1\end{array}\right)$ è detta **matrice identità**

****

# Rango

## Def

- **Sottospazio ortogonale**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N} - \{0\}$
> - $V \subset \mathbb{K}^n$ sottospazio vettoriale
> - $V^{\perp} := \{w \in \mathbb{K}^n \mid \forall v \in V \quad w \cdot v = 0_{\mathbb{K}^n}\}$ è detto **sottospazio ortogonale di $\mathbb{K}^n$**
>     - la definizione ha significato poiché il prodotto scalare tra due vettori è nullo esattamente quando i due vettori sono perpendicolari tra loro, per osservazione precedente

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N} - \{0\}$
    - $V \subset \mathbb{K}^n$ sottospazio vettoriale
- **Th**
    - $V^{\bot}$ è sottospazio vettoriale di $\mathbb{K}^n$
- **Dim**
    - **⚠️  TODO**

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N} - \{0\}$
    - $V \subset \mathbb{K}^n$ sottospazio vettoriale
- **Th**
    - $\dim(V^{\bot}) = \dim(\mathbb{K}^n) - \dim(V)$
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
    - $\forall A \in \textrm{Mat}_{m \times n}(\mathbb{K}) \quad \ker(L_A) = \textrm{span}(A_1, \ldots, A_m)^\bot \land \textrm{im}(L_A) = \textrm{span}(A^1, \ldots, A^n)$
- **Dim**
    - $\ker(L_A) = \textrm{span}(A_1, \ldots, A_m)^\bot$
        - $\ker(L_A) := \left\{x \in \mathbb{K}^n \mid L_A(x) = 0_{\mathbb{K}^m} \iff A \cdot x = 0_{\mathbb{K}^m} \iff \left(\begin{array}{c}A_1\cdot x \\ \vdots \\ A_m \cdot x\end{array}\right)= \left(\begin{array}{c} 0 \\ \vdots \\ 0\end{array}\right)\right\} = \textrm{span}(A_1, \ldots, A_m)^\bot$

    - $\textrm{im}(L_A) = \textrm{span}(A^1, \ldots, A^n)$
        - $\textrm{im}(L_A) \subset \textrm{span}(A^1, \ldots, A^n)$
            - $\forall A \in \textrm{Mat}_{m \times n}(\mathbb{K}) \quad L_A(x) = A \cdot x$ per definizione di $L_A$
            - $A \cdot x = \left(\begin{array}{ccc} a_{1,1} & \cdots & a_{1,n}\\ \vdots & \ddots & \vdots \\ a_{m,1} & \cdots & a_{m,n}\end{array}\right) \cdot \left(\begin{array}{c} x_1 \\ \vdots \\ x_n \end{array}\right) = \left(\begin{array}{c}a_{1, 1} x_1 + \ldots + a_{1,n}x_n \\ \vdots \\ a_{m,1}x_1 + \ldots + a_{m,n} x_n \end{array}\right) = \left(\begin{array}{c}A_1 \cdot x \\ \vdots \\ A_m \cdot x\end{array}\right) = x_1 \left(\begin{array}{c}a_{1, 1} \\ \vdots \\ a_{m, 1}\end{array}\right) + \ldots + x_n \left(\begin{array}{c}a_{1, n}\\ \vdots \\ a_{m, n}\end{array}\right) = x_1A^1 + \ldots + x_nA^n$, e poiché $x_1, \ldots x_n \in \mathbb{K} \implies x_1A^1+ \ldots + x_nA^n \in \textrm{span}(A^1, \ldots, A^n) \implies \textrm{im}(L_A) \subset \textrm{span}(A^1, \ldots, A^n)$
        - $\textrm{span}(A^1, \ldots, A^n) \subset \textrm{im}(L_A)$
            - $\forall v \in \textrm{span}(A^1, \ldots, A^n) \quad \exists x_1, \ldots, x_n \in \mathbb{K} \mid v = x_1 A^1 + \ldots + x_n A^n = A \cdot x$ per ragionamento analogo, e poiché $A \cdot x \in \textrm{im}(L_A)$, allora $\textrm{span}(A^1, \ldots, A^n) \subset \textrm{im}(L_A)$

## Oss

- **Rango di una matrice**

> - $\mathbb{K}$ campo
> - $m,n \in \mathbb{N} - \{0\}$
> - $A \in \textrm{Mat}_{m \times n}(\mathbb{K})$
> - $x \in \textrm{Mat}_{n \times 1}(\mathbb{K})$
> - $\textrm{rk}(A):=\textrm{rk}(L_A)$ è il **rango di $A$**

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $m,n \in \mathbb{N} - \{0\}$
    - $A \in \textrm{Mat}_{m \times n}(\mathbb{K})$
    - $x \in \textrm{Mat}_{n \times 1}(\mathbb{K})$
- **Th**
    - $\textrm{rk}(A) =\dim(\textrm{span}(A^1, \ldots, A^n)) = \dim(\textrm{span}(A_1, \ldots, A_n)^\bot)$
- **Dim**
    - per definizione $\textrm{rk}(A) = \textrm{rk}(L_A)$
    - per dimostrazione precedente $L_A$ è una trasforamzione lineare, allora per definizione $\textrm{rk}(L_A) = \dim(\textrm{im}(L_A))$
    - per dimostrazione precedente si ha che $\textrm{im}(L_A) = \textrm{span}(A^1, \ldots, A^n)$, allora $\dim(\textrm{im}(L_A)) = \dim(\textrm{span}(A^1, \ldots, A^n))$, e per ragionamento analogo $\dim(\ker(L_A)) = \dim(\textrm{span}(A_1, \ldots, A_m)^\bot)$
    - allora $\dim(\textrm{im}(L_A)) = \textrm{rk}(L_A) = \dim(\mathbb{K}^n) - \dim(\ker(L_A)) = \dim(\mathbb{K}^n) - \dim(\textrm{span}(A_1, \ldots, A_m)^\bot)$
    - per dimostrazione precedente si ha che $\dim(\textrm{span}(A_1, \ldots, A_m)^\bot)= \dim(\mathbb{K}^n) - \dim(\textrm{span}(A_1, \ldots, A_m))$
    - allora $\textrm{rk}(A) = \dim(\textrm{span}(A^1, \ldots, A^n)) = \dim(\mathbb{K}) - (\dim(\mathbb{K}^n) - \dim(\textrm{span}(A_1, \ldots, A_m))) = \dim(\textrm{span}(A_1, \ldots, A_m))$

## Def

- **Matrice completa**

> - $\mathbb{K}$ campo
> - $m, n \in \mathbb{N} - \{0\}$
> - $A \in \textrm{Mat}_{m \times n}(\mathbb{K})$
> - $b \in \textrm{Mat}_{m \times 1}(\mathbb{K})$
> - $A_b:=\left(\begin{array}{cccc}a_{1, 1} & \cdots & a_{1, n} & b_1 \\ \vdots & \ddots & \vdots & \vdots \\ a_{m, 1} & \cdots & a_{m,n} & b_m\end{array}\right)$

****

# Operazioni su righe e colonne

## Def

- **Scambio di righe di una matrice**

> - $\mathbb{K}$ campo
> - $m, n \in \mathbb{N} - \{0\}$
> - $A \in \textrm{Mat}_{m \times n}(\mathbb{K})$
> - $\forall A_1, \ldots, A_m$ righe di $A$, scambiare $A_i$ e $A_j$ lascia invariato $\ker(L_A)$

- **Moltiplicazione di una riga per una costante**

> - $\mathbb{K}$ campo
> - $m, n \in \mathbb{N} - \{0\}$
> - $A \in \textrm{Mat}_{m \times n}(\mathbb{K})$
> - $\lambda \in \mathbb{K}^*$
> - $\forall A_1, \ldots, A_m$ righe di $A$, moltiplicare $A_i$ per $\lambda$ lascia invariato $\ker(L_A)$

- **Somma di una riga con un multiplo di un'altra**

> - $\mathbb{K}$ campo
> - $m, n \in \mathbb{N} - \{0\}$
> - $A \in \textrm{Mat}_{m \times n}(\mathbb{K})$
> - $\lambda \in \mathbb{K}^*$
> - $\forall A_1, \ldots, A_m$ righe di $A$, sommare ad $A_i$ un certo $\lambda \cdot A_j$ lascia invariato $\ker(L_A)$

- **Scambio di colonne di una matrice**

> - $\mathbb{K}$ campo
> - $m, n \in \mathbb{N} - \{0\}$
> - $A \in \textrm{Mat}_{m \times n}(\mathbb{K})$
> - $\forall A^1, \ldots, A^m$ colonne di $A$, scambiare $A^i$ e $A^j$ lascia invariato $\textrm{im}(L_A)$

- **Moltiplicazione di una colonna per una costante**

> - $\mathbb{K}$ campo
> - $m, n \in \mathbb{N} - \{0\}$
> - $A \in \textrm{Mat}_{m \times n}(\mathbb{K})$
> - $\lambda \in \mathbb{K}^*$
> - $\forall A^1, \ldots, A^m$ colonne di $A$, moltiplicare $A^i$ per $\lambda$ lascia invariato $\textrm{im}(L_A)$

- **Somma di una colonna con un multiplo di un'altra**

> - $\mathbb{K}$ campo
> - $m, n \in \mathbb{N} - \{0\}$
> - $A \in \textrm{Mat}_{m \times n}(\mathbb{K})$
> - $\lambda \in \mathbb{K}^*$
> - $\forall A^1, \ldots, A^m$ righe di $A$, sommare ad $A^i$ un certo $\lambda \cdot A^j$ lascia invariato $\textrm{im}(L_A)$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $m, n \in \mathbb{N} - \{0\}$
    - $A, B \in \textrm{Mat}_{m \times n}(\mathbb{K})$
    - $A \equiv B \iff$ è possibile ricavare $B$ da $A$ eseguendo operazioni tra righe definite precedentemente
- **Th**
    - $\equiv$ una relazione di equivalenza

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $m, n \in \mathbb{N} - \{0\}$
    - $A, B \in \textrm{Mat}_{m \times n}(\mathbb{K})$
    - $A \equiv B \iff$ è possibile ricavare $B$ da $A$ eseguendo operazioni tra righe definite precedentemente
- **Th**
    - $A \equiv B \implies \ker(L_A) = \ker(L_B) \land \textrm{rk}(A) = \textrm{rk}(B)$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $m, n \in \mathbb{N} - \{0\}$
    - $A, B \in \textrm{Mat}_{m \times n}(\mathbb{K})$
    - $A \equiv B \iff$ è possibile ricavare $B$ da $A$ eseguendo operazioni tra colonne definite precedentemente
- **Th**
    - $\equiv$ una relazione di equivalenza

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $m, n \in \mathbb{N} - \{0\}$
    - $A, B \in \textrm{Mat}_{m \times n}(\mathbb{K})$
    - $A \equiv B \iff$ è possibile ricavare $B$ da $A$ eseguendo operazioni tra colonne definite precedentemente
- **Th**
    - $A \equiv B \implies \textrm{im}(L_A) = \textrm{im}(L_B) \land \textrm{rk}(A) = \textrm{rk}(B)$

