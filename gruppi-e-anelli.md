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
  - per assurdo, $\exists e_1, e_2 \mid e_1 \neq e_2$ elementi neutri, allora $\left.\begin{array}{l}m\left(x, e_{1}\right)=m\left(e_{1}, x\right)=x \\ m\left(x, e_{2}\right)=m\left(e_{2}, x\right)=x\end{array}\right\} \implies m\left(e_{1}, x\right)=m\left(e_{2}, x\right) \implies e_1=e_2$ necessariamente, quindi è unico

## Oss

- **Hp**
  - $(G, m)$ gruppo
  - $x \in G$
  - $\exists x^{-1} \in G$ inverso di $x$ rispetto ad $m$
- **Th**
  - $x^{-1}$ è unico in $G$ per $x$ rispetto a $m$
- **Dim**
  - per assurdo, per un certo $x \in G \quad \exists x^{-1}_1, x^{-1}_2 \mid x^{-1}_1 \neq x^{-1}_2$, allora $\left.\begin{array}{l}m\left(x, x_{1}^{-1}\right)=m\left(x_{1}^{-1}, x\right)=e \\ m\left(x, x_{2}^{-1}\right)=m\left(x_{2}^{-1}, x\right)=e \end{array}\right\} \implies m\left(e_{1}^{-1}, x\right)=m\left(x_{2}^{-1}, x\right) \implies x_1^{-1}=x_2^{-1}$ necessariamente, quindi è unico

## Ex

- **Hp**
  - $X, Y$ insiemi,
  - $Y^X = \{f \mid f:X \rightarrow Y\}$
- **Th**
  - $(X^X, \circ)$ è **monoide**
- **Dim**
    - $\forall f, g, h \in Y^X \quad (f \circ g) \circ h=f \circ(g \circ h)$. poiché la composizione di funzioni è associativa
    - $\forall X \quad \exists \textrm{id}_X \mid \textrm{id}_X : X \rightarrow X : x \rightarrow x$, che costituisce dunque l'elemento neutro, mappando ogni elemento in sé stesso

## Oss

- **Hp**
  - $X, Y$ insiemi finiti
- **Th**
  - $\left| Y^X \right| = \left| Y \right| ^ {|X|}$

## Oss

⚠️ **MANCA OSSERVAZIONE, non capisco che cosa ho scritto**

****

# Anelli

## Def

- **Anello**
> - $A$ insieme
> - $+: A \times A \implies A$
> - $*: A \times A \implies A$
> - $(A, +, *)$ **anello** $\iff (A, +)$ gruppo abeliano, $(A, *)$ monoide e  $a*(b + c) = a * b + a * c \quad \forall a, b, c \in A$
> - $a * b=b * a \quad \forall a, b \in A \implies   (A, *, +)$ è un **anello commutativo**

- **Campo**
> - $(A, +, *)$ anello
> - $(A, +, *)$ è un **campo** $\iff \forall x \in A \quad \exists x^{-1}$ rispetto a $*$

## Def

- **Invertibili**
> - $(A, +, \cdot)$ anello commutativo
> - $a \in A$ **invertibile** $\iff \exists a^{-1} \in A \mid a \cdot a^{-1}=e$, dove $e$ è l'elemento neutro dell'anello rispetto a $\cdot$
> - $A^* := \{a \in A \mid a$ invertibile$\}$ è l'**insieme degli invertibili di $A$**

## Oss

- **Hp**
  - $(A, +, \cdot)$ anello commutativo
- **Th**
  - $(A^*, \cdot)$ è un gruppo
- **Dim**
    - $(xy)z = x(yz)$
    - $1^{-1} = 1 \implies 1$ invertibile $\implies 1 \in A^*$ per definizione di $A^* \implies \exists e \in A^*$
    - $\forall x \in A^{*} \quad \exists x^{-1}$ per definizione di $A^*$, ma poiché $x^{-1}$ è inverso di $x$, allora $x^{-1} \in A^*$ per definizione

## Oss

- **Hp**
  - $(A, +, \cdot)$ anello commutativo
- **Th**
    - $(A^*, \cdot) \subset (A, \cdot)$ è un sottogruppo
- **Dim**
  - esiste il neutro per dimostrazione precedente
  - $\forall x, y \in A^{*} \quad \exists x^{-1}, y^{-1}$, e in particolare $y^{-1}x^{-1} = (xy)^{-1} \implies xy \in A^*$ per definizione
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
  - $x \mid 0 \iff x \notin A^*$
- **Dim**
  - ipotizzando che $\exists a \in A \mid a$ invertibile e divisore dello $0$, allora $\exists a^{-1} \in A, b \in A - \{0\} \mid a^{-1}a = 1 \land ab = 0$
  - $b = 1 \cdot b = (a^{-1} a)\cdot b = a^{-1}\cdot(ab)=a^{-1}\cdot 0= 0 \ \bot$

## Oss

- **Hp**
  - $A$ campo
- **Th**
  - $A$ dominio di integrità
- **Dim**
   - $A$ campo $\implies$ ogni elemento non nullo è invertibile, dunque $A^*=A - \{0\}$
     - $0$ è l'unico elemento non invertibile
     - $0 \notin A^* \iff 0 \mid 0$ per dimostrazione precedente
   - quindi $A$ è dominio di integrità poiché $0$ è l'unico divisore dello $0$

## Def

- **Sottoanello**
> - $(A, +, \cdot)$ anello
> - $(B, + , \cdot) \subset (A, +, \cdot)$ **sottoanello** $\iff (B, +) \subset (A, +)$ sottogruppo e $B \cdot B \subset B$

****

# Sottogruppi

## Def

- **Sottogruppo**
> - $(G, *)$ gruppo 
> - $(H, *) \subset (G, *)$ **sottogruppo** $\iff \exists e \in H \mid e$ è l'elemento neutro,$H * H \subset H$ e $\exists x^{-1} \in H \quad \forall x \in H$

## Def

- **Sottogruppo normale**
> - $(G, *)$ gruppo
> - $(H, *) \subset (G, *)$ sottogruppo
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
      - ⚠️ **INCOMPLETA**

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

## Oss

- **Hp**
  - $G$ gruppo
  - $g \in G$
  - $I(g):=\{n \in \mathbb{Z} \mid g^n = e\}$
- **Th**
  - $I(g)$ è un ideale
- **Dim**
  - $(I(g), +) \subset (\mathbb{Z}, +)$ è sottogruppo
    - $0 \in \mathbb{Z} \land g^{0}=e \implies 0 \in I(g)$ per definizione di $I(g)$
    - $m, n \in \mathbb{Z} \mid  g^{m}=g^{n}=e \implies g^{m} \cdot g^{n}= g^{m + n} \iff e \cdot e = e \implies m +n \in I(g)$ per definizoine di $I(g)$, quindi $I(g) + I(g) \subset I(g)$
    - $n \in I(g) \mid g^n = e \iff (g^n)^{-1} = e ^{-1 } \iff g^{-n} =e \implies -n \in I(g)$ per definizione di $I(g)$
  - $\forall n \in I(g), k \in \mathbb{Z} \quad g^{n \cdot k} = (g^n)^k = e^k = e \implies n \cdot k \in I(g)$

## Oss

- **Hp**
  - $G$ gruppo
  - $g \in G$
  - $\exists! d \geq 0 \mid I(g)=I(d)$
- **Th**
  - $d = 0 \implies o(g) := |H(g)| = |\mathbb{Z}|$, dunque infinito
  - $d>0 \implies d = o(g)$
- **Dim**
  - $d = 0$
    - la funzione $f: \mathbb{Z} \rightarrow H(g) : n \rightarrow g^n$ è biiettiva
      - $f$ iniettività $\iff \forall m, n \in \mathbb{Z} \quad g^n =g^m \implies n = m$
        - $m, n \in \mathbb{Z} \mid g^m = g^n \implies g^{-m} \cdot g^m=g^{-m} \cdot g^n \iff e = g^{n - m} \implies n - m \in I(g) = I(d) \implies d \mid n - m$
        - $d = 0 \implies 0 \mid n - m \iff n -m = 0 \iff n = m$, di conseguenza $g^m = g^n \implies n = m$
      - $f$ suriettività è data al fatto che l'immagine di $f$ coincide con $H(g)$ per definizione di $H(g)$
    - $f$ è biiettiva $\implies |\mathbb{Z} | = |H(g)| = o(g)$, dunque infinito
  - $d \gt 0$
    - $I(g) = I(d) \land d \in I(d) \implies d \in I(g) \implies g^d = e$
    - ⚠️ **QUESTA IPOTESI SOTTO L'HO AGGIUNTA IO, NON SO SE È GIUSTA PENSO DI SI**
    - $d \gt 0 \implies \forall n \in I(g) \quad \exists q, r \mid n = dq + r \quad 0 \le r \lt d$ per il teorema della divisione euclidea con il resto, dunque $g^n = g^{dq +r}=(g^d)^q \cdot g^r=e^q \cdot g^r =e \cdot g^r = g^r$
    - ⚠️ **NON HO CAPITO UN CAZZO**
    - ⚠️ **PER QUALCHE COSA CHE NON HO CAPITO** allora $H(g) = \{g^0, g^1, \ldots, g^{d-1}\} \implies |H(g)|=d$

## Oss

- **Hp**
  - $G$ gruppo finito
  - $g \in G$
- **Th**
  - $H(g)$ sottogruppo finito
- **Dim**
  - per il teorema di Lagrange $|H(g)| \bigg\vert |G|$, e dunque $G$ finito $\implies H(g)$ finito necessariamente

## Oss

- **Hp**
  - $G$ gruppo finito
  - $g \in G$
- **Th**
  - $g^{|G|}=e$
- **Dim**
  - $\exists ! d = o(g) \mid I(d) = I(g)$ per dimostrazione precedente, e dunque $d \in I(d) \implies d \in  I(g) \implies g^d = e$
  - $d = o(g) = |H(g)| \bigg\vert |G|$ per il teorema di Lagrange, e dunque $\exists k \in \mathbb{Z} \quad |G|=d \cdot k \implies g^{|G|} = g^{d \cdot k} = (g^d)^k = e^k = e$
