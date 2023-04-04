# Determinante

## Def

- **Applicazione multilineare**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N}$
> - $V_1, \ldots, V_n, W$ spazi vettoriali su $\mathbb{K}$
> - $f: V_1 \times \ldots \times V_n \rightarrow W:(v_1, \ldots, v_n) \rightarrow w$
> - $f$ è detta **multilineare** $\iff \forall i \in [1, n],  v_1 , \ldots, v_n \in V_1 \times \ldots \times V_n, v_i, v_i' \in V_i, \lambda, \mu \in \mathbb{K} \quad f(v_1, \ldots, \lambda v_i+\mu v_i', \ldots, v_n) = \lambda f(v_1, \ldots, v_i, \ldots, v_n) + \mu f(v_1, \ldots, v_i', \ldots, v_n)$
>   - in particolare, tenendo fisse tutte le variabili tranne la $i$-esima, $f$ è una trasformazione lineare

- **Determinante**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N}$
> - $\det : \textrm{Mat}_{n \times n}(\mathbb{K}) \rightarrow \mathbb{K}$
> - 1. $\forall A \in \textrm{Mat}_{n \times n}(\mathbb{K}) \quad \det$ multilineare su $A_1, \ldots A_n$ e $A^1, \ldots, A^n$
> - 2. $\forall A \in \textrm{Mat}_{n \times n}(\mathbb{K}) \quad A_1, \ldots A_n$ e $A^1, \ldots, A^n$ basi di $\mathbb{K}^n \iff \det(A) \neq 0$
>   - in particolare $\exists i, j \in [1, n], i \neq j \mid A^i = A^j \lor A_i = A_j \implies \det(A) = 0$
> - 3. $\det(I_n) = 1$
> - 4. per $\mathbb{K} \mid 1_{\mathbb{K}} \neq -1_{\mathbb{K}} \quad$ scambiando due righe o due colonne $\det(A)$ cambia segno
>   - ad esempio in $\mathbb{Z}_2 = \{[0], [1]\}$ si ha che $[1] = [-1]$
> - $\det$ è detto **determinante** $\iff \det$ verifica 1, 2 e 3, oppure 1, 3 e 4
>   - poiché è possibile dimostrare che la funzione che verifica tali condizioni esiste ed è unica, allora il $\det$ è totalmente determinato da tali caratteristiche

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N}$
    - $\lambda \in \mathbb{K}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
    - $A_i \in A$
- **Th**
    - $\det(A_1, \ldots, \lambda A_i, \ldots, A_n) = \lambda \cdot \det(A)$
- **Dim**
    - per il punto 1 della definizione di $\det$, si ha che $\det(A_1, \ldots,\lambda A_i, \ldots, A_n) = \lambda \cdot \det(A_1, \ldots, A_n) = \lambda \cdot \det(A)$
    - si noti che la tesi è verificata sia per righe che per colonne, per definizione di $\det$

## Oss

- **Hp**
    - $\mathbb{K}$ campo $\mid 1_{\mathbb{K}} \neq -1_{\mathbb{K}}$
    - $n \in \mathbb{N}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
    - $A_i, A_j \in A$
- **Th**
    - $\det(A_1, \ldots, A_i, \ldots, A_j , \ldots, A_n) = -\det(A_1, \ldots, A_j, \ldots, A_i, \ldots, A_n)$
- **Dim**
    - per il punto 2 della definizione di $\det$ si ha che $\det(A_1, \ldots, A_i + A_j, \ldots, A_j + A_i, \ldots, A_n) = 0$
    - allora, per multilinearità di $\det$ si ha che $\det$ si ha che $0 =\det(A_1, \ldots, A_i + A_j, \ldots, A_j + A_i, \ldots, A_n) = \det(A_1, \ldots, A_i, \ldots, A_j + A_i, \ldots, A_n) + \det(A_1, \ldots, A_j, \ldots, A_j + A_i, \ldots, A_n) =\det(A_1, \ldots, A_i, \ldots, A_j, \ldots, A_n)+\det(A_1, \ldots, A_i, \ldots, A_i, \ldots, A_n) + \det(A_1, \ldots, A_j, \ldots,A_j, \ldots, A_n) + \det(A_1, \ldots, A_j, \ldots, A_i, \ldots, A_n) = \det(A_1, \ldots, A_i, \ldots, A_j, \ldots, A_n) + 0 + 0 + \det(A_1, \ldots, A_j , \ldots, A_i, \ldots, A_n) \iff \det(A_1, \ldots, A_i, \ldots, A_j, \ldots, A_n) = -\det(A_1,\ldots, A_j, \ldots, A_i, \ldots, A_n)$
    - si noti che la tesi è verificata sia per righe che per colonne, per definizione di $\det$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N}$
    - $\mu \in \mathbb{K}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
    - $A_i, A_j \in A$
- **Th**
    - $\det(A_1, \ldots, A_i + \mu A_j , \ldots, A_n) = \det(A)$
- **Dim**
    - per il punto 1 della definizione di $\det$ si ha che $\det(A_1, \ldots, A_i + \mu A_j , \ldots, A_n) = \det(A_1,\ldots, A_i, \ldots, A_j, \ldots, A_n) + \mu \cdot\det(A_1, \ldots, A_j, \ldots, A_j, \ldots, A_n) = \det(A_1, \ldots, A_n) + \mu \cdot 0 = \det(A)$
    - si noti che la tesi è verificata sia per righe che per colonne, per definizione di $\det$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
- **Th**
    - $\det(A) = \det(A^T)$

## Formula di Leibniz

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
- **Th**
    - $\displaystyle{\det(A) = \sum_{\sigma \in \mathcal{S}_n} \textrm{sgn}(\sigma) \cdot \prod_{i=1}^n{a_{i, \sigma(i)}}}$

## Ex

- **Hp**
    - $\mathbb{K}$ campo
    - $A \in \textrm{Mat}_{2 \times 2}(\mathbb{K})$
    - $A = \left(\begin{array}{cc}a_{1,1} & a_{1, 2} \\ a_{2, 1} & a_{2, 2}\end{array}\right)$
- **Th**
    - $\det(A) = a_{1,1}a_{2,2}-a_{1,2}a_{2,1}$
- **Dim**
    - $\mathcal{S}_2 = \{(1,2), (2,1)\}$
    - si noti che $\left \{ \begin{array}{l} \textrm{sgn}(1,2)=(-1)^{|\varnothing|}=+1 \\ \textrm{sgn}(2,1)=(-1)^{\left|\{(2,1)\}\right|}=-1 \end{array}\right.$
    - allora, per la formula di Leibniz si ha $\det(A) = \textrm{sgn}(1, 2) (a_{1,1} a_{2, 2}) + \textrm{sgn}(2,1)(a_{1,2}a_{2,1}) = a_{1,1}a_{2,2} - a_{1,2}a_{2,1}$

## Ex

- **Hp**
    - $\mathbb{K}$ campo
    - $A \in \textrm{Mat}_{3 \times 3}(\mathbb{K})$
    - $A = \left(\begin{array}{ccc}a_{1,1} & a_{1, 2} & a_{1,3}\\ a_{2, 1} & a_{2, 2} & a_{2,3} \\ a_{3,1} & a_{3,2} & a_{3,3}\end{array}\right)$
- **Th**
    - $\det(A) = a_{1,1}a_{2,2}a_{3,3}+a_{1,3}a_{2,1}a_{3,2}+a_{1,2}a_{2,3}a_{3,1} - a_{1,3}a_{2,2}a_{3,1}-a_{1,1}a_{2,3}a_{3,2}-a_{1,2}a_{2,1}a_{3,3}$
- **Dim**
    - $\mathcal{S}_3 = \{(1,2,3), (1,3,2), (2,1,3), (2,3,1),(3,1,2),(3,2,1)\}$
    - si noti che $\left \{ \begin{array}{l} \textrm{sgn}(1,2,3)=(-1)^{|\varnothing|}=+1 \\ \textrm{sgn}(1,3,2)=(-1)^{\left|\{(3,2)\}\right|}=-1 \\ \textrm{sgn}(2,1,3)=(-1)^{\left|\{(2,1)\}\right|}=-1 \\ \textrm{sgn}(2,3,1)=(-1)^{\left| \{(3,1),(2,1)\}\right|}=+1 \\ \textrm{sgn}(3,1,2)=(-1)^{\left|\{(3,1),(3,2)\}\right|}=+1 \\ \textrm{sgn}(3,2,1)=(-1)^{\left|\{(3,2),(2,1),(3,1)\}\right|}=-1 \end{array}\right.$
    - allora, per la formula di Leibniz si ha $\det(A) =\textrm{sgn}(1,2,3)(a_{1,1}a_{2,2}a_{3,3})+\textrm{sgn}(1,3,2)(a_{1,1}a_{2,3}a_{3,2})+\textrm{sgn}(2,1,3)(a_{1,2}a_{2,1}a_{3,3})+\textrm{sgn}(2,3,1)(a_{1,2}a_{2,3}a_{3,1})+\textrm{sgn}(3,1,2)(a_{1,3}a_{2,1}a_{3,2})+\textrm{sgn}(3,2,1)(a_{1,3}a_{2,2}a_{3,1})=a_{1,1}a_{2,2}a_{3,3}-a_{1,1}a_{2,3}a_{3,2}-a_{1,2}a_{2,1}a_{3,3}+a_{1,2}a_{2,3}a_{3,1}+a_{1,3}a_{2,1}a_{3,2})-a_{1,3}a_{2,2}a_{3,1}$

## Formula di Laplace

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
- **Th**
    - $\forall 1 \le i, j \le n \quad \det(A) = \displaystyle \sum_{k = 1}^{n}{(-1)^{i + k}\cdot a_{i, k} \cdot \det(A_i^k)} = \sum_{h = 1}^n{(-1)^{h + j}\cdot a_{h, j} \cdot \det(A_h^j)}$

## Def

- **Matrice dei cofattori**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N}$
> - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
> - $A^*$ è detta **matrice dei cofattori di $A$** $\iff \forall i, j \in [1, n] \quad a^*_{i, j} = (-1)^{i + j}\cdot \det(A_i^j)$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K}) \mid \det(A) \neq 0$
- **Th**
    - $A^{-1}=\det(A)^{-1} \cdot (A^*)^T$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $A \in \textrm{Mat}_{2 \times 2}(\mathbb{K}) \mid \det(A) \neq 0$
    - $A = \left(\begin{array}{cc}a & b \\ c & d\end{array}\right)$
- **Th**
    - $A^{-1}=\dfrac{1}{ad - bc} \left(\begin{array}{cc}d & -b \\ -c & a\end{array}\right)$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
    1. $A$ invertibile
    2. $\textrm{rk}(A)=n$
    3. $A_1, \ldots, A_n$ base di $\mathbb{K}^n$
    4. $A^1, \ldots, A^n$ base di $\mathbb{K}^n$
    5. $\det(A) \neq 0$
    6. $A \equiv_R I_n$
    7. $A \equiv_C I_n$
- **Th**
    - le proposizioni sono equivalenti
- **Dim**
    - 1 $\iff$ 2
        - sia $B = (B^1, \ldots, B^n) \in \textrm{Mat}_{n \times n}(\mathbb{K}) \mid A \cdot B = B \cdot A = I_n$
        - allora $I_n = A \cdot B = (A \cdot B^1, \ldots, A \cdot B^n) = (\mathscr{L}_A(B^1), \ldots, \mathscr{L}_A(B^n)) \iff \left \{ \begin{array}{c} \mathscr{L}_A(B^1) = e_1 \\  \vdots \\  \mathscr{L}_A(B^n) = e_n \end{array} \right.\iff e_1, \ldots, e_n \in \textrm{im}(\mathscr{L}_A) \implies \textrm{span}(e_1, \ldots, e_n) \subseteq \textrm{im}(\mathscr{L}_A)$
        - $e_1, \ldots, e_n$ base canonica di $\mathbb{K}^n \implies \dim(\textrm{span}(e_1, \ldots, e_n)) = n$, allora segue necessariamente che $\textrm{span}(e_1, \ldots, e_n) \subseteq \textrm{im}(\mathscr{L}_A) \iff \textrm{span}(e_1, \ldots, e_n) = \textrm{im}(\mathscr{L}_A)$ 
        - allora $\textrm{rk}(A) := \textrm{rk}(\mathscr{L}_A) = \dim(\textrm{span}(A^1, \ldots, A^n)) = \dim(\textrm{im}(\mathscr{L}_A)) = \dim(\mathbb{K}^n) = n$
    - 2 $\iff$ 3 $\land$ 4
        - sia $\textrm{rk}(A) = n$
        - per dimostrazione precedente $n = \textrm{rk}(A) = \dim(\textrm{span}(A^1, \ldots, A^n)) = \dim(\textrm{span}(A_1, \ldots, A_n))$
        - in particolare $\dim(\textrm{span}(A_1, \ldots, A_n)) = n \iff \textrm{span}(A_1, \ldots, A_n) = \mathbb{K}^n$
        - per dimostrazione precedente $A_1, \ldots, A_n$ generatori di $\mathbb{K}^n \iff A_1, \ldots, A_n$ linearmente indipententi
        - allora, $A_1, \ldots, A_n$ base di $\mathbb{K}^n$
        - è possibile ripetere il ragionamento analogo per $A^1, \ldots, A^n$
    - 3 $\land$ 4 $\iff$ 5
        - per definizione di $\det$, $\det(A) \neq 0 \iff A_1, \ldots, A_n$ e $A^1, \ldots, A^n$ basi di $\mathbb{K}^n$
    - 2 $\iff$ 6 $\land$ 7
        - per definizione delle operazioni su righe e colonne, si ha che $\textrm{rk}(A) = n \iff A \equiv_R I_n$ oppure $A \equiv_C I_n$, poiché rimarranno solamente gli $1$ sulla diagonale e tutti gli altri elementi possono diventare $0$

****

# Polinomio caratteristico

## Def

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N}$
> - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
> - $p_A(x) := \det(x\cdot I_n - A)$ è detto **polinomio caratteristico di $A$**

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
- **Th**
    - $p_A(x) = x^n - \textrm{tr}(A)\cdot x^{n -1} + \ldots + (-1)^n \cdot \det(A)$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N}$
    - $A, B \in \textrm{Mat}_{n \times n}(\mathbb{K}) \mid A$ simile a $B$
- **Th**
    - $p_A(x) = p_B(x)$

## Def

- **Autovalore**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N}$
> - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
> - $\lambda \in \mathbb{K}$
> - $\lambda$ è detto **autovalore di $A$** $\iff p_A(\lambda) = 0$

- **Spettro**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N}$
> - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
> - $\textrm{sp}(A) := \{\lambda \in \mathbb{K} \mid p_A(\lambda) = 0\}$ è detto **spettro di $A$**

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N}$
    - $A, B \in \textrm{Mat}_{n \times n}(\mathbb{K}) \mid A$ simile a $B$
- **Th**
    - $\textrm{sp}(A) = \textrm{sp}(B)$
- **Dim**
    - $A$ simile a $B \implies p_A(x) = p_B(x)$, allora $\forall \lambda \in \textrm{sp}(A) \quad p_A(\lambda) = p_B(\lambda) = 0 \iff \lambda \in \textrm{sp}(B)$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
    - $\lambda \in \mathbb{K}$
- **Th**
    - $\lambda$ autovalore $\iff \exists v \in \mathbb{K}^n - \{0_{\mathbb{K}^n}\} \mid A \cdot v = \lambda \cdot v$
- **Dim**
    - $\exists v \in \mathbb{K}^n - \{0_{\mathbb{K}^n}\} \mid A \cdot v = \lambda \cdot v = \lambda \cdot I_n \cdot v \iff \exists v \in \mathbb{K}^n - \{0_{\mathbb{K}^n}\} \mid (A - \lambda \cdot I_n)\cdot v = 0 \iff v \in \ker(\mathscr{L}_{A - \lambda \cdot I_n}) \iff \ker(\mathscr{L}_{A - \lambda \cdot I_n}) \neq \{0_{\mathbb{K}^n}\} \iff \dim(\ker(\mathscr{L}_{A - \lambda \cdot I_n})) \gt 0$
    - per il teorema del rango $\textrm{rk}(\mathscr{L}_{A - \lambda \cdot I_n}) = \dim(\mathbb{K}^n) - \dim(\ker(\mathscr{L}_{A - \lambda \cdot I_n})) = n - \dim(\ker(\mathscr{L}_{A - \lambda \cdot I_n})) \lt n$, e in particolare $\textrm{rk}(\mathscr{L}_{A-\lambda \cdot I_n}) \neq n$
    - $\textrm{rk}(\mathscr{L}_{A- \lambda \cdot I_n}) \neq n \iff \det(A - \lambda \cdot I_n) = 0$ per dimostrazione precedente, e $\det(A - \lambda \cdot I_n) := p_A(\lambda) = 0 \iff \lambda$ autovalore

## Def

- **Autovettore relativo ad un autovalore**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N}$
> - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
> - $\lambda \in \textrm{sp}(A)$
> - $v \in \mathbb{K}^n - \{0_{\mathbb{K}^n}\}$
> - $v$ è detto **autovettore di $A$ relativo a $\lambda$** $\iff (A- \lambda \cdot I_n) \cdot v = 0$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
    - $\lambda_1, \ldots, \lambda_k \in \textrm{sp}(A)$
    - $v_1, \ldots, v_k$ autovettori di $A$ relativi rispettivamente a $\lambda_1, \ldots, \lambda_k$
- **Th**
    - $v_1, \ldots, v_k$ linearmente indipendenti

## Def

- **Autospazio relativo ad un autovalore**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N}$
> - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
> - $\lambda \in \textrm{sp}(A)$
> - $\textrm{E}_\lambda(A) := \{v \in \mathbb{K}^n \mid (A - \lambda \cdot I_n) \cdot v = 0\}$ è detto **autospazio di $A$ relativo a $\lambda$**
>   - in particolare $0_{\mathbb{K}^n} \in \textrm{E}_\lambda(A)$, altrimenti non sarebbe sottospazio vettoriale

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
    - $\lambda \in \textrm{sp}(A)$
- **Th**
    - $\textrm{E}_\lambda(A) \subset \mathbb{K}$ sottospazio vettoriale

## Def

- **Molteplicità algebrica di un autovalore**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N}$
> - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
> - $\lambda \in \textrm{sp}(A)$
> - $\mu(\lambda) := \underset{\varepsilon \in \mathbb{N}}{\operatorname{arg\,max}} \ (x - \lambda)^\varepsilon \mid p_A(x)$ è detta **molteplicità algebrica di $\lambda$**

- **Molteplicità geometrica di un autovalore**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N}$
> - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
> - $\lambda \in \textrm{sp}(A)$
> - $\nu(\lambda):=\dim(\textrm{E}_\lambda(A))$ è detta **molteplicità geometrica di $\lambda$**

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N}$
    - $A, B \in \textrm{Mat}_{n \times n}(\mathbb{K}) \mid A$ simile a $B$
    - $\lambda \in \textrm{sp}(A) = \textrm{sp}(B)$
- **Th**
    - $\mu_A(\lambda) = \mu_B(\lambda)$
    - $\nu_A(\lambda) = \nu_B(\lambda)$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
    - $\lambda \in \textrm{sp}(A)$
- **Th**
    - $\nu(\lambda) = n - \textrm{rk}(A - \lambda \cdot I_n)$
- **Dim**
    - $\textrm{E}_\lambda(A) := \{v \in \mathbb{K}^n \mid (A - \lambda \cdot I_n) \cdot v = 0\} =: \textrm{E}_\lambda(A) = \ker(\mathscr{L}_{A- \lambda \cdot I_n})$
    - allora, per il teorema del rango $\textrm{rk}(\mathscr{L}_{A - \lambda \cdot I_n}) = n - \dim(\ker(\mathscr{L}_{A - \lambda \cdot I_n})) \iff  \dim(\ker(\mathscr{L}_{A - \lambda \cdot I_n})) = n - \textrm{rk}(\mathscr{L}_{A - \lambda \cdot I_n}) = \dim(\textrm{E}_\lambda(A)) =: \nu(\lambda)$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
    - $\lambda \in \textrm{sp}(A)$
- **Th**
    - $\nu(\lambda) \le \mu(\lambda)$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
    1. $A$ triangolarizzabile
    2. $\displaystyle \sum_{\lambda \in \textrm{sp}(A)}{\mu(\lambda)} = n$
    3. $\displaystyle p_A(x) = \prod_{\lambda \in \textrm{sp}(A)}{(x - \lambda)}^{\mu(\lambda)}$, ovvero $p_A(x)$ è completamente fattorizzabile
- **Th**
    - le proposizioni sono equivalenti

## Oss

- **Hp**
    - $n \in \mathbb{N}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{C})$
- **Th**
    - $A$ è triangolarizzabile
- **Dim**
    - per dimostrazione precedente $A$ triangolarizzabile $\iff \displaystyle p_A(x) = \prod_{\lambda \in \textrm{sp}(A)}{(x - \lambda)}^{\mu(\lambda)}$, e per il teorema fondamentale dell'algebra, in $\mathbb{C}$ è sempre possibile fattorizzare un polinomio in polinomi di grado $1 \implies$ ogni matrice in $\textrm{Mat}_{n \times n}(\mathbb{C})$ è triangolarizzabile

## Oss

- **Hp**
    - $n \in \mathbb{N}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{R})$
- **Th**
    - $A$ triangolarizzabile $\iff \forall \lambda \in \textrm{sp}(A) \quad \lambda \in \mathbb{R}$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
    1. $A$ diagonalizzabile
    2. $\displaystyle \sum_{\lambda \in \textrm{sp}(A)}{\nu(\lambda)} = n$
    3. $\exists B^1, \ldots, B^n$ autovettori di $A \mid B^1, \ldots, B^n$ base di $\mathbb{K}^n$
- **Th**
    - le proposizioni sono equivalenti

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
    - $B^1, \ldots, B^n$ autovettori di $A \mid B = (B^1, \ldots, B^n) \in \textrm{GL}(n, \mathbb{K}) \land B^1, \ldots, B^n$ base di $\mathbb{K}^n$
- **Th**
    - $A$ diagonalizzabile, dove $B$ è la matrice diagonalizzante

