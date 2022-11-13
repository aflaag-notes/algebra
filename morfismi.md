# Morfismi

## Def 

- \*\*Morfismo di gruppi\*\*
> - $(G, \cdot), (H, \cdot)$ gruppi
> - $f: G \rightarrow H$
> - $f$ \*\*morfismo di gruppi\*\* $\iff f(x\cdot y)=f(x)\cdot f(y) \quad \forall x, y \in G$

- \*\*Morfismo di anelli\*\*
> - $(A, +, \cdot), (B, +, \cdot)$ anelli
> - $f: A \rightarrow B$
> - $f$ \*\*morfismo di anelli\*\* $\iff f(x+ y) = f(x) + f(y)$ e $f(x \cdot y) = f(x) \cdot f(y) \quad \forall x, y \in A$
>     -   la stessa definizione si applica per morfismo di campi

## Oss

- **Hp**
  - $(G, \cdot), (H, \cdot)$ gruppi
  - $1\_G$ neutro per $G$
  - $1\_H$ neutro per $H$
  - $f: G \rightarrow H$ morfismo
- **Th**
  - $f(1\_G) = 1\_H$
- **Dim**
  - $\forall g \in G \quad f(g) = f(1\_G \cdot g) = f(1\_G) \cdot f(g)$ poiché $f$ morfismo
  - quindi $f(g) = f(1\_G) \cdot f(g) \implies f(g) \cdot f(g)^{-1} = f(1\_G) \cdot f(g) \cdot f(g)^{-1} \implies 1\_H = f(1\_G) \cdot 1\_H \implies 1\_H = f(1\_G)$ (poiché $f(g), f(g)^{-1} \in H$ per definizione di $f$)
 
## Oss

- **Hp**
  - $(G, \cdot), (H, \cdot)$ gruppi
  - $1\_G$ neutro per $G$
  - $1\_H$ neutro per $H$
  - $f: G \rightarrow H$ morfismo
- **Th**
  - $f(g^{-1}) = f(g)^{-1}$
- **Dim**
  - per dimostrazione precedente, $1\_H = f(1\_G) = f(g \cdot g^{-1})=f(g) \cdot f(g^{-1}) \implies 1\_H = f(g) \cdot f(g^{-1}) \implies f(g)^{-1} = f(g^{-1})$

\*\*\*\*

# Isomorfismi

## Def

- \*\*Isomorfismo\*\*
> - $f$ isomorfismo $\iff f$ morfismo e $f$ biiettiva

## Oss

- **Hp**
  - $f: G \rightarrow H$ isomorfismo
- **Th**
  - $f ^{-1}: H \rightarrow G$ morfismo
- **Dim**
  - $\forall g \in G, h \in H \quad \exists !f^{-1} \mid \left\{\begin{array}{c}f^{-1}(f(g))=g \\ f\left(f^{-1}(h)\right)=h\end{array}\right.$
  - $\forall h, h^{\prime} \in H \quad f^{-1}\left(h h^{\prime}\right)=f^{-1}(h) \cdot f^{-1}\left(h^{\prime}\right) \iff f\left(f^{-1}\left(h h^{\prime})\right)=f(f^{-1}(h)\cdot f^{-1}(h^\prime)) = f(f^{-1}(h))\cdot f(f^{-1}(h^\prime))\right.$, dunque $hh^\prime =  f(f^{-1}(h))\cdot f(f^{-1}(h^\prime)) = hh^\prime$ ⚠️  \*\*RIVEDI\*\*

## Ex

- **Hp**
  - $z \in \mathbb{C} \mid z^n = 1$ sono le radici $n$ -esime di $1$
  - $\zeta := e^{i \frac{2 \pi}{n}}$
  - $H := \{\zeta ^0, \zeta^1, \zeta^k, \ldots, \zeta^{n-1}\}$ è l'insieme delle radici $n$-esime di $1$
- **Th**
  - $(H, \cdot) \subset (\mathbb{C}-\{0\}, \cdot)$ è un sottogruppo
- **Dim**
  - $\zeta ^0 = 1 \implies 1 \in H$
  - $z, w \in H \iff z^n=w^n = 1$, allora $1 = z^n \cdot w^n = (z \cdot w)^n = 1 \implies z \cdot w \in H$ per definizione di $H$
  - $z^n = 1 \implies \dfrac{1}{z^n} = 1 \iff (z^{-1})^n = 1 \implies z^{-1} \in H$ per definizione di $H$

## Ex

- **Hp**
  - $f: \mathbb{Z}\_n \rightarrow H : [k] \rightarrow \zeta^k$
- **Th**
  - $f$ morfismo di gruppi $(\mathbb{Z}\_n , +)$ e $(H, \cdot)$
- **Dim**
  - $f$ è biiettiva per costruzione di $\mathbb{Z}\_n := \{[0], [1], \ldots, [n - 1]\}$ e $H := \{\zeta ^0, \zeta^1, \ldots, \zeta^{n-1}\}$
  - $f$ morfismo
    - $f([i]+[j])=f([i]) \cdot f([j])$
      - $[i] + [j] = [k]$ per un certo $k \in \mathbb{Z}\_n \implies \exists h \in \mathbb{Z} \mid i + j = k + hn$
      - $f([i]+[j])= f([k]) = \zeta^k$
      - $f([i]) \cdot f([j]) = \zeta^i \cdot \zeta ^j = \zeta ^{i + j}$, ma per osservazione precedente $\zeta^{i + j} = \zeta^{k + nh} = \zeta^{k} \cdot (\zeta^n)^h$
      - $\zeta^n = 1$ per definzione di $\zeta \implies$ entrambe i membri dell'equazione sono pari a $\zeta^k$

## Ex

- **Hp**
  - $(G, \cdot)$ gruppo
  - $f: \mathbb{Z} \rightarrow G: n \rightarrow g^n$ per qualche $g \in G$
- **Th**
  - $f$ morfismo di gruppi $(\mathbb{Z}, +)$ e $(G, \cdot)$
- **Dim**
  - $f(n + m ) = g^{n + m} = g^m \cdot g^n = f(m) \cdot f(n) \implies f$ morfismo

## Oss

- **Hp**
  - ⚠️ \*\*MANCA UN TEOREMA CHE NON HO CAPITO NIENTE\*\*
- **Th**
- **Dim**

## Ex

- **Hp**
  - $f: \mathbb{Z} \rightarrow \mathbb{Z}\_n : k \rightarrow [k]$
- **Th**
  - $f$ morfismo di anelli $\left(\mathbb{Z},+, \cdot\right)$ e $\left(\mathbb{Z}\_{n},+, \cdot\right)$
- **Dim**
  - per come le operazioni $+$ e $\cdot$ sono state definite, $f([x+y])=f([x])+f([y])$ e
$f([x \cdot y])=f([x]) \cdot f([y])$

## Ex

- **Hp**
  - $n \mid m$
  - $f : \mathbb{Z}\_m \rightarrow \mathbb{Z}\_n: x \ (\bmod m) \rightarrow x \ (\bmod n)$
- **Th**
  - $f$ morfismo di anelli $\left(\mathbb{Z}\_{m},+, \cdot\right)$ e $\left(\mathbb{Z}\_{n},+, \cdot\right)$
- **Dim**
  - $x \ (\bmod m) + y \ (\bmod m) = x +y \ (\bmod m)$
  - $f(x + y \ (\bmod m)) = x +y \ (\bmod n)$
  - $x +y \ (\bmod n) = x \ (\bmod n)+ y \ (\bmod n)$
  - il ragionamento è analogo per l'operazione $\cdot$, e dunque segue la tesi
 
## Ex

- **Hp**
  - $(G, \cdot)$ gruppo
  - $\textrm{Bij}(G) := \{f \mid f: G \rightarrow G\}$
  - $\textrm{L}\_g \in G \mid \textrm{L}\_g: G \rightarrow G:g \rightarrow gh$
  - $f: G \rightarrow \textrm{Bij}(G): g \rightarrow \textrm{L}\_g$
- **Th**
  - $f$ morfismo di gruppi $(\textrm{Bij}(G), \circ)$ e $(G, \cdot)$
- **Dim**
  - \*\*⚠️ MANCA DIMOSTRAZIONE\*\*

## Ex

- **Hp**
  - $G$ gruppo
  - $f: G \rightarrow G : h \rightarrow g \cdot h \cdot g^{-1}$ per qualche $g \in G$
- **Th**
  - $f$ morfismo di gruppi $(G, \cdot)$ e $(G, \cdot)$
- **Dim**
  - $\forall h, h^\prime \in G \quad f(h) \cdot f\left(h^{\prime}\right)=\left(g h g^{-1}\right)\cdot \left(g h^{\prime} g^{-1}\right)=gh(g^{-1} \cdot g)h^\prime g^{-1}=g h h^{\prime} g^{-1}=f\left(h h^{\prime})\right.$

\*\*\*\*

# Kernel e Immagine

## Def

- \*\*Kernel e Immagine di gruppi\*\*
> - $G, H$ gruppi
> - $f: G \rightarrow H$ morfismo
> - $\textrm{Ker}(f):=\{g \in G \mid f(g) = 1\_H\}$
> - $\textrm{Im}(f):=\{h \in H \mid \exists g \in G : f(g) = h\}$

 -  \*\*Kernel e Immagine di anelli\*\*
> - $A, B$ gruppi
> - $f: A \rightarrow B$ morfismo
> - $\textrm{Ker}(f):=\{a \in A \mid f(a)= 0\_B\}$
> - $\textrm{Im}(f):=\{b \in B \mid \exists a \in A : f(a) = b\}$

## Oss

- **Hp**
  - $G, H$ gruppi
  - $f: G \rightarrow H$ morfismo
- **Th**
  - $\textrm{Ker}(f) \subset G$ è sottogruppo
- **Dim**
  - per dimostrazione precedente, $f(1\_G) = 1\_H \implies 1\_G \in \textrm{Ker}(f)$ per definizione
  - $x, y \in \textrm{Ker}(f) \implies f(x) = f(y ) = 1\_H$ per definizione, dunque $f(x) \cdot f(y) = 1\_H \cdot 1\_H = 1\_H$, e $f(x) \cdot f(y) = f(x \cdot y) = 1\_H$ perché $f$ morfismo, quindi $x \cdot y \in \textrm{Ker}(f)$ per definizione
  - $g \in \textrm{Ker}(f) \implies f(g) =1\_H \implies f(g)^{-1} = 1\_H^{-1} = 1\_H$, ma poiché per dimostrazione precedente $f(g)^{-1} = f(g^{-1}) \implies f(g^{-1})= 1\_H \implies g^{-1} \in \textrm{Ker}(f)$ per definizione
 
## Oss

- **Hp**
  - $G, H$ gruppi
  - $f: G \rightarrow H$ morfismo
- **Th**
  - $\textrm{Im}(f) \subset G$ è sottogruppo
- **Dim**
  - per dimostrazione precedente $f(1\_G)= 1\_H \implies 1\_H \in \textrm{Im}(f)$ per definizione
  - $x, y \in \textrm{Im}(f) \implies \exists g, g^\prime \in G \mid x = f(g) \land y = f(g^\prime) \implies x \cdot y = f(g) \cdot f(g^\prime) = f(g\cdot g^\prime)$ perché $f$ morfismo, quindi $x \cdot y \in \textrm{Im}(f)$ per definizione
  - $x \in \textrm{Im}(f) \implies \exists g \in G \mid f(g) = x \implies x^{-1} = f(g)^{-1} = f(g^{-1})$ per dimostrazione precedente, quindi $x ^{-1} \in \textrm{Im}(f)$ per definizione
 
## Oss

- **Hp**
  - $G, H$ gruppi
  - $f: G \rightarrow H$ morfismo
- **Th**
  - $f$ iniettiva $\iff \textrm{Ker}(f) = \{1\_G\}$
- **Dim**
  - $f$ iniettiva $\implies \textrm{Ker}(f) = \{1\_G\}$
    - $f(1\_G) = 1\_H$ per dimostrazione precedente, dunque $1\_G \in \textrm{Ker}(f)$ per definizione
    - $f$ iniettiva $\implies \nexists x, y \in G \mid x \neq y \implies f(x) = f(y)$, di conseguenza è unico $1\_G \in G \mid f(1\_G) = 1\_H$, dunque $\textrm{Ker}(f)$ conterrà esclusivamente $1\_G$ per definizione
  - $f$ iniettiva $\impliedby \textrm{Ker}(f) = \{1\_G\}$
    - $\forall g, g^\prime \in G \quad f(g) = f(g^\prime) \iff f(g)^{-1} \cdot f(g) = f(g)^{-1} \cdot f(g^\prime) \iff 1\_H = f(g) \cdot f(g^\prime) = f(g \cdot g^\prime)$
    - $\textrm{Ker}(f) = \{1\_G\} \implies f(1\_G)=1\_H$ per definizione, allora $f(g\cdot g^\prime) = 1\_H \implies g \cdot g^\prime = 1\_G$ necessariamente, e $g \cdot g^\prime = 1\_G \iff g= g^\prime \implies f(g) = f(g^\prime) \implies g = g^\prime \implies f$ iniettiva

## Oss

- **Hp**
  - $A, B$ anelli
  - $f: A \rightarrow B$ morfismo di anelli
- **Th**
  - $\textrm{Ker}(f)$ ideale
- **Dim**
  - $(\textrm{Ker}(f), +) \subset (A, +)$ sottogruppo per dimostrazione precedente
  - per analogia con dimostrazione precedente, $f(0\_A) = 0\_B$
  - $x \in \textrm{Ker}(f) \implies f(x) = 0\_B$ per definizione, quindi $\forall x \in \textrm{Ker}(f), y \in A \quad f(x \cdot y )= f(x) \cdot f(y) )= 0\_B \cdot f(y) = 0\_B \implies x \cdot y \in \textrm{Ker}(f)$ per definizione, quindi $\textrm{Ker}(f) \cdot A \subset \textrm{Ker}(f)$

## Oss

- **Hp**
  - $A, B$ anelli
  - $f: A \rightarrow B$ morfismo di anelli
- **Th**
  - $\textrm{Im}(f)$ sottoanello
- **Dim**
  - $(\textrm{Im}(f), +) \subset (A, +)$ sottogruppo per dimostrazione precedente
  - $x, y \in \textrm{Im}(f) \implies \exists a, a^\prime \mid x = f(a) \land y = f(a^\prime) \implies x \cdot y = f(a) \cdot f(a^\prime) = f(a\cdot a^\prime)$ perche $f$ morfismo, quindi $\exists a \cdot a^\prime \mid x \cdot y = f(a \cdot a^\prime) \implies x\cdot y \in \textrm{Im}(f) \implies \textrm{Im}(f) \cdot \textrm{Im}(f) \subset \textrm{Im}(f)$
 
## Oss

- **Hp**
  - $f: \mathbb{Z} \in \mathbb{C} - \{0\} : k \rightarrow \zeta^k$
  - $f$ morfismo di gruppi $(\mathbb{Z}, +)$ e $(\mathbb{C} - \{0\}, \cdot)$
  - $I(n)$ ideale generato da $n$ \*\*⚠️ CHI È N\*\*
- **Th**
  - $\textrm{Ker}(f) = I(n)$
- **Dim**
  - pass

## Oss

- ⚠️ \*\*coso finale su H che non ho capito niente\*\*

## Oss

- **Hp**
  - $G, H$ gruppi
  - $f: G \rightarrow H$ morfismo
- **Th**
  - $\textrm{Ker}(f)$ è sottogruppo normale
- **Dim**
  - per la formulazione 2 della definizione di sottogruppo normale, $\forall g \in G, h \in \textrm{Ker}(f) \implies g h g^{-1} \in \textrm{Ker}(f)$
  - $f(ghg^{-1}) = f(g) \cdot f(h) \cdot f(g^{-1})$
  - $h \in \textrm{Ker}(f) \implies f(h) = 1\_H$ per definizione
  - per dimostrazione precedente $f(g^{-1}) = f(g)^{-1}$
  - $f(ghg^{-1})= f(g) \cdot 1\_H \cdot f(g)^{-1} = 1\_H \implies ghg ^{-1} \in \textrm{Ker}(f)$ per definizione