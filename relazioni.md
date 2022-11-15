# Relazioni

## Def

- **Relazioni**
> - $S$ insieme
> - ogni elemento $R \subseteq S \times S$ è una **relazione** su $S$

- **Relazione riflessiva**
> - $S$ insieme
> - $R$ relazione in $S \times S$
> - $R$ **riflessiva** $\iff \forall x \in R \quad (x, x) \in R$

- **Relazione simmetrica**
> - $S$ insieme
> - $R$ relazione in $S \times S$
> - $R$ **simmetrica** $\iff \forall x, y \in R \quad (x, y) \in R \implies (y, x) \in R$

- **Relazione transitiva**
> - $S$ insieme
> - $R$ relazione in $S \times S$
> - $R$ **transitiva** $\iff \forall x, y, z \in R \quad (x, y) \in R \land (y, z) \in R \implies (x, z) \in R$

- **Relazione antisimmetrica**
> - $S$ insieme
> - $R$ relazione in $S \times S$
> - $R$ **transitiva** $\iff \forall x, y \in R \quad (x, y) \in R \land (y, x) \in R \implies x = y$

- **Relazione totale**
> - $S$ insieme
> - $R$ relazione in $S \times S$
> - $R$ **totale** $\iff \forall x, y \in R \quad (x, y) \in R \lor (y, x) \in R$

- **Relazione di equivalenza**
> - $S$ insieme
> - $R$ relazione in $S \times S$
> - $R$ è una **relazione di equivalenza** $\iff R$ riflessiva, simmetrica e transitiva

- **Ordine parziale**
> - $S$ insieme
> - $R$ relazione in $S \times S$
> - $R$ **ordine parziale** $\iff R$ riflessiva, transitiva e antisimmetrica

- **Ordine totale**
> - $S$ insieme
> - $R$ relazione in $S \times S$
> - $R$ **ordine totale** $\iff R$ ordine parziale in cui vale la totalità

## Ex

- **Hp**
  - $m, n \in \mathbb{N}$
  - $m \mid n \iff \exists p \in \mathbb{N} \mid mp = n$
- **Th**
  - $\mid$ è ordine parziale
- **Dim**
    - *riflessività*: $\forall x \in \mathbb{N} \quad x\mid x$
      - $x\mid x \iff \exists p \in \mathbb{N} \mid  x p=x \iff p = 1 \in \mathbb{N}$
    - *transitività*: $\forall d, m, n \in \mathbb{N} \quad d \mid m \wedge m| n \implies d \mid n$
      -  $\left.\begin{array}{l}d \mid m \iff \exists p_{1} \in \mathbb{N}\mid d p_{1}=m \\ m\mid n \iff \exists p_{2} \in \mathbb{N}\mid m p_{2}=n\end{array}\right\} \implies d p_{1} p_{2}=n \implies d \mid n$ poiché $p_1 \in \mathbb{N} \land p_2 \in \mathbb{N} \implies p_1 p_2 \in \mathbb{N}$
    -  *antisimmetria*: $\forall m, n \in \mathbb{N}, \ m\mid n \wedge n\mid m \implies m=n$
       - $\left.\begin{array}{l}m\mid n \iff \exists p_{1} \in \mathbb{N}\mid m p_{1}=n \\ n\mid m \iff \exists p_{2} \in \mathbb{N}\mid n p_{2}=m\end{array}\right\} \implies m p_{1} p_{2}=m \iff p_1 p_2 = 1 \iff p_1 = p_2 = 1$, e dunque $m p_1 =n \iff m = n$

## Ex

- **Hp**
  - $a, b \in \mathbb{Z}$
  - $a \equiv b \ (\bmod n) \iff m \mid b-a$ è detta congruenza modulo $n$
- **Th**
  - $\equiv$ è una relazione di equivalenza
- **Dim**
    - _riflessività_: $\forall a \in \mathbb{Z} \quad a \equiv a \ (\bmod n)$
      - $a \equiv a \ (\bmod n) \iff n \mid a - a \iff n \mid 0 \iff \exists p \in \mathbb{Z} \mid n p = 0 \iff p = 0 \in \mathbb{Z}$
    - _simmetria_: $\forall a, b \in \mathbb{Z}\quad a \equiv b \ (\bmod n) \implies b \equiv a \ (\bmod n)$
      - $a \equiv b \ (\bmod n) \iff n \mid b - a \iff \exists p_1 \in \mathbb{Z} \mid n  p_1 = b - a$
      - $b \equiv a \ (\bmod n) \iff n \mid a - b \iff \exists p_2 \in \mathbb{Z} \mid n  p_2 = a - b$
       - $\left.\begin{array}{l}n p_{1}=b-a \implies b=n p_{1}+a \\ n p_{2}=a-b\end{array}\right\} \implies np_2 = a - np_1 - a = -np_1$, e dunque $np_2 = -np_1 \iff np_2+np_1 = 0 \iff n(p_2 + p_1)=0$
       - $n \neq 0\implies n(p_2+p_1) 0 \iff p_{2}+p_{1}=0 \implies -p_{2}=p_{1}$
       - $n\mid b -a \iff np_1= b - a \iff n(-p_2) = b - a \iff np_2 = a - b \iff n \mid a- b$
    - _transitivtà_: $\forall a, b, c \in \mathbb{Z} \quad a \equiv b \ (\bmod n) \land b \equiv c \ (\bmod n) \implies a \equiv c \ (\bmod n)$
      - $a \equiv b \ (\bmod n) \iff n \mid b - a \iff \exists p_1 \in \mathbb{Z} \mid n p_1 = b - a$
      - $b \equiv c \ (\bmod n) \iff n \mid c - b \iff \exists p_2 \in \mathbb{Z} \mid n p_2 = c - b$
      - $\left.\begin{array}{l}n p_{1}=b-a \implies b=n p_{1}+a \\ n p_{2}=c-b\end{array}\right\} \implies np_2 = c - np_2 - a \iff np_2 + np_1 = c - a \implies n(p_2 + p_1)=c -a$
      - $p_{1}, p_{2} \in \mathbb{Z} \implies p_{1}+p_{2} \in \mathbb{Z}$, e qundue per la proposizione precedente $\exists p_1 + p_2 \in \mathbb{Z} \mid n(p_1 + p_2) = c - a \iff n \mid c - a$

## Oss

- **Hp**
  - $x, y \in \mathbb{Z} \mid x \equiv y \ (\bmod n)$
  - $d \in \mathbb{Z} : d\mid n$
- **Th**
  - $x \equiv y \ (\bmod d)$
- **Dim**
  - $x \equiv y \ (\bmod n) \iff n \mid y - x \iff \exists p \in \mathbb{Z} \mid np = y - x$
  - $d \mid n \iff \exists k \in \mathbb{Z} \mid dk = n$
  - allora, $np = y - x \iff dkp = y -x \implies \exists kp \in \mathbb{Z} : d \mid y - x \iff x \equiv y \ (\bmod d)$

## Ex

- ⚠️ **DA RILEGGERE**
  - $G$ gruppo $g, h \in G$, **$g$ coniugato ad $h$**  $\iff \exists a \in G \mid h = a\cdot g \cdot a^{-1}$
  - $G$ abeliano $\iff a \cdot g\cdot a^{-1} = g$
  - la relazione di coniugio è una **relazione di equivalenza**
    - _riflessività_: $g \sim g$
      - $g = 1 \cdot g \cdot 1^{-1} \implies g \sim g$
    - _simmetria_: $g \sim h \implies h \sim g$
      - $g \sim h \implies h = a \cdot g \cdot a^{-1} \implies a^{-1} \cdot h = a^{-1} \cdot a \cdot g \cdot a^{-1} \implies a^{-1} \cdot h = g \cdot a^{-1}\implies$ $a^{-1} \cdot h \cdot a = g \cdot a^{-1} \cdot a \implies a ^{-1} \cdot h \cdot a = g$
      - $b := a^{-1} \implies b \cdot h \cdot b^{-1} = g \implies h \sim g$
    - _transitività_: $g \sim h \land h \sim k \implies g \sim k$
      - $g \sim h \land h \sim k \implies \exists a, b \mid h = a \cdot g \cdot a^{-1} \land k = b \cdot h \cdot b^{-1} \implies k = b \cdot a \cdot g \cdot a ^{-1} \cdot b^{-1}$
      - $c:= b \cdot a \implies c^{-1} = a^{-1} \cdot b^{-1}$
        - $k = c \cdot g \cdot c^{-1} \implies g \sim k$

****

# Partizione

## Def

- **Partizione**
> - $X$ insieme
> - $I$ insieme di indici
> - $\forall i \in I \quad X_i \subset X$
> - $\displaystyle X = \coprod_{i \in I}X_i$

## Oss

- **Hp**
  - $G$ gruppo
- **Th**
  - $\forall x, y \in G \quad x \nsim y \iff [x] \cap [y] = \varnothing \lor x \sim y \iff [x] = [y]$
- **Dim**
  - $x \sim y \iff [x] = [y]$
      - $\forall x, y \in G \mid x \sim y$, sia $z \in [x] \implies z \sim x \land x \sim y \implies z \sim y$ per transitività di $\sim \implies z \in [y]$
      - $\forall x, y \in G \mid y \sim x$, sia $z \in [y] \implies z \sim y \land y \sim x \implies z \sim x$ per transitività si $\sim \implies z \in [x]$
      - poiché $\sim$ è relazione di equivalenza, allora $x \sim y \iff y \sim x$, allora $z \in [y] \land z \in [x] \implies[x] = [y]$ necessariamente
  - $x \nsim y \iff [x] \cap [y] = \varnothing$
    - ipotizzando che $[x] \cap [y] \neq \varnothing \implies \exists z \in [x] \cap [y] \implies z \in [x] \land z \in [y] \implies z \sim x \land z \sim y$, che per simmetria e transitività di $\sim\implies x \sim y \ \bot$

## Oss

- **Hp**
  - $G$ gruppo
  - $\sim$ è una relazione di equivalenza in $G$
- **Th**
  - $\sim$ induce una partizione di $G$, dunque $\displaystyle G = \coprod_{[x] \in X/\sim}[x]$
- **Dim**
  - ⚠️ **MANCA DIMOSTRAZIONE, NON C'HO VOGLIA MO**
     
****

# Classi laterali

## Oss

- **Hp**
  - $G$ gruppo
  - $H \subset G$ sottogruppo
  - $x, y \in G$
- **Th**
  - $x \sim_S y \iff x^{-1}y \in H$ è una relazione di equivalenza
- **Dim**
    - _riflessività_: $x \sim x$
      - $x^{-1}x \in H \quad \forall x$ perché $H$ sottogruppo, dunque chiuso rispetto a prodotto ed inversi, e $x^{-1}x = 1 \in H$
    - _simmetria_: $x \sim y \implies y \sim x$
      - $x \sim y \implies x^{-1}y \in H,\quad y \sim x \implies y^{-1}x \in H$
        - $\forall x, y \in G \quad (x^{-1}y)^{-1} = (y^{-1} x)$
          - $(xy)(y^{-1}x^{-1})=x(yy^{-1})x^{-1}$ per associatività di $G$, e $xx^{-1} = 1$, dunque necessariamente $(xy)^{-1}=(y^{-1}x^{-1})$, e in particolare, $(x^{-1}y)^{-1}=(y^{-1}x)$
        - $h:=x^{-1}y \implies h^{-1} =y^{-1}x \in H$ perché $H$ sottogruppo $\iff h^{-1} \in H \iff y \sim x$
    - _transitività_: $x \sim y \land y \sim z \implies x \sim z$
      - $\left.\begin{array}{l}h:=x^{-1} y \in H \\ k:=y^{-1} z \in H\end{array}\right\} \implies a:=h \cdot k=x^{-1} y \cdot y^{-1} z= x^{-1} z$
      - $a \in H$ perche $H$ sottogruppo, dunque chiuso su $\cdot$, e dunque $\implies a \in H \iff x^{-1}z \in H \iff x \sim z$
        - quindi basta considerare il prodotto $h \cdot k$ per ottenere l'elemento di transitività

## Def 

- **Classi laterali**
> - $(G, \cdot)$ gruppo
> - $(H, \cdot) \subset (G, \cdot)$ sottogruppo
> - $\forall x,y \in G \quad x \sim_S y \iff x^{-1}y \in H$ è una relazione di equivalenza
> - $\forall x, y \in G \quad x \sim_D y \iff xy^{-1} \in H$ è una relazione di equivalenza
> - $x \in G$
> - $[x] = \{y \in G \mid y \sim_S x\}$ è detta **classe laterale sinistra**
> - $[x] = \{y \in G \mid y \sim_D x\}$ è detta **classe laterale destra**
> - $G/H := \{[x] \mid x \in G\}$ è l'**insieme delle classi laterali sinistre o destre**

## Oss

- **Hp**
  - $(\mathbb{Z}, +)$ anello
  - $n \in \mathbb{N}_{\ge 2}$
  - $I(n) := \{n k \mid k \in \mathbb{Z}\}$
  - $a, b \in \mathbb{Z}$
- **Th**
  - $a \sim_S b \iff a \equiv b \ (\bmod \ n)$
- **Dim**
  - $a \equiv b \ (\bmod \ n) \iff n \mid b - a \iff \exists p \in \mathbb{Z} \mid n p = b - a$, ma allora $b - a$ è un multiplo di $n$, quindi $b - a \in I(n)$ per definizione
  - $I(n)$ è un sottogruppo per dimostrazione precedente, dunque $b - a = (-a) + b \in I(n) \iff a \sim_S b$

## Oss

- **Hp**
  - $G$ gruppo
  - $H \subset G$ sottogruppo
  - $x \in G$
  - $[x] = \{y \in G \mid y \sim_S x\}$
- **Th**
  - $xH:= \{ xh \mid h \in H\} = [x]$
- **Dim**
  - $[x] \subset xH$
    - $y \in[x] \implies y \sim x \implies x \sim y \implies \exists h:= x^{-1}y \in H$ $\implies xh = x(x^{-1}y)=(xx^{-1})y=y \in H$ in quanto $H$ è sottogruppo, quindi $y \in [x] \implies \exists h \in H \mid y = xh \in H \implies y \in xH$
  - $xH \subset [x]$
    - $y \in x H \implies \exists h \in H \mid y=x h \implies x^{-1}y = x^{-1}xh= h$, quindi $h \in H \implies x^{-1}y \in H \implies x \sim y \implies y \in [x]$

## Oss

- **Hp**
  - $G$ gruppo
  - $H \subset G$ sottogruppo
  - $x \in G$
- **Th**
  - $| xH |= |H|$
- **Dim**
  - $\forall h, k \in H \quad h \neq k \iff xh \neq xk$, quindi simmetricamente $h = k \iff xh = xk$, di conseguenza è possibile definire una funzione $H \rightarrow xH : h \rightarrow xh$
    - la funzione è suriettiva per costruzione, perché $\forall h \quad \exists xh$
    - la funzione è iniettiva perché $xh$ è univoco $\forall x, h$
    - la funzione è biiettiva, di conseguenza insieme di partenza e di arrivo hanno la stessa cardinalità, quindi $|H| = |xH|$

## Oss

- **Hp**
  - $G$ gruppo
  - $H \subset G$ sottogruppo
  - $+: G/H \times G/H \rightarrow G/H$
- **Th**
  - $(G/H, +)$ è gruppo abeliano
- **Dim**
  - bisogna dimostrare che $+$ è un operazione ben definita
  - $+$ ben definita $\iff$$\left.\forall x, x^{\prime}, y, y' \in G \quad \begin{array}{l}{[x]=\left[x^{\prime}\right]} \\ {[y]=\left[y^{\prime}\right]}\end{array}\right\} \implies[x+y]=\left[x^{\prime}+y' \right]$
    - $\forall k, k' \in G \quad [k]=\left[k^{\prime}\right] \iff k \sim k^{\prime}$, dunque il sistema precedente è equivalente a $\left.\begin{array}{l}x \sim x^{\prime} \\ y \sim y^{\prime}\end{array}\right\} \implies x+y \sim x^{\prime}+y^{\prime}$
    - $x \sim x' \iff (-x)+x' \in H \implies x' - x \in H$
    - $y \sim y' \iff (-y) +y' \in H \implies y' - y \in H$
    - $H$ è sottogruppo, di conseguenza $(x'-x)+(y'-y) \in H \implies -(x+y)+(x'+y') \in H \iff x +y \sim x'+y'$
  - $(G/H, +)$ gruppo abeliano
    - $\forall [x], [y], [z] \in G/H \quad ([x]+[y])+[z]=[x+y]+[z]=[(x+y)+z]= [x+(y+z)]=[x]+[y+z]=[x]+([y]+[z])$
    - $\forall [x] \in G/H \quad [x]+[0]=[0]+[x]=[x]$ e $[0] + [x] = [0 + x] = [x]$, e $[0] \in G/H$ perché $G$ gruppo
    - $\forall [x] \in G/H \quad [x]+[-x]=[x+(-x)]=[0]$ e $[-x] +[x]=[-x +x]=[0]$$\implies -[x] = [-x]$
    - $[x]+[y]=[x+y]=[y+x]=[y]+[x]$

## Oss

- **Hp**
  - $n \in \mathbb{Z}$
  - $I(n) := \{nk \mid k \in \mathbb{Z}\}$
- **Th**
  - $(\mathbb{Z}_n, +)$ è un gruppo
- **Dim**
  - per dimostrazione precedente, $I(n)$ è un sottogruppo, quindi ha senso definire $\mathbb{Z}/I(n)$, che conterrà le classi laterali sinistre definite in $\mathbb{Z}$ rispetto a $I(n)$, che per dimostrazione precedente corrispondono alle classi di equivalenza definite da $\equiv$
  - di conseguenza, $\mathbb{Z}/I(n) = \mathbb{Z}/ \equiv \textrm{} = \mathbb{Z}_n$ per definizione precedente
  - per dimostrazione precedente, la somma tra classi di equivalenza è ben definita, di conseguenza è possibile definire la struttura di gruppo $(\mathbb{Z}_n, +)$