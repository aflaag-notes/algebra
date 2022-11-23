# Morfismi

## Def 

- **Morfismo di gruppi**
> - $(G, \cdot), (H, \cdot)$ gruppi
> - $f: G \rightarrow H$
> - $f$ **morfismo di gruppi** $\iff f(x\cdot y)=f(x)\cdot f(y) \quad \forall x, y \in G$

- **Morfismo di anelli**
> - $(A, +, \cdot), (B, +, \cdot)$ anelli
> - $f: A \rightarrow B$
> - $f$ **morfismo di anelli** $\iff f(x+ y) = f(x) + f(y)$ e $f(x \cdot y) = f(x) \cdot f(y) \quad \forall x, y \in A$
>     -   la stessa definizione si applica per morfismo di campi

## Oss

- **Hp**
  - $(G, \cdot), (H, \cdot)$ gruppi
  - $1_G$ neutro per $G$
  - $1_H$ neutro per $H$
  - $f: G \rightarrow H$ morfismo
- **Th**
  - $f(1_G) = 1_H$
- **Dim**
  - $\forall g \in G \quad f(g) = f(1_G \cdot g) = f(1_G) \cdot f(g)$ poiché $f$ morfismo
  - quindi $f(g) = f(1_G) \cdot f(g) \implies f(g) \cdot f(g)^{-1} = f(1_G) \cdot f(g) \cdot f(g)^{-1} \implies 1_H = f(1_G) \cdot 1_H \implies 1_H = f(1_G)$ (poiché $f(g), f(g)^{-1} \in H$ per definizione di $f$)
 
## Oss

- **Hp**
  - $(G, \cdot), (H, \cdot)$ gruppi
  - $1_G$ neutro per $G$
  - $1_H$ neutro per $H$
  - $f: G \rightarrow H$ morfismo
- **Th**
  - $f(g^{-1}) = f(g)^{-1}$
- **Dim**
  - per dimostrazione precedente, $1_H = f(1_G) = f(g \cdot g^{-1})=f(g) \cdot f(g^{-1}) \implies 1_H = f(g) \cdot f(g^{-1}) \implies f(g)^{-1} = f(g^{-1})$

****

# Isomorfismi

## Def

- **Isomorfismo**
> - $f$ isomorfismo $\iff f$ morfismo e $f$ biiettiva

## Oss

- **Hp**
  - $f: G \rightarrow H$ isomorfismo
- **Th**
  - $f ^{-1}: H \rightarrow G$ isomorfismo
- **Dim**
  - $\forall g \in G, h \in H \quad \exists !f^{-1} \mid \left\{\begin{array}{c}f^{-1}(f(g))=g \\ f\left(f^{-1}(h)\right)=h\end{array}\right.$
  - $\forall h, h^{\prime} \in H \quad f^{-1}\left(h h^{\prime}\right)=f^{-1}(h) \cdot f^{-1}\left(h^{\prime}\right) \iff hh'=f\left(f^{-1}\left(h h^{\prime})\right)=f(f^{-1}(h)\cdot f^{-1}(h^\prime)) = f(f^{-1}(h))\cdot f(f^{-1}(h^\prime))\right. = hh'$, e dunque $f^{-1}$ è un morfismo, e poiché è invertibile è un isomorfismo

## Ex

- **Hp**
  - $z \in \mathbb{C} \mid z^n = 1$ sono le radici $n$-esime di $1$
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
  - $f: \mathbb{Z}_n \rightarrow H : [k] \rightarrow \zeta^k$
- **Th**
  - $f$ isomorfismo di gruppi $(\mathbb{Z}_n , +)$ e $(H, \cdot)$
- **Dim**
  - $f$ è biiettiva per costruzione di $\mathbb{Z}_n := \{[0], [1], \ldots, [n - 1]\}$ e $H := \{\zeta ^0, \zeta^1, \ldots, \zeta^{n-1}\}$
  - $f$ morfismo
    - $f([i]+[j])=f([i]) \cdot f([j])$
      - $[i] + [j] = [k]$ per un certo $k \in \mathbb{Z}_n \implies \exists h \in \mathbb{Z} \mid i + j = k + hn$
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

## Ex

- **Hp**
  - $f: \mathbb{Z} \rightarrow \mathbb{Z}_n : k \rightarrow [k]$
- **Th**
  - $f$ morfismo di anelli $\left(\mathbb{Z},+, \cdot\right)$ e $\left(\mathbb{Z}_{n},+, \cdot\right)$
- **Dim**
  - per come le operazioni $+$ e $\cdot$ sono state definite, $f([x+y])=f([x])+f([y])$ e
$f([x \cdot y])=f([x]) \cdot f([y])$

## Ex

- **Hp**
  - $n, m \in \mathbb{Z} : n \mid m$
  - $f : \mathbb{Z}_m \rightarrow \mathbb{Z}_n: x \ (\bmod \ m) \rightarrow x \ (\bmod\ n)$
- **Th**
  - $f$ morfismo di anelli $\left(\mathbb{Z}_{m},+, \cdot\right)$ e $\left(\mathbb{Z}_{n},+, \cdot\right)$
- **Dim**
  - $\forall [x], [y] \in \mathbb{Z}_m \quad x \ (\bmod \ m) + y \ (\bmod \ m) = x +y \ (\bmod \ m)$
  - $f(x + y \ (\bmod \ m)) = x +y \ (\bmod \ n) = x \ (\bmod \ n)+ y \ (\bmod \ n) = f(x \ (\bmod \ m)) + f(y \ (\bmod \ m))$
  - il ragionamento è analogo per l'operazione $\cdot$, e dunque segue la tesi
 
## Ex

- **Hp**
  - $G$ gruppo
  - $f: G \rightarrow G : h \rightarrow g \cdot h \cdot g^{-1}$ per qualche $g \in G$
- **Th**
  - $f$ morfismo di gruppi $(G, \cdot)$ e $(G, \cdot)$
- **Dim**
  - $\forall h, h^\prime \in G \quad f(h) \cdot f\left(h^{\prime}\right)=\left(g h g^{-1}\right)\cdot \left(g h^{\prime} g^{-1}\right)=gh(g^{-1} \cdot g)h^\prime g^{-1}=g h h^{\prime} g^{-1}=f\left(h h^{\prime})\right.$

****

# Kernel e Immagine

## Def

- **kernel e Immagine di gruppi**
> - $G, H$ gruppi
> - $f: G \rightarrow H$ morfismo
> - $\textrm{ker}(f):=\{g \in G \mid f(g) = 1_H\}$
> - $\textrm{Im}(f):=\{h \in H \mid \exists g \in G : f(g) = h\}$

 -  **kernel e Immagine di anelli**
> - $A, B$ gruppi
> - $f: A \rightarrow B$ morfismo
> - $\textrm{ker}(f):=\{a \in A \mid f(a)= 0_B\}$
> - $\textrm{Im}(f):=\{b \in B \mid \exists a \in A : f(a) = b\}$

## Oss

- **Hp**
  - $G, H$ gruppi
  - $f: G \rightarrow H$ morfismo
- **Th**
  - $\textrm{ker}(f) \subset G$ è sottogruppo
- **Dim**
  - per dimostrazione precedente, $f(1_G) = 1_H \implies 1_G \in \textrm{ker}(f)$ per definizione
  - $x, y \in \textrm{ker}(f) \implies f(x) = f(y ) = 1_H$ per definizione, dunque $f(x) \cdot f(y) = 1_H \cdot 1_H = 1_H$, e $f(x) \cdot f(y) = f(x \cdot y) = 1_H$ perché $f$ morfismo, quindi $x \cdot y \in \textrm{ker}(f)$ per definizione
  - $g \in \textrm{ker}(f) \implies f(g) =1_H \implies f(g)^{-1} = 1_H^{-1} = 1_H$, ma poiché per dimostrazione precedente $f(g)^{-1} = f(g^{-1}) \implies f(g^{-1})= 1_H \implies g^{-1} \in \textrm{ker}(f)$ per definizione
 
## Oss

- **Hp**
  - $G, H$ gruppi
  - $f: G \rightarrow H$ morfismo
- **Th**
  - $\textrm{Im}(f) \subset G$ è sottogruppo
- **Dim**
  - per dimostrazione precedente $f(1_G)= 1_H \implies 1_H \in \textrm{Im}(f)$ per definizione
  - $x, y \in \textrm{Im}(f) \implies \exists g, g^\prime \in G \mid x = f(g) \land y = f(g^\prime) \implies x \cdot y = f(g) \cdot f(g^\prime) = f(g\cdot g^\prime)$ perché $f$ morfismo, quindi $x \cdot y \in \textrm{Im}(f)$ per definizione
  - $x \in \textrm{Im}(f) \implies \exists g \in G \mid f(g) = x \implies x^{-1} = f(g)^{-1} = f(g^{-1})$ per dimostrazione precedente, quindi $x ^{-1} \in \textrm{Im}(f)$ per definizione
 
## Oss

- **Hp**
  - $G, H$ gruppi
  - $f: G \rightarrow H$ morfismo
- **Th**
  - $f$ iniettiva $\iff \textrm{ker}(f) = \{1_G\}$
- **Dim**
  - $f$ iniettiva $\implies \textrm{ker}(f) = \{1_G\}$
    - $f(1_G) = 1_H$ per dimostrazione precedente, dunque $1_G \in \textrm{ker}(f)$ per definizione
    - $f$ iniettiva $\implies \nexists x, y \in G \mid x \neq y \implies f(x) = f(y)$, di conseguenza è unico $1_G \in G \mid f(1_G) = 1_H$, dunque $\textrm{ker}(f)$ conterrà esclusivamente $1_G$ per definizione
  - $f$ iniettiva $\impliedby \textrm{ker}(f) = \{1_G\}$
    - $\forall g, g^\prime \in G \quad f(g) = f(g^\prime) \iff f(g)^{-1} \cdot f(g) = f(g)^{-1} \cdot f(g^\prime) \iff 1_H = f(g) \cdot f(g^\prime) = f(g \cdot g^\prime)$
    - $\textrm{ker}(f) = \{1_G\} \implies f(1_G)=1_H$ per definizione, allora $f(g\cdot g^\prime) = 1_H \implies g \cdot g^\prime = 1_G$ necessariamente, e $g \cdot g^\prime = 1_G \iff g= g^\prime \implies f(g) = f(g^\prime) \implies g = g^\prime \implies f$ iniettiva

## Oss

- **Hp**
  - $A, B$ anelli
  - $f: A \rightarrow B$ morfismo di anelli
- **Th**
  - $\textrm{ker}(f)$ ideale
- **Dim**
  - $(\textrm{ker}(f), +) \subset (A, +)$ sottogruppo per dimostrazione precedente
  - per analogia con dimostrazione precedente, $f(0_A) = 0_B$
  - $x \in \textrm{ker}(f) \implies f(x) = 0_B$ per definizione, quindi $\forall x \in \textrm{ker}(f), y \in A \quad f(x \cdot y )= f(x) \cdot f(y) )= 0_B \cdot f(y) = 0_B \implies x \cdot y \in \textrm{ker}(f)$ per definizione, quindi $\textrm{ker}(f) \cdot A \subset \textrm{ker}(f)$

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
  - $f: \mathbb{Z} \rightarrow \mathbb{C} - \{0\} : k \rightarrow \zeta^k$
  - $f$ morfismo di gruppi $(\mathbb{Z}, +)$ e $(\mathbb{C} - \{0\}, \cdot)$
  - $I(n)$ ideale generato da $n$ **⚠️ CONTROLLA SE SERVE QUESTA COSA**
- **Th**
  - $\textrm{ker}(f) = I(n)$
- **Dim**
  - pass

## Oss

- **Hp**
  - $G, H$ gruppi
  - $f: G \rightarrow H$ morfismo
- **Th**
  - $\textrm{ker}(f)$ è sottogruppo normale
- **Dim**
  - per la formulazione 2 della definizione di sottogruppo normale, $\forall g \in G, h \in \textrm{ker}(f) \implies g h g^{-1} \in \textrm{ker}(f)$
  - $f(ghg^{-1}) = f(g) \cdot f(h) \cdot f(g^{-1})$
  - $h \in \textrm{ker}(f) \implies f(h) = 1_H$ per definizione
  - per dimostrazione precedente $f(g^{-1}) = f(g)^{-1}$
  - $f(ghg^{-1})= f(g) \cdot 1_H \cdot f(g)^{-1} = 1_H \implies ghg ^{-1} \in \textrm{ker}(f)$ per definizione
