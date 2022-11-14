# Gruppi

## Def

- **Semigruppo**
> - $S$ insieme
> - $m: S \times S \rightarrow S$
> - $(S, m)$ **semigruppo** $\iff  m(x, m(y, z))=m(m(x, y),z) \quad \forall x, y, z \in S$

- **Monoide**
> - $S$ insieme
> - $m: S \times S \rightarrow S$
> - $(S, m)$ **monoide** $\iff (S, m)$ semigruppo e $\exists e \in S  \mid m(x, e) = m(e, x) = x \quad \forall x \in S$

- **Gruppo**
> - $S$ insieme
> - $m: S \times S \rightarrow S$
> - $(S, m)$ **gruppo** $\iff (S, m)$ monoide e $\exists x^{-1} \in S \mid m(x, x^{-1}) =m(x^{-1}, x) =e \quad \forall x \in S$

- **Gruppo abeliano**
> - $S$ insieme
> - $m: S \times S \rightarrow S$
> - $(S, m)$ **gruppo abeliano** $\iff (S,m)$ gruppo e $m(x, y) = m(y, x) \quad \forall x, y \in S$

## Oss

- **Hp**
  - $G$ monoide
  - $\exists e \in G$ elemento neutro
- **Th**
  - $e$ è unico in $G$
- **Dim**
  - per assurdo, $\exists e\_1, e\_2 \mid e\_1 \neq e\_2$ elementi neutri, allora $\left.\begin{array}{l}m\left(x, e\_{1}\right)=m\left(e\_{1}, x\right)=x \\ m\left(x, e\_{2}\right)=m\left(e\_{2}, x\right)=x\end{array}\right\} \implies m\left(e\_{1}, x\right)=m\left(e\_{2}, x\right) \implies e\_1=e\_2$ necessariamente, quindi è unico

## Oss

- **Hp**
  - $(G, m)$ gruppo
  - $x \in G$
  - $\exists x^{-1} \in G$ inverso di $x$ rispetto ad $m$
- **Th**
  - $x^{-1}$ è unico in $G$ per $x$ rispetto a $m$
- **Dim**
  - per assurdo, per un certo $x \in G \quad \exists x^{-1}\_1, x^{-1}\_2 \mid x^{-1}\_1 \neq x^{-1}\_2$, allora $\left.\begin{array}{l}m\left(x, x\_{1}^{-1}\right)=m\left(x\_{1}^{-1}, x\right)=e \\ m\left(x, x\_{2}^{-1}\right)=m\left(x\_{2}^{-1}, x\right)=e \end{array}\right\} \implies m\left(e\_{1}^{-1}, x\right)=m\left(x\_{2}^{-1}, x\right) \implies x\_1^{-1}=x\_2^{-1}$ necessariamente, quindi è unico

## Ex

- **Hp**
  - $X, Y$ insiemi,
  - $Y^X = \{f \mid f:X \rightarrow Y\}$
- **Th**
  - $(X^X, \circ)$ è **monoide**
- **Dim**
    - $\forall f, g, h \in Y^X \quad (f \circ g) \circ h=f \circ(g \circ h)$. poiché la composizione di funzioni è associativa
    - $\forall X \quad \exists \textrm{id}\_X \mid \textrm{id}\_X : X \rightarrow X : x \rightarrow x$, che costituisce dunque l'elemento neutro, mappando ogni elemento in sé stesso

## Oss

- **Hp**
  - $X, Y$ insiemi finiti
- **Th**
  - $\left| Y^X \right| = \left| Y \right| ^ {|X|}$
- **Dim**
  - ⚠️ **MANCA DIMOSTRAZIONE**

## Oss

- **Hp**
  - $S\_X := \{f \mid f : X \rightarrow Y$ biiettiva $\}$
- **Th**
  - $(S\_X, \circ)$ è un gruppo, non commutativo se $|X| \ge 3$
- **Dim**
  - la composizione di funzioni è associativa
  - $\textrm{id}$ è biiettiva $\implies \textrm{id} \in S\_X$ per definizione, e costituisce l'elemento neutro
  - $\forall f:X \rightarrow Y \in S\_X \quad \exists f^{-1}: Y \rightarrow X$, poiché $f \in S\_X \implies f$ biiettiva, e ogni funzione biiettiva è invertibile
  - $|X| = 2 \implies X$ è della forma $X = \{a, b\}$, quindi $S\_X =\left\{\begin{array}{l}a \rightarrow a \\ b \rightarrow b\end{array}\right. \ ,\ \left.\begin{array}{l}a \rightarrow b \\ b \rightarrow a\end{array}\right\}$, dove uno dei due elementi è $\rm id$
    - $\rm id \circ id = id$
    - $\rm \sigma \circ id = id \circ \sigma = \sigma$
    - $\rm \sigma \circ \sigma = id$ per costruzione
  - quindi $|X| = 2 \implies S\_X$ è abeliano, mentre $|X| = 1 \implies S\_X$ è abeliano perché contiene un solo elemento
  - ⚠️ **perche >= 3 non è abeliano?**

## Oss

⚠️ **MANCA OSSERVAZIONE, non capisco che cosa ho scritto**

****

# Anelli

## Def

- **Anello**
> - $A$ insieme
> - $+: A \times A \implies A$
> - $\*: A \times A \implies A$
> - $(A, +, \*)$ **anello** $\iff (A, +)$ gruppo abeliano, $(A, \*)$ monoide e  $a\*(b + c) = a \* b + a \* c \quad \forall a, b, c \in A$
> - $a \* b=b \* a \quad \forall a, b \in A \implies   (A, \*, +)$ è un **anello commutativo**

- **Campo**
> - $(A, +, \*)$ anello
> - $(A, +, \*)$ è un **campo** $\iff \forall x \in A \quad \exists x^{-1}$ rispetto a $\*$

## Def

- **Invertibili**
> - $(A, +, \cdot)$ anello commutativo
> - $a \in A$ **invertibile** $\iff \exists a^{-1} \in A \mid a \cdot a^{-1}=e$, dove $e$ è l'elemento neutro dell'anello rispetto a $\cdot$
> - $A^\* := \{a \in A \mid a$ invertibile$\}$ è l'**insieme degli invertibili di $A$**

## Oss

- **Hp**
  - $(A, +, \cdot)$ anello commutativo
- **Th**
  - $(A^\*, \cdot)$ è un gruppo
- **Dim**
    - $(xy)z = x(yz)$
    - $1^{-1} = 1 \implies 1$ invertibile $\implies 1 \in A^\*$ per definizione di $A^\* \implies \exists e \in A^\*$
    - $\forall x \in A^{\*} \quad \exists x^{-1}$ per definizione di $A^\*$, ma poiché $x^{-1}$ è inverso di $x$, allora $x^{-1} \in A^\*$ per definizione

## Oss

- **Hp**
  - $(A, +, \cdot)$ anello commutativo
- **Th**
    - $(A^\*, \cdot) \subset (A, \cdot)$ è un sottogruppo
- **Dim**
  - esiste il neutro per dimostrazione precedente
  - $\forall x, y \in A^{\*} \quad \exists x^{-1}, y^{-1}$, e in particolare $y^{-1}x^{-1} = (xy)^{-1} \implies xy \in A^\*$ per definizione
  - è chiuso rispetto agli inversi per dimostrazione precedente

## Def

- **Divisori dello $0$**
> - $(A, + , \cdot)$ anello commutativo
> - $a \in A$ **divisore dello $0$** $\iff \exists b \in A - \{0\} \mid a \cdot b = 0$

- **Dominio di integrità**
> - $(A, +, \cdot)$ anello commutativo
> - $A$ **dominio di integrità** $\iff \nexists x : x \mid 0$, oltre a $x = 0$
> - alternativamente, $A$ è dominio di integrità $\iff$ in $A$ vale la legge di annullamento del prodotto


## Oss

- **Hp**
  - $(A, +, \cdot)$ anello commutativo
- **Th**
  - $x \mid 0 \iff x \notin A^\*$
- **Dim**
  - ipotizziamo che $\exists a \in A \mid a$ invertibile e divisore dello $0$, allora $\exists a^{-1} \in A, b \in A - \{0\} \mid a^{-1}a = 1 \land ab = 0$
  - $b = 1 \cdot b = (a^{-1} a)\cdot b = a^{-1}\cdot(ab)=a^{-1}\cdot 0= 0 \ \bot$

## Oss

- **Hp**
  - $A$ campo
- **Th**
  - $A$ dominio di integrità
- **Dim**
   - $A$ campo $\implies$ ogni elemento non nullo è invertibile, dunque $A^\*=A - \{0\}$
     - $0$ è l'unico elemento non invertibile
     - $0 \notin A^\* \iff 0 \mid 0$ per dimostrazione precedente
   - quindi $A$ è dominio di integrità poiché $0$ è l'unico divisore dello $0$

## Def

- **Sottoanello**
> - $(A, +, \cdot)$ anello
> - $(B, + , \cdot) \subset (A, +, \cdot)$ **sottoanello** $\iff (B, +) \subset (A, +)$ sottogruppo e $B \cdot B \subset B$

****

# Sottogruppi

## Def

- **Sottogruppo**
> - $(G, \*)$ gruppo 
> - $(H, \*) \subset (G, \*)$ **sottogruppo** $\iff \exists e \in H \mid e$ è l'elemento neutro,$H \* H \subset H$ e $\exists x^{-1} \in H \quad \forall x \in H$

## Def

- **Sottogruppo normale**
> - $(G, \*)$ gruppo
> - $(H, \*) \subset (G, \*)$ sottogruppo
> - $x \in G$
> - $xH := \{xh \mid h \in H\}$
> - $Hx := \{hx \mid h \in H\}$
> - $H$ **sottogruppo normale** $\iff xH = Hx \quad \forall x \in G$

## Oss

- **Hp**
  1) $H$ è sottogruppo normale
  2) $\forall g \in G, h \in H \quad g \cdot h \cdot g^{-1} \in H$
  3) $\forall g \in G, h \in H \quad \exists k \in H \mid g \cdot h = k \cdot g$
- **Th**
  - le tre formulazioni sono equivalenti
- **Dim**
  - 1 $\implies$ 3
    - $gH = Hg$ per ipotesi 1  $\implies \forall gh \in gH = Hg = \{kg \mid k \in H\} \implies \exists k \in H \mid gh = kg$ per definizione di $Hg$
  - 3 $\implies$ 2
    - $\forall g \in G, h \in H \quad \exists k \in H \mid gh = kg$ per ipotesi 3
    - $gh = kg \iff g h g^{-1} =k g g^{-1} \iff k = ghg^{-1}$, ma $k \in H$ per ipotesi, dunque $ghg^{-1} \in H$
  - 2 $\implies$ 1
    - $gH = Hg \iff gH \subset Hg \land Hg \subset gH$
    - $gH \subset Hg$
      - $\forall h \in H, g \in G \implies gh \in gH$
      - $k:= ghg^{-1} \in H$ per ipotesi 2
      - $k = ghg^{-1} \iff k g= ghg^{-1}g \iff kg = gh$, e $kg \in Hg$ e $gh \in gH$, quindi $gH \subset Hg$
    - $Hg \subset gH$
      -  $G$ gruppo $\implies \forall g \in G \quad \exists g^{-1} \in G$
      -  $\forall g^{-1} \in G \quad h:= g^{-1}k(g^{-1})^{-1} \in H$ per ipotesi
      -  $h = g^{-1}kg \iff gh = gg^{-1}kg \iff gh = kg$, ma $$

## Oss

- ⚠️ **CONTROLLA, MA IN TEORIA QUESTA ROBA È DA BUTTARE**
- **Hp**
  - $G$ gruppo
  - $H \subset$ sottogruppo normale
  - $G/H := \{[x] \mid x \in H\}$, che per 
  - $\cdot$ è l'operazione di prodotto definita tra classi laterali sinistre in $G/H$, tale che $\forall [x], [y] \in G/H$
- **Th**
  - $(G/H, \cdot)$ è un gruppo
- **Dim**
  - l'operazione $\cdot$ è ben definita $\iff$ $\left.\begin{array}{c}{[x]=[x']} \\ {[y]=[y']}\end{array}\right\} \implies [x\cdot y]=[x' \cdot y']$
    - $H$ è un sottogruppo normale, dunque $\left\{\begin{array}{c}{[x]=xH=Hx} \\ {[x']=x'H =Hx'} \\ {[y]=yH=Hy} \\ {[y'] = y'H = Hy'} \\ {[x\cdot y]=x yH = H xy} \\ {[x'\cdot y']=x' y'H = H x'y'}\end{array}\right.$
    - in particolare, $[x]=[x'] \land [x]= xH \land [x'] = x'H \implies xH = x'H$, e in particolare $xH \subset x'H \implies \exists h \in H \mid xh = x'$
    - inoltre, in particolare $[y] = [y'] \land [y] = yH \land [y'] = y'H \implies yH = y'H$, e in particolare $\forall hy' \in Hy' \quad hy' \in Hy$, e $Hy' = yH \implies \exists k \in H \mid yk = hy'$
    - $x'=xh \implies x'y' = xh\cdot y'$, e $yk = hy' \implies xhy' = x \cdot yk$, e in particolare $xyk \in xyH$ per definizione, quindi $x'y' \in xyH$, dunque $[x' \cdot y'] = [x \cdot y]$
    - ⚠️ **RIVEDI**
    - ⚠️ **PERCHÉ NON SERVE L'IMPLICAZIONE AL CONTRARIO?**
  - $(G/H, \cdot)$
    - $\forall [x], [y], [z] \in G/H \quad ([x][y])[z] = [x y][z] = [x y z] = [x][y z]=[x]([y][z])$, quindi l'operazione è associativa
    - $1\_G \in G$ poiché $G$ gruppo $\implies [1\_G] \in G/H$, l'elemento neutro
    - $\forall [x], [x^{-1}] \in G/H \quad [x][x^{-1}]=[x \cdot x^{-1}] = [1\_G] \implies [x^{-1}] = [x]^{-1}$

****

# Ordine

## Def

- **Ordine di un elemento in un gruppo**
> - $G$ gruppo
> - $g \in G$
> - $H(g):=\left\{g^{n} \mid n \in \mathbb{Z}\right\}$
> - $o(g):= |H(g)|$ è detto **ordine di $g \in G$**

## Oss

- **Hp** 
  - $G$ gruppo
  - $g \in G$
- **Th**
  - $(H(g), \cdot) \subset (G, \cdot)$  è sottogruppo
- **Dim**
  - $e=g^{0} \implies e \in H(g)$ per definizione di $H(g)$
  - $\forall m, n \in \mathbb{Z} \quad m + n \in \mathbb{Z} \implies g^m \cdot g^n = g^{m + n} \in H(g)$ per definizione di $H(g)$, quindi $H(g) \cdot Hg(g) \subset H(g)$
  - $\forall n \in \mathbb{Z} \quad -n \in \mathbb{Z} \implies (g^n)^{-1} = g^{-n} \in H(g)$ per definizione di $H(g)$
  ****
   ⚠️ **CONTINUA DA QUA**
- $\exists! d \geq 0 \mid I(g)=I(d)$
  - $d = 0 \implies o(g) = |H(g)| = |\mathbb{Z}|$, dunque infinito
  - $d>0 \implies d = o(g)$
 - ⚠️ **MANCA DIMOSTRAZIONE**


