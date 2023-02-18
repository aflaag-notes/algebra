# Permutazioni

## Def

- **Permutazioni**

> - $X$ insieme
> - $\mathcal{S}_X := \{f \mid f:X \rightarrow X$ biettiva$\}$ è l'**insieme delle permutazioni di $X$**
>   - in particolare, una _permutazione_ è una biezione $X \rightarrow X$
>   - inoltre, si ha che $|\mathcal{S}_X| = |X|!$

## Oss

- **Hp**
    - $f$ funzione
- **Th**
    - $f$ biettiva $\iff f$ invertibile

## Oss

- **Hp**
  - $\mathcal{S}_X := \{f \mid f : X \rightarrow X$ biettiva$\}$
- **Th**
  - $(\mathcal{S}_X, \circ)$ è un gruppo, non abeliano se $|X| \ge 3$
- **Dim**
  - la composizione di funzioni è associativa
  - $\textrm{id}$ è biettiva $\implies \textrm{id} \in \mathcal{S}_X$ per definizione, e costituisce l'elemento neutro
  - $\forall f \in \mathcal{S}_X \quad \exists f^{-1} \in \mathcal{S}_X$ poiché $f \in \mathcal{S}_X \implies f$ biettiva, e dunque invertibile per dimostrazione precedente
  - $\forall f \in \mathcal{S}_X \quad f$ biettiva $\iff f$ invertibile $\iff \exists f^{-1} \in \mathcal{S}_X$, poiché $f^{-1}$ anch'essa biettiva
  - $|X| = 2 \implies X$ è della forma $X = \{a, b\}$, quindi $\mathcal{S}_X =\left\{\begin{array}{l}a \rightarrow a \\ b \rightarrow b\end{array}\right. , \left.\begin{array}{l}a \rightarrow b \\ b \rightarrow a\end{array}\right\}$, dove uno dei due elementi è $\rm id$
    - $\rm id \circ id = id$
    - $\rm \sigma \circ id = id \circ \sigma = \sigma$
    - $\rm \sigma \circ \sigma = id$ per costruzione
  - quindi $|X| = 2 \implies \mathcal{S}_X$ è abeliano, mentre $|X| = 1 \implies \mathcal{S}_X$ è abeliano perché contiene un solo elemento
  - se $|X| \ge 3$, allora non è abeliano poiché $\circ$ non è commutativo

## Def

- **Gruppo simmetrico**

> - $n \in \mathbb{N} - \{0\}$
> - $X = \{1, \ldots, n\}$
> - $\mathcal{S}_n := \{f \mid f: X \rightarrow X$ biettiva$\}$ è detto **gruppo simmetrico di $n$**
>   - inoltre, si ha che $|\mathcal{S}_n| = n!$

## Def

- **Ciclo di una permutazione**

> - $n \in \mathbb{N}$
> - $\sigma \in \mathcal{S}_n$
> - $i_1, \ldots, i_d \in \mathbb{N} \mid 1 \leq i_1, \ldots, i_d \leq n$
> - $(i_1, \ldots, i_d)$ è detto **ciclo di $\sigma$** $\iff \left\{\begin{array}{c}\sigma\left(i_{1}\right)=i_{2} \\\sigma\left(i_{2}\right)=i_{3} \\\vdots \\\sigma\left(i_{d-1}\right)=i_{d} \\\sigma\left(i_{d}\right)=i_{1}\end{array}\right.$
>   - $d$ è detta _lunghezza del ciclo_ $i_1, \ldots, i_d$
>   - in generale, è possibile scomporre $\sigma = \gamma_1, \ldots, \gamma_k$, dove ogni $\gamma_i$ è un ciclo di $\sigma$

## Oss

- **Hp**
  - $n \in \mathbb{N}$
  - $\sigma \in \mathcal{S}_n$
  - $i \in \mathbb{N} \mid 1 \le i \le n$
  - $I(\sigma, i):=\left\{n \in \mathbb{Z} \mid \sigma^{n}(i)=i\right\}$
- **Th**
  - $(I(\sigma, i), +) \subset (\mathbb{Z}, +)$ ideale
- **Dim**
  - $(I(\sigma, i), +) \leqslant (\mathbb{Z}, +)$
    - $\sigma ^0 = \textrm{id} \implies \forall i \quad \sigma ^0(i) = \textrm{id}(i) = i \implies 0 \in I(\sigma, i)$
    - $m, n \in I(\sigma, i) \implies \sigma^m (i) = \sigma^n(i) = i$, ma $\sigma^{m+n}(i)=\sigma^{m}\left(\sigma^{n}(i)\right) = \sigma^m(i)=i \implies m + n \in I(\sigma, i)$
    - $n \in I(\sigma, i) \implies \sigma ^n (i) = i$, ma per simmetria della permutazione $\sigma^ {-n} (i) = i \implies -n \in I(\sigma, i)$
  - $\forall n \in I(\sigma, i) \quad \sigma^n(i) = i \iff \forall k \in \mathbb{Z} \quad (\sigma^n)^k(i) = i \implies \sigma^{nk}(i) = i \implies nk \in I(\sigma, i)$

## Oss

- **Hp**
    - $n \in \mathbb{N}$
    - $\sigma \in \mathcal{S}_n \mid \sigma = \gamma_1 \ldots \gamma_k$ sia la sua decomposizione in cicli
    - $i \in \gamma_j$
    - $\exists d \in I(\sigma, i) \mid I(\sigma, i) = I(d)$
- **Th**
    - $d$ è la lunghezza di $\gamma_j$
- **Dim**
    - per definizione $\forall n \in I(\sigma, i) \quad \sigma^n(i) = i$
    - si noti che le uniche potenze per cui tale proprietà è rispettata sono quelle per cui viene permutato ogni elemento del ciclo col suo successivo, e in particolare si ritornerà sull'elemento di partenza esattamente ogni $d$ permutazioni, dove $d$ è la lunghezza di $\gamma_j$
    - allora, $I(\sigma, i)$ corrisponde ai multipli della lunghezza di $\gamma_j$, ovvero $I(d) \implies I(\sigma, i) = I(d)$, con $d$ lunghezza di $\gamma_j$

## Cor

- **Hp**
  - $n \in \mathbb{N}$
  - $\sigma \in \mathcal{S}_n \mid \sigma = \gamma_1 \ldots \gamma_k$ sia la sua decomposizione in cicli
  - $\forall j \in [1, k] \quad d_j:=$ lunghezza di $\gamma_j$
  - $m := \textrm{mcm}(d_1, \ldots, d_k)$
  -  $I(\sigma):=\left\{n \in \mathbb{Z} \mid \sigma^{n}=\textrm{id}\right\}$
- **Th**
  - $o(\sigma) = m$
- **Dim**
  - $x \in I(\sigma) \iff \sigma^{n}=\textrm{id} \iff \forall 1 \leq i \leq n \quad \sigma^{x}(i)=i \iff \forall 1 \leq i \leq n \quad x \in I(\sigma, i) \iff x \in I(\sigma, 1) \cap \ldots \cap I(\sigma, n)$
  - inoltre, per dimostrazione precedente $I(\sigma) = I(\sigma, 1) \cap \ldots \cap I(\sigma, n) = I(d_1) \cap \ldots \cap I(d_k)$
  - $m:= \textrm{mcm}(d_1, \ldots, d_k) \implies I(d_1) \cap \ldots \cap I(d_k) = I(m)$
  - allora $I(\sigma) = I(m) \implies o(\sigma) = m$

****

# Trasposizioni

## Def

- **Trasposizione**

> - $n \in \mathbb{N}$
> - $i, j \in \mathbb{N} \mid 1 \leq i \lt j \leq n \quad$
> - $k \in [1, n]$
> - $\tau_{i, j} \in \mathcal{S}_n \mid \tau_{i, j} =$$\left\{\begin{array}{ll}j & k=i \\ i & k=j \\ k & k \neq i, j\end{array}\right.$ è detta **trasposizione**, ovvero una permutazione che inverte esclusivamente due elementi tra loro
>   - in particolare, si ha che $\tau_{i, j}^2 = \textrm{id} \iff \tau_{i, j} = \tau_{i, j} ^{-1}$

- **Trasposizione adiacente**

> - $n \in \mathbb{N}$
> - $i, j \in \mathbb{N} \mid 1 \le i \le  n$
> - $\tau_{i, i+1}$ è detta **trasposizione adiacente**
>   - in particolare, inverte esclusivamente due elementi $i$ e $i + 1$ adiacenti

## Oss

- **Hp**
  - $n \in \mathbb{N}$
  - $\sigma \in \mathcal{S}_n$
- **Th**
  - $\exists 1 \leq i_1, \ldots, i_k \le n \mid \sigma = \tau_{i_1, i_1 + 1} \ldots \tau_{i_k, i_k + 1}$, quindi ogni permutazione può essere riscritta come composizione di trasposizioni adiacenti
- **Dim**
  - $\tau_{i, j}=\left(\begin{array}{ccccccc}1 & \cdots & i & \cdots & j & \cdots & n \\ 1 & \cdots & j & \cdots & i & \cdots & n\end{array}\right)$ è una trasposizione
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
> - $\sigma \in \mathcal{S}_n$
> - $\textrm{Inv}(\sigma) := \{ (i, j) \mid 1 \leq i \lt j \le n : \sigma(i) \gt \sigma(j)\}$ è detto **insieme delle inversioni di $\sigma$**
> - $\textrm{sgn}(\sigma) := (-1)^{|\textrm{Inv}(\sigma)|} =$$\left\{\begin{array}{ll}+1 & |\operatorname{Inv}(\sigma)| \equiv 0 \ (\bmod  \ 2) \\ -1 & |\operatorname{Inv}(\sigma)| \equiv 1 \ (\bmod \ 2)\end{array}\right.$
>   - in particolare $\sigma$ è detta _pari_ $\iff \textrm{sgn}(\sigma) = +1$, e vivecersa

## Oss

- **Hp**
  - $n \in \mathbb{N}$
  - $\alpha, \beta \in \mathcal{S}_n \mid \textrm{sgn}(\alpha) \cdot \textrm{sgn}(\beta) = 1$
- **Th**
  - $\textrm{sgn}(\alpha)= \textrm{sgn}(\beta)$
- **Dim**
  - $\textrm{sgn}(\alpha), \textrm{sgn}(\beta) = \pm 1$ per definizione, allora necessariamente i due segni devono essere o entrambi $1$ o entrambi $-1$, e dunque $\textrm{sgn}(\alpha) = \textrm{sgn}(\beta)$

## Oss

- **Hp**
    - $n \in \mathbb{N}$
    - $\sigma \in \mathcal{S}_n \mid \sigma=\tau_{1} \ldots \tau_{k}$ dove $\forall j \in [1, k] \quad \tau_{j} = \tau_{j, j + 1}$, dunque tutte le trasposizioni sono adiacenti
- **Th**
    - $\textrm{sgn}(\sigma)= (-1)^k$
- **Dim**
   - $\tau_{i, i + 1}=\left(\begin{array}{ccccccc}1 & \cdots & i &  & i + 1 & \cdots & n \\ 1 & \cdots & i + 1 &  & i & \cdots & n\end{array}\right)$ è una trasposizione adiacente
  - $\sigma=\left(\begin{array}{ccccccc}1 & \cdots & i &  & i + 1 & \cdots & n \\ \sigma(1) & \cdots & \sigma(i) &  & \sigma(i + 1) & \cdots & \sigma(n) \end{array}\right)$ è una permutazione
  - allora $\sigma \tau_{i, i + 1}=\left(\begin{array}{ccccccc}1 & \cdots & i &  & i + 1 & \cdots & n \\ \sigma(1) & \cdots & \sigma(i + 1) &  & \sigma(i) & \cdots & \sigma(n) \end{array}\right)$
  - $\forall i \in [1, n] \quad i \lt i + 1 \implies \sigma \tau_{i, i + 1}(i + 1) \gt \sigma \tau_{i, i + 1}(i) \iff (i, i + 1) \in \textrm{Inv}(\sigma \tau_{i, i + 1})$ per definizione
  - allora $\textrm{Inv}(\sigma \tau_{i, i + 1})=\left\{\begin{array}{ll}\operatorname{Inv}(\sigma) \cup\{(i, i+1)\} & (i, i+1) \notin \operatorname{Inv}(\sigma) \\ \operatorname{Inv}(\sigma)-\{(i, i+1)\} & (i, i+1) \in \operatorname{Inv}(\sigma)\end{array}\right.$
  - dunque $|\textrm{Inv}(\sigma \tau_{i, i + 1}) | = | \textrm{Inv}(\sigma) | \pm 1 \iff (-1)^{\mid \textrm{Inv}(\sigma \tau_{i, i + 1})\mid} = (-1)^{\mid \textrm{Inv}(\sigma) \mid \pm 1} \iff \textrm{sgn}(\sigma \tau_{i, i + 1}) = - \textrm{sgn}(\sigma)$, poiché $\pm 1$ all'esponente di $(-1)$ ne invertirà il segno
  - dunque aggiungendo o togliendo una trasposizione adiacente ad una permutazione, si inverte il segno della composizione
  - $\sigma =\tau_{1} \ldots \tau_{k} \implies \textrm{id} = \sigma \tau_k \ldots \tau_1$ poiché ogni trasposizione è l'inversa di sé stessa, e dunque $\textrm{sgn}(\textrm{id}) = 1 = \textrm{sgn}(\sigma \tau_k \ldots \tau_1)= -\textrm{sgn}(\sigma \tau_k \ldots \tau_2) = \textrm{sgn}(\sigma \tau_k \ldots \tau_3) = \ldots = (-1)^k \cdot \textrm{sgn}(\sigma)$, poiché sono state rimosse esattamente $k$ trasposizioni adiacenti
  - allora $(-1)^k \cdot \textrm{sgn}(\sigma) = \textrm{sgn}(\textrm{id}) = 1$
  - $\textrm{sgn}(\sigma) = \pm 1$, e poiché $(-1)^k \cdot \textrm{sgn}(\sigma)  = 1$, allora necessariamente $\textrm{sgn}(\sigma) = (-1)^k$

## Oss

- **Hp**
    - $n \in \mathbb{N}$
    - $\sigma, \sigma^{\prime} \in \mathcal{S}_n | \left\{\begin{array}{l}\sigma = \tau_1 \ldots \tau_k \\ \sigma ' = \tau_1^{\prime} \ldots \tau_h^{\prime}\end{array}\right.$, dove ogni trasposizione è adiacente
- **Th**
    - $\operatorname{sgn}\left(\sigma \sigma^{\prime}\right)=\operatorname{sgn}(\sigma)\cdot \textrm{sgn}(\sigma ')$
- **Dim**
  - $\sigma \sigma^\prime = \tau_1 \ldots \tau_k \cdot \tau_1^\prime \ldots \tau_h^\prime$, dunque il numero di trasposizioni adiacenti di $\sigma \sigma^\prime$ è $k + h$
  - per dimostrazione precedente $\textrm{sgn}(\sigma \sigma^\prime) = (-1)^ {k + h} = (-1)^k \cdot (-1)^h = \textrm{sgn}(\sigma) \cdot \textrm{sgn}(\sigma^\prime)$

## Oss

- **Hp**
    - $n \in \mathbb{N}$
    - $\sigma \in \mathcal{S}_n$
- **Th**
    - $\textrm{sgn}(\sigma^{-1})=\textrm{sgn}(\sigma)$
- **Dim**
  - $\left.\begin{array}{l}\operatorname{sgn}(\textrm{id})=1 \\ \sigma \sigma^{-1}=\textrm{id} \implies \operatorname{sgn}\left(\sigma \sigma^{-1}\right)=\textrm{sgn}(\textrm{id}) \\ \operatorname{sgn}\left(\sigma \sigma^{-1}\right)=\operatorname{sgn}(\sigma) \cdot \operatorname{sgn}\left(\sigma^{-1}\right)\end{array}\right\} \implies \textrm{sgn}(\sigma) \cdot \textrm{sgn}(\sigma^{-1})= 1 \implies \textrm{sgn}(\sigma^{-1}) = \textrm{sgn}(\sigma)$

## Oss

- **Hp**
    - $n \in \mathbb{N}$
  - $\sigma, \sigma^\prime \in \mathcal{S}_n$
  - $\sigma \sim \sigma ^\prime \iff \exists\alpha \in \mathcal{S}_n \mid \sigma^\prime = \alpha \sigma \alpha^{-1}$
- **Th**
    - $\textrm{sgn}(\sigma^\prime) = \textrm{sgn}(\sigma)$
- **Dim**
  - $\sigma \sim \sigma' \implies \textrm{sgn}(\sigma^\prime) = \textrm{sgn}(\alpha)\cdot \textrm{sgn}(\sigma)\cdot \textrm{sgn}(\alpha^{-1})$
  - per dimostrazione precedente $\forall \alpha \in \mathcal{S}_n \quad \textrm{sgn}(\alpha)= \textrm{sgn}(\alpha^{-1})$, dunque entrambe $1$ o entrambe $-1$
  - quindi $\textrm{sgn}(\alpha) \cdot \textrm{sgn}(\alpha^{-1}) = 1 \implies \textrm{sgn}(\sigma^\prime) = \textrm{sgn}(\sigma)$

## Oss

- **Hp**
    - $n \in \mathbb{N}$
    - $\sigma, \sigma^\prime \in \mathcal{S}_n \mid \left \{ \begin{array}{l} \sigma := \gamma_1 \ldots \gamma_k \\ \sigma^\prime := \gamma_1^\prime \ldots \gamma_h^\prime \end{array} \right.$ siano le loro decomposizioni in cicli
    - $\sigma \sim \sigma ^\prime \iff \exists\alpha \in \mathcal{S}_n \mid \sigma^\prime = \alpha \sigma \alpha^{-1}$, che costituisce dunque la relazione di coniugio
- **Th**
    - $\sigma \sim \sigma ^\prime \iff$$\left\{\begin{array}{c}k=h \\ d_1=d_{1}^{\prime} \\ \vdots \\ d_{k}=d_{h}^{\prime}\end{array}\right.$, dove $d_j$ è la lunghezza del ciclo $\gamma_j$ e $d_j^\prime$ è la lunghezza del ciclo $\gamma_j^\prime$
- **Dim**
  - _prima implicazione_
    - $\sigma \sim \sigma^\prime \iff \exists\alpha \in \mathcal{S}_n \mid \sigma^\prime = \alpha \sigma \alpha^{-1}$
    - $\forall i_1, \ldots, i_d \mid (i_1 \ldots i_d)$ è un ciclo di $\sigma$, per la relazione di coniugio si ottiene che $\sigma^\prime(\alpha(i_j))=(\alpha \sigma \alpha^{-1})(\alpha(i_j))= (\alpha\sigma)(i_j)=\left\{\begin{array}{ll}\alpha\left(i_{j+1}\right) & j<d \\ \alpha\left(i_{1}\right) & j=d\end{array}\right. \implies$ la relazione di coniugio determina un ciclo in $\sigma^\prime$ della forma $(\alpha(i_1) \ldots \alpha(i_d))$
    - allora, vi è una corrispondenza biunivoca tra cicli di $\sigma$ e $\sigma^\prime$, e dunque necessariamente $\sigma$ e $\sigma'$ devono avere lo stesso numero di cicli, ovvero $h = k$, e i cicli devono avere stessa lunghezza, e dunque $\left\{\begin{array}{c} d_1=d_{1}^{\prime} \\ \vdots \\ d_{k}=d_{h}^{\prime}\end{array}\right.$
  - _seconda implicazione_
    - $\sigma = (i_1 \ldots i_{d_1}) \ldots (j_1 \ldots j_{d_k})$ è la decomposizione in cicli di $\sigma$
    - $\sigma^\prime =(a_1 \ldots a_{d_1}) \ldots (b_1 \ldots b_{d_k})$ è la decomposizione in cicli di $\sigma'$
    - poiché in ipotesi $\sigma$ e $\sigma'$ hanno stesso numero di cicli, e cicli di stessa lunghezza, allora $\exists \alpha \in \mathcal{S}_n \mid$$\left\{\begin{array}{c}\alpha\left(i_{p}\right)=a_{p} \\ \vdots \\ \alpha\left(j_{q}\right)=b_{q}\end{array}\right.$
      - _esempio_
        - $\begin{aligned} \sigma\ =\ &(13)(254)(876) \\ & \ \downarrow  \downarrow \ \ \  \downarrow   \downarrow \downarrow \  \ \ \downarrow \downarrow  \downarrow \\ \sigma^{\prime}=\ &(25)(184)(376) \end{aligned}$ $\implies$$\alpha=\left(\begin{array}{llllllll}1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 \\ 2 & 1 & 5 & 4 & 8 & 6 & 7 & 3\end{array}\right)$
    - scelto $\alpha \in \mathcal{S}_n$ in questo modo, allora ad esempio $\forall i_p \in (i_1 \ldots i_{d_1})$ primo ciclo di $\sigma \quad i_p = \alpha^{-1}(a_p)$ per definizione di $\alpha \implies \alpha \sigma \alpha^{-1} (a_p) = \alpha \sigma (i_p) =$$\left\{\begin{array}{ll}\alpha\left(i_{p+1}\right) & p<d_1 \\ \alpha\left(i_{1}\right) & p=d_{1}\end{array}\right. = \left\{\begin{array}{ll}a_{p+1} & p<d_{1} \\ a_{1} & p=d_{1}\end{array}\right. = \sigma^\prime(a_p)$ per definizione di $\sigma^\prime$
    - poiché in questa osservazione non è stato fatto uso dell'ipotesi per cui $i_p$ fosse stato scelto all'interno del primo ciclo, il ragionamento vale analogamente per ogni altro elemento in ogni altro ciclo
    - allora, $\alpha$ è proprio scelto tale che $\sigma^\prime = \alpha \sigma \alpha ^{-1} \iff \sigma \sim \sigma'$

## Def

- **Gruppo alterno**

> - $n \in \mathbb{N}$
> - $\mathcal{A}_n := \{\sigma \in \mathcal{S}_n \mid \sigma$ pari$\}$ è detto **gruppo alterno di ordine $n$**

## Oss

- **Hp**
    - $n \in \mathbb{N}$
- **Th**
    - $\mathcal{A}_n \trianglelefteq \mathcal{S}_n$
- **Dim**
    - $\textrm{sgn}(\textrm{id}) = (-1)^0 = 1$, in quanto $\textrm{id}$ non ha inversioni, dunque $\textrm{id} \in \mathcal{A}_n$
    - $\sigma, \sigma' \in \mathcal{A}_n \implies \textrm{sgn}(\sigma)=\textrm{sgn}(\sigma')=1 \implies \textrm{sgn}(\sigma)\cdot\textrm{sgn}(\sigma') = 1 = \textrm{sgn}(\sigma \sigma')$ per dimostrazione precedente $\implies \sigma \sigma' \in \mathcal{A}_n$
    - $\sigma \in \mathcal{A}_n \implies \textrm{sgn}(\sigma) = 1 = \textrm{sgn}(\sigma^{-1})$ per dimostrazione predecente $\implies \sigma^{-1} \in \mathcal{A}_n$
    <!-- - $\mathcal{A}_n \trianglelefteq \mathcal{S}_n \iff \forall \sigma \in \mathcal{A}_n, \alpha \in \mathcal{S}_n \quad \sigma \alpha \sigma^{-1} \in \mathcal{A}_n$ per dimostrazione precedente -->
    <!-- - inoltre, per dimostrazione precedente $\textrm{sgn}(\sigma) = 1 = \textrm{sgn}(\sigma \alpha \sigma^{-1}) \implies \sigma \alpha \sigma^{-1} \in \mathcal{A}_n$ -->
    - $\sigma \in \mathcal{S}_n, \alpha \in \mathcal{A}_n \implies \left \{ \begin{array}{l} \textrm{sgn}(\sigma \alpha \sigma^{-1}) = \textrm{sgn}(\sigma) \cdot \textrm{sgn}(\alpha) \cdot \textrm{sgn}(\sigma^{-1}) = \textrm{sgn}(\sigma) \cdot \textrm{sgn}(\sigma)^{-1} = 1 \\ \textrm{sgn}(\alpha) = 1 \end{array} \right. \implies \sigma \alpha \sigma^{-1} \in \mathcal{A}_n \implies \mathcal{A}_n \trianglelefteq \mathcal{S}_n$

## Oss

- **Hp**
    - $n \in \mathbb{N}$
- **Th**
    - $|\mathcal{A}_n| = \dfrac{n!}{2}$
- **Dim**
    - $\mathcal{A}_n \trianglelefteq \mathcal{S}_n \implies \mathcal{S}_n/\mathcal{A}_n$ è ben definito
    - in particolare, considerando la relazione di classe laterale sinistra, si ha che $\forall \sigma, \sigma' \in \mathcal{S}_n \quad \sigma \sim_S \sigma' \iff \sigma^{-1}\sigma' \in \mathcal{A}_n \iff \textrm{sgn}(\sigma^{-1}\sigma') = 1 = \textrm{sgn}(\sigma^{-1})\cdot \textrm{sgn}(\sigma)=\textrm{sgn}(\sigma)\cdot\textrm{sgn}(\sigma') \iff \textrm{sgn}(\sigma) = \textrm{sgn}(\sigma')$
    - poiché $\textrm{sgn}(\sigma) = \pm 1$ per definizione, si ha che $\mathcal{S}_n/\mathcal{A}_n=\{[\textrm{id}]_{+1}, [\alpha]_{-1}\}$, dove $\alpha$ è dispari, e in particolare $|\mathcal{S}_n/\mathcal{A}_n| = 2$
    - inoltre, per il teorema di Lagrange si ha che $|\mathcal{S}_n| = |\mathcal{A}_n| \cdot |\mathcal{S}_n/\mathcal{A}_n| \iff |\mathcal{A}_n| = \dfrac{|\mathcal{S}_n|}{|\mathcal{S}_n/\mathcal{A}_n|} = \dfrac{n!}{2}$

## Oss

- **Hp**
    - $n \in \mathbb{N}$
    - $\sigma \in \mathcal{S}_n \mid \sigma := \gamma_1 \ldots \gamma_k$ sia la sua decomposizione in cicli
- **Th**
    - $\textrm{sgn}(\sigma)=(-1)^{n - k}$
- **Dim**
  - $\sigma = (i_1 \ldots i_{d_1})(i_{d_1+ 1} \ldots i_{d_2}) \ldots (j_1 \ldots j_{d_k})$
  - $\forall \sigma \in \mathcal{S}_n \quad \exists \sigma' \in \mathcal{S}_n \mid \sigma^\prime := (1 \ldots d_1)(d_1 + 1 \ldots d_1 + d_2) \ldots (n -d_k + 1 \ldots n)$
  - dunque $\sigma^\prime$ è composta da cicli lunghi esattamente quanto i cicli di $\sigma$, ma ha i numeri da $1$ a $n$ in sequenza nei cicli
  - allora $\sigma^{\prime}=\left(\begin{array}{cccccccccccc}1 & 2 & \cdots & d_{1} & d_{1}+1 & \cdots & d_{1}+d_{2} & \cdots & \cdots & n - d_k + 1 & \cdots & n \\ 2 & 3 & \cdots & 1 & d_{1}+2 & \cdots & d_{1}+1 & \cdots & \cdots  & n - d_k + 2 & \cdots & n - d_k + 1\end{array}\right)$
    - si noti che, ad esempio, per portare $1$ nella prima colonna, è necessario applicare $d_1 - 1$ trasposizioni adiacenti, o analogamente per portare $d_1 + 1$ nella colonna corretta, è necessario applicare $d_1 + d_2 - (d_1 + 1) = d_1 + d_2 - d_1 - 1 = d_2 - 1$ trasposizioni adiacenti, e vale il ragionamento analogo per ogni altro ciclo
    - _esempio_
      - nel ciclo $(2 \ 3 \ 4\ 5\ 6\ 1)$ è necessario applicare $6 - 1 = 5$ trasposizioni adiacenti per ottenere $(1\ 2\ 3\ 4\ 5 \ 6)$, e il ciclo è lungo $6$
  - allora, per ottenere $\textrm{id}$ a partire da $\sigma^\prime$, bisogna applicare $(d_1 -1) + (d_2 - 1) + \ldots + (d_k - 1)$ trasposizioni adiacenti, ovvero $d_1 + \ldots + d_k - 1 \cdot k$
  - si noti che $d_1 + \ldots + d_k$ è il numero di colonne di $\sigma^\prime \in \mathcal{S}_n$, dunque è pari a $n$
  - allora si hanno $d_1 + \ldots + d_1 - 1 \cdot k = n - k$ trasposizioni adiacenti
  - di conseguenza, $\textrm{id} = \sigma^\prime \tau_1 \ldots \tau_{n -k} \iff \sigma^\prime = \tau_{n - k} \ldots \tau_1 \implies \textrm{sgn}(\sigma^\prime) = \textrm{sgn}(\tau_{n-k} \ldots \tau_1)= (-1)^{n -k}$ per dimostrazione precedente
  - poiché $\sigma$ e $\sigma^\prime$ hanno lo stesso numero di cicli, e i cicli hanno la stessa lunghezza, allora $\sigma \sim \sigma^\prime \implies \textrm{sgn}(\sigma^\prime)=\textrm{sgn}(\sigma)$ per dimostrazione precedente, e dunque $\textrm{sgn}(\sigma') = \textrm{sgn}(\sigma)=(-1)^{n - k}$

