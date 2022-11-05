# Teorema fondamentale dell'algebra

Data un'equazione \( a_{0}+a_{1} x+a_{2} x^{2}+\cdots+a_{n} x^{n}=0 \), con \( a_{0}, a_{1}, a_{2}, \ldots, a_{n} \in \mathbb{C}, \ n \geq 1, a_n \neq 0 \quad \implies \quad \exists x \in \mathbb{C}\)

****

# Teorema della divisione euclidea con il resto

- $m, n \in \mathbb{Z}, n>0 \implies \exists !  \ q, r \in \mathbb{Z} \mid m=n q+r, \ 0 \leq r<n$
  - ⚠️ **MANCA DIMOSTRAZIONE**

****

# Teorema di Lagrange (teoria dei gruppi)

- $xH = \{xh \mid h \in H\}$ dove $H \subset G$ e $x \in G$, è detta **classe laterale sinistra** di $H$ in $G$
  - quando $G$ è finito, $| xH | = | H |$ perché per ogni elemento $x$ che genera $xH$, $xH$ è l'insieme dei prodotti di $x$ con ogni elemento di $H$
    - $H \rightarrow xH$ è biunivoca $\forall x \in G$
  - $G / H = \{xH \mid x \in G\}$ è l'insieme delle classi laterali sinistre, e poiché sono disgiunte a due a due, e la loro unione equivale a $G$, allora ogni $xH$ è una **partizione** di $G$
  - $|G| = |H| \cdot [G : H]$ è il **teorema di Lagrange**
    - $|G|$ è la cardinalità di $G$
    - $|H|$ è la cardinalità di $H$, che equivale a $|xH| \ \forall x \in G$
    - $[G : H]$ è la cardinalità di $|G / H|$, ovvero il numero di classi laterali sinistre

****

# Teorema fondamentale dell'aritmetica

- $\forall a, b \in \mathbb{N} \quad \textrm{mcm}(a, b) \cdot \textrm{MCD}(a, b) = a \cdot b$
  - $a = 0 \lor b = 0 \lor a, b = 0 \implies \textrm{mcm}(a, b) = 0$
  - $a, b \gt 0$
    - $\mathbb{P} = \{p \in \mathbb{N} \mid p \textrm{ primo}\}$
    - $\forall n \in \mathbb{N} - \{0\} \quad \exists ! n_2, n_3, n_5, \ldots, n_p \in \mathbb{N} \mid p \in \mathbb{P} : n = 2^{n_2} \cdot 3 ^ {n_3} \cdot \ldots \cdot p ^ {n_p}$
      - $p \nmid n \implies n_p = 0 \implies p ^  {n_p} = 1$, dunque non influisce nella produttoria
    - $\displaystyle{n = \prod_{p \in \mathbb{P}}^{} p ^{n_p}}$, quindi possiamo riscrivere anche $a$ e $b$ tramite i loro fattori primi
      - \(\displaystyle{a=\prod_{p \in \mathbb{P}} p^{a_{p}}} \) e \( \displaystyle{b=\prod_{p \in \mathbb{P}} p^{b_{p}} }\)
    - $d:= \textrm{MCD}(a, b)$ e $m:=\textrm{mcm}(a, b)$
      - per definizione di $d$ ed $m$, e attraverso le regole che permettono di trovarli tramite le fattorizzazioni di $a$ e $b$, è possibile riscrivere $d$ ed $m$ come $\displaystyle{d = \prod_{p \in \mathbb{P}} p^{\min(a_p, b_p)}}$ e $\displaystyle{m = \prod_{p \in \mathbb{P}} p^{\max(a_p, b_p)}}$
      - $d \cdot m =\displaystyle{\prod_{p \in \mathbb{P}} p^{\min(a_p, b_p)}} \cdot \displaystyle{\prod_{p \in \mathbb{P}} p^{\max(a_p, b_p)}} = \displaystyle{\prod_{p \in \mathbb{P}} p^{\min(a_p, b_p) + \max(a_p, b_p)}}$
    - $\forall a, b \in \mathbb{N} \quad a + b = \min(a, b) + \max(a, b)$
      - $a = \min(a, b) \implies \max(a, b) = b$, e viceversa
    - $d \cdot m = \displaystyle{\prod_{p \in \mathbb{P} }p ^{a_p + b_p}} = \displaystyle{\prod_{p \in \mathbb{P}} p^{a_p}} \cdot \displaystyle{\prod_{p \in \mathbb{P}} p^{b_p}} = a \cdot b$

****

# Teorema cinese dei resti

## Lemma 1

## Lemma 2

## Teorema

- $\forall a_1, \ldots, a_n \ge 2 \in \mathbb{Z} \mid \textrm{MCD}(a_i, a_j) = 1 \quad \forall i, j \in [1, n] \mid i \neq j$
- presi \( b_1, \ldots, b_n \in \mathbb{Z} \mid 0 \leq b_{1}<a_{1}, 0 \leq b_{2}<a_{2}, \ldots 0 \leq b_n \lt a_n\)
- $m := \textrm{mcm}(a_1, \ldots, a_n) = a_1 \cdot \ldots \cdot a_n$
- allora $\exists ! x \ (\bmod m)$ \( \left\{\begin{array}{c}x \equiv b_{1}\ \left(\bmod a_{1}\right) \\ \vdots \\ x \equiv b_{n}\ \left(\bmod a_{n}\right)\end{array}\right. \)
  - per il **lemma 1** $m = a_1 \cdot \ldots \cdot a_n$ poiché coprimi in ipotesi
  - per il **lemma 2** $m = \textrm{mcm}(a_1, \ldots, a_n) \implies \exists \phi : \mathbb{Z}_m \rightarrow \mathbb{Z}_ {a_1} \times \cdots \times \mathbb{Z}_{a_m}$ ben definita e iniettiva
  - \( \left|X_{1} \times \cdots \times X_{n}\right|=\left|X_{1}\right| \cdot\ldots\cdot\left|X_{n}\right| \implies\) \( \left|\mathbb{Z}_{a_{1}} \times \ldots \times \mathbb{Z}_{a_{n}}\right|=\left|\mathbb{Z}_{a_{1}}\right| \cdot\ldots\cdot\left|\mathbb{Z}_{a_{n}}\right| \)
    - \( \mathbb{Z}_n = \{[0],[1], \cdots,[n-1]\} \implies \left|\mathbb{Z}_{n}\right|=n\), quindi \(\left|\mathbb{Z}_{a_{1}}\right| \cdot\ldots\cdot\left|\mathbb{Z}_{a_{n}}\right|  = a_1 \cdot \ldots \cdot a_n = m = \left| \mathbb{Z}_m \right|\) per ragionamento analogo
  - \( |X|=|Y|<\infty \implies f: X \rightarrow Y \) iniettiva $\iff$ $f$ suriettiva
    - applicando questa osservazione, $\phi$ iniettiva $\implies \phi$ suriettiva, in quanto, per l'osservazione precedente, insieme di partenza e di arrivo di $\phi$ hanno la stessa cardinalità $\left| \mathbb{Z}_m \right|$
  - $\phi$ **suriettiva** $\implies$ $\exists x \mid x \ (\bmod m)$ è soluzione del sistema
    - \( \varphi(x \ (\bmod m))=\left(b_{1}\ \left( \bmod  a_{1}\right), \ldots, b_{n} \ (\bmod a_{n})\right) \), e poiché $\phi$ è suriettiva, allora ogni tupla di $n$ elementi dell'insieme di arrivo, che descrive un sistema come in ipotesi, ha una controimmagine $x \ (\bmod m)$, e $x \ (\bmod m)\in \mathbb{Z}_m$ per definizione, dunque **esiste sempre una soluzione**
  - $\phi$ **iniettiva** $\implies$ $\exists ! x \mid x \ (\bmod m)$ è soluzione del sistema
    - poiché $\phi$ è iniettiva, $x \ (\bmod m) \in \mathbb{Z}_m$ è unica, dunque **la soluzione è sempre unica**

****

# Piccolo teorema di Fermat

- \( a^{p} \equiv a \ (\bmod p) \quad \forall p \in \mathbb{P}, a \in \mathbb{Z} \)
  - \( a=0 \implies [0]^{p} =[0] \)
  - $a \gt 0 \implies$ \( [a+1]^{p}=[a+1] \implies[a]^{p}+[1]^{p}=[a+1] \implies [a]^p + [1] = [a + 1]\)
    - per ipotesi induttiva, $[a]^p = [a]$, dunque $[a] + [1] = [a + 1]$
   
## Corollario

- \( \forall[a] \in \mathbb{Z}_{p}-\{0\}, \ p \in \mathbb{P} \quad[a]^{-1}=\left[a^{p-2}\right] \)
  - poiché $[a] \neq [0]$, allora $[a]^p = [a] \iff [a]^p \cdot [a]^{-1} = [a] \cdot [a]^{-1}$, e dunque $[a]^{p -1} = [1] \implies [a] \cdot [a]^{p -2} = [1]\implies [a]^{-1} = [a]^{p-2}$



