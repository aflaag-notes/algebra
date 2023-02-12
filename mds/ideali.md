# Ideali

## Def

- **Ideali**

> - $(A, +, \cdot)$ anello
> - $I \subset A$ è detto **ideale** $\iff$
>    - $(I, +) \leqslant (A, +)$
>    - $A \cdot I \subseteq I$
>    - $I \cdot A \subseteq I$

## Oss

- **Hp**
  - $(A, +, \cdot)$ anello
  - $a \in \mathbb{Z}$
  - $I(a) := \{ax \mid x \in A\}$
- **Th**
  - $I(a)$ è un ideale, e prende il nome di _ideale di $A$ generato da $a$_
- **Dim**
  - $(I(a), + ) \leqslant (A, +)$
    -  $0$ multiplo di $a \implies 0 \in I(a)$
    - $\forall ax, ay \in I(a) \quad ax + ay = a(x + y) \implies ax + ay \in I(a)$ per definizione
    - $\forall ax \in I(a) \quad a(-x) \in I(a)$ poiché $-x$ è un multiplo di $a$, e $a(-x) = -ax \in I(a)$, che corrisponde all'opposto di $ax$ rispetto a $+$
  - $A \cdot I \subseteq I \iff \forall x \in I(a), b \in A \quad bx \in I(a)$
    - $x \in I(a) \iff \exists c \in A \mid x = ac \implies bx = b (ac) = a(bc)$, poiché il prodotto è commutativo, e dunque $bx \in I(a)$ per definizione
  - poiché il prodotto è commutativo, $A \cdot I \subseteq I \implies I \cdot A \subseteq I$

## Oss

- **Hp**
    - $A$ dominio di integrità
    - $a, b \in A$
- **Th**
    - $I(a)=I(b) \iff \exists c \in A^* \mid a = bc$
- **Dim**
    - _prima implicazione_
        - $I(a) = I(b)$ in ipotesi
            - $a \in I(a) = I(b) \implies b \mid a \implies \exists c \in A \mid a = bc$
            - $b \in I(b) = I(a) \implies a \mid b \implies \exists d \in A \mid b = da$
        - allora $a = bc \iff a = da \cdot c = a \cdot cd \iff a - acd = 0 \iff a(1 - cd) = 0$
        - $A$ dominio $\implies$ in $A$ vale la legge di annullamento del prodotto, dunque $a(1 - cd) = 0 \iff a = 0 \lor 1 - cd = 0$
            - $a = 0 \implies b = da = 0$, ma allora $a, b = 0 \implies a = 0 = 0 \cdot 1 = b \cdot 1$, e ponendo $c:= 1$ è vero che $a = bc$
                - in particolare, $c := 1 \implies \exists c^{-1} = 1^{-1} = 1$
            - $1 - cd = 0 \iff -cd = -1 \iff cd = 1$, dunque $d$ è l'inverso di $c$
    - _seconda implicazione_
        - $\exists c \in A^* \mid a= bc \implies b \mid a \implies a \in I(b) \implies I(a) \subset I(b)$
        - $c \in A^* \implies \exists c^{-1} \in A$, dunque $a = bc \iff a \cdot c^{-1} = b \implies a \mid b \implies b \in I(a) \implies I(b) \subset I(a)$
        - dunque $I(a) = I(b)$ per doppia inclusione

## Oss

- **Hp**
  - $a, b \in \mathbb{Z} - \{0\}$
- **Th**
  - $I(a)=I(b) \iff a=\pm b$
- **Dim**
    - $a=\pm b \implies I(a)=I(b)$
      - $a = b \implies I(a)$ e $I(b)$ coincidono
      - $a = -b \implies I(-b) = \{ k(-b) \mid k \in \mathbb{Z}\} = \{(-k)b \mid (-k) \in \mathbb{Z}\} = I(b) = I(-b)=I(a)$
    - $I(a) = I(b) \implies a = \pm b$
      - $I(a) = I(b) \iff a \in I(b) \land b \in I(a) \implies \exists p, q \in \mathbb{Z} \mid a = pb \wedge b = qa$, di conseguenza $b = q (pb) \implies b = (qp)b \implies pq = 1 \iff p = q = 1 \lor p = q = -1 \implies a = \pm b$

## Oss

- **Hp**
  - $(A, +, \cdot)$ anello
  - $a_1, \ldots, a_n \in\mathbb{Z}$
  - $I(a_1, \ldots, a_n) := \{ a_1b_1 + \ldots +a_nb_n \mid b_1, \ldots, b_n \in A\}$
- **Th**
  - $I(a_1, \ldots, a_n)$ è un ideale, e prende il nome di _ideale di $A$ generato dagli $a_1, \ldots, a_n \in A$_
- **Dim**
  - $(I(a_1, \ldots, a_n) , +) \leqslant (A, +)$
    - $0 = a_1 \cdot 0  + \ldots + a_n \cdot 0 \in I(a_1, \ldots a_n)$, dunque $0$ è l'elemento neutro
    - $\forall x, y \in I(a_1, \ldots, a_n) \quad x = a_1b_1 + \ldots +a_nb_n \land y = a_1c_1 + \ldots+ a_nc_n \implies x+ y = a_1b_1 + \ldots + a_nb_n + a_1c_1 + \ldots +a_nc_n$, che è possibile riscrivere come $x + y = a_1(b_1 + c_1) + \ldots + a_n(b_n + c_n)$, che per definizione implica che $x + y \in I(a_1, \ldots, a_n)$
    - $\forall x \in I(a_1, \ldots, a_n) \quad x = a_1b_1 + \ldots + a_nb_n \iff -x = -a_1b_1 - \ldots - a_nb_n \iff -x = a_1(-b_1) + \ldots + a_n(-b_n)$, che per definizione implica che $-x \in I(a_1, \ldots, a_n)$
  - $\forall x \in I(a_1, \ldots, a_n), c \in A \quad x = a_1b_1 + \ldots + a_nb_n \implies c \cdot x = a_1 (b_1c)+ \ldots + a_n(b_nc)$, che per definizione implica che $cx \in I(a_1, \ldots, a_n)$

## Def

- **Dominio ad ideali principali**

> - $A$ dominio di integrità
> - $A$ è detto **ad ideali principali** $\iff \forall I \subset A$ ideale$\quad \exists d \in I \mid I = I(d)$

## Oss

- **Hp**
  - $I \subset \mathbb{Z}$ ideale
- **Th**
  -  $\exists  d  \in I \mid I = I(d)$, o equivalentemente, in $\mathbb{Z}$ ogni ideale è principale
- **Dim**
    - $d = 0$
        - $I = \{0\} \implies I = I(0)$ poiché i multipli di $0$ sono tutti pari a $0$
        - se invece $I \neq \{0\} \implies I \cap \mathbb{Z}_{>0} \neq \varnothing$, dunque $I$ contiene almeno un numero non nullo, in particolare positivo
        - è possibile considerare solo il caso dei positivi in quanto $\forall x \in I - \{0\} \quad -x \in I$ per definizione di $I$, dunque per valori negativi è sufficiente considerare il loro opposto
        - dunque, ha senso considerare $d:=\min(I \cap \mathbb{Z}_{\gt 0})$, che esiste per principio del minimo numero
    - $d \gt 0$
        - $I(d)=I \implies I(d) \subseteq I \wedge I \subseteq I(d)$
          - $I(d) \subseteq I$
            - $\forall x \in I(d) \quad \exists y \in \mathbb{Z} \mid x = dy$ per definizione
            - $I \subset \mathbb{Z}$ ideale $\implies I \cdot \mathbb{Z} \subset I$ 
            - $d := \min(I \cap \mathbb{Z}_{\gt 0}) \implies d \in I \implies y \in \mathbb{Z} \land d \in I \implies dy \in I \implies x \in I \implies I(d) \subseteq I$
          - $I \subseteq I(d)$
            - $d := \min(I \cap \mathbb{Z}_{\gt 0}) \implies d \neq 0$
            - per il teorema della divisione euclidea con il resto $\forall x \in I \quad \exists ! q,r \in \mathbb{Z} \mid x=d q+r \quad 0 \leq r<d$
              - $r = 0 \iff x = dq \implies x \in I(d)$ per definizione, dunque $I \subseteq I(d)$
              - ipotizzando $r \neq 0$
                - $dq \in I(d) \implies dq \in I$ per dimostrazione precedente
                - quindi $x = dq + r \implies r = x - dq \in I$ poiché $I$ è un ideale
                - $r \neq 0 \implies r \in I \cap \mathbb{Z}_{\gt 0}$
                - per definizione, $0 \le r \lt d$, ma $d:=\min(I \cap \mathbb{Z}_{\gt 0})$, quindi il minimo numero che $d$ può assumere è $1$, e poiché $r < d \implies r = 0$ necessariamente, dunque segue la dimostrazione precedente
    - dunque, ogni ideale in $\mathbb{Z}$ è generato dall'insieme dei multipli di un certo $d \ge 0$, che esiste sempre ed è unico, e di conseguenza $\mathbb{Z}$ è un anello ad ideali principali

## Def

- **Massimo Comun Divisore**

> - $a_{1}, \ldots , a_{n} \in \mathbb{Z}$
> - $\exists !d \in \mathbb{N}  \mid I\left(a_{1}, \ldots , a_{n}\right)=I(d)$, ed è detto **massimo comun divisore degli $a_1, \ldots, a_n$**
>   - poiché $\mathbb{Z}$ è dominio ad ideali principali, $\exists d \in I(a_1, \ldots, a_n) \mid I(a_1, \ldots, a_n) = I(d)$, poiché $I(a_1, \ldots, a_n)$ è ideale per dimostrazione precedente
>   - allora considerando la definizione canonica di $d :=\textrm{MCD}(a_1, \ldots, a_n)$ in cui $d \ge0$, si ha che $d \in \mathbb{N}$ è unico
>   - in particolare, $d \in \mathbb{Z}$ non è unico poiché $I(d) = I(-d)$

## Oss

- **Hp**
    - $a_1, \ldots, a_n \in \mathbb{Z}$
    - $\exists ! d \in \mathbb{N} \mid I(d) = I(a_1, \ldots, a_n)$
- **Th**
    - $d = \textrm{MCD}(a_1, \ldots, a_n)$
- **Dim**
    - $d$ è _divisore comune_
        - $I(d) = I(a_1, \ldots, a_n) \implies \forall x \in I(a_1, \ldots, a_n) \quad x \in I(d) \implies d \mid x$ per definizione di $I(d)$
        - preso ad esempio $a_1$, è possibile riscriverlo come $a_1 = a_1 \cdot 1 + a_2 \cdot 0 + \ldots + a_n \cdot 0$, di conseguenza $a_1 \in I(a_1, \ldots, a_n)$, dunque $d \mid a_1$
        - vale il ragionamento analogo per ogni $a_1, \ldots , a_n$, dunque $d \mid a_1, \ldots, a_n$
    - $d$ è il _massimo tra i divisori comuni_
        - $d$ è il massimo tra i divisori comuni se $\forall k \in \mathbb{Z}: k \mid a_1, \ldots, a_n \quad  k \mid d$
        - $\forall i \in [1, n] \quad k \mid a_i \iff \exists x_i \in \mathbb{Z} \mid kx_i = a_i$
        - $d \in I(d) = I(a_1, \ldots, a_n) \iff d \in I(a_1, \ldots, a_n) \implies \exists b_1, \ldots b_n \in \mathbb{Z} \mid d = a_1 b_1 + \ldots + a_n b_n$, e per osservazione precedente si ottiene che $d = kx_1b_1 + \ldots + kx_nb_n = k(b_1x_1 + \ldots + b_nx_n) \implies k \mid d$

## Oss

- **Hp**
  - $a_1, \ldots, a_n \in \mathbb{Z}$
  - $d := \textrm{MCD}(a_1, \ldots, a_n)$
- **Th**
  - $\exists x_1, \ldots, x_n \in \mathbb{Z} \mid a_1 x_1 + \ldots + a_nx_n=d$, che prende il nome di _identità di Bézout_
- **Dim**
  - per dimostrazione precedente, $I(a_{1}, \ldots a_{n})=I(d)$, quindi $d \in I(a_1, \ldots, a_n) \implies \exists x_1, \ldots, x_n \in \mathbb{Z} \mid a_1x_1 + \ldots + a_n x_n = d$

****

# Operazioni sugli ideali

## Def

- **$+$ tra ideali**

> - $(A, +, \cdot)$ anello commutativo
> - $I, J \subset A$ ideali
> - $I + J = \{i + j \mid i \in I, j \in J\}$ è detta **somma tra $I$ e $J$**

## Oss

- **Hp**
  - $(A, +, \cdot)$ anello commutativo
  - $I, J \subset A$ ideali
- **Th**
  - $I + J$ è un ideale
- **Dim**
  - ⚠️ **rivedila fa schifo**
  - $0 \in I, 0 \in J, 0+0=0 \implies 0 \in I + J$
  - la chiusura rispetto a $+$ deve implicare che $\forall i_1, i_2 \in I, j_1, j_2 \in J \quad (i_1 + j_1) + (i_2 + j_2) \in I + J$, allora si ottiene che $(i_1 + j_1) + (i_2 + j_2) = (i_1 + i_2) + (j_1 + j_2)$, e $i_1 + i_2 \in I, j_1 + j_2 \in J \implies (i_1 + i_2) + (j_1 + j_2) \in I + J$
  - $\forall i \in I, j \in J \quad i + j \in I + J$, l'opposto rispetto a $+$ di $i + j$ è $- (i + j) = (-i) + (-j)$, e $\forall i \in I, j \in J \quad -i \in I, -j \in J  \implies (-i) + (-j) \in I + J$
  - $A \cdot I \subseteq I \implies \forall a \in A, i \in I, j \in J \quad a(i + j) \in I + J$
    - $i + j \in I + J$ per definizione, e $a(i + j) = ai + aj$, e $ai \in I, aj \in J$ per definizione, quindi $ai + aj \in I + J$

## Def

- **$\cap$ tra ideali**

> - $(A, +, \cdot)$ anello commutativo
> - $I, J \subset A$ ideali
> - $I \cap J = \{x \mid x \in I \land x \in J\}$ è detta **intersezione tra $I$ e $J$**

## Oss

- **Hp**
    - $(A, +, \cdot)$ anello commutativo
    - $I, J \subset A$ ideali
- **Th**
    - $I \cap J$ è un ideale
- **Dim**
    - $0 \in I \land 0 \in J \implies 0 \in I \cap J$
    - $\forall x, y \in I \cap J \quad x, y \in I \land x, y \in J \implies x + y \in I \land x + y \in J \implies x + y \in I \cap J$
    - $\forall x \in I \cap J \quad x \in I \land x \in J \implies x^{-1} \in I \land x ^{-1} \in J \implies x^{-1} \in I \cap J$
    - $\forall a \in A, x \in I \cap J \quad x \in I \land x \in J \implies ax \in I \land ax \in J \implies ax \in I \cap J$

## Def

- **Minimo Comune Multiplo**

> - $a_{1}, \ldots, a_{n} \in \mathbb{Z}$
> - $\displaystyle \exists ! m  \in \mathbb{N} \mid I(m) = I(a_1) \cap \ldots \cap I(a_n) = \bigcap_{i=1}^{n}{I(a_i)}$, ed è detto **minimo comune multiplo degli $a_1, \ldots, a_n$**
>   - poiché $\mathbb{Z}$ è dominio ad ideali principali, $\exists m \in \displaystyle \bigcap_{i = 1}^n{I(a_i)} \mid \bigcap_{i = 1}^n{I(a_i)} = I(m)$, poiché $\displaystyle \bigcap_{i=1}^{n}{I(a_i)}$ è ideale per dimostrazione precedente
>   - allora considerando la definizione canonica di $m :=\textrm{mcm}(a_1, \ldots, a_n)$ in cui $m \ge0$, si ha che $m \in \mathbb{N}$ è unico
>   - in particolare, $m \in \mathbb{Z}$ non è unico poiché $I(m) = I(-m)$

## Oss


- **Hp**
    - $a_1, \ldots, a_n \in \mathbb{Z}$
    - $\exists ! m \in \mathbb{N} \mid I(m) = \displaystyle \bigcap_{i=1}^n{I(a_i)}$
- **Th**
    - $m = \textrm{mcm}(a_1, \ldots, a_n)$
- **Dim**
    - $m$ è _multiplo comune_
        - $I(m) = \displaystyle \bigcap_{i=1}^n{I(a_i)} \implies m \in I(a_1) \cap \ldots \cap I(a_n) \implies \forall i \in [1, n] \quad \exists x_i \in \mathbb{Z} : a_ix_i = m \iff a_i \mid k$
    - $m$ è il _minimo tra i multipli comuni_
        - $m$ è il minimo tra i multipli comuni se $\forall k \in \mathbb{Z} : a_1, \ldots, a_n \mid k \quad  m \mid k$
        - $\forall i \in [1, n] \quad a_i \mid k \iff \exists x_i \in \mathbb{Z} \mid a_ix_i = k \iff k \in I(a_i)$, allora $k \in I(a_1) \cap \ldots \cap I(a_n) = I(m)$
        - in particolare $k \in I(m) \iff m \mid k$

## Oss

- **Hp**
    - $a, b \in \mathbb{Z}$
    - $d := \textrm{MCD}(a, b)$
    - $m := \textrm{mcm}(a, b)$
    - $x_0, y_0 \in \mathbb{Z} \mid d = a x_0 + b y_0$, dunque $x_0, y_0$ soddisfano l'equazione di Bézout
- **Th**
    - $ax + by = d \iff \left \{ \begin{array}{l}x = x_0 + \dfrac{m}{a}k \\ \\ y = y_0 - \dfrac{m}{b}k\end{array}\right. \forall k \in \mathbb{Z}$
- **Dim**
    - $a \left (x_0 + \dfrac{m}{a}k \right) + b \left(y_0 - \dfrac{m}{b}k \right) = ax_0 + mk + by_0 -mk = ax_0 + by_0 = d \implies x_0$ e $y_0$ rispettano il sistema
    - per verificare che ogni soluzione è di questa forma, presi $x_1, y_1 \in \mathbb{Z} \mid a x_1 + by_1 = d$ si ha che $\left \{ \begin{array}{l} ax_0 + by_0 = d \\ a x_1 + by_1 = d \end{array} \right. \implies ax_0 + by_0 = ax_1 + by_1 \iff a(x_1 - x_0) = b(y_0 - y_1) =: N \implies a, b \mid N \implies m \mid N \iff \exists k \in \mathbb{Z} \mid mk = N \iff \left \{ \begin{array}{l} a(x_1 - x_0) = mk \\ \\ b(y_0 - y_1) = mk \end{array} \right . \iff \left \{\begin{array}{l} x_1 - x_0 = \dfrac{m}{a}k \\ \\ y_0 - y_1 = \dfrac{m}{b}k \end{array} \right. \iff \left \{ \begin{array}{l} x_1 = x_0 + \dfrac{m}{a}k \\ \\ y_1 = y_0 - \dfrac{m}{b}k \end{array} \right.$

## Def

- **$\cdot$ tra ideali**

> - $(A, +, \cdot)$ anello commutativo
> - $I, J \subset A$ ideali
> - $I \cdot J = \{i_1 j_1 + \ldots + i_k j_k \mid k \ge  1, i_1 , \ldots , i_k \in I, j_1 , \ldots , j_k \in J \}$ è detto **prodotto tra $I$ e $J$**

## Oss

- **Hp**
  - $(A, +, \cdot)$ anello commutativo
  - $I, J \subset A$ ideali
- **Th**
  - $I \cdot J$ è un ideale
- **Dim**
    - $0 \in I \land 0 \in J \implies 0 \cdot 0 = 0 \in I \cdot J$
    - $\forall x, y \in I \cdot J \quad \exists i_1, \ldots, i_k, i_1', \ldots, i_h' \in I, j_1, \ldots, j_k, j_1', \ldots, j_h' \in J \mid x = i_1j_1 + \ldots + i_k j_k \land y = i_1'j_1' + \ldots + i_h'j_h' \implies x + y = i_1j_1 + \ldots + i_kj_k + i_1'j_1'+ \ldots + i_hj_h' \in I\cdot J$
    - $\forall x \in I \cdot J \quad \exists i_1, \ldots, i_k \in I, j_1, \ldots, j_k \in J \mid x = i_1j_1 + \ldots + i_kj_k \implies -x = (-i_1j_1) + \ldots + (-i_kj_k) \in I \cdot J$
    - $I$ ideale $\implies \forall a \in A, i \in I \quad a i \in I$, allora $\forall x \in I \cdot J \quad \exists i_1, \ldots, i_k \in I, j_1, \ldots, j_k \in J \mid x = i_1j_1 + \ldots + i_kj_k \implies \forall a \in A \quad a\cdot x = a(i_1j_1 + \ldots + i_kj_k) = (ai_1)j_1 + \ldots + (ai_k)j_k \in I \cdot J$

## Oss

- **Hp**
  - $a, b \in \mathbb{Z}$
  - $d:= \textrm{MCD}(a, b)$
- **Th**
  - $I(a) + I(b) = I(d)$
- **Dim**
   - per dimostrazione precedente $I(a)$ e $I(b)$ sono ideali, e poiché la somma tra ideali è ben definita, allora $I(a)+I(b)=\{i+j \mid i \in I(a), j \in I(b) \}$
   - $i \in I(a) \implies \exists x \in \mathbb{Z} \mid i = ax$ e $j \in I(b) \implies \exists y \in \mathbb{Z} \mid j = by$
   - quindi $i + j = ax + by \implies$ $I(a)+I(b)=\{a x+b y \mid x, y \in \mathbb{Z}\} = I(a, b)$ per definizione
   - in particolare, per dimostrazione precedente, $I(a, b) = I(d)$
   - questa dimostrazione si può estendere per un numero arbitrario di ideali, ottenendo $I(a_1) + \ldots + I(a_n) = I(\textrm{MCD}(a_1, \ldots, a_n))$

## Oss

- **Hp**
  - $a, b \in \mathbb{Z}$
- **Th**
  - $I(a) \cdot I(b)=I(a \cdot b)$
- **Dim**
  - $I(a) \cdot I(b) \subseteq I(a \cdot b)$
    - per dimostrazione precedente $I(a)$ e $I(b)$ sono ideali, e poiché il prodotto tra ideali è ben definito, allora $x \in I(a) \cdot I(b) \implies x = i_1 j_1 + \ldots + i_k j_k$ con $i_1 , \ldots , i_k \in I(a)$ e $j_1 , \ldots , j_k \in I(b)$
    - per definizione, $i \in I(a) \implies \exists x \in \mathbb{Z} \mid i = ax$, e dunque $i_1, \ldots, i_k = ax_1, \ldots, ax_k$ con $x_1, \ldots, x_k \in \mathbb{Z}$
    - analogamente $j_1, \ldots, j_k = by_1, \ldots, by_k$ con $y_1, \ldots, y_k \in \mathbb{Z}$
    - segue che $x = (ax_1)(by_1),+\ldots+ (ax_k)(by_k) = ab\cdot(x_1y_1+ \ldots+ x_ky_k)$
    - poiché $(x_1y_1+ \ldots+ x_ky_k) \in \mathbb{Z}$, segue che $ab \mid x \implies x \in I(a \cdot b)$
  - $I(a \cdot b) \subseteq I(a) \cdot I(b)$
    - $x \in I(a \cdot b) \implies \exists k \in \mathbb{Z} \mid x = ab \cdot k$
    - $x = abk$, ma $a \in I(a) \land bk \in I(b) \implies x \in I(a) \cdot I(b)$

