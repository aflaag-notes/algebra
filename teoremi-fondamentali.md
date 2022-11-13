# Teorema fondamentale dell'algebra

- **Hp**
  - $a\_{0}, \ldots, a\_{n} \in \mathbb{C}$
  - $n \in \mathbb{N}\_{\geq 1}$
  - $a\_n \neq 0$
- **Th**
  - $\exists x \in \mathbb{C} \mid x$ è soluzione dell'equazione $a\_{0}+a\_{1} x+a\_{2} x^{2}+\cdots+a\_{n} x^{n}=0$

****

# Teorema della divisione euclidea con il resto

- **Hp**
  - $m \in \mathbb{Z}$
  - $n \in \mathbb{Z} - \{0\}$
- **Th**
  - $\exists !  \ q, r \in \mathbb{Z} \mid m=n q+r \quad 0 \leq r<n$
- **Dim**
  - \_esistenza\_
    - sia $[m] \in \mathbb{Z}\_n$
    - $a \equiv m \ (\bmod \ n) \iff \exists p\_1 \in \mathbb{Z} \mid np\_1 = m - a$
    - $r:=\min(\{a \in \mathbb{Z} \mid a \in [m], a \ge 0\})$
    - $r \in [m] \iff \exists p\_2 \in \mathbb{Z} \mid np\_2 = m - r  \iff r = m - np\_2 \iff m = np\_2 +r$
    - ⚠️ **INCOMPLETA**

****

# Teorema di Lagrange (teoria dei gruppi)

- **Hp**
  - $G$ gruppo finito
  - $H \subset G$ sottogruppo finito
- **Th**
  - $|G| = |H| \cdot |G / H|$
- **Dim**
  - $G$ è decomponibile attraverso l'unione disgiunta delle sue classi laterali sinistre, poiché ogni relazione di equivalenza induce una partizione per dimostrazione precedente
  - in particolare, ogni classe laterale sinistra è equivalente a $xH$ per opportuni $x \in G$, e hanno tutte cardinalità $|H|$ per dimostrazione precedente
  - $G = X\_1 \coprod X\_2 \coprod \ldots \coprod X\_k \implies |G| = |X\_1| + |X\_2| + \ldots  + |X\_k|$ poiché ogni $X\_i$ è una partizione, e dunque disgiunta con le altre, e poiché sono tutte classi laterali sinistre hanno tutte cardinalità $|H|$
  - dunque, $|G| = k \cdot |H|$, dove $k$ corrisponde al numero di classi laterali, che è proprio $|G/H| \implies |G| = |H| \cdot |G/H|$

****

# Teorema fondamentale dell'aritmetica

- **Hp**
  - $a, b \in \mathbb{N}$
- **Th**
  - $\textrm{mcm}(a, b) \cdot \textrm{MCD}(a, b) = a \cdot b$
- **Dim**
  - $a = 0 \lor b = 0 \lor a = b = 0 \implies \textrm{mcm}(a, b) = 0$
  - $a, b \gt 0$
    - $\mathbb{P} := \{p \in \mathbb{N} \mid p \textrm{ primo}\}$
    - $\forall n \in \mathbb{N} - \{0\} \quad \exists ! n\_2, n\_3, n\_5, \ldots, n\_p \in \mathbb{N} \mid p \in \mathbb{P} : n = 2^{n\_2} \cdot 3 ^ {n\_3} \cdot \ldots \cdot p ^ {n\_p}$
      - $p \nmid n \implies n\_p = 0 \implies p ^  {n\_p} = 1$, dunque non influisce nella produttoria
    - $\displaystyle{n = \prod\_{p \in \mathbb{P}}^{} p ^{n\_p}}$, quindi possiamo riscrivere anche $a$ e $b$ tramite i loro fattori primi
      - $\displaystyle{a=\prod\_{p \in \mathbb{P}} p^{a\_{p}}}$ e $\displaystyle{b=\prod\_{p \in \mathbb{P}} p^{b\_{p}} }$
    - $d:= \textrm{MCD}(a, b)$ e $m:=\textrm{mcm}(a, b)$
      - per definizione di $d$ ed $m$, e attraverso le regole che permettono di trovarli tramite le fattorizzazioni di $a$ e $b$, è possibile riscrivere $d$ ed $m$ come $\displaystyle{d = \prod\_{p \in \mathbb{P}} p^{\min(a\_p, b\_p)}}$ e $\displaystyle{m = \prod\_{p \in \mathbb{P}} p^{\max(a\_p, b\_p)}}$
      - $d \cdot m =\displaystyle{\prod\_{p \in \mathbb{P}} p^{\min(a\_p, b\_p)}} \cdot \displaystyle{\prod\_{p \in \mathbb{P}} p^{\max(a\_p, b\_p)}} = \displaystyle{\prod\_{p \in \mathbb{P}} p^{\min(a\_p, b\_p) + \max(a\_p, b\_p)}}$
    - $\forall a, b \in \mathbb{N} \quad a + b = \min(a, b) + \max(a, b)$
      - $a = \min(a, b) \implies \max(a, b) = b$, e viceversa
    - $d \cdot m = \displaystyle{\prod\_{p \in \mathbb{P} }p ^{a\_p + b\_p}} = \displaystyle{\prod\_{p \in \mathbb{P}} p^{a\_p}} \cdot \displaystyle{\prod\_{p \in \mathbb{P}} p^{b\_p}} = a \cdot b$

****

# Teorema cinese dei resti

## Lem

- **Hp**
  - $a\_1, \ldots, a\_n \ge 2 \in \mathbb{Z}  \mid \textrm{MCD}(a\_i, a\_j) = 1 \quad \forall i, j \in [1, n] : i \neq j$
- **Th**
  - $m := \textrm{mcm}(a\_1, \ldots, a\_n)= a\_1 \cdot \ldots \cdot a\_n$
- **Dim**
  - $\textrm{MCD}(a\_i, a\_j) = 1 \implies \forall p \in \mathbb{P} \quad p \mid a\_i \implies p \nmid a\_j$, poiché altrimenti $p \mid \textrm{MCD}(a\_i, a\_j)$
    - prese le fattorizzazioni $\displaystyle a\_1 = \prod\_{p \in \mathbb{P}}{p^{a\_{1\_p}}} \ \ldots \ a\_n = \prod\_{p \in \mathbb{P}}{p^{a\_{n\_p}}}$, allora $\forall p \in \mathbb{P} \quad a\_{i\_p} \gt 0 \implies a\_{j\_p} = 0 \quad \forall i \neq j$, dunque ogni fattore è presente solo in una delle fattorizzazioni degli $n$ interi, poiché coprimi
      - $a\_{k\_p} = 0 \implies p^{a\_{k\_p}} = 1 \implies$ non compare nella fattorizzazione
      - di conseguenza, la somma degli esponenti di $p$ su tutte le fattorizzazioni degli $n$ interi, sarà il numero stesso, poiché nelle altre fattorizzazioni varrà $0$, e quindi $\forall p \in \mathbb{P} \quad a\_{1\_p} + \ldots + a\_{n\_p} = \max(a\_{1\_p}, \ldots, a\_{n\_p})$
    - allora $m = \displaystyle \prod\_{p \in \mathbb{P}}{p^{\max(a\_{1\_p}, \ldots, a\_{n\_p})}}=\prod\_{p \in \mathbb{P}}{p^{a\_{1\_p} + \ldots + a\_{n\_p}}} = \prod\_{p \in \mathbb{P}}{p^{a\_{1\_p}}} \cdot \ldots \cdot \prod\_{p \in \mathbb{P}}{p^{a\_{n\_p}}} = a\_1 \cdot \ldots \cdot a\_n$
    
## Lem

- **Hp**
  - $a\_1, \ldots, a\_n \ge 2 \in \mathbb{Z}$
  - $m:= \textrm{mcm}(a\_1, \ldots, a\_n)$
- **Th**
  - $\exists \phi \mid \phi: \mathbb{Z}\_m \rightarrow \mathbb{Z}\_{a\_1} \times \ldots \times \mathbb{Z}\_{a\_n}: x \ (\bmod m) \rightarrow (x \ (\bmod a\_1), \ldots, x \ (\bmod a\_n))$
  - $\phi$ è una funzione ben definita, ed è iniettiva
  - $\phi$ ben definita $\implies \phi$ non dipende dalla scelta di $[x] \in \mathbb{Z}\_m$
- **Dim**
    - se $\phi$ è ben definita, allora $x\equiv x^{\prime} \ (\bmod m) \implies \left\{\begin{array}{c}x \equiv x^{\prime}\ \left(\bmod a\_{1}\right) \\ \vdots \\ x \equiv x^{\prime}\ \left(\bmod a\_{n}\right)\end{array}\right.$
    - **⚠️ BASTA DIMOSTRARE SOLO UNA DELLE DUE MA NON HO CAPITO PERCHÉ**
    - se $\phi$ è iniettiva, allora vale anche l'implicazione opposta
      - $\left\{\begin{array}{c}x \equiv x^{\prime}\ \left(\bmod a\_{1}\right) \\ \vdots \\ x \equiv x^{\prime}\ \left(\bmod a\_{n}\right)\end{array}\right. \iff \left\{\begin{array}{c}x^{\prime}-x \in I\left(a\_{1}\right) \\ \vdots \\ x^{\prime}-x \in I\left(a\_{m}\right)\end{array}\right. \iff x - x^\prime \in I(a\_1) \cap \ldots \cap I(a\_n) = I(m)$, e per definizione $x - x^\prime \in I(m) \implies x \equiv x^\prime \ (\bmod m)$

## Teorema

- **Hp**
  - $a\_1, \ldots, a\_n \ge 2 \in \mathbb{Z} \mid \textrm{MCD}(a\_i, a\_j) = 1 \quad \forall i, j \in [1, n] \mid i \neq j$
  - $b\_1, \ldots, b\_n \in \mathbb{Z} \mid 0 \leq b\_{1}<a\_{1}, \ldots 0 \leq b\_n \lt a\_n$
  - $m := \textrm{mcm}(a\_1, \ldots, a\_n) = a\_1 \cdot \ldots \cdot a\_n$
- **Th**
  - $\exists ! x \ (\bmod m) \mid$ $\left\{\begin{array}{c}x \equiv b\_{1}\ \left(\bmod a\_{1}\right) \\ \vdots \\ x \equiv b\_{n}\ \left(\bmod a\_{n}\right)\end{array}\right.$
- **Dim**
  - per il primo lemma $m = a\_1 \cdot \ldots \cdot a\_n$ poiché coprimi in ipotesi
  - per il secondo lemma $m = \textrm{mcm}(a\_1, \ldots, a\_n) \implies \exists \phi : \mathbb{Z}\_m \rightarrow \mathbb{Z}\_ {a\_1} \times \cdots \times \mathbb{Z}\_{a\_m}$ ben definita e iniettiva
  - $\left|X\_{1} \times \cdots \times X\_{n}\right|=\left|X\_{1}\right| \cdot\ldots\cdot\left|X\_{n}\right| \implies$ $\left|\mathbb{Z}\_{a\_{1}} \times \ldots \times \mathbb{Z}\_{a\_{n}}\right|=\left|\mathbb{Z}\_{a\_{1}}\right| \cdot\ldots\cdot\left|\mathbb{Z}\_{a\_{n}}\right|$
    - $\mathbb{Z}\_n = \{[0],[1], \cdots,[n-1]\} \implies \left|\mathbb{Z}\_{n}\right|=n$, quindi $\left|\mathbb{Z}\_{a\_{1}}\right| \cdot\ldots\cdot\left|\mathbb{Z}\_{a\_{n}}\right|  = a\_1 \cdot \ldots \cdot a\_n = m = \left| \mathbb{Z}\_m \right|$ per ragionamento analogo
  - $|X|=|Y|<\infty \implies f: X \rightarrow Y$ iniettiva $\iff$ $f$ suriettiva
    - applicando questa osservazione, $\phi$ iniettiva $\implies \phi$ suriettiva, in quanto, per l'osservazione precedente, insieme di partenza e di arrivo di $\phi$ hanno la stessa cardinalità $\left| \mathbb{Z}\_m \right|$
  - $\phi$ **suriettiva** $\implies$ $\exists x \mid x \ (\bmod m)$ è soluzione del sistema
    - $\varphi(x \ (\bmod m))=\left(b\_{1}\ \left( \bmod  a\_{1}\right), \ldots, b\_{n} \ (\bmod a\_{n})\right)$, e poiché $\phi$ è suriettiva, allora ogni tupla di $n$ elementi dell'insieme di arrivo, che descrive un sistema come in ipotesi, ha una controimmagine $x \ (\bmod m)$, e $x \ (\bmod m)\in \mathbb{Z}\_m$ per definizione, dunque **esiste sempre una soluzione**
  - $\phi$ **iniettiva** $\implies$ $\exists ! x \mid x \ (\bmod m)$ è soluzione del sistema
    - poiché $\phi$ è iniettiva, $x \ (\bmod m) \in \mathbb{Z}\_m$ è unica, dunque **la soluzione è sempre unica**

****

# Piccolo teorema di Fermat

- **Hp**
  - $p \in \mathbb{P}$
  - $a \in \mathbb{Z}$
- **Th**
  - $a^{p} \equiv a \ (\bmod p)$
- **Dim**
  - $a=0 \implies [0]^{p} =[0]$
  - $a \gt 0 \implies$ $[a+1]^{p}=[a+1] \implies[a]^{p}+[1]^{p}=[a+1] \implies [a]^p + [1] = [a + 1]$
    - per ipotesi induttiva, $[a]^p = [a]$, dunque $[a] + [1] = [a + 1]$
   
## Cor

- **Hp**
  - $[a] \in \mathbb{Z}\_{p}-\{0\}$
  - $p \in \mathbb{P}$
- **Th**
  - $[a]^{-1}=\left[a^{p-2}\right]$
- **Dim**
  - $[a] \neq [0] \implies [a]^p = [a] \iff [a]^p \cdot [a]^{-1} = [a] \cdot [a]^{-1}$, e dunque $[a]^{p -1} = [1] \implies [a] \cdot [a]^{p -2} = [1]\implies [a]^{-1} = [a]^{p-2}$

****

# Teorema fondamentale di isomorfismo

- **Hp**
  - $A, B$ anelli
  - $f: A \rightarrow B$ morfismo di anelli
- **Th**
  - $A / \textrm{Ker}(f) \cong \textrm{Im}(f)$, o alternativamente $\exists \varphi \mid \varphi : A / \textrm{Ker}(f) \rightarrow \textrm{Im}(f): [a] \rightarrow f(a)$ isomorfismo di anelli
- **Dim**
  - $\varphi$ è ben definita
    - $\varphi$ è ben definita $\iff [x] = [y] \implies f(x) = f(y) \quad \forall x, y \in A$
    - $[x] = [y] \iff x \equiv y \ (\bmod \textrm{Ker}(f)) \implies y - x \in \textrm{Ker}(f) \implies f(y - x) = 0\_B$ per definizione, e inoltre $f(y-x) = f(y)-f(x)$ in quanto $f$ morfismo di anelli **⚠️ PERCHE?**, quindi $0\_B = f(y) - f(x) \implies f(y) = f(x)$
  - $\varphi$ morfismo di anelli
    - $\varphi$ morfismo di anelli $\iff \varphi([a]) \cdot \varphi([b]) = \varphi([a]\cdot [b])$ e $\varphi([a]) + \varphi([b]) = \varphi([a]+ [b])$
      - $\varphi([a]) \cdot \varphi([b]) = f(a) \cdot f(b)$ per definizione di $\varphi$
      - $f(a) \cdot f(b) = f(a\cdot b)$ per morfismo di $f$
      - $f(a \cdot b ) = \varphi([a \cdot b])$ per definizione di $\varphi$
      - $\varphi([a \cdot b]) = \varphi([a] \cdot [b])$ per definizione di $\cdot$
      - per $+$ vale il ragionamento analogo
  - $\varphi$ isomorfismo di anelli $\iff \varphi$ iniettiva e suriettiva
    - $\varphi$ iniettiva
      - $\varphi$ iniettiva $\iff \textrm{Ker}(\varphi)=\{[0\_A]\}$ per dimostrazione precedente
      - $x \in \textrm{Ker}(f) \iff x - 0\_A \in \textrm{Ker}(f) \implies x \equiv 0\_A \ (\bmod \textrm{Ker}(f)) \implies [x] = [0\_A] \implies \varphi([x]) = \varphi([0\_A])$, poiché $\varphi$ è ben definita, dunque $f(x) = 0\_B$ **⚠️ NON HO CAPITO**
    - $\varphi$ suriettiva
      - $\varphi : A / \textrm{Ker}(f) \rightarrow \textrm{Im}(f) \implies$ l'insieme di arrivo di $\varphi$ coincide è proprio l'insieme delle immagini di $f$, quindi $\varphi$ è suriettiva per costruzione

## Oss

- **Hp**
  - $G, H$ gruppi
  - $f: G \rightarrow H$ morfismo di gruppi
- **Th**
  - $G / \textrm{Ker}(f) \cong \textrm{Im}(f)$, o alternativamente $\exists \varphi \mid \varphi : G / \textrm{Ker}(f) \rightarrow \textrm{Im}(f): [g] \rightarrow f(g)$ isomorfismo di gruppi
- **Dim**
  - la dimostrazione è analoga al caso degli anelli

****

## Teorema di Cayley

- **Hp**
  - $G$ gruppo finito
  - $p \in \mathbb{P}$
  - $p \bigg\vert |G|$
- **Th**
  - $\exists g \in G \mid o(g) = p$

## Oss

- **Hp**
  - $G$ gruppo $\bigg\vert |G|=4$
- **Th**
  - $G \cong \mathbb{Z}\_4$ oppure $G \cong K\_4$
- **Dim**
  - ⚠️ **L'HO SCRITTA MA NON HO CAPITO NIENTE IN QUESTA DIMOSTRAZIONE**
  - preso $a \in G \mid a \neq 1$, per dimostrazione precedente $o(a) \bigg\vert |G| \implies o(a)=1 \lor o(a) =2 \lor o(a) = 4$, ma $a \neq 1 \implies o(a) \neq 1$
  - 2 casi
    - $\exists x \in G \mid o(x)=4 \implies G \cong \mathbb{Z}\_4$ **⚠️ PERCHÉ?**
    - $\nexists x \in G \mid o(x) =4$
      - $|G| = 4 \implies G$ è della forma $\{1, a, b, c\}$ con $o(a)=o(b)=o(c)=2$ **⚠️ PERCHÉ?**
        - $1 \in G$ perché $G$ gruppo in ipotesi
        - $a \neq b \neq c \neq 1$, altrimenti $|G| \lt 4$
      - $a^2=b^2=c^2=1 \implies$$\left\{\begin{array}{l}a=a^{-1} \\ b=b^{-1} \\ c=c^{-1}\end{array}\right.$
      - $G$ abeliano $\iff$ presi i 3 elementi non neutri, moltiplicandone due tra loro si ottiene il terzo **⚠️ PERCHÉ?**
        - $ab = c$
          - $ab = 1 \implies b = a^{-1} = a \ \bot$
          - $ab = a \implies b = 1 \ \bot$
          - $ab = b \implies a = 1 \ \bot$
          - quindi necessariamente $ab = c$
          - il ragionamento è analogo per tutti gli altri prodotti
      - quindi $G \cong K\_4$ **⚠️ PERCHÉ? non mancano altre cose?**
