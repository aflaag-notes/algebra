# Gruppi

- $S$ insieme e $m: S \times S \rightarrow S$
  - $(S, m)$ \*\*semigruppo\*\* $\iff$ vale la \*\*proprietà associativa\*\* in $m$ su $S$
    - $m(x, m(y, z))=m(m(x, y),z) \quad \forall x, y, z \in S$
  - $(S, m)$ \*\*monoide\*\* $\iff$ è un semigruppo in cui \*\*esiste l'elemento neutro\*\* rispetto a $m$
    - $\exists e  \mid m(x, e) = m(e, x) = x \quad \forall x \in S$
    - se esiste, $e$ è unico
        - per assurdo, $\exists e\_1, e\_2 \mid e\_1 \neq e\_2$ elementi neutri, allora $\left.\begin{array}{l}m\left(x, e\_{1}\right)=m\left(e\_{1}, x\right)=x \\ m\left(x, e\_{2}\right)=m\left(e\_{2}, x\right)=x\end{array}\right\} \Rightarrow m\left(e\_{1}, x\right)=m\left(e\_{2}, x\right) \implies e\_1=e\_2$ necessariamente

  - $(S, m)$ \*\*gruppo\*\* $\iff$ è un monoide in cui \*\*esiste l'inverso\*\* per ogni elemento di $S$
    - $\exists x^{-1} \mid m(x, x^{-1}) =m(x^{-1}, x) =e \quad \forall x \in S$
    - se esiste, $x^{-1}$ è unico
      - ⚠️ \*\*MANCA DIMOSTRAZIONE\*\*
  - $(S, m)$ \*\*gruppo abeliano\*\* $\iff$ è un gruppo in cui vale la \*\*proprietà commutativa\*\* in $m$ su $S$
    - $m(x, y) = m(y, x) \quad \forall x, y \in S$

## Esempi

- $X, Y$ insiemi, $Y^X = \{f \mid f:X \rightarrow Y\}$
  - $X, Y$ finiti $\Rightarrow \left| Y^X \right| = \left| Y \right| ^ {|X|}$
      - ⚠️ \*\*MANCA DIMOSTRAZIONE\*\*
  - $(X^X, \circ)$ è \*\*monoide\*\*
    - $(f \circ g) \circ h=f \circ(g \circ h)$
    - $\forall X, \ \exists \textrm{id}\_X \mid \textrm{id}\_X : X \rightarrow X : x \rightarrow x$, che costituisce dunque l'elemento neutro, mappando ogni elemento in sé stesso
  - $S\_X = \{f \mid f : X \rightarrow Y \ \textrm{biiettiva}\}$ è detto \*\*gruppo simmetrico di $X$\*\*
    - $|S\_X|$ = $|X|!$
    - $(S\_X, \circ)$ è un \*\*gruppo\*\*, non commutativo se $|X| \ge 3$

\*\*\*\*

# Anelli

- $A$ insieme
- $+: A \times A \implies A$
- $\*: A \times A \implies A$

- $(A, +, \*)$ anello $\iff$
  - $(A, +)$ \*\*gruppo abeliano\*\*
  - $(A, \*)$ \*\*monoide\*\*
  - vale la \*\*proprietà distributiva\*\* della forma $a\*(b + c) = a \* b + a \* c$

- $a \* b=b \* a \quad \forall a, b \in A \implies  \rm (A, \*, +)$ è un \*\*anello commutativo\*\*

- $\exists x^{-1} \quad \forall x \in A \mid x \* x^{-1}=x^{-1} \* x=e  \implies  (A, +, \*)$ è un \*\*campo\*\*

## Esempi

- $(\mathbb{Z}, +, \cdot)$ è un \*\*anello commutativo\*\*
- $(\mathbb{C}, +, \cdot)$ è un \*\*campo\*\*
- ⚠️ \*\*MANCA DIMOSTRAZIONE\*\* polinomi a coefficienti in $A$

\*\*\*\*

# Sottogruppi

- $H \subset G$ \*\*sottogruppo\*\* di un gruppo $(G, \*)\iff$
    - $\exists e \in H \mid e$ è l'\*\*elemento neutro\*\*
    - $H$ è \*\*chiuso rispetto all'operazione $\*$\*\*
        - $\forall x, y \in H, \ x \* y \in H$
    -  $H$ è \*\*chiuso rispetto agli inversi\*\*
        -  $\forall x \in H, \ \exists x^{-1} \in H$
     
## Esempi

- $(\mathbb{Z},+) \subset(\mathbb{Q},+) \subset(\mathbb{R},+) \subset(\mathbb{C},+)$ tutti sottogruppi

\*\*\*\*

# Ordine

- $\forall g \in G$ gruppo, $H(g):=\left\{g^{n} \mid n \in \mathbb{Z}\right\}$ è un \*\*sottogruppo\*\* $(H(g), \cdot) \subset (G, \cdot)$ 
  - $e=g^{0} \implies e \in H(g)$
  - $g^m \cdot g^n = g^{m + n} \in H(g)$ per definizione di $H(g)$, quindi $H(g) \cdot Hg(g) \subset H(g)$, poiché $\forall m, n \in \mathbb{Z} \quad m + n \in \mathbb{Z}$
  - $(g^n)^{-1} = g^{-n} \in H(g)$ per definizione di $H(g)$, poiché $\forall n \in \mathbb{Z} \quad -n \in \mathbb{Z}$
- $o(g) :=  | H(g) |$ è detto \*\*ordine di $g \in G$\*\*
- $\exists! d \geq 0 \mid I(g)=I(d)$
  - $d = 0 \implies o(g) = |H(g)| = |\mathbb{Z}|$, dunque infinito
  - $d>0 \implies d = o(g)$
 - ⚠️ \*\*MANCA DIMOSTRAZIONE\*\*


