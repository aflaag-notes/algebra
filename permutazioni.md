# Permutazioni

- ⚠️ \*\*MANCA UN PEZZO\*\*

- $\sigma \in S\_n$, un \*\*ciclo di $\sigma$\*\* è una sequenza di interi distinti $1 \leq i\_1, \ldots, i\_d \leq n$ tali che  $\left\{\begin{array}{l}
\sigma\left(i\_{1}\right)=i\_{2} \\
\sigma\left(i\_{2}\right)=i\_{3} \\
\vdots \\
\sigma\left(i\_{d-1}\right)=i\_{d} \\
\sigma\left(i\_{d}\right)=i\_{1}
\end{array}\right.$

- $\sigma \in S\_n, \forall 1 \leq i \leq n \quad I(\sigma, i):=\left\{n \in \mathbb{Z} \mid \sigma^{n}(i)=i\right\}$, allora $(I(\sigma, i), +) \subset (\mathbb{Z}, +)$ è \*\*ideale\*\* in $\mathbb{Z}$
  - $\sigma ^0 = \textrm{id} \implies \sigma ^0(i) = \textrm{id}(i) = i \implies 0 \in I(\sigma, i)$
  - $m, n \in I(\sigma, i) \implies \sigma^m (i) = \sigma^n(i) = i$, ma $\sigma^{m+n}(i)=\sigma^{m}\left(\sigma^{n}(i)\right) = \sigma^m(i)=i \implies m + n \in I(\sigma, i)$
  - $n \in I(\sigma, i) \implies \sigma ^n (i) = i$, ma per simmetria della permutazione $\sigma^ {-n} (i) = i \implies -n \in I(\sigma, i)$
  - $\forall \tau \in S\_n \mid \tau (i) = i \implies \tau ^k (i) = i \quad \forall k \in \mathbb{Z}$, ma allora $\forall n \in I(\sigma, i) \quad \sigma^n(i) = i$ si può riscrivere come $(\sigma^n)^k(i) = i \quad \forall k \in \mathbb{Z} \implies \sigma^{nk}(i) = i \implies nk \in I(\sigma, i)$
- $I(g, i)$ è \*\*ideale principale\*\* in $\mathbb{Z}$ generato da $I(d)$, dove $d$ è la lunghezza del ciclo di $i$, quindi $I(\sigma, i) = I(d)$
  - $I(\sigma, i) = I(d) \implies d \in I(\sigma, i)$
  - ⚠️ \*\*MANCA DIMOSTRAZIONE\*\*

- $\sigma \in S\_n$ tale che la sua decomposizione in cicli sia $\sigma := \gamma\_1 \ldots \gamma\_k, d\_j$ definito pari alla lunghezza di $\gamma\_j, j \in [1, k] \implies o(\sigma) = m := \textrm{mcm}(d\_1, \ldots, d\_k)$
  - $I(\sigma):=\left\{n \in \mathbb{Z} \mid \sigma^{n}=\textrm{id}\right\}$
  - $n \in I(\sigma) \implies \sigma^{n}=\textrm{id} \iff \sigma^{n}(i)=i \quad 1 \leq i \leq n \iff n \in I(\sigma, i) \quad 1 \leq i \leq n \iff n \in I(\sigma, 1) \cap \ldots \cap I(\sigma, n)$
  - $d := o(\sigma) \implies I(d) = I(\sigma) = I(\sigma, 1) \cap \ldots \cap I(\sigma, n) = I(d\_1) \cap \ldots \cap I(d\_k) = I(m)$

\*\*\*\*

# Trasposizioni

- $\forall i, j \mid 1 \leq i \lt j \leq n \quad \tau\_{i, j} :=$ $\left\{\begin{array}{ll}j & k=i \\ i & k=j \\ k & k \neq i, j\end{array}\right.$
  - $\tau\_{i, j}^2 = \textrm{id} \implies \tau\_{i, j} = \tau\_{i, j} ^{-1}$
  - se $j = i + 1$, allora $\tau\_{i, j}=\tau\_{i, i+1}$ è detta \*\*trasposizione adiacente\*\*
- $\forall \sigma \in S\_n \quad \exists 1 \leq i\_1, \ldots, i\_k \lt n \mid \sigma = \tau\_{i\_1, i\_1 + 1} \ldots \tau\_{i\_k, i\_k + 1}$, quindi ogni permutazione può essere riscritta come composizione di trasposizioni adiacenti
  - $\tau\_{i, j}=\left(\begin{array}{ccccccc}1 & \cdots & i & \cdots & j & \cdots & n \\ 1 & \cdots & j & \cdots & i & \cdots & n\end{array}\right)$ è una trasposizione qualsiasi
  - $\sigma=\left(\begin{array}{ccccccc}1 & \cdots & i & \cdots & j & \cdots & n \\ \sigma(1) & \cdots & \sigma(i) & \cdots & \sigma(j) & \cdots & \sigma(n) \end{array}\right)$ è una permutazione
  - allora $\sigma \tau\_{i, j}=\left(\begin{array}{ccccccc}1 & \cdots & i & \cdots & j & \cdots & n \\ \sigma(1) & \cdots & \sigma(j) & \cdots & \sigma(i) & \cdots & \sigma(n) \end{array}\right)$
  - in particolare, se le trasposizioni devono essere adiacenti, allora ogni trasposizione invertirà due colonne adiacenti alla volta
    - \_esempio\_
      - $\sigma=\left(\begin{array}{llll}1 & 2 & 3 & 4 \\ 2 & 4 & 3 & 1\end{array}\right) \implies \sigma \tau\_{34}\left(\begin{array}{llll}1 & 2 & 3 & 4 \\ 2 & 4 & 1 & 3\end{array}\right) \implies$ $\sigma \tau\_{3 4} \tau\_{23}=\left(\begin{array}{llll}1 & 2 & 3 & 4 \\ 2 & 1 & 4 & 3\end{array}\right) \implies$$\sigma \tau\_{3 4} \tau\_{23} \tau\_{12}=\left(\begin{array}{llll}1 & 2 & 3 & 4 \\ 1 & 2 & 4 & 3\end{array}\right) \implies$$\sigma \tau\_{34} \tau\_{23} \tau\_{12} \tau\_{34}=\left(\begin{array}{llll}1 & 2 & 3 & 4 \\ 1 & 2 & 3 & 4\end{array}\right) = \textrm{id}$, ma allora $\textrm{id} = \sigma \tau\_{34} \tau\_{23} \tau\_{12} \tau\_{34} \iff \sigma =\tau\_{34} \tau\_{12} \tau\_{23} \tau\_{34}$
     
\*\*\*\*

# Segno

- $\sigma \in S\_n, \ \textrm{Inv}(\sigma) := \{ (i, j) \mid 1 \leq i \lt j \lt n : \sigma(i) \gt \sigma(j)\}, \ \textrm{sgn}(\sigma) := (-1)^{|\textrm{Inv}(\sigma)|} =$$\left\{\begin{array}{ll}+1 & |\operatorname{Inv}(\sigma)| \equiv 0 \ (\bmod 2) \\ -1 & |\operatorname{Inv}(\sigma)| \equiv 1 \ (\bmod 2)\end{array}\right. \implies \sigma$ \*\*pari\*\* $\iff \textrm{sgn}(\sigma) = +1$
  - $\textrm{sgn}(\textrm{id}) = (-1)^0 = 1$, in quando la funzione identità non ha inversioni

- $\sigma \in S\_{n} \mid \sigma:=\tau\_{1} \ldots \tau\_{k}, \quad \tau\_{j} = \tau\_{j, j + 1} \quad \forall j \in [1, k]$, dunque se tutte le trasposizioni sono adiacenti, allora $\textrm{sgn}(\sigma)= (-1)^k$
   - $\tau\_{i, i + 1}=\left(\begin{array}{ccccccc}1 & \cdots & i &  & i + 1 & \cdots & n \\ 1 & \cdots & i + 1 &  & i & \cdots & n\end{array}\right)$ è una trasposizione adiacente
  - $\sigma=\left(\begin{array}{ccccccc}1 & \cdots & i &  & i + 1 & \cdots & n \\ \sigma(1) & \cdots & \sigma(i) &  & \sigma(i + 1) & \cdots & \sigma(n) \end{array}\right)$ è una permutazione
  - allora $\sigma \tau\_{i, i + 1}=\left(\begin{array}{ccccccc}1 & \cdots & i &  & i + 1 & \cdots & n \\ \sigma(1) & \cdots & \sigma(i + 1) &  & \sigma(i) & \cdots & \sigma(n) \end{array}\right)$
  - di conseguenza $\textrm{Inv}(\sigma \tau\_{i, i + 1})=$$\left\{\begin{array}{ll}\operatorname{Inv}(\sigma) \cup\{(i, i+1)\} & (i, i+1) \notin \operatorname{Inv}(\sigma) \\ \operatorname{Inv}(\sigma)-\{(i, i+1)\} & (i, i+1) \in \operatorname{Inv}(\sigma)\end{array}\right.$
    - $(i, i + 1) \in \textrm{Inv}(\sigma) \implies \sigma(i) \gt \sigma(i + 1)$ (poiché $i \lt i + 1 \quad \forall i$)
    - di conseguenza, in $\sigma \tau\_{i, i + 1}$, poiché sto invertendo le colonne $i$ e $i + 1$, $\sigma \tau\_{i, i + 1}(i) \lt \sigma \tau\_{i, i + 1}(i +1) \implies (i, i + 1) \notin \textrm{Inv}(\sigma \tau\_{i, i + 1})$ per definizione (vale il ragionamento opposto per il caso $(i, i + 1) \in \textrm{Inv}(\sigma)$)
  - dunque $\mid \textrm{Inv}(\sigma \tau\_{i, i + 1}) \mid = \mid \textrm{Inv}(\sigma) \mid \pm 1 \implies (-1)^{\mid \textrm{Inv}(\sigma \tau\_{i, i + 1})\mid} = (-1)^{\mid \textrm{Inv}(\sigma) \mid \pm 1} \implies \textrm{sgn}(\sigma \tau\_{i, i + 1}) = - \textrm{sgn}(\sigma)$ poiché $\pm 1$ all'esponente di $(-1)$ invertirà il segno
    - dunque aggiungendo o togliendo una trasposizione adiacente ad una permutazione, si inverte il segno della composizione
  - $\sigma =\tau\_{1} \ldots \tau\_{k} \implies \textrm{id} = \sigma \tau\_k \ldots \tau\_1 \implies \textrm{sgn}(\textrm{id}) = 1 = \textrm{sgn}(\sigma \tau\_k \ldots \tau\_1)$ poiché se sono uguali, saranno uguali anche i loro segni
    - $\textrm{sgn}(\sigma \tau\_k \ldots \tau\_1) = -\textrm{sgn}(\sigma \tau\_k \ldots \tau\_2) = \textrm{sgn}(\sigma \tau\_k \ldots \tau\_3) = \ldots = (-1)^k \cdot \textrm{sgn}(\sigma)$ poiché ho rimosso esattamente $k$ trasposizioni adiacenti
  - $(-1)^k \cdot \textrm{sgn}(\sigma) = \textrm{sgn}(\textrm{id}) = 1 \implies \textrm{sgn}(\sigma) = (-1)^k$
- $\forall \sigma, \sigma^{\prime} \in S\_{n} \quad \operatorname{sgn}\left(\sigma \sigma^{\prime}\right)=\operatorname{sgn}(\sigma)\cdot \textrm{sgn}(\sigma ')$
  - $\sigma = \tau\_1 \ldots \tau\_k$
  - $\sigma ' = \tau\_1^{\prime} \ldots \tau\_h^{\prime}$
  - $\sigma \sigma^\prime = \tau\_1 \ldots \tau\_k \cdot \tau\_1^\prime \ldots \tau\_h^\prime \implies \textrm{sgn}(\sigma \sigma^\prime) = (-1)^ {k + h} = (-1)^k \cdot (-1)^h = \textrm{sgn}(\sigma) \cdot \textrm{sgn}(\sigma^\prime)$
- $\forall \sigma \in S\_n \quad \textrm{sgn}(\sigma^{-1})=\textrm{sgn}(\sigma)$
  - $\left.\begin{array}{l}\operatorname{sgn}(\textrm{id})=1 \\ \sigma \sigma^{-1}=\textrm{id} \implies \operatorname{sgn}\left(\sigma \sigma^{-1}\right)=\textrm{sgn}(\textrm{id}) \\ \operatorname{sgn}\left(\sigma \sigma^{-1}\right)=\operatorname{sgn}(\sigma) \cdot \operatorname{sgn}\left(\sigma^{-1}\right)\end{array}\right\} \implies \textrm{sgn}(\sigma) \cdot \textrm{sgn}(\sigma^{-1})= 1\implies \textrm{sgn}(\sigma)= \textrm{sgn}(\sigma^{-1})$
- $A\_n := \{\sigma \in S\_n \mid \sigma$ pari$\}$, è un \*\*sottogruppo\*\* di $S\_n$, detto \*\*gruppo alterno di ordine $n$\*\*
  - ⚠️ \*\*MANCA DIMOSTRAZIONE\*\*
- \*\*permutazioni coniugate hanno lo stesso segno\*\*
  - $\forall \sigma, \sigma^\prime \in S\_n \quad \sigma \sim \sigma ^\prime \iff \exists\alpha \in S\_n \mid \sigma^\prime = \alpha \sigma \alpha^{-1} \implies \textrm{sgn}(\sigma^\prime) = \textrm{sgn}(\alpha)\cdot \textrm{sgn}(\sigma)\cdot \textrm{sgn}(\alpha^{-1})$
  - $\forall \alpha \quad \textrm{sgn}(\alpha)= \textrm{sgn}(\alpha^{-1}) \implies$ entrambe $1$ o entrambe $-1 \implies \textrm{sgn}(\alpha) \cdot \textrm{sgn}(\alpha^{-1}) = 1 \implies \textrm{sgn}(\sigma^\prime) = \textrm{sgn}(\sigma)$
- $\forall \sigma, \sigma^\prime \in S\_n \mid  \sigma := \gamma\_1 \ldots \gamma\_k, \sigma^\prime := \gamma\_1^\prime \ldots \gamma\_h^\prime \implies \sigma \sim \sigma ^\prime \iff$$\left\{\begin{array}{c}k=h \\ d=d\_{1}^{\prime} \\ \vdots \\ d\_{k}=d\_{h}^{\prime}=d\_{k}^{\prime}\end{array}\right.$, dove $d\_j$ è la lunghezza del ciclo $\gamma\_j$ e $d\_j^\prime$ è la lunghezza del ciclo $\gamma\_j^\prime$
  - \_prima implicazione\_
    - $\sigma \sim \sigma^\prime \implies \exists\alpha \in S\_n \mid \sigma^\prime = \alpha \sigma \alpha^{-1}$
      - $(i\_1 \ldots i\_d)$ un certo ciclo in $\sigma \implies (\alpha(i\_1) \ldots \alpha(i\_d))$ è un ciclo in $\sigma^\prime$
        - $\sigma^\prime(\alpha(i\_j))=(\alpha \sigma \alpha^{-1})(\alpha(i\_j)) \implies (\alpha\sigma)(i\_j)=$$\left\{\begin{array}{ll}\alpha\left(i\_{j}+1\right) & j<d \\ \alpha\left(i\_{1}\right) & j=d\end{array}\right.$ perché $\sigma(i) = i\_{j + 1} \quad \forall j \lt d$ perché $i\_j \in (i\_1 \ldots i\_d)$ ciclo di $\sigma$
        - quindi la relazione di coniugio determina un ciclo in $\sigma^\prime$ della forma $(\alpha(i\_1) \ldots \alpha(i\_d))$
        - ⚠️ \*\*PERCHÉ È BIUNIVOCA?\*\*
      - corrispondenza biunivoca tra cicli di $\sigma$ e $\sigma^\prime \implies h = k$ (devono avere lo stesso numero di cicli), e inoltre implica $\left\{\begin{array}{c}k=h \\ d=d\_{1}^{\prime} \\ \vdots \\ d\_{k}=d\_{h}^{\prime}=d\_{k}^{\prime}\end{array}\right.$, ovvero i cicli hanno la stessa lunghezza
  - \_seconda implicazione\_
    - $\sigma = (i\_1 \ldots i\_{d\_1}) \ldots (j\_1 \ldots j\_{d\_k})$
    - $\sigma^\prime =(a\_1 \ldots a\_{d\_1}) \ldots (b\_1 \ldots b\_{d\_k})$
    - $\exists \alpha \in S\_n \mid$$\left\{\begin{array}{c}\alpha\left(i\_{p}\right)=a\_{p} \\ \vdots \\ \alpha\left(i\_{q}\right)=b\_{q}\end{array}\right.$

      - \_esempio\_
        - $\begin{aligned} \sigma\ =\ &(13)(254)(876) \\ & \downarrow  \downarrow \ \downarrow \downarrow \downarrow \ \downarrow \downarrow \downarrow \\ \sigma^{\prime}=\ &(25)(184)(376) \end{aligned}$ $\implies$$\alpha=\left(\begin{array}{llllllll}1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 \\ 2 & 1 & 5 & 4 & 8 & 6 & 7 & 3\end{array}\right)$
    - $\alpha$ è tale che $\sigma^\prime = \alpha \sigma \alpha ^{-1}$
      - ad esempio, prendendo $i\_p$ in $\sigma \implies i\_p = \alpha^{-1}(a\_p)$ per definizione di $\alpha$, allora $\alpha \sigma \alpha^{-1} (a\_p) = \alpha \sigma (i\_p) =$$\left\{\begin{array}{ll}\alpha\left(i\_{p+1}\right) & p<d\_1 \\ \alpha\left(i\_{1}\right) & p=d\_{1}\end{array}\right.$ perché $\sigma(i\_p) = i\_{p +1} \quad \forall p \lt d\_1$ perche $i\_p \in (i\_1 \ldots i\_{d\_1})$ ciclo di $\sigma$
      - ma per definizione di $\alpha$, $\left\{\begin{array}{ll}\alpha\left(i\_{p+1}\right) & p<d\_1 \\ \alpha\left(i\_{1}\right) & p=d\_{1}\end{array}\right. \iff$ $\left\{\begin{array}{ll}a\_{p+1} & p<d\_{1} \\ a\_{1} & p=d\_{1}\end{array}\right. = \sigma^\prime(a\_p)$ per definizione di $\sigma^\prime$
    - poiché $\alpha$ è tale che la relazione $\sigma^\prime = \alpha \sigma \alpha ^{-1}$ sia rispettata, allora per definizione $\sigma \sim \sigma ^\prime$ 
- $\forall \sigma \in S\_n \mid \sigma = \gamma\_1 \ldots \gamma\_k \implies \textrm{sgn}(\sigma)=(-1)^{n - k}$
  - $\sigma = (i\_1 \ldots i\_{d\_1}) \ldots (j\_1 \ldots j\_{d\_k})$
  - $\sigma^\prime := (1 \ldots d\_1)(d\_1 + 1 \ldots d\_1 + d\_2) \ldots (n -d\_k + 1 \ldots n)$ (poiché $n - d\_k + d\_k = n$)
    - $\sigma^\prime \in S\_n$
    - dunque $\sigma^\prime$ è composta da cicli lunghi esattamente come i cicli di $\sigma$, ma i numeri sono in sequenza da $1$ a $n$ 
  - $\sigma^{\prime}=\left(\begin{array}{cccccccc}1 & 2 & \cdots & d\_{1} & d\_{1}+1 & \cdots & d\_{1}+d\_{2} & \cdots \\ 2 & 3 & \cdots & 1 & d\_{1}+2 & \cdots & d\_{1}+1 & \cdots \end{array}\right)$
    - per portare $1$ nella prima colonna, devo applicare $d\_1 - 1$ trasposizioni adiacenti
      - \_esempio\_
        - in $(2 \ 3 \ 4\ 5\ 6\ 1)$ devo applicare $5$ trasposizioni adiacenti per ottenere $(1\ 2\ 3\ 4\ 5)$
    - per portare $d\_1 + 1$ nella colonna corretta, devo applicare $d\_2 - 1$ trasposizioni adiacenti
  - per ottenere $\textrm{id}$ a partire da $\sigma^\prime$, devo applicare $(d\_1 -1) + (d\_2 - 1) + \ldots + (d\_k - 1)$ trasposizioni adiacenti, ovvero $d\_1 + \ldots + d\_k - k \cdot 1 = n - k$
    - $d\_1 + \ldots + d\_k$ è il numero di colonne di $\sigma^\prime \in S\_n$, dunque è pari a $n$
    - $k$ è il numero di cicli, quindi nell'equazione $-1$ appare esattamente $k$ volte
    - di conseguenza, $\textrm{id} = \sigma^\prime \tau\_1 \ldots \tau\_{n -k} \implies \sigma^\prime = \tau\_k \ldots \tau\_1 \implies \textrm{sgn}(\sigma^\prime) = \textrm{sgn}(\tau\_{n-k} \ldots \tau\_1)$, e dunque rimuovendo ogni trasposizione adiacente si ottiene che $\textrm{sgn}(\sigma^\prime) = (-1)^{n -k}$
  - poiché $\sigma$ e $\sigma^\prime$ hanno lo stesso numero di cicli, e i cicli hanno la stessa lunghezza, allora per dimostrazione precedente $\sigma \sim \sigma^\prime \implies \textrm{sgn}(\sigma^\prime)=\textrm{sgn}(\sigma) \implies \textrm{sgn}(\sigma)=(-1)^{n - k}$
