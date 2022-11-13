# Ideali

## Def

- \*\*Ideali\*\*
> - $(A, +, \cdot)$ anello
> - $I \subset A$ \*\*ideale\*\* $\iff (I, +) \subset (A, +)$ è un sottogruppo e $A \cdot I \subset I$ e $I \cdot A \subset I$

## Oss

- \*\*Hp\*\*
  - $(A, +, \cdot)$ anello
  - $a \in \mathbb{Z}$
  - $I(a) := \{ax \mid x \in A\}$
- \*\*Th\*\*
  - $I(a)$ è un ideale, e prende il nome di \_ideale di $A$ generato da $a \in A$\_
- \*\*Dim\*\*
  - $(I(a), + ) \subset(A, +)$ sottogruppo
    -  $0$ multiplo di $a \implies 0 \in I(a)$
    - $\forall ax, ay \in I(a) \quad ax + ay = a(x + y) \implies ax + ay \in I(a)$ per definizione
    - $\forall ax \in I(a) \quad a(-x) \in I(a)$ poiché $-x$ è un multiplo di $a$, e $a(-x) = -ax \in I(a)$, che corrisponde all'opposto di $ax$ rispetto a $+$
  - $A \cdot I \subset I \iff \forall x \in I(a), b \in A \quad bx \in I(a)$
    - $x \in I(a) \iff \exists c \in A \mid x = ac \implies bx = b (ac) = a(bc)$, poiché il prodotto è commutativo, e dunque $bx \in I(a)$ per definizione
  - poiché il prodotto è commutativo, $A \cdot I \subset I \implies I \cdot A \subset I$

## Oss

- \*\*Hp\*\*
  - $a, b \in \mathbb{Z} - \{0\}$
- \*\*Th\*\*
  - $I(a)=I(b) \iff a=\pm b$
- \*\*Dim\*\*
    - $a=\pm b \implies I(a)=I(b)$
      - $a = b \implies I(a)$ e $I(b)$ coincidono
      - $a = -b \implies I(-b) = \{ k(-b) \mid k \in \mathbb{Z}\} = \{(-k)b \mid (-k) \in \mathbb{Z}\} = I(b) = I(-b)=I(a)$
    - $I(a) = I(b) \implies a = \pm b$
      - $I(a) = I(b) \iff a \in I(b) \land b \in I(a) \implies \exists p, q \in \mathbb{Z} \mid a = pb \wedge b = qa$, di conseguenza $b = q (pb) \implies b = (qp)b \implies pq = 1 \iff p = q = 1 \lor p = q = -1 \implies a = \pm b$

## Oss

- \*\*Hp\*\*
  - $(A, +, \cdot)$ anello
  - $a\_1, \ldots, a\_n \in\mathbb{Z}$
  - $I(a\_1, \ldots, a\_n) := \{ a\_1b\_1 + \ldots +a\_nb\_n \mid b\_1, \ldots, b\_n \in A\}$
- \*\*Th\*\*
  - $I(a\_1, \ldots, a\_n)$ è un ideale, e prende il nome di \_ideale di $A$ generato dagli $a\_1, \ldots, a\_n \in A$\_
- \*\*Dim\*\*
  - $(I(a\_1, \ldots, a\_n) , +) \subset (A, +)$ sottogruppo
    - $0 = a\_1 \cdot 0  + \ldots + a\_n \cdot 0 \in I(a\_1, \ldots a\_n)$, dunque $0$ è l'elemento neutro
    - $\forall x, y \in I(a\_1, \ldots, a\_n) \quad x = a\_1b\_1 + \ldots +a\_nb\_n \land y = a\_1c\_1 + \ldots+ a\_nc\_n \implies x+ y = a\_1b\_1 + \ldots + a\_nb\_n + a\_1c\_1 + \ldots +a\_nc\_n$, che è possibile riscrivere come $x + y = a\_1(b\_1 + c\_1) + \ldots + a\_n(b\_n + c\_n)$, che per definizione implica che $x + y \in I(a\_1, \ldots, a\_n)$
    - $\forall x \in I(a\_1, \ldots, a\_n) \quad x = a\_1b\_1 + \ldots + a\_nb\_n \iff -x = -a\_1b\_1 - \ldots - a\_nb\_n \iff -x = a\_1(-b\_1) + \ldots + a\_n(-b\_n)$, che per definizione implica che $-x \in I(a\_1, \ldots, a\_n)$
  - $\forall x \in I(a\_1, \ldots, a\_n), c \in A \quad x = a\_1b\_1 + \ldots + a\_nb\_n \implies c \cdot x = a\_1 (b\_1c)+ \ldots + a\_n(b\_nc)$, che per definizione implica che $cx \in I(a\_1, \ldots, a\_n)$

## Def

- \*\*Congruenza modulo di un ideale\*\*
> - $(A, +, \cdot)$ anello
> - $I \subset A$ ideale
> - per definizione, $I$ ideale $\implies(I, +) \subset (A, +)$ sottogruppo, dunque ha senso definire $A/I$, e infatti $I$ induce una relazione di equivalenza su $A$ detta \*\*congruenza modulo $I$\*\*, dove $\forall a, b \in A \quad a \equiv b \ (\bmod I) \iff b - a \in I$
> - $b -a \in I \iff  (-a) + b \in I$, di conseguenza questa congruenza coincide con la classe laterale sinistra di $(A, +)$

## Oss

- \*\*Hp\*\*
  - $(A, +, \cdot)$ anello
  - $+: A/I \times A/I \rightarrow A/I$
  - $\cdot : A/I \times A/I \rightarrow A/I$
- \*\*Th\*\*
  - $(A/I, +, \cdot)$ è un anello
- \*\*Dim\*\*
  - $(A/I, +)$ è un gruppo abeliano
    - $+$ è un'operazione ben definita per dimostrazione precedente, dunque le proprietà di gruppo abeliano sono rispettate per come l'operazione è definita
  - $(A/I, \cdot)$ è monoide
    - $\cdot$ è un'operazione ben definita per dimostrazione analoga, dunque le proprietà di monoide sono rispettate per come l'operazione è definita
  - proprietà distributiva
    - per come $+$ e $\cdot$ sono definite, segue che $\forall [x],[y],[z] \in A/I \quad [x]([y]+[z])=[x][y+z]=[x(y+z)]=[x y+x z]=[x y]+[x z] =[x][y]+[x][z]$

## Oss

- \*\*Hp\*\*
  - $I \subset \mathbb{Z}$ ideale
- \*\*Th\*\*
  -  $\exists ! \ d \in \mathbb{Z}\_{\ge 0} \mid I = I(d)$, o equivalentemente, $\mathbb{Z}$ è un anello a ideali principali
- \*\*Dim\*\*
  - \*esistenza\*
      - $I = \{0\} \implies I = I(0)$ poiché i multipli di $0$ sono tutti pari a $0$
      - se invece $I \neq \{0\} \implies I \cap \mathbb{Z}\_{>0} \neq \varnothing$, dunque $I$ contiene almeno un numero non nullo, in particolare positivo
        - è possibile considerare solo il caso dei positivi in quanto$\forall x \in I - \{0\} \quad x < 0 \iff (-x)>0$, e $(-x) \in I$ per definizione di $I$, dunque per valori negativi è sufficiente considerare il loro opposto, sicuramente contenuto in $I$
    - dunque, ha senso considerare $d:=\min(I \cap \mathbb{Z}\_{\gt 0})$
    - $I(d)=I \implies I(d) \subset I \wedge I \subset I(d)$
      - $I(d) \subset I$
        - $\forall x \in I(d) \quad \exists y \in \mathbb{Z} \mid x = dy$ per definizione
        - $\mathbb{Z}$ è anello commutativo
        - $I \subset \mathbb{Z}$ ideale, e dunque $I \cdot \mathbb{Z} \subset I$ 
        - $d := \min(I \cap \mathbb{Z}\_{\gt 0}) \implies d \in I \implies y \in \mathbb{Z} \land d \in I \implies dy \in I \implies x \in I \implies I(d) \subset I$
      - $I \subset I(d)$
        - $d := \min(I \cap \mathbb{Z}\_{\gt 0}) \implies d \neq 0$
        - per il teorema della divisione euclidea con il resto $\forall x \in I \quad \exists ! q,r \in \mathbb{Z} \mid x=d q+r \quad 0 \leq r<d$
          - $r = 0 \iff x = dq \implies x \in I(d)$ per definizione, dunque $I \subset I(d)$
          - ipotizzando $r \neq 0$
            - $dq \in I(d) \implies dq \in I$ per dimostrazione precedente
            - quindi $x = dq + r \implies r = x - dq \in I$ poiché $I$ è un ideale
            - $r \neq 0 \implies r \in I \cap \mathbb{Z}\_{\gt 0}$
            - per definizione, $0 \le r \lt d$, ma $d:=\min(I \cap \mathbb{Z}\_{\gt 0})$, quindi il minimo numero che $d$ può assumere è $1$, e poiché $r < d \implies r = 0$ necessariamente, dunque segue la dimostrazione precedente

  - \*unicità\*
      - l'unicità deriva dal fatto che $d:=\min(I \cap \mathbb{Z}\_{\gt 0})$, e dunque nella dimostrazione $d > 0$, ma vale il ragionamento analogo per $d < 0$ considerando $I(-d)$, in quanto $I(d) = I(-d)$ per dimostrazione precedente
  - quindi, ogni ideale in $\mathbb{Z}$ è generato dall'insieme dei multipli di un certo $d \ge 0$, che esiste sempre ed è unico, e di conseguenza $\mathbb{Z}$ è un anello ad ideali principali

## Oss

- \*\*Hp\*\*
  - $a\_{1}, \ldots a\_{n} \in \mathbb{Z}$
- \*\*Th\*\*
  - $\exists ! d=\textrm{MCD}(a\_{1}, \ldots, a\_{n})  \mid I\left(a\_{1}, \ldots a\_{n}\right)=I(d)$
- \*\*Dim\*\*
    - ⚠️ \*\*MANCA DIMOSTRAZIONE\*\*
        - $\forall x \in I(a\_1, \cdots, a\_n), \ d \mid x$, dunque $d$ è \*divisore comune\*
        - $d$ è il \_massimo tra i divisori comuni\_

## Oss

- \*\*Hp\*\*
  - $a\_1, \ldots, a\_n \in \mathbb{Z}$
  - $d := \textrm{MCD}(a\_1, \ldots, a\_n)$
- \*\*Th\*\*
  - $\exists x\_1, \ldots, x\_n \in \mathbb{Z} \mid a\_1 x\_1 + \ldots + a\_nx\_n=d$, che prende il nome di \_identità di Bézout\_
- \*\*Dim\*\*
  - per dimostrazione precedente, $I\left(a\_{1}, \ldots a\_{n}\right)=I(d)$, quindi $d \in I(a\_1, \ldots, a\_n) \implies \exists x\_1, \ldots, x\_n \in \mathbb{Z} \mid a\_1x\_1 + \ldots + a\_n x\_n = d$

## Oss

- ⚠️ \*\*MANCA DIMOSTRAZIONE SISTEMA DI IDENTITÀ DI BÉZOUT\*\*

\*\*\*\*

# Operazioni sugli ideali

## Def

- \*\*$+$ tra ideali\*\*
> - $(A, +, \cdot)$ anello commutativo
> - $I, J \subset A$ ideali
> - $I + J = \{i + j \mid \forall i \in I, j \in J\}$

## Oss

- \*\*Hp\*\*
  - $(A, +, \cdot)$ anello commutativo
  - $I, J \subset A$ ideali
- \*\*Th\*\*
  - $I + J$ è un ideale
- \*\*Dim\*\*
  - $0 \in I, 0 \in J, 0+0=0 \implies 0 \in I + J$ per definizione
  - la chiusura rispetto a $+$ deve implicare che $\forall i\_1, i\_2 \in I, j\_1, j\_2 \in J \quad (i\_1 + j\_1) + (i\_2 + j\_2) \in I + J$
    - poiché $(i\_1 + j\_1) + (i\_2 + j\_2) = (i\_1 + i\_2) + (j\_1 + j\_2)$, e $i\_1 + i\_2 \in I, j\_1 + j\_2 \in J \implies (i\_1 + i\_2) + (j\_1 + j\_2) \in I + J$ per definizione di $I + J$
  - $\forall i \in I, j \in J \quad i + j \in I + J$, l'opposto rispetto a $+$ di $i + j$ è $- (i + j) = (-i) + (-j)$, e $\forall i \in I, j \in J \quad -i \in I, -j \in J  \implies (-i) + (-j) \in I + J$ per definizione
  - $A \cdot I \subset I \implies \forall a \in A, i \in I, j \in J \quad a(i + j) \in I + J$
    - $i + j \in I + J$ per definizione, e $a(i + j) = ai + aj$, e $ai \in I, aj \in J$ per definizione, quindi $ai + aj \in I + J$ per definizione

## Def

- \*\*$\cap$ tra ideali\*\*
> - $(A, +, \cdot)$ anello commutativo
> - $I, J \subset A$ ideali
> - $I \cap J = \{x \in I \land x \in J\}$

## Oss

- \*\*Hp\*\*
  - $(A, +, \cdot)$ anello commutativo
  - $I, J \subset A$ ideali
- \*\*Th\*\*
  - $I \cap J$ è un ideale
- \*\*Dim\*\*
  - ⚠️ \*\*MANCA DIMOSTRAZIONE\*\*

## Def

- \*\*$\cdot$ tra ideali\*\*
> - $(A, +, \cdot)$ anello commutativo
> - $I, J \subset A$ ideali
> - $I \cdot J = \{i\_1 j\_1 + \ldots + i\_k j\_k \mid k \ge  1, \forall i\_1 , \ldots , i\_k \in I, j\_1 , \ldots , j\_k \in J \}$

## Oss

- \*\*Hp\*\*
  - $(A, +, \cdot)$ anello commutativo
  - $I, J \subset A$ ideali
- \*\*Th\*\*
  - $I \cdot J$ è un ideale
- \*\*Dim\*\*
  - ⚠️ \*\*MANCA DIMOSTRAZIONE\*\*

## Oss

- \*\*Hp\*\*
  - $a, b \in \mathbb{Z}$
  - $d:= \textrm{MCD}(a, b)$
- \*\*Th\*\*
  - $I(a) + I(b) = I(d)$
- \*\*Dim\*\*
   - per dimostrazione precedente $I(a)$ e $I(b)$ sono ideali, e poiché la somma tra ideali è ben definita, allora $I(a)+I(b)=\{i+j \mid i \in I(a), j \in I(b) \}$
   - $i \in I(a) \implies \exists x \in \mathbb{Z} \mid i = ax$ e $j \in I(b) \implies \exists y \in \mathbb{Z} \mid j = by$
   - quindi $i + j = ax + by \implies$ $I(a)+I(b)=\{a x+b y \mid x, y \in \mathbb{Z}\} = I(a, b)$ per definizione
   - in particolare, per dimostrazione precedente, $I(a, b) = I(d)$

## Oss

- \*\*Hp\*\*
  - $a, b \in \mathbb{Z}$
- \*\*Th\*\*
  - $I(a) \cdot I(b)=I(a \cdot b)$
- \*\*Dim\*\*
  - $x \in I(a) \cdot I(b) \implies x \in I(a \cdot b)$
    - per dimostrazione precedente $I(a)$ e $I(b)$ sono ideali, e poiché il prodotto tra ideali è ben definito, allora $x \in I(a) \cdot I(b) \implies x = i\_1 j\_1 + \ldots + i\_k j\_k$ con $i\_1 , \ldots , i\_k \in I(a)$ e $j\_1 , \ldots , j\_k \in I(b)$
    - per definizione, $i \in I(a) \implies \exists x \in \mathbb{Z} \mid i = ax$, e dunque $i\_1, \ldots, i\_k = ax\_1, \ldots, ax\_k$ con $x\_1, \ldots, x\_k \in \mathbb{Z}$
    - analogamente $j\_1, \ldots, j\_k = by\_1, \ldots, by\_k$ con $y\_1, \ldots, y\_k \in \mathbb{Z}$
    - segue che $x = (ax\_1)(by\_1),+\ldots+ (ax\_k)(by\_k) = ab\cdot(x\_1y\_1+ \ldots+ x\_ky\_k)$
    - poiché $(x\_1y\_1+ \ldots+ x\_ky\_k) \in \mathbb{Z}$, segue che $ab \mid x \implies x \in I(a \cdot b)$
  - $x \in I(a \cdot b)  \implies x \in I(a) \cdot I(b)$
    - $x \in I(a \cdot b) \implies \exists k \in \mathbb{Z} \mid x = ab \cdot k$
    - $x = abk$, ma $a \in I(a) \land bk \in I(b) \implies x \in I(a) \cdot I(b)$
   
## Minimo comune multiplo

- $\displaystyle{\forall a\_{1}, \ldots, a\_{n} \in \mathbb{Z}  \quad \exists ! m  \in \mathbb{N} \mid m:= \textrm{mcm}(a\_1, \ldots, a\_n) : I(m) = I(a\_1) \cap \ldots \cap I(a\_n) = \bigcap\_{i=1}^{n}{I(a\_i)}}$

## Esempi

- $\forall g \in G$ gruppo, $I(g):=\left\{n \in \mathbb{Z} \mid g^{n}=e\right\}$ è un \*\*ideale\*\* $(I(g), +) \subset (\mathbb{Z}, +)$
  - $0 \in \mathbb{Z}, g^{0}=e \implies 0 \in I(g)$
  - $m, n \in I(g) \Rightarrow g^{m}=g^{n}=e \implies g^{m} \cdot g^{n}= g^{m + n} = e \cdot e = e \implies g^{m +n} \in I(g)$ per definizoine di $I(g) \implies I(g) + I(g) \subset I(g)$, poiché $\forall m, n \in \mathbb{Z} \quad m + n \in \mathbb{Z}$
  - $n \in I(g) \implies (g^n)^{-1} = e ^{-1 } = g^{-n} =e \implies -n \in I(g)$, poiché $\forall n \in \mathbb{Z} \quad -n \in \mathbb{Z}$
  - $n \in I(g), k \in \mathbb{Z} \implies g^{k \cdot n} = (g^n)^k = e^k = e \implies n \cdot k \in I(g)$

