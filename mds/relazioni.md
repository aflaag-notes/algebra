# Relazioni

## Def

- **Relazioni**

> - $S$ insieme
> - $R \subseteq S \times S$ è detta **relazione** su $S$

- **Relazione riflessiva**

> - $S$ insieme
> - $R \subseteq S \times S$ relazione su $S$
> - $R$ è detta **riflessiva** $\iff \forall x \in S \quad (x, x) \in R$

- **Relazione simmetrica**

> - $S$ insieme
> - $R \subseteq S \times S$ relazione su $S$
> - $R$ è detta **simmetrica** $\iff \forall x, y \in S \quad (x, y) \in R \implies (y, x) \in R$

- **Relazione transitiva**

> - $S$ insieme
> - $R \subseteq S \times S$ relazione su $S$
> - $R$ è detta **transitiva** $\iff \forall x, y, z \in S \quad (x, y), (y, z) \in R \implies (x, z) \in R$

- **Relazione antisimmetrica**

> - $S$ insieme
> - $R \subseteq S \times S$ relazione su $S$
> - $R$ è detta **transitiva** $\iff \forall x, y \in S \quad (x, y), (y, x) \in R \implies x = y$

- **Relazione totale**

> - $S$ insieme
> - $R \subseteq S \times S$ relazione su $S$
> - $R$ è detta **totale** $\iff \forall x, y \in S \quad (x, y) \in R \lor (y, x) \in R$

- **Relazione di equivalenza**

> - $S$ insieme
> - $R \subseteq S \times S$ relazione su $S$
> - $R$ è detta **relazione di equivalenza** $\iff R$ riflessiva, simmetrica e transitiva

- **Ordine parziale**

> - $S$ insieme
> - $R \subseteq S \times S$ relazione su $S$
> - $R$ è detto **ordine parziale** $\iff R$ riflessiva, transitiva e antisimmetrica

- **Ordine totale**

> - $S$ insieme
> - $R \subseteq S \times S$ relazione su $S$
> - $R$ è detto **ordine totale** $\iff R$ ordine parziale in cui vale la totalità

## Ex

- **Hp**
  - $m, n \in \mathbb{N}$
  - $m \mid n \iff \exists p \in \mathbb{N} \mid mp = n$
- **Th**
  - $\mid$ è ordine parziale
- **Dim**
    - *riflessività*
      - $x\mid x \iff \exists p \in \mathbb{N} \mid  x p=x \iff p = 1 \in \mathbb{N}$
    - *transitività*
      -  $\left.\begin{array}{l}d \mid m \iff \exists p_{1} \in \mathbb{N}\mid d p_{1}=m \\ m\mid n \iff \exists p_{2} \in \mathbb{N}\mid m p_{2}=n\end{array}\right\} \implies d p_{1} p_{2}=n \implies d \mid n$ poiché $p_1 \in \mathbb{N} \land p_2 \in \mathbb{N} \implies p_1 p_2 \in \mathbb{N}$
    -  *antisimmetria*
       - $\left.\begin{array}{l}m\mid n \iff \exists p_{1} \in \mathbb{N}\mid m p_{1}=n \\ n\mid m \iff \exists p_{2} \in \mathbb{N}\mid n p_{2}=m\end{array}\right\} \implies m p_{1} p_{2}=m \iff p_1 p_2 = 1 \iff p_1 = p_2 = 1$, e dunque $m p_1 =n \iff m = n$

## Ex

- **Hp**
  - $a, b \in \mathbb{Z}$
  - $a \equiv b \ (\bmod \ n) \iff m \mid b-a$ è detta congruenza modulo $n$
- **Th**
  - $\equiv$ è una relazione di equivalenza
- **Dim**
    - _riflessività_
      - $a \equiv a \ (\bmod \ n) \iff n \mid a - a \iff n \mid 0 \iff \exists p \in \mathbb{Z} \mid n p = 0 \iff p = 0 \in \mathbb{Z}$
    - _simmetria_
      - $a \equiv b \ (\bmod \ n) \iff n \mid b - a \iff \exists p_1 \in \mathbb{Z} \mid n  p_1 = b - a$
      - $b \equiv a \ (\bmod \ n) \iff n \mid a - b \iff \exists p_2 \in \mathbb{Z} \mid n  p_2 = a - b$
       - $\left.\begin{array}{l}n p_{1}=b-a \implies b=n p_{1}+a \\ n p_{2}=a-b\end{array}\right\} \implies np_2 = a - np_1 - a = -np_1$, e dunque $np_2 = -np_1 \iff np_2+np_1 = 0 \iff n(p_2 + p_1)=0$
       - $n \neq 0\implies n(p_2+p_1) 0 \iff p_{2}+p_{1}=0 \implies -p_{2}=p_{1}$
       - $n\mid b -a \iff np_1= b - a \iff n(-p_2) = b - a \iff np_2 = a - b \iff n \mid a- b$
    - _transitivtà_
      - $a \equiv b \ (\bmod \ n) \iff n \mid b - a \iff \exists p_1 \in \mathbb{Z} \mid n p_1 = b - a$
      - $b \equiv c \ (\bmod \ n) \iff n \mid c - b \iff \exists p_2 \in \mathbb{Z} \mid n p_2 = c - b$
      - $\left.\begin{array}{l}n p_{1}=b-a \implies b=n p_{1}+a \\ n p_{2}=c-b\end{array}\right\} \implies np_2 = c - np_2 - a \iff np_2 + np_1 = c - a \implies n(p_2 + p_1)=c -a$
      - $p_{1}, p_{2} \in \mathbb{Z} \implies p_{1}+p_{2} \in \mathbb{Z}$, e qundue per la proposizione precedente $\exists p_1 + p_2 \in \mathbb{Z} \mid n(p_1 + p_2) = c - a \iff n \mid c - a$

## Oss

- **Hp**
  - $x, y \in \mathbb{Z} \mid x \equiv y \ (\bmod \ n)$
  - $d \in \mathbb{Z} : d\mid n$
- **Th**
  - $x \equiv y \ (\bmod  \ d)$
- **Dim**
  - $x \equiv y \ (\bmod  \ n) \iff n \mid y - x \iff \exists p \in \mathbb{Z} \mid np = y - x$
  - $d \mid n \iff \exists k \in \mathbb{Z} \mid dk = n$
  - allora, $np = y - x \iff dkp = y -x \implies \exists kp \in \mathbb{Z} : d \mid y - x \iff x \equiv y \ (\bmod \ d)$

## Oss

- **Hp**
    - $n \in \mathbb{N}$
    - $[a], [b] \in \mathbb{Z}_n$
    - $d:= \textrm{MCD}(a, n)$
- **Th**
    - $d \nmid b \implies \nexists [x] \in \mathbb{Z}_n \mid ax \equiv b \ (\bmod \ n)$
    - $d \mid b \implies \forall [x] \in \mathbb{Z}_n \mid ax \equiv b \ (\bmod \ n) \quad x$ è anche tale che $\dfrac{a}{d}x \equiv \dfrac{b}{d} \ \left(\bmod \ \dfrac{n}{d}\right)$
- **Dim**
    - ⚠️ **tipo pag 40 appunti simone**

## Ex

- **Hp**
  - $G$ gruppo
  - $g, h \in G$
  - $g \sim h \iff \exists a \in G \mid h = a\cdot g \cdot a^{-1}$ è detta _relazione di coniugio_
- **Th**
  - $\sim$ è una relazione di equivalenza
- **Dim**
    - _riflessività_
      - $g = 1 \cdot g \cdot 1^{-1} \implies g \sim g$
    - _simmetria_
      - $g \sim h \implies \exists a \in G \mid h = a \cdot g \cdot a^{-1} \iff a^{-1} \cdot h = a^{-1} \cdot a \cdot g \cdot a^{-1} \iff a^{-1} \cdot h = g \cdot a^{-1}\iff a^{-1} \cdot h \cdot a = g \cdot a^{-1} \cdot a \iff a ^{-1} \cdot h \cdot a = g$
      - $b := a^{-1} \implies b \cdot h \cdot b^{-1} = g \implies h \sim g$
    - _transitività_
      - $g \sim h \land h \sim k \implies \exists a, b \mid h = a \cdot g \cdot a^{-1} \land k = b \cdot h \cdot b^{-1} \implies k = b \cdot a \cdot g \cdot a ^{-1} \cdot b^{-1}$
      - $c:= b \cdot a \implies c^{-1} = a^{-1} \cdot b^{-1} \implies k = c \cdot g \cdot c^{-1} \implies g \sim k$

****

# Partizioni

## Def

- **Partizione**

> - $X$ insieme
> - $I$ insieme di indici
> - $\forall i \in I \quad X_i \subset X$
> - $\displaystyle X = \bigsqcup_{i \in I}X_i$ è detta **partizione di $X$**
>   - in particolare $\forall i, j \in I \quad \left \{ \begin{array}{ll} X_i = X_j && i = j \\ X_i \cap X_j = \varnothing && i \neq j \end{array}\right.$

## Oss

- **Hp**
  - $X$ insieme
- **Th**
  - $\forall x, y \in X \quad \left \{ \begin{array}{ll}x \nsim y \iff [x] \cap [y] = \varnothing \\ x \sim y \iff [x] = [y]\end{array}\right.$, ovvero $\sim$ _induce una partizione_
- **Dim**
    - $x \sim y \iff [x] = [y]$
        - _prima implicazione_
            - $\forall x, y \in X \mid x \sim y$, sia $z \in [x] \implies z \sim x \land x \sim y \implies z \sim y$ per transitività di $\sim \implies z \in [y] \implies [x] \subseteq [y]$
            - $\forall x, y \in G \mid y \sim x$, sia $z \in [y] \implies z \sim y \land y \sim x \implies z \sim x$ per transitività si $\sim \implies z \in [x] \implies [y] \subseteq [x]$
            - allora necessariamente $[x] = [y]$
        - _seconda implicazione_
            - $[x] = [y] \implies x \sim y \land y \sim x$
    - $x \nsim y \iff [x] \cap [y] = \varnothing$
        - _prima implicazione_
            - per assurdo, ipotizzando $[x] \cap [y] \neq \varnothing \implies \exists z \in [x] \cap [y] \implies z \in [x] \land z \in [y] \implies z \sim x \land z \sim y$, allora per simmetria e transitività di $\sim\implies x \sim y \ \bot$
        - _seconda implicazione_
            - $[x] \cap [y] = \varnothing \implies \nexists z \in [x] \cap [y]$, in particolare $x \notin [y] \land y \notin [x]$

## Oss

- **Hp**
    - $X$ insieme
    - $I$ insieme di indici
    - $\displaystyle X = \bigsqcup_{i \in I}X_i$ partizione di $X$
- **Th**
    - $\displaystyle X = \bigsqcup_{[x] \in X/\sim}[x]$, ovvero una partizione _induce una relazione di equivalenza_, dove $x \sim y \iff \exists i \in I \mid x, y \in X_i$
- **Dim**
    - $\forall x \in X \quad \exists i \in I \mid x \in X_i \implies x \sim x$
    - $x \sim y \implies \exists i \in I \mid x, y \in X_i \implies y \sim x$
    - $x \sim y, y \sim z \implies \exists i, j \in I \mid x, y \in X_i \land y, z \in X_j \implies y \in X_i \cap X_j$, ma poiché $X_i$ e $X_j$ sono insiemi di una partizione allora $\left \{ \begin{array}{l} i = j \implies X_i = X_j \implies x \sim z \\ i \neq j \implies X_i \cap X_j = \varnothing \implies x \nsim y \land y \nsim z \end{array}\right.$
     
****

# Classi laterali

## Oss

- **Hp**
  - $G$ gruppo
  - $H \leqslant G$
  - $x, y \in G$
- **Th**
  - $x \sim_S y \iff x^{-1}y \in H$ è una relazione di equivalenza
- **Dim**
    - _riflessività_
      - $H \leqslant G \implies x^{-1}x = 1 \in H$
    - _simmetria_
      - $x \sim y \implies x^{-1}y \in H,\quad y \sim x \implies y^{-1}x \in H$
        - $\forall x, y \in G \quad (x^{-1}y)^{-1} = (y^{-1} x)$
          - $(xy)(y^{-1}x^{-1})=x(yy^{-1})x^{-1}$ per associatività di $G$, e $xx^{-1} = 1$, dunque necessariamente $(xy)^{-1}=(y^{-1}x^{-1})$, e in particolare, $(x^{-1}y)^{-1}=(y^{-1}x)$
        - $h:=x^{-1}y \implies h^{-1} =y^{-1}x \in H \iff h^{-1} \in H \iff y \sim x$
    - _transitività_: $x \sim y \land y \sim z \implies x \sim z$
      - $\left.\begin{array}{l}h:=x^{-1} y \in H \\ k:=y^{-1} z \in H\end{array}\right\} \implies h \cdot k=x^{-1} y \cdot y^{-1} z= x^{-1} z$
      - $H \leqslant G \implies h \cdot k \in H \implies x^{-1} z \in H \iff x \sim z$

# Oss

- **Hp**
    - $G$ gruppo
    - $H \leqslant G$
    - $x, y \in G$
- **Th**
    - $x \sim_D y \iff xy^{-1} \in H$ è una relazione di equivalenza
- **Dim**
    - la dimostrazione è analoga alla precedente

## Def 

- **Classi laterali su gruppi**

> - $G$ gruppo
> - $H \leqslant G$
> - $x \in G$
> - $[x] = \{y \in G \mid y \sim_S x\}$ è detta **classe laterale sinistra**
> - $[x] = \{y \in G \mid y \sim_D x\}$ è detta **classe laterale destra**
> - $G/H := \{[x] \mid x \in G\}$ è l'**insieme delle classi laterali sinistre o destre**
>   - $G/H$ è un simbolismo ambiguo, poiché in base al contesto può voler significare l'insieme delle classi laterali sinistre o destre, ma all'interno di questi appunti, a meno di specifica, saranno sottointese le classi laterali sinistre
>   - si noti che con $x^{-1}$ si intende l'inverso rispetto all'operazione considerata

- **Classi laterali su anelli**

> - $(A, +, \cdot)$ anello
> - $I \subset A$ ideale
> - $[x] = \{y \in A \mid y \sim_S x\}$ è detta **classe laterale sinistra**
> - $[x] = \{y \in A \mid y \sim_D x\}$ è detta **classe laterale destra**
> - $A/I := \{[x] \mid x \in A\}$ è l'**insieme delle classi laterali sinistre o destre**
>   - $\sim_S$ e $\sim_D$ sono dette anche _congruenza modulo $I$_, e dunque $\forall a,b \in A \quad a \equiv b \ (\bmod \ I) \iff b - a \in I$

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
    - $H \leqslant G$
- **Th**
    - $H = [1] \in G/H$
- **Dim**
    - $\forall x \in G \quad 1 \sim x \iff 1^{-1}x \in H \iff x \in H \implies \forall x \in H \quad 1 \sim x$


## Oss

- **Hp**
  - $G$ gruppo
  - $H \leqslant G$
  - $x \in G$
  - $[x] = \{y \in G \mid y \sim_S x\}$
- **Th**
  - $xH:= \{ xh \mid h \in H\} = [x]$
- **Dim**
  - $y \in xH \iff \exists h \in H \mid y = xh \iff x^{-1}y = h \in H \iff x \sim_S y$

## Oss

- **Hp**
  - $G$ gruppo
  - $H \leqslant G$
  - $x \in G$
- **Th**
  - $|xH| = |H|$
- **Dim**
    - è possibile definire una funzione $\varphi: H \rightarrow xH : h \rightarrow xh$
    - $\forall h, k \in H \mid h \neq k \quad xh \neq xk \implies \varphi$ iniettiva
    - $\forall xh \in xH \quad \exists h \in H \mid \varphi(x) = xh \implies \varphi$ suriettiva
    - $\varphi$ biiettiva $\implies |H| = |xH|$

## Oss

- **Hp**
  - $(G, +)$ gruppo abeliano
  - $H \leqslant G$
- **Th**
  - $(G/H, +)$ è gruppo abeliano, dove $+: G/H \times G/H \rightarrow G/H$
- **Dim**
  - $+$ ben definita $\iff\left.\forall x, x^{\prime}, y, y' \in G \quad \begin{array}{l}{[x]=\left[x^{\prime}\right]} \\ {[y]=\left[y^{\prime}\right]}\end{array}\right\} \implies[x+y]=\left[x^{\prime}+y' \right]$
    - $\forall k, k' \in G \quad [k]=\left[k^{\prime}\right] \iff k \sim k^{\prime}$, dunque il sistema precedente è equivalente a $\left.\begin{array}{l}x \sim x^{\prime} \\ y \sim y^{\prime}\end{array}\right\} \implies x+y \sim x^{\prime}+y^{\prime}$
    - $x \sim x' \iff (-x)+x' \in H \iff x' - x \in H$
    - $y \sim y' \iff (-y) +y' \in H \iff y' - y \in H$
    - $H \leqslant G \implies (x'-x)+(y'-y) \in H \implies -(x+y)+(x'+y') \in H \iff x +y \sim x'+y'$
  - $(G/H, +)$ gruppo abeliano
    - $\forall [x], [y], [z] \in G/H \quad ([x]+[y])+[z]=[x+y]+[z]=[(x+y)+z]= [x+(y+z)]=[x]+[y+z]=[x]+([y]+[z])$
    - $\forall [x] \in G/H \quad [x]+[0]=[0]+[x]=[x]$ e $[0] + [x] = [0 + x] = [x]$, e $[0] \in G/H$ perché $G$ gruppo
    - $\forall [x] \in G/H \quad [x]+[-x]=[x+(-x)]=[0]$ e $[-x] +[x]=[-x +x]=[0]$$\implies -[x] = [-x]$
    - $[x]+[y]=[x+y]=[y+x]=[y]+[x]$

## Oss

- **Hp**
    - $(A, +, \cdot)$ anello commutativo
    - $I \subset A$ ideale
- **Th**
    - $(A/I, +, \cdot)$ è anello commutativo, dove $+, \cdot : A/I \times A/I \rightarrow A/I$
- **Dim**
    - $+$ è ben definita per dimostrazione precedente, poiché $(I, +) \leqslant (A, +)$ gruppo abeliano per definizione di $I$
    - $\cdot$ ben definita $\iff\left.\forall x, x^{\prime}, y, y' \in A \quad \begin{array}{l}{[x]=\left[x^{\prime}\right]} \\ {[y]=\left[y^{\prime}\right]}\end{array}\right\} \implies[xy]=\left[x^{\prime}y' \right]$
        - $\forall k, k' \in A \quad [k]=\left[k^{\prime}\right] \iff k \sim k^{\prime}$, dunque il sistema precedente è equivalente a $\left.\begin{array}{l}x \sim x^{\prime} \\ y \sim y^{\prime}\end{array}\right\} \implies xy \sim x^{\prime}y^{\prime}$
        - $x \sim x' \iff (-x)+x' \in I \iff i_1:=x' - x \in I$
        - $y \sim y' \iff (-y) +y' \in I \iff i_2:=y' - y \in I$
        - $I$ ideale $\implies A \cdot I \subseteq I \implies \forall a \in A, i \in I \quad a i \in I$, in particolare $i_1y', xi_2 \in I$
        - $(I, +) \leqslant (A, +) \implies i_1y' + xi_2 \in I$
        - $i_1y' + xi_2 = (x'-x)y' + x(y'-y) = x'y' - xy' + xy' - xy = x'y' - xy \in I \iff x'y \sim xy$
    - $(A/I, +, \cdot)$ anello commutativo
        - $\forall [x], [y], [z] \in A/I \quad ([x][y])[x] = [xy][z] = [xyz] = [x][yz] = [x]([y][z])$
        - $\forall [x] \in A/I \quad [x][1]=[1][x]=[x]$ e $[1] \cdot [x] = [1 \cdot x] = [x]$, e $[1] \in A/I$ perché $A$ anello
        - $\forall [x] \in A/I \quad [x]\cdot[x^{-1}]=[x \cdot x^{-1}]=[1]$ e $[x^{-1}] \cdot[x]=[x^{-1} \cdot x]=[1] \implies [x]^{-1} = [x^{-1}]$
        - $[x][y] = [xy] = [yx] = [y][x]$

## Oss

- **Hp**
    - $(G, \cdot)$ gruppo
    - $H \trianglelefteq G$
- **Th**
    - $(G/H, \cdot)$ è gruppo abeliano, dove $\cdot: G/H \times G/H \rightarrow G/H$
- **Dim**
    - ⚠️ todo

