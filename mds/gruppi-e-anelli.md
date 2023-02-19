# Gruppi e Anelli

## Def

- **Semigruppo**

> - $S$ insieme
> - $m: S \times S \rightarrow S$
> - $(S, m)$ è detto **semigruppo** $\iff \forall x, y, z \in S \quad m(x, m(y, z))=m(m(x, y),z) \quad$
>   - in particolare, deve valere la _proprietà associativa_

- **Monoide**

> - $S$ insieme
> - $m: S \times S \rightarrow S$
> - $(S, m)$ è detto **monoide** $\iff$
>   - $(S, m)$ semigruppo
>   - $\exists e \in S \mid \forall x \in S \quad m(x, e) = m(e, x) = x$
>     - in particolare, deve esistere l'_elemento neutro_

- **Gruppo**

> - $S$ insieme
> - $m: S \times S \rightarrow S$
> - $(S, m)$ è detto **gruppo** $\iff$
>   - $(S, m)$ monoide
>   - $\forall x \in S \quad \exists x^{-1} \in S \mid m(x, x^{-1}) =m(x^{-1}, x) =e$
>     - in particolare, per ogni elemento deve esistere l'_inverso_

- **Gruppo abeliano**

> - $S$ insieme
> - $m: S \times S \rightarrow S$
> - $(S, m)$ è detto **gruppo abeliano** $\iff$
>   - $(S,m)$ gruppo
>   - $\forall x, y \in S \quad m(x, y) = m(y, x)$
>     - in particolare, deve valere la _proprietà commutativa_

## Oss

- **Hp**
  - $G$ monoide
- **Th**
  - $e \in G$ elemento neutro è unico in $G$
- **Dim**
  - per assurdo, ipotizzando $\exists e_1, e_2 \in G \mid e_1 \neq e_2$ elementi neutri, allora $\left.\begin{array}{l}m\left(x, e_{1}\right)=m\left(e_{1}, x\right)=x \\ m\left(x, e_{2}\right)=m\left(e_{2}, x\right)=x\end{array}\right\} \implies m\left(e_{1}, x\right)=m\left(e_{2}, x\right) \implies e_1=e_2$ necessariamente, quindi è unico

## Oss

- **Hp**
  - $(G, m)$ gruppo
- **Th**
  - $\forall x \in G \quad x^{-1}$ è unico in $G$, rispetto a $m$
- **Dim**
  - per assurdo, ipotizzando che per un certo $x \in G \quad \exists x^{-1}_1, x^{-1}_2 \mid x^{-1}_1 \neq x^{-1}_2$, allora $\left.\begin{array}{l}m\left(x, x_{1}^{-1}\right)=m\left(x_{1}^{-1}, x\right)=e \\ m\left(x, x_{2}^{-1}\right)=m\left(x_{2}^{-1}, x\right)=e \end{array}\right\} \implies m\left(x_{1}^{-1}, x\right)=m\left(x_{2}^{-1}, x\right) \implies x_1^{-1}=x_2^{-1}$ necessariamente, quindi è unico

## Ex

- **Hp**
  - $X, Y$ insiemi,
  - $Y^X := \{f \mid f:X \rightarrow Y\}$
- **Th**
  - $(X^X, \circ)$ è monoide
- **Dim**
    - $\forall f, g, h \in Y^X \quad (f \circ g) \circ h=f \circ(g \circ h)$. poiché la composizione di funzioni è associativa
    - $\textrm{id}_X \mid \textrm{id}_X : X \rightarrow X : x \rightarrow x$, è detta _funzione identità_, che costituisce dunque l'elemento neutro, mappando ogni elemento in sé stesso

## Oss

- **Hp**
  - $X, Y$ insiemi finiti
- **Th**
  - $\left| Y^X \right| = \left| Y \right| ^ {|X|}$

## Def

- **Anello**

> - $A$ insieme
> - $+: A \times A \rightarrow A$
> - $\cdot: A \times A \rightarrow A$
> - $(A, +, \cdot)$ è detto **anello** $\iff$
>   - $(A, +)$ gruppo abeliano
>   - $(A, \cdot)$ monoide
>   - $\forall a, b, c \in A \quad a \cdot (b + c) = a \cdot b + a \cdot c$
>     - in particolare, deve valere la _proprietà distributiva a sinistra_

- **Anello commutativo**

> - $A$ insieme
> - $+: A \times A \rightarrow A$
> - $\cdot: A \times A \rightarrow A$
> - $(A, +, \cdot)$ è detto **anello commutativo** $\iff$
>   - $(A, +, \cdot)$ anello
>   - $\forall a, b \in A \quad a \cdot b=b \cdot a$
>     - in particolare, deve valere la _proprietà commutativa_

- **Campo**

> - $(A, +, \cdot)$ anello commutativo
> - $(A, +, \cdot)$ è detto **campo** $\iff \forall x \in A \quad \exists x^{-1} \in A$ rispetto a $\cdot$

- **Semianello commutativo**

> - $A$ insieme
> - $+: A \times A \rightarrow A$
> - $\cdot: A \times A \rightarrow A$
> - $(A, +, \cdot)$ è detto **semianello commutativo** $\iff$
>   - $(A, +)$ monide commutativo
>   - $(A, \cdot)$ monoide commutativo
>   - $\forall a, b, c \in A \quad a\cdot (b + c) = a \cdot b + a \cdot c$
>     - in particolare, deve valere la _proprietà distributiva a sinistra_

## Def

- **Invertibili**

> - $(A, +, \cdot)$ anello commutativo
> - $a \in A$ è detto **invertibile** $\iff \exists a^{-1} \in A \mid a \cdot a^{-1}=a^{-1}\cdot a = e$, dove $e$ è l'elemento neutro dell'anello rispetto a $\cdot$
> - $A^* := \{a \in A \mid a$ invertibile$\}$ è detto **insieme degli invertibili di $A$**

## Oss

- **Hp**
  - $(A, +, \cdot)$ anello commutativo
- **Th**
  - $(A^*, \cdot)$ è un gruppo
- **Dim**
    - $(xy)z = x(yz)$
    - $1^{-1} = 1 \implies 1$ invertibile $\implies 1 \in A^*$ per definizione di $A^*$
    - $\forall x \in A^{*} \quad \exists x^{-1}$ per definizione di $A^*$, ma poiché $x^{-1}$ è inverso di $x$, allora $x^{-1} \in A^*$ per definizione
        - $x \in A^* \iff x, x^{-1} \in A^*$

## Def

- **Divisori dello $0$**

> - $(A, + , \cdot)$ anello commutativo
> - $a \in A$ è detto **divisore dello $0$** $\iff \exists b \in A - \{0\} \mid a \cdot b = 0$

- **Dominio di integrità**

> - $(A, +, \cdot)$ anello commutativo
> - $A$ è detto **dominio di integrità** $\iff \nexists x \in A - \{0\} : x \mid 0$
>   - in particolare, $A$ è dominio di integrità $\iff$ in $A$ vale la legge di annullamento del prodotto

## Oss

- **Hp**
  - $(A, +, \cdot)$ anello commutativo
- **Th**
  - $x \mid 0 \implies x \notin A^*$
- **Dim**
  - per assurdo, ipotizzando $\exists a \in A \mid a$ divisore dello $0$ e invertibile, allora $\exists a^{-1} \in A, b \in A - \{0\} \mid a^{-1}a = 1 \land ab = 0$
  - $b = 1 \cdot b = (a^{-1} a)\cdot b = a^{-1}\cdot(ab)=a^{-1}\cdot 0= 0 \ \bot$

## Oss

- **Hp**
  - $A$ campo
- **Th**
  - $A$ dominio di integrità
- **Dim**
   - $A$ campo $\implies$ in $A$ ogni elemento non nullo è invertibile, dunque $A^*=A - \{0\} \implies \forall a \in A - \{0\} \quad a \in A^* \implies a \nmid 0$, il che implica che $A$ è dominio di integrità per definizione

## Def

- **Elemento irriducibile**

> - $A$ anello commutativo
> - $a \in A - \{0\} \mid a \in A^*$
> - $a$ è detto **irriducibile** $\iff \exists b, c \in A \mid a = b c \implies b \in A^* \lor c \in A^*$

- **Elemento primo**

> - $A$ anello commutativo
> - $a \in A - \{0\} \mid a \in A^*$
> - $a$ è detto **primo** $\iff \exists b, c \in A : a \mid bc \implies a \mid b \lor a \mid c$

- **Interi primi**

> - $\mathbb{P} := \{p \in \mathbb{N} - \{0, 1\} \mid \nexists y \in \mathbb{N} - \{1, p\} : y \mid p\}$ è detto **insieme degli interi primi**
>   - si noti che $\mathbb{P}$ _non coincide necessariamente_ con gli _elementi primi_

## Oss

- **Hp**
  - $p \in \mathbb{P}$
- **Th**
  - $p$ primo
- **Dim**
  - siano $a, b \in \mathbb{Z} : p \mid ab \implies p$ è nella fattorizzazione di $ab \implies$ o $p$ è nella fattorizzazione di $a$, e quindi $p \mid a$, oppure $p$ è nella fattorizzazione di $b$, e quindi $p \mid b$, e dunque $p$ primo

## Oss

- **Hp**
    - $A$ dominio di integrità
    - $a \in A \mid a$ primo
- **Th**
    - $a$ irriducibile
- **Dim**
    - si supponga $\exists b, c \in A \mid a = bc$
    - $\forall a \in A \quad a \mid a$ per riflessività
    - per ipotesi $a$ primo, dunque per definizione $\exists b, c \in A : a \mid bc \implies a \mid b \lor a \mid c$, ma poiché $a \mid a = bc$, allora i coefficienti moltiplicativi sono proprio gli stessi che compongono $a$
    - prendendo ad esempio $a \mid b \implies \exists d \in A \mid ad = b \implies a = bc \iff a = adc \iff a \cdot( 1 - dc ) = 0$
    - $A$ dominio di integrità per ipotesi, e dunque in esso vale la legge di annullamento del prodotto
    - per definizione $a$ primo $\implies a \neq 0 \implies 1 - cd = 0 \iff -cd = -1 \iff cd = 1$, che per definizione implica che $d$ è l'inverso di $c$, e dunque $c \in A^*$
    - dunque, avendo preso un numero primo in ipotesi che si potesse scrivere come prodotto di altri due numeri nel dominio, si è ottenuta la definizione di irriducibilità di un elemento

## Oss

- **Hp**
    - $a \in \mathbb{Z}_{\ge 2} \mid a$ irriducibile
- **Th**
    - $a \in \mathbb{P}$
- **Dim**
    - $a$ irriducibile $\iff \exists b, c \in A \mid a = bc \implies b \in \mathbb{Z}^* \lor c \in \mathbb{Z}^*$
    - inoltre $\mathbb{Z}^* = \{+1, -1\}$ poiché sono gli unici elementi invertibili rispetto a $\cdot$ sono $\pm 1$
    - allora $a = bc \implies \left \{ \begin{array}{l}b = \pm 1 \\ c = a \end{array}\right. \lor \left \{ \begin{array}{l} b = a \\ c = \pm 1 \end{array} \right. \lor \left \{ \begin{array}{l} b = \pm 1 \\ c = \pm \end{array} \right.$
    - per i primi due casi, si ha che $a \in \mathbb{P}$, per l'ultimo caso si avrebbe $bc = a = \pm 1$, ma $a \in \mathbb{Z}_{\ge 2} \ \bot$
        - si noti che $\mathbb{P} \subset \mathbb{N}$, dunque nel caso di $-1$ si tratta di "estendere" la definizione di $\mathbb{P} \subset \mathbb{Z}$

****

# Sottogruppi

## Def

- **Sottogruppo**

> - $G$ insieme
> - $H \subseteq G$
> - $\cdot: G \times G \rightarrow G$
> - $(G, \cdot)$ gruppo 
> - $(H, \cdot) \leqslant (G, \cdot)$ è detto **sottogruppo** $\iff$
>   - $\exists e \in H \mid e$ è l'elemento neutro di $G$ rispetto a $\cdot$
>   - $H \cdot H \subseteq H$
>     - in particolare, deve essere _chiuso sull'operazione_
>   - $\forall x \in H \quad \exists x^{-1} \in H$
>     - in particolare, deve essere _chiuso sugli inversi_

## Oss

- **Hp**
    - $(A, \cdot)$ gruppo
- **Th**
    - $(A^*, \cdot) \leqslant (A, \cdot)$
- **Dim**
    - esiste il neutro per dimostrazione precedente
    - $\forall x, y \in A^{*} \quad \exists x^{-1}, y^{-1} \in A^*$, e in particolare $y^{-1}x^{-1} = (xy)^{-1} \implies xy \in A^*$ per definizione
    - è chiuso rispetto agli inversi per dimostrazione precedente

## Def

- **Sottoanello**

> - $A$ insieme
> - $B \subseteq A$
> - $+: A \times A \rightarrow A$
> - $(A, +, \cdot)$ anello
> - $\cdot: A \times A \rightarrow A$
> - $(B, + , \cdot) \leqslant (A, +, \cdot)$ è detto **sottoanello** $\iff$
>   - $(B, +) \leqslant (A, +)$
>   - $B \cdot B \subseteq B$
>     - in particolare $B \cdot B := \{b_1 \cdot b_2 \mid b_1, b_2 \in B\}$

## Def

- **Sottogruppo normale**

> - $(G, \cdot)$ gruppo
> - $(H, \cdot) \leqslant (G, \cdot)$
> - $x \in G$
> - $xH := \{xh \mid h \in H\}$
> - $Hx := \{hx \mid h \in H\}$
> - $H \trianglelefteq G$ è detto **sottogruppo normale** $\iff \forall x \in G \quad xH = Hx$

## Oss

- **Hp**
  - $G$ gruppo
  1) $H \trianglelefteq G$
  2) $\forall g \in G, h \in H \quad g \cdot h \cdot g^{-1} \in H$
  3) $\forall g \in G, h \in H \quad \exists k \in H \mid g \cdot h = k \cdot g$
- **Th**
  - le proposizioni sono equivalenti
- **Dim**
  - 1 $\implies$ 3
    - $gH = Hg$ per ipotesi 1  $\implies gH = Hg = \{kg \mid k \in H\} \implies \exists k \in H \mid gh = kg$ per definizione di $Hg$
  - 3 $\implies$ 2
    - $\forall g \in G, h \in H \quad \exists k \in H \mid gh = kg$ per ipotesi 3
    - $gh = kg \iff g h g^{-1} =k g g^{-1} \iff k = ghg^{-1}$, ma $k \in H$ per ipotesi, dunque $ghg^{-1} \in H$
  - 2 $\implies$ 1
    - $gH = Hg \iff gH \subseteq Hg \land Hg \subseteq gH$
    - _prima implicazione_
      - $k:= ghg^{-1} \in H$ per ipotesi 2
      - $k = ghg^{-1} \iff k g= ghg^{-1}g \iff kg = gh$, e in particolare $kg \in Hg$ e $gh \in gH$
    - _seconda implicazione_
      -  $\forall g^{-1} \in G \quad \exists h \in H \mid h:= g^{-1}k(g^{-1})^{-1} \in H$ per ipotesi 2
      - $g^{-1}kg = h \iff gg^{-1}kg = gh \iff kg = gh \in gH$
      - $k \in H \implies kg \in Hg$, ma $kg = gh \implies kg \in gH$

****

# Ordine

## Def

- **Ordine di un elemento**

> - $G$ gruppo
> - $g \in G$
> - $H(g):=\left\{g^{n} \mid n \in \mathbb{Z}\right\}$ è detto **sottogruppo ciclico**
>   - prende il nome di _sottogruppo ciclico_ poiché, a seconda del gruppo, le potenze di $g$ possono essere infinite o finite, ma quest'ultimo caso si verifica esclusivamente quando le potenze ciclano su loro stesse
> - $o(g):= |H(g)|$ è detto **ordine di $g$**
>   - tale valore può dunque essere infinito o finito, e in quest'ultimo caso l'ordine costituisce il valore più piccolo, non nullo, per cui $g^{o(g)} = e$, poiché per valori maggiori le potenze cicleranno infinitamente
>   

## Oss

- **Hp**
    - $(G, +)$ gruppo
    - $g \in G$
- **Th**
    - $(H(g), +) \leqslant (G, +)$
- **Dim**
    - $0 = 0 \cdot g \implies 0 \in H(g)$
    - $\forall xg, yg \in H(g) \quad xg + yg = (x + y)g \in H(g)$
    - $\forall xg \in H(g) \quad -xg = (-x)g \in H(g)$

## Oss

- **Hp** 
  - $(G, \cdot)$ gruppo
  - $g \in G$
- **Th**
  - $(H(g), \cdot) \leqslant (G, \cdot)$
- **Dim**
  - $e=g^{0} \implies e \in H(g)$
  - $\forall m, n \in \mathbb{Z} \quad m + n \in \mathbb{Z} \implies g^m \cdot g^n = g^{m + n} \in H(g)$
  - $\forall n \in \mathbb{Z} \quad -n \in \mathbb{Z} \implies (g^n)^{-1} = g^{-n} \in H(g)$

## Oss

- **Hp**
  - $G$ gruppo
  - $g \in G$
  - $I(g):=\{n \in \mathbb{Z} \mid g^n = e\}$
- **Th**
  - $I(g)$ è un ideale
- **Dim**
  - $(I(g), +) \leqslant (\mathbb{Z}, +)$
    - $0 \in \mathbb{Z} \land g^{0}=e \implies 0 \in I(g)$
    - $m, n \in \mathbb{Z} \mid  g^{m}=g^{n}=e \implies g^{m} \cdot g^{n}= g^{m + n} \iff e \cdot e = e \implies m +n \in I(g)$ per definizoine di $I(g)$, quindi $I(g) + I(g) \subseteq I(g)$
    - $n \in I(g) \mid g^n = e \iff (g^n)^{-1} = e ^{-1 } \iff g^{-n} =e \implies -n \in I(g)$
  - $\forall n \in I(g), k \in \mathbb{Z} \quad g^{n \cdot k} = (g^n)^k = e^k = e \implies n \cdot k \in I(g)$

## Oss

- **Hp**
  - $G$ gruppo
  - $g \in G$
  - $\exists! d \in I(g)_{\ge 0} \mid I(g)=I(d)$
- **Th**
  - $d = 0 \implies o(g) = |\mathbb{Z}| = + \infty$
  - $d>0 \implies d = o(g)$, e questo implica che in $I(g)$ sono presenti tutti i multipli di $o(g)$
- **Dim**
  - $d = 0$
    - sia $f: \mathbb{Z} \rightarrow H(g) : n \rightarrow g^n$
    - $f$ iniettiva $\iff \forall m, n \in \mathbb{Z} \quad g^n =g^m \implies n = m$
    - $m, n \in \mathbb{Z} \mid g^m = g^n \implies g^{-m} \cdot g^m=g^{-m} \cdot g^n \iff e = g^{n - m} \implies n - m \in I(g) = I(d) \implies d \mid n - m$
    - $d = 0 \implies 0 \mid n - m \iff n -m = 0 \iff n = m$, di conseguenza $g^m = g^n \implies n = m$
    - la suriettività di $f$ è data al fatto che l'immagine di $f$ coincide con $H(g)$
    - $f$ biettiva $\implies o(g) := |H(g)| = |\mathbb{Z}| = + \infty$
  - $d \gt 0$
    - $|H(g)| \le d$, ovvero $g$ ha _al massimo $d$_ potenze
        - $d \in I(g)_{\ge 0} \implies g^d = e$
        - $d \gt 0 \implies \forall n \in \mathbb{Z} \quad \exists q, r \in \mathbb{Z} \mid n = dq + r \quad 0 \le r \lt d$ per il teorema della divisione euclidea con il resto, dunque $g^n = g^{dq +r}=(g^d)^q \cdot g^r=e^q \cdot g^r =e \cdot g^r = g^r$
        - $0 \le r \lt d \implies$ ci sono al massimo $d$ valori per $g^r$, e poiché $g^r = g^n$, allora $g$ ha al massimo $d$ potenze
    - $|H(g)| \ge d$, ovvero $g$ ha _al minimo_ $d$ potenze
        - $\forall x, y \in \mathbb{Z} \mid 0 \le x, y \lt d \quad g^x = g^y \iff g^x \cdot g^{-y} = e \iff g^{x - y} = e \iff x- y \in I(g) = I(d) \iff \exists k \in \mathbb{Z} \mid x - y = dk$
        - $0 \le x, y \lt d \implies -d \lt x - y \lt d \implies x - y = 0 \iff x = y$, allora $f:[0,d) \rightarrow H(g)$ è iniettiva, e dunque $g$ ha almeno $d$ potenze
    - di conseguenza, si ottiene che $H(g) = \{g^0, g^1, \ldots, g^{d-1}\} \implies |H(g)|=d$

## Oss

- **Hp**
  - $(G, \cdot)$ gruppo finito
  - $g \in G \mid d := o(g)$ finito
- **Th**
  - $g^{|G|}=e$
- **Dim**
  - $I(d) = I(g)$, allora $d \in I(d) \implies d \in  I(g) \implies g^d = e$
  - $d = o(g) = |H(g)| \bigg\vert |G|$ per il teorema di Lagrange, e dunque $\exists k \in \mathbb{Z} : |G|=d \cdot k \implies g^{|G|} = g^{d \cdot k} = (g^d)^k = e^k = e$

## Oss

- **Hp**
    - $G$ gruppo finito
    - $g \in G$
- **Th**
    - $o(g) = o(g^{-1})$
- **Dim**
    - $H(g) \subseteq H(g^{-1})$
        - $\forall g^n \in H(g) \quad g^n = (g^{-1})^{-n} \implies g^n \in H(g^{-1})$
    - $H(g^{-1}) \subseteq H(g)$
        - $\forall (g^{-1})^n \in H(g^{-1}) \quad (g^{-1})^n=g^{-n} \implies (g^{-1})^n \in H(g)$
    - dunque $H(g) = H(g^n) \implies o(g) = |H(g)| = |H(g^{-1})| = o(g^{-1})$

## Oss

- **Hp**
    - $G$ gruppo finito
    - $g \in G$
    - $k \in \mathbb{Z}$
- **Th**
    - $o(g^k) \mid o(g)$
- **Dim**
    - $\forall (g^k)^n \in H(g^k) \quad (g^k)^n = g^{nk} \implies g^{nk} \in H(g) \implies H(g^k) \subseteq H(g)$
    - $(H(g^k), \cdot) \leqslant (H(g), \cdot)$
        - $(g^k)^0 = g^0 =e \implies e \in H(g)$
        - $\forall (g^k)^x, (g^k)^y \in H(g^k) \quad (g^k)^x \cdot (g^k)^y = g^{kx} \cdot g^{ky} = g^{k(x + y)} = (g^k)^{x + y} \in H(g^k)$
        - $\forall (g^k)^x \in H(g^k) \quad (g^k)^{-x} \in H(g^k)$
    - allora, per il teorema di Lagrange si ha che $o(g^k) = | H(g^k)| \bigg\vert |H(g)| = o(g)$

## Oss

- **Hp**
    - $G$ gruppo finito
    - $g, h \in G \mid gh = hg$
    - $d := \textrm{MCD}(o(g), o(h))$
    - $m := \textrm{mcm}(o(g), o(h))$
- **Th**
    - $\dfrac{m}{d} \mid o(gh) \land o(gh) \mid m$
- **Dim**
    - ⚠️ **manca dimostrazione**

## Oss

- **Hp**
    - $G$ gruppo finito
    - $g, h \in G \mid gh = hg$
    - $d := \textrm{MCD}(o(g), o(h)) = 1$
    - $m := \textrm{mcm}(o(g), o(h))$
- **Th**
    - $o(gh) = o(hg) = m$
- **Dim**
    - per dimostrazione precedente, $d = 1 \implies m \mid o(gh) \land o(gh) \mid m \implies m = o(gh)$

## Def

- **Gruppo ciclico**

> - $G$ gruppo
> - $G$ è detto **ciclico** $\iff \exists g \in G \mid H(g) = G$
>   - ovvero, $G$ è l'insieme delle potenze di $g$

## Oss

- **Hp**
    - $G$ gruppo
    - $g \in G \mid o(g) = |G|$
- **Th**
    - $G$ ciclico
- **Dim**
    - $\left .\begin{array}{l} H(g) \leqslant G \implies H(g) \subseteq G \\ o(g) := |H(g)| = |G| \end{array} \right \} \implies G = H(g) \implies G$ ciclico

## Oss

- **Hp**
    - $G$ gruppo
    - $g \in G$
- **Th**
    - $H(g) \cong \left \{ \begin{array}{ll} \mathbb{Z} & o(g) = + \infty \\ \mathbb{Z}_d & o(g) = d\end{array} \right.$
- **Dim**
    - sia $f: \mathbb{Z} \rightarrow H(g): n \rightarrow g^n$
    - $\forall n, m \in \mathbb{Z} \quad f(n + m) = g^{n + m} = g^n \cdot g^m = f(n) \cdot f(m) \iff f$ morfismo di gruppi tra $(\mathbb{Z}, +)$ e $(H(g), \cdot)$
    - $\ker(f) := \{n \in \mathbb{Z} \mid f(n) = g^n = 1_{H(g)}\} =: I(g)$
    - allora $\mathbb{Z} / I(g) = \mathbb{Z} / \ker(f) \cong \textrm{im}(f)$ per il teorema di isomorfismo
    - $\textrm{im}(f) := \{g^n \in H(g) \mid \exists n \in \mathbb{Z} : f(n) = g^n\} =: H(g)$
    - per dimostrazione precedente $\exists ! d \in I(g)_{\ge 0} \mid I(g) = I(d)$, dove $\left \{ \begin{array}{l} d = 0 \implies o(g) = + \infty \\ d \gt 0 \implies o(g) = d \end{array} \right.$
    - allora $H(g) = \textrm{im}(f) \cong \mathbb{Z}/ \ker(f) = \mathbb{Z}/I(d) = \mathbb{Z}_d$
    - in particolare $d = 0 \implies \mathbb{Z}/I(0) =: \mathbb{Z}_0 \cong H(g)$
    - considerando $\mathbb{Z}_0$, si ha che $\forall x, y \in \mathbb{Z} \quad x \sim_S y \iff y - x \in I(0) \iff \exists k \in \mathbb{Z} \mid y - x = 0 \cdot k = 0 \iff x = y$, dunque $\mathbb{Z}_0$ conterrà esclusivamente classi laterali di singoli elementi, allora $\pi: \mathbb{Z} \rightarrow \mathbb{Z}_0: x \rightarrow [x]$ è biettiva, e per come è definito $+$ in $\mathbb{Z}_0$ è anche morfismo
    - allora poiché $\pi$ isomorfismo, si ha che $\mathbb{Z}_0 \cong \mathbb{Z}$, allora per transitività di $\cong$ si ha che $d = 0 \implies H(g) \cong \mathbb{Z}_0 \land \mathbb{Z}_0 \cong \mathbb{Z} \implies H(g) \cong \mathbb{Z}$
    - allora $H(g) \cong \left \{ \begin{array}{ll} \mathbb{Z} & o(g) = + \infty \\ \mathbb{Z}_d & o(g) = d\end{array} \right.$

## Oss

- **Hp**
    - $G$ gruppo $\big\vert p := |G| \in \mathbb{P}$
- **Th**
    - $G \cong \mathbb{Z}_p$
- **Dim**
    - $\forall g \in G \quad |H(g)| \bigg\vert |G|$ per il teorema di Lagrange
    - $p \in \mathbb{P} \implies |H(g)| = \left \{ \begin{array}{ll} 1 & g = 1_G \\ p & g \neq 1_G \end{array} \right. \implies \forall g \in G - \{1_G\} \quad |H(g)| = p =|G| \implies H(g) \iff G = H(g) \cong \mathbb{Z}_p$ per dimostrazione precedente

## Oss

- **Hp**
    - $G$ gruppo ciclico
- **Th**
    - $G \cong \mathbb{Z}_{|G|}$
- **Dim**
    - $G$ ciclico $\iff \exists g \in G \mid G = H(g) \cong \mathbb{Z}_{o(g)}= \mathbb{Z}_{|G|}$

