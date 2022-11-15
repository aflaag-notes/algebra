# Permutazioni

## Def

- **Permutazioni**
> - $X$ insieme
> - $S_X := \{f \mid f:X \rightarrow X$ biiettiva $\}$ è l'**insieme delle permutazioni di $X$**
> - $X = \{1, \ldots, n\} \implies S_n$ è detto **gruppo simmetrico di $n$**

- **Ciclo di una permutazione**
> - $n \in \mathbb{N}$
> - $\sigma \in S_n$
> - $\exists 1 \leq i_1, \ldots, i_d \leq n \in \mathbb{N} \mid \left\{\begin{array}{c}
\sigma\left(i_{1}\right)=i_{2} \\
\sigma\left(i_{2}\right)=i_{3} \\
\vdots \\
\sigma\left(i_{d-1}\right)=i_{d} \\
\sigma\left(i_{d}\right)=i_{1}
\end{array}\right. \implies i_1, \ldots, i_n$ costituiscono un **ciclo di $\sigma$**

## Oss

- **Hp**
  - $n \in \mathbb{N}$
  - $\sigma \in S_n$
  - $1 \le i \lt n \in \mathbb{N}$
  - $I(\sigma, i):=\left\{n \in \mathbb{Z} \mid \sigma^{n}(i)=i\right\}$
- **Th**
  - $(I(\sigma, i), +) \subset (\mathbb{Z}, +)$ è un ideale
- **Dim**
  - $(I(\sigma, i), +) \subset (\mathbb{Z}, +)$ è un sottogruppo
    - $\sigma ^0 = \textrm{id} \implies \forall i \quad \sigma ^0(i) = \textrm{id}(i) = i \implies 0 \in I(\sigma, i)$
    - $m, n \in I(\sigma, i) \implies \sigma^m (i) = \sigma^n(i) = i$, ma $\sigma^{m+n}(i)=\sigma^{m}\left(\sigma^{n}(i)\right) = \sigma^m(i)=i \implies m + n \in I(\sigma, i)$
    - $n \in I(\sigma, i) \implies \sigma ^n (i) = i$, ma per simmetria della permutazione $\sigma^ {-n} (i) = i \implies -n \in I(\sigma, i)$
  - $\forall \tau \in S_n \mid \tau (i) = i \implies \forall k \in \mathbb{Z} \quad  \tau ^k (i) = i$, ma allora $\forall n \in I(\sigma, i) \quad \sigma^n(i) = i$ si può riscrivere come $(\sigma^n)^k(i) = i \quad \forall k \in \mathbb{Z} \implies \sigma^{nk}(i) = i \implies nk \in I(\sigma, i)$

## Oss

⚠️ **CHE CAZZO HO SCRITTO**
- $I(\sigma, i)$ è **ideale principale** in $\mathbb{Z}$ generato da $I(d)$, dove $d$ è la lunghezza del ciclo di $i$, quindi $I(\sigma, i) = I(d)$
  - $I(\sigma, i) = I(d) \implies d \in I(\sigma, i)$
  - ⚠️ **MANCA DIMOSTRAZIONE**

## Cor

- **Hp**
  - $n \in \mathbb{N}$
  - $\sigma \in S_n \mid \sigma = \gamma_1 \ldots \gamma_k$ sia la sua decomposizione in cicli
  - $d_j:=$ lunghezza di $\gamma_j \quad \forall j \in [1, k]$
  - $m := \textrm{mcm}(d_1, \ldots, d_k)$
  -  $I(\sigma):=\left\{n \in \mathbb{Z} \mid \sigma^{n}=\textrm{id}\right\}$
- **Th**
  - $o(\sigma) = m$
- **Dim**
  - $n \in I(\sigma) \iff \sigma^{n}=\textrm{id} \iff \forall 1 \leq i \leq n \quad \sigma^{n}(i)=i \iff \forall 1 \leq i \leq n \quad n \in I(\sigma, i) \iff n \in I(\sigma, 1) \cap \ldots \cap I(\sigma, n)$
  - di conseguenza $n \in I(\sigma) \iff n \in I(\sigma, 1) \cap \ldots \cap I(\sigma, n)$ e dunque $I(\sigma) =I(\sigma, 1) \cap \ldots \cap I(\sigma, n)$
  - inoltre, per dimostrazione precedente $I(\sigma) = I(\sigma, 1) \cap \ldots \cap I(\sigma, n) = I(d_1) \cap \ldots \cap I(d_k)$
  - per dimostrazione precedente $I(d_1) \cap \ldots \cap I(d_k) = I(m) = I(\sigma)$
  - ⚠️ **MANCA LA CONCLUSIONE FINALE**

****

# Trasposizioni

## Def

- **Trasposizione**
> - $n \in \mathbb{N}$
> - $i, j \in \mathbb{N} \mid 1 \leq i \lt j \leq n \quad$
> - $k \in [1, n]$
> - $\tau_{i, j} \in S_n \mid \tau_{i, j} =$$\left\{\begin{array}{ll}j & k=i \\ i & k=j \\ k & k \neq i, j\end{array}\right.$ è detta **trasposizione**, ovvero una permutazione che inverte esclusivamente due elementi tra loro
>   - $\tau_{i, j}^2 = \textrm{id} \iff \tau_{i, j} = \tau_{i, j} ^{-1}$

- **Trasposizioni adiacente**
> - $n \in \mathbb{N}$
> - $i, j \in \mathbb{N} \mid 1 \le i \lt j \le  n \land  j = i + 1$
> - $\tau_{i, j}=\tau_{i, i+1}$ è detta **trasposizione adiacente**, poiché inverte esclusivamente due elementi, adiacenti, tra loro

## Oss

- **Hp**
  - $n \in \mathbb{N}$
  - $\sigma \in S_n$
- **Th**
  - $\exists 1 \leq i_1, \ldots, i_k \lt n \mid \sigma = \tau_{i_1, i_1 + 1} \ldots \tau_{i_k, i_k + 1}$, quindi ogni permutazione può essere riscritta come composizione di trasposizioni adiacenti
- **Dim**
  - $\tau_{i, j}=\left(\begin{array}{ccccccc}1 & \cdots & i & \cdots & j & \cdots & n \\ 1 & \cdots & j & \cdots & i & \cdots & n\end{array}\right)$ è una trasposizione qualsiasi
  - $\sigma=\left(\begin{array}{ccccccc}1 & \cdots & i & \cdots & j & \cdots & n \\ \sigma(1) & \cdots & \sigma(i) & \cdots & \sigma(j) & \cdots & \sigma(n) \end{array}\right)$ è una permutazione
  - allora $\sigma \tau_{i, j}=\left(\begin{array}{ccccccc}1 & \cdots & i & \cdots & j & \cdots & n \\ \sigma(1) & \cdots & \sigma(j) & \cdots & \sigma(i) & \cdots & \sigma(n) \end{array}\right)$
  - in particolare, se le trasposizioni devono essere adiacenti, allora ogni trasposizione invertirà due colonne adiacenti alla volta
  - _esempio_
    - $\sigma=\left(\begin{array}{llll}1 & 2 & 3 & 4 \\ 2 & 4 & 3 & 1\end{array}\right) \implies \sigma \tau_{34}\left(\begin{array}{llll}1 & 2 & 3 & 4 \\ 2 & 4 & 1 & 3\end{array}\right) \implies$ $\sigma \tau_{3 4} \tau_{23}=\left(\begin{array}{llll}1 & 2 & 3 & 4 \\ 2 & 1 & 4 & 3\end{array}\right) \implies$$\sigma \tau_{3 4} \tau_{23} \tau_{12}=\left(\begin{array}{llll}1 & 2 & 3 & 4 \\ 1 & 2 & 4 & 3\end{array}\right) \implies$$\sigma \tau_{34} \tau_{23} \tau_{12} \tau_{34}=\left(\begin{array}{llll}1 & 2 & 3 & 4 \\ 1 & 2 & 3 & 4\end{array}\right) = \textrm{id}$, ma allora $\textrm{id} = \sigma \tau_{34} \tau_{23} \tau_{12} \tau_{34} \iff \sigma =\tau_{34} \tau_{12} \tau_{23} \tau_{34}$
     
****

# Segno

## Def

- **Segno di una permutazione**
> - $n \in \mathbb{N}$
> - $\sigma \in S_n$
> - $\textrm{Inv}(\sigma) := \{ (i, j) \mid 1 \leq i \lt j \lt n : \sigma(i) \gt \sigma(j)\}$ è l'**insieme delle inversioni di $\sigma$**
> - $\textrm{sgn}(\sigma) := (-1)^{|\textrm{Inv}(\sigma)|} =$$\left\{\begin{array}{ll}+1 & |\operatorname{Inv}(\sigma)| \equiv 0 \ (\bmod 2) \\ -1 & |\operatorname{Inv}(\sigma)| \equiv 1 \ (\bmod 2)\end{array}\right. \implies \sigma$ **pari** $\iff \textrm{sgn}(\sigma) = +1$
>   - $\textrm{sgn}(\textrm{id}) = (-1)^0 = 1$, in quando la funzione identità non ha inversioni


## Oss

- **Hp**
    - $\sigma \in S_{n} \mid \sigma=\tau_{1} \ldots \tau_{k}$ dove $\forall j \in [1, k] \quad \tau_{j} = \tau_{j, j + 1}$, dunque tutte le trasposizioni sono adiacenti
- **Th**
    - $\textrm{sgn}(\sigma)= (-1)^k$
- **Dim**
   - $\tau_{i, i + 1}=\left(\begin{array}{ccccccc}1 & \cdots & i &  & i + 1 & \cdots & n \\ 1 & \cdots & i + 1 &  & i & \cdots & n\end{array}\right)$ è una trasposizione adiacente
  - $\sigma=\left(\begin{array}{ccccccc}1 & \cdots & i &  & i + 1 & \cdots & n \\ \sigma(1) & \cdots & \sigma(i) &  & \sigma(i + 1) & \cdots & \sigma(n) \end{array}\right)$ è una permutazione
  - allora $\sigma \tau_{i, i + 1}=\left(\begin{array}{ccccccc}1 & \cdots & i &  & i + 1 & \cdots & n \\ \sigma(1) & \cdots & \sigma(i + 1) &  & \sigma(i) & \cdots & \sigma(n) \end{array}\right)$
  - di conseguenza $\textrm{Inv}(\sigma \tau_{i, i + 1})=$$\left\{\begin{array}{ll}\operatorname{Inv}(\sigma) \cup\{(i, i+1)\} & (i, i+1) \notin \operatorname{Inv}(\sigma) \\ \operatorname{Inv}(\sigma)-\{(i, i+1)\} & (i, i+1) \in \operatorname{Inv}(\sigma)\end{array}\right.$
    - $(i, i + 1) \in \textrm{Inv}(\sigma) \implies \sigma(i) \gt \sigma(i + 1)$ (poiché $i \lt i + 1 \quad \forall i$)
    - di conseguenza, in $\sigma \tau_{i, i + 1}$, poiché sto invertendo le colonne $i$ e $i + 1$, $\sigma \tau_{i, i + 1}(i) \lt \sigma \tau_{i, i + 1}(i +1) \implies (i, i + 1) \notin \textrm{Inv}(\sigma \tau_{i, i + 1})$ per definizione (vale il ragionamento opposto per il caso $(i, i + 1) \in \textrm{Inv}(\sigma)$)
  - dunque $\mid \textrm{Inv}(\sigma \tau_{i, i + 1}) \mid = \mid \textrm{Inv}(\sigma) \mid \pm 1 \implies (-1)^{\mid \textrm{Inv}(\sigma \tau_{i, i + 1})\mid} = (-1)^{\mid \textrm{Inv}(\sigma) \mid \pm 1} \implies \textrm{sgn}(\sigma \tau_{i, i + 1}) = - \textrm{sgn}(\sigma)$ poiché $\pm 1$ all'esponente di $(-1)$ invertirà il segno
    - dunque aggiungendo o togliendo una trasposizione adiacente ad una permutazione, si inverte il segno della composizione
  - $\sigma =\tau_{1} \ldots \tau_{k} \implies \textrm{id} = \sigma \tau_k \ldots \tau_1 \implies \textrm{sgn}(\textrm{id}) = 1 = \textrm{sgn}(\sigma \tau_k \ldots \tau_1)$ poiché se sono uguali, saranno uguali anche i loro segni
    - $\textrm{sgn}(\sigma \tau_k \ldots \tau_1) = -\textrm{sgn}(\sigma \tau_k \ldots \tau_2) = \textrm{sgn}(\sigma \tau_k \ldots \tau_3) = \ldots = (-1)^k \cdot \textrm{sgn}(\sigma)$ poiché ho rimosso esattamente $k$ trasposizioni adiacenti
  - $(-1)^k \cdot \textrm{sgn}(\sigma) = \textrm{sgn}(\textrm{id}) = 1 \implies \textrm{sgn}(\sigma) = (-1)^k$
****
- $\forall \sigma, \sigma^{\prime} \in S_{n} \quad \operatorname{sgn}\left(\sigma \sigma^{\prime}\right)=\operatorname{sgn}(\sigma)\cdot \textrm{sgn}(\sigma ')$
  - $\sigma = \tau_1 \ldots \tau_k$
  - $\sigma ' = \tau_1^{\prime} \ldots \tau_h^{\prime}$
  - $\sigma \sigma^\prime = \tau_1 \ldots \tau_k \cdot \tau_1^\prime \ldots \tau_h^\prime \implies \textrm{sgn}(\sigma \sigma^\prime) = (-1)^ {k + h} = (-1)^k \cdot (-1)^h = \textrm{sgn}(\sigma) \cdot \textrm{sgn}(\sigma^\prime)$
- $\forall \sigma \in S_n \quad \textrm{sgn}(\sigma^{-1})=\textrm{sgn}(\sigma)$
  - $\left.\begin{array}{l}\operatorname{sgn}(\textrm{id})=1 \\ \sigma \sigma^{-1}=\textrm{id} \implies \operatorname{sgn}\left(\sigma \sigma^{-1}\right)=\textrm{sgn}(\textrm{id}) \\ \operatorname{sgn}\left(\sigma \sigma^{-1}\right)=\operatorname{sgn}(\sigma) \cdot \operatorname{sgn}\left(\sigma^{-1}\right)\end{array}\right\} \implies \textrm{sgn}(\sigma) \cdot \textrm{sgn}(\sigma^{-1})= 1\implies \textrm{sgn}(\sigma)= \textrm{sgn}(\sigma^{-1})$
- $A_n := \{\sigma \in S_n \mid \sigma$ pari$\}$, è un **sottogruppo** di $S_n$, detto **gruppo alterno di ordine $n$**
  - ⚠️ **MANCA DIMOSTRAZIONE**
- **permutazioni coniugate hanno lo stesso segno**
  - $\forall \sigma, \sigma^\prime \in S_n \quad \sigma \sim \sigma ^\prime \iff \exists\alpha \in S_n \mid \sigma^\prime = \alpha \sigma \alpha^{-1} \implies \textrm{sgn}(\sigma^\prime) = \textrm{sgn}(\alpha)\cdot \textrm{sgn}(\sigma)\cdot \textrm{sgn}(\alpha^{-1})$
  - $\forall \alpha \quad \textrm{sgn}(\alpha)= \textrm{sgn}(\alpha^{-1}) \implies$ entrambe $1$ o entrambe $-1 \implies \textrm{sgn}(\alpha) \cdot \textrm{sgn}(\alpha^{-1}) = 1 \implies \textrm{sgn}(\sigma^\prime) = \textrm{sgn}(\sigma)$
- $\forall \sigma, \sigma^\prime \in S_n \mid  \sigma := \gamma_1 \ldots \gamma_k, \sigma^\prime := \gamma_1^\prime \ldots \gamma_h^\prime \implies \sigma \sim \sigma ^\prime \iff$$\left\{\begin{array}{c}k=h \\ d=d_{1}^{\prime} \\ \vdots \\ d_{k}=d_{h}^{\prime}=d_{k}^{\prime}\end{array}\right.$, dove $d_j$ è la lunghezza del ciclo $\gamma_j$ e $d_j^\prime$ è la lunghezza del ciclo $\gamma_j^\prime$
  - _prima implicazione_
    - $\sigma \sim \sigma^\prime \implies \exists\alpha \in S_n \mid \sigma^\prime = \alpha \sigma \alpha^{-1}$
      - $(i_1 \ldots i_d)$ un certo ciclo in $\sigma \implies (\alpha(i_1) \ldots \alpha(i_d))$ è un ciclo in $\sigma^\prime$
        - $\sigma^\prime(\alpha(i_j))=(\alpha \sigma \alpha^{-1})(\alpha(i_j)) \implies (\alpha\sigma)(i_j)=$$\left\{\begin{array}{ll}\alpha\left(i_{j}+1\right) & j<d \\ \alpha\left(i_{1}\right) & j=d\end{array}\right.$ perché $\sigma(i) = i_{j + 1} \quad \forall j \lt d$ perché $i_j \in (i_1 \ldots i_d)$ ciclo di $\sigma$
        - quindi la relazione di coniugio determina un ciclo in $\sigma^\prime$ della forma $(\alpha(i_1) \ldots \alpha(i_d))$
        - ⚠️ **PERCHÉ È BIUNIVOCA?**
      - corrispondenza biunivoca tra cicli di $\sigma$ e $\sigma^\prime \implies h = k$ (devono avere lo stesso numero di cicli), e inoltre implica $\left\{\begin{array}{c}k=h \\ d=d_{1}^{\prime} \\ \vdots \\ d_{k}=d_{h}^{\prime}=d_{k}^{\prime}\end{array}\right.$, ovvero i cicli hanno la stessa lunghezza
  - _seconda implicazione_
    - $\sigma = (i_1 \ldots i_{d_1}) \ldots (j_1 \ldots j_{d_k})$
    - $\sigma^\prime =(a_1 \ldots a_{d_1}) \ldots (b_1 \ldots b_{d_k})$
    - $\exists \alpha \in S_n \mid$$\left\{\begin{array}{c}\alpha\left(i_{p}\right)=a_{p} \\ \vdots \\ \alpha\left(i_{q}\right)=b_{q}\end{array}\right.$

      - _esempio_
        - $\begin{aligned} \sigma\ =\ &(13)(254)(876) \\ & \downarrow  \downarrow \ \downarrow \downarrow \downarrow \ \downarrow \downarrow \downarrow \\ \sigma^{\prime}=\ &(25)(184)(376) \end{aligned}$ $\implies$$\alpha=\left(\begin{array}{llllllll}1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 \\ 2 & 1 & 5 & 4 & 8 & 6 & 7 & 3\end{array}\right)$
    - $\alpha$ è tale che $\sigma^\prime = \alpha \sigma \alpha ^{-1}$
      - ad esempio, prendendo $i_p$ in $\sigma \implies i_p = \alpha^{-1}(a_p)$ per definizione di $\alpha$, allora $\alpha \sigma \alpha^{-1} (a_p) = \alpha \sigma (i_p) =$$\left\{\begin{array}{ll}\alpha\left(i_{p+1}\right) & p<d_1 \\ \alpha\left(i_{1}\right) & p=d_{1}\end{array}\right.$ perché $\sigma(i_p) = i_{p +1} \quad \forall p \lt d_1$ perche $i_p \in (i_1 \ldots i_{d_1})$ ciclo di $\sigma$
      - ma per definizione di $\alpha$, $\left\{\begin{array}{ll}\alpha\left(i_{p+1}\right) & p<d_1 \\ \alpha\left(i_{1}\right) & p=d_{1}\end{array}\right. \iff$ $\left\{\begin{array}{ll}a_{p+1} & p<d_{1} \\ a_{1} & p=d_{1}\end{array}\right. = \sigma^\prime(a_p)$ per definizione di $\sigma^\prime$
    - poiché $\alpha$ è tale che la relazione $\sigma^\prime = \alpha \sigma \alpha ^{-1}$ sia rispettata, allora per definizione $\sigma \sim \sigma ^\prime$ 
- $\forall \sigma \in S_n \mid \sigma = \gamma_1 \ldots \gamma_k \implies \textrm{sgn}(\sigma)=(-1)^{n - k}$
  - $\sigma = (i_1 \ldots i_{d_1}) \ldots (j_1 \ldots j_{d_k})$
  - $\sigma^\prime := (1 \ldots d_1)(d_1 + 1 \ldots d_1 + d_2) \ldots (n -d_k + 1 \ldots n)$ (poiché $n - d_k + d_k = n$)
    - $\sigma^\prime \in S_n$
    - dunque $\sigma^\prime$ è composta da cicli lunghi esattamente come i cicli di $\sigma$, ma i numeri sono in sequenza da $1$ a $n$ 
  - $\sigma^{\prime}=\left(\begin{array}{cccccccc}1 & 2 & \cdots & d_{1} & d_{1}+1 & \cdots & d_{1}+d_{2} & \cdots \\ 2 & 3 & \cdots & 1 & d_{1}+2 & \cdots & d_{1}+1 & \cdots \end{array}\right)$
    - per portare $1$ nella prima colonna, devo applicare $d_1 - 1$ trasposizioni adiacenti
      - _esempio_
        - in $(2 \ 3 \ 4\ 5\ 6\ 1)$ devo applicare $5$ trasposizioni adiacenti per ottenere $(1\ 2\ 3\ 4\ 5)$
    - per portare $d_1 + 1$ nella colonna corretta, devo applicare $d_2 - 1$ trasposizioni adiacenti
  - per ottenere $\textrm{id}$ a partire da $\sigma^\prime$, devo applicare $(d_1 -1) + (d_2 - 1) + \ldots + (d_k - 1)$ trasposizioni adiacenti, ovvero $d_1 + \ldots + d_k - k \cdot 1 = n - k$
    - $d_1 + \ldots + d_k$ è il numero di colonne di $\sigma^\prime \in S_n$, dunque è pari a $n$
    - $k$ è il numero di cicli, quindi nell'equazione $-1$ appare esattamente $k$ volte
    - di conseguenza, $\textrm{id} = \sigma^\prime \tau_1 \ldots \tau_{n -k} \implies \sigma^\prime = \tau_k \ldots \tau_1 \implies \textrm{sgn}(\sigma^\prime) = \textrm{sgn}(\tau_{n-k} \ldots \tau_1)$, e dunque rimuovendo ogni trasposizione adiacente si ottiene che $\textrm{sgn}(\sigma^\prime) = (-1)^{n -k}$
  - poiché $\sigma$ e $\sigma^\prime$ hanno lo stesso numero di cicli, e i cicli hanno la stessa lunghezza, allora per dimostrazione precedente $\sigma \sim \sigma^\prime \implies \textrm{sgn}(\sigma^\prime)=\textrm{sgn}(\sigma) \implies \textrm{sgn}(\sigma)=(-1)^{n - k}$
