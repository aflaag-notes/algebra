# Teorema fondamentale dell'algebra

- **Hp**
  - $\mathbb{K}$ campo
  - $p(x) \in \mathbb{K}[x] \mid p(x) = a_{0}x^0 + \ldots +a_{n} x^{n}$
- **Th**
  - $\exists z \in \mathbb{C} \mid p(z) = 0$

****

# Teorema della divisione euclidea con il resto

- **Hp**
  - $m \in \mathbb{Z}$
  - $n \in \mathbb{Z} - \{0\}$
- **Th**
  - $\exists !  \ q, r \in \mathbb{Z} \mid m=n q+r \quad 0 \leq r<n$
- **Dim**
  - _esistenza_
    - sia $[m] \in \mathbb{Z}_n$
    - $a \equiv m \ (\bmod \ n) \iff \exists p_1 \in \mathbb{Z} \mid np_1 = m - a$
    - $r:=\min(\{a \in \mathbb{Z} \mid a \in [m], a \ge 0\})$
    - $r \in [m] \iff \exists p_2 \in \mathbb{Z} \mid np_2 = m - r  \iff r = m - np_2 \iff m = np_2 +r$
    - ⚠️ **INCOMPLETA**

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $a(x), b(x) \in \mathbb{K}[x] \mid b(x) \neq 0$
- **Th**
    - $\exists ! q(x), r(x) \in \mathbb{K}[x] \mid a(x) = b(x) \cdot q(x) + r(x) \quad \deg(r(x)) \lt \deg(b(x))$, che è detto _teorema della divisione con il resto tra polinomi_

****

# Teorema di Lagrange

- **Hp**
  - $G$ gruppo finito
  - $H \subset G$ sottogruppo finito
- **Th**
  - $|G| = |H| \cdot |G / H|$
- **Dim**
  - $G$ è decomponibile attraverso l'unione disgiunta delle sue classi laterali sinistre, poiché ogni relazione di equivalenza induce una partizione per dimostrazione precedente
  - in particolare, ogni classe laterale sinistra è equivalente a $xH$ per opportuni $x \in G$, e hanno tutte cardinalità $|H|$ per dimostrazione precedente
  - $G = X_1 \coprod X_2 \coprod \ldots \coprod X_k \implies |G| = |X_1| + |X_2| + \ldots  + |X_k|$ poiché ogni $X_i$ è una partizione, e dunque disgiunta con le altre, e poiché sono tutte classi laterali sinistre hanno tutte cardinalità $|H|$
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
    - $\mathbb{P} := \{p \in \mathbb{N} \mid p$ primo$\}$
    - $\forall n \in \mathbb{N} - \{0\} \quad \exists ! n_2, n_3, n_5, \ldots, n_p \in \mathbb{N} \mid p \in \mathbb{P} : n = 2^{n_2} \cdot 3 ^ {n_3} \cdot \ldots \cdot p ^ {n_p}$
      - $p \nmid n \implies n_p = 0 \implies p ^  {n_p} = 1$, dunque non influisce nella produttoria
    - $\displaystyle{n = \prod_{p \in \mathbb{P}}^{} p ^{n_p}}$, quindi è possibile riscrivere anche $a$ e $b$ tramite i loro fattori primi come  $\displaystyle{a=\prod_{p \in \mathbb{P}} p^{a_{p}}}$ e $\displaystyle{b=\prod_{p \in \mathbb{P}} p^{b_{p}} }$
    - $d:= \textrm{MCD}(a, b)$ e $m:=\textrm{mcm}(a, b)$
      - per definizione di $d$ ed $m$, e attraverso le regole che permettono di trovarli tramite le fattorizzazioni di $a$ e $b$, è possibile riscrivere $d$ ed $m$ come $\displaystyle{d = \prod_{p \in \mathbb{P}} p^{\min(a_p, b_p)}}$ e $\displaystyle{m = \prod_{p \in \mathbb{P}} p^{\max(a_p, b_p)}}$
      - $d \cdot m =\displaystyle{\prod_{p \in \mathbb{P}} p^{\min(a_p, b_p)}} \cdot \displaystyle{\prod_{p \in \mathbb{P}} p^{\max(a_p, b_p)}} = \displaystyle{\prod_{p \in \mathbb{P}} p^{\min(a_p, b_p) + \max(a_p, b_p)}}$
    - $\forall a, b \in \mathbb{N} \quad a + b = \min(a, b) + \max(a, b)$
      - $a = \min(a, b) \implies \max(a, b) = b$, e viceversa
    - $d \cdot m = \displaystyle{\prod_{p \in \mathbb{P} }p ^{a_p + b_p}} = \displaystyle{\prod_{p \in \mathbb{P}} p^{a_p}} \cdot \displaystyle{\prod_{p \in \mathbb{P}} p^{b_p}} = a \cdot b$

****

# Teorema cinese dei resti

## Lem

- **Hp**
  - $a_1, \ldots, a_n \ge 2 \in \mathbb{Z}  \mid \textrm{MCD}(a_i, a_j) = 1 \quad \forall i, j \in [1, n] : i \neq j$
  - $m := \textrm{mcm}(a_1, \ldots, a_n)$
- **Th**
  - $m = a_1 \cdot \ldots \cdot a_n$
- **Dim**
  - $\textrm{MCD}(a_i, a_j) = 1 \implies \forall p \in \mathbb{P} \quad p \mid a_i \implies p \nmid a_j$, poiché altrimenti $p \mid \textrm{MCD}(a_i, a_j)$
  - prese le fattorizzazioni $\displaystyle a_1 = \prod_{p \in \mathbb{P}}{p^{a_{1_p}}} \ \ldots \ a_n = \prod_{p \in \mathbb{P}}{p^{a_{n_p}}}$, allora $\forall p \in \mathbb{P} \quad a_{i_p} \gt 0 \implies a_{j_p} = 0 \quad \forall i \neq j$, dunque ogni fattore è presente solo in una delle fattorizzazioni degli $n$ interi, poiché coprimi
    - $a_{k_p} = 0 \implies p^{a_{k_p}} = 1 \implies$ non compare nella fattorizzazione
  - di conseguenza, la somma degli esponenti di $p$ su tutte le fattorizzazioni degli $n$ interi, sarà il numero stesso, poiché nelle altre fattorizzazioni varrà $0$, e quindi $\forall p \in \mathbb{P} \quad a_{1_p} + \ldots + a_{n_p} = \max(a_{1_p}, \ldots, a_{n_p})$
  - allora $m = \displaystyle \prod_{p \in \mathbb{P}}{p^{\max(a_{1_p}, \ldots, a_{n_p})}}=\prod_{p \in \mathbb{P}}{p^{a_{1_p} + \ldots + a_{n_p}}} = \prod_{p \in \mathbb{P}}{p^{a_{1_p}}} \cdot \ldots \cdot \prod_{p \in \mathbb{P}}{p^{a_{n_p}}} = a_1 \cdot \ldots \cdot a_n$
    
## Lem

- **Hp**
  - $n \in \mathbb{N}$
  - $a_1, \ldots, a_n \in \mathbb{Z}_{n \ge 2}$
  - $m:= \textrm{mcm}(a_1, \ldots, a_n)$
- **Th**
  - $\exists \phi \mid \phi: \mathbb{Z}_m \rightarrow \mathbb{Z}_{a_1} \times \ldots \times \mathbb{Z}_{a_n}: x \ (\bmod \ m) \rightarrow (x \ (\bmod \ a_1), \ldots, x \ (\bmod \ a_n))$
  - $\phi$ è una funzione ben definita, ed è iniettiva
- **Dim**
  - $\phi$ ben definita $\implies \phi$ non dipende dalla scelta di $[x] \in \mathbb{Z}_m$
  - se $\phi$ è ben definita, allora $x\equiv x^{\prime} \ (\bmod \ m) \implies \left\{\begin{array}{c}x \equiv x^{\prime}\ \left(\bmod \ a_{1}\right) \\ \vdots \\ x \equiv x^{\prime}\ \left(\bmod \ a_{n}\right)\end{array}\right.$
  - $\left\{\begin{array}{c}x \equiv x^{\prime}\ \left(\bmod \ a_{1}\right) \\ \vdots \\ x \equiv x^{\prime}\ \left(\bmod \ a_{n}\right)\end{array}\right. \iff \left\{\begin{array}{c}x^{\prime}-x \in I\left(a_{1}\right) \\ \vdots \\ x^{\prime}-x \in I\left(a_{n}\right)\end{array}\right. \iff x - x^\prime \in I(a_1) \cap \ldots \cap I(a_n) = I(m)$, e per definizione $x - x^\prime \in I(m) \implies x \equiv x^\prime \ (\bmod \ m)$
  - poiché tale osservazione è valida in entrambe i versi dell'implicazione, $\phi$ risulta essere iniettiva

## Teorema cinese dei resti

- **Hp**
  - $n \in \mathbb{N}$
  - $a_1, \ldots, a_n \in \mathbb{Z}_{\ge 2} \mid \forall i, j \in [1, n] \quad i \neq j \implies \textrm{MCD}(a_i, a_j) = 1$
  - $b_1, \ldots, b_n \in \mathbb{Z} \mid 0 \leq b_{1}<a_{1}, \ldots, 0 \leq b_n \lt a_n$
  - $m := \textrm{mcm}(a_1, \ldots, a_n)$
- **Th**
  - $\exists ! x \ (\bmod \ m) \mid$ $\left\{\begin{array}{c}x \equiv b_{1}\ \left(\bmod  \ a_{1}\right) \\ \vdots \\ x \equiv b_{n}\ \left(\bmod  \ a_{n}\right)\end{array}\right.$
- **Dim**
  - per il primo lemma $m = a_1 \cdot \ldots \cdot a_n$ poiché coprimi a due a due in ipotesi
  - per il secondo lemma $m = \textrm{mcm}(a_1, \ldots, a_n) \implies \exists \phi : \mathbb{Z}_m \rightarrow \mathbb{Z}_ {a_1} \times \cdots \times \mathbb{Z}_{a_n}$ ben definita e iniettiva
  - $\left|X_{1} \times \cdots \times X_{n}\right|=\left|X_{1}\right| \cdot\ldots\cdot\left|X_{n}\right| \implies$ $\left|\mathbb{Z}_{a_{1}} \times \ldots \times \mathbb{Z}_{a_{n}}\right|=\left|\mathbb{Z}_{a_{1}}\right| \cdot\ldots\cdot\left|\mathbb{Z}_{a_{n}}\right|$
    - $\mathbb{Z}_n := \{[0],[1], \cdots,[n-1]\} \implies \left|\mathbb{Z}_{n}\right|=n$, quindi $\left|\mathbb{Z}_{a_{1}}\right| \cdot\ldots\cdot\left|\mathbb{Z}_{a_{n}}\right|  = a_1 \cdot \ldots \cdot a_n = m = \left| \mathbb{Z}_m \right|$ per ragionamento analogo
  - $|X|=|Y|<\infty \implies f: X \rightarrow Y$ iniettiva $\iff$ $f$ suriettiva
    - applicando questa osservazione, $\phi$ iniettiva $\implies \phi$ suriettiva, in quanto, per l'osservazione precedente, insieme di partenza e di arrivo di $\phi$ hanno la stessa cardinalità $\left| \mathbb{Z}_m \right|$
  - $\phi$ suriettiva $\implies$ $\exists x \mid x \ (\bmod m)$ è soluzione del sistema
    - $\varphi(x \ (\bmod m))=\left(b_{1}\ \left( \bmod  a_{1}\right), \ldots, b_{n} \ (\bmod a_{n})\right)$, e poiché $\phi$ è suriettiva, allora ogni tupla di $n$ elementi dell'insieme di arrivo, che descrive un sistema come in ipotesi, ha una controimmagine $x \ (\bmod m)$, e $x \ (\bmod m)\in \mathbb{Z}_m$ per definizione, dunque _esiste sempre una soluzione_
  - $\phi$ iniettiva $\implies$ $\exists ! x \mid x \ (\bmod m)$ è soluzione del sistema
    - poiché $\phi$ è iniettiva, $x \ (\bmod m) \in \mathbb{Z}_m$ è unica, dunque _la soluzione è sempre unica_

## Cor

- **Hp**
    - $k \in \mathbb{N}$
    - $n_1, \ldots, n_k \in \mathbb{N} - \{0\} \mid \forall i, j \in [1, k] \quad i \neq j \implies \textrm{MCD}(n_i, n_j) = 1$
    - $N := \textrm{mcm}(n_1, \ldots, n_k)$
    - $[a] \in \mathbb{Z}_N^*$
    - $o := o([a])$ in $\mathbb{Z}_N^*$
    - $\forall h \in [1, k] \quad o_h := o([a])$ in $\mathbb{Z}_{n_h}^*$
- **Th**
    - $o = \textrm{mcm}(o_1, \ldots, o_k)$
- **Dim**
    - per il primo lemma del teorema cinese dei resti $N = n_1 \cdot \ldots \cdot n_k$ poiché coprimi a due a due in ipotesi
    - per il teorema cinese dei resti $a^o \equiv 1 \ (\bmod \ N) \implies \left\{\begin{array}{c}a^o \equiv 1 \ (\bmod \ n_1) \\ \vdots \\ a^o \equiv 1 \ (\bmod \ n_k)\end{array}\right.$ poiché $n_1, \ldots, n_k$ coprimi a due a due in ipotesi
    - per dimostrazione precedente, $o_1$ è il più piccolo esponente di $[a]$ per cui $[a]^{o_1} = 1$ in $\mathbb{Z}_{n_1}^*$, ma questo implica che $\forall k \in \mathbb{Z} \quad ([a]^{o_1})^k = 1$ in $\mathbb{Z}_{n_1}^*$, e allora necessariamente $a^o \equiv 1 \ (\bmod \ n_1)$ implica che $o$ sia un multiplo di $o_1$
    - per ragionamento analogo, vale il seguente sistema $\left\{\begin{array}{c}o_1 \mid o \\ \vdots \\ o_k \mid o \end{array}\right. \implies \textrm{mcm}(o_1, \ldots, o_k) \mid o$
    - sia $m := \textrm{mcm}(o_1, \ldots, o_k)$
    - per definizione $\left\{\begin{array}{c}o_1 \mid m \\ \vdots \\ o_k \mid m \end{array}\right.$
    - per ragionamento analogo all'osservazione precedente, si ottiene che $\left\{\begin{array}{c}a^m \equiv 1 \ (\bmod \ n_1) \\ \vdots \\ a^m \equiv  1 \ (\bmod \ n_k)\end{array}\right. \implies a^m \equiv 1 \ (\bmod \ N) \implies o \mid m$
    - $m \mid o \land o \mid m \implies o = m$

****

# Teorema del binomio di Newton

- **Hp**
  - $A$ anello commutativo
  - $a, b \in A$
  - $n \in \mathbb{N}$
- **Th**
  - $(a+b )^n = \displaystyle{\sum_{k = 0}^{n}{\binom{n}{k} a^k b ^{n - k}}}$
- **Dim**
  - $n = 0 \implies (a+b)^0 = \displaystyle{\sum_{k = 0}^{0}{\binom{0}{k}a^kb^{0 - k}}} = \binom{0}{0}a^0b^0=1$
  - $(a+ b)^{n + 1} = (a+b)^{n }\cdot (a+b)$
  - ⚠️ **INCOMPLETA**

## Cor

- ⚠️ **NON HO CAPITO UN CAZZO**

****

# Piccolo teorema di Fermat

- **Hp**
  - $p \in \mathbb{P}$
  - $a \in \mathbb{Z}$
- **Th**
  - $a^{p} \equiv a \ (\bmod \ p)$
- **Dim**
  - _prima dimostrazione_
    - $a=0 \implies [0]^{p} =[0]$
    - $a \gt 0 \implies$ $[a+1]^{p}=[a+1]$
      - per definizione di $+$, si ottiene che $[a +1] = [a] + [1] \iff [a+1]^p = ([a] + [1])^p$, e per dimostrazione precedente, $([a]+[1])^p = [a]^p +[1]^p$ in $\mathbb{Z}_p$
      - $[a+1]^{p}=[a+1] \iff [a]^{p}+[1]^{p}=[a+1] \implies [a]^p + [1] = [a + 1] \iff [a]^p = [a + 1] -[1] = [a]$, che coincide con l'ipotesi induttiva
  - _seconda dimostrazione_
    - $p \in \mathbb{P} \implies \mathbb{Z}_p^* = \mathbb{Z} - \{[0]\}$ per dimostrazione precedente, e dunque $|\mathbb{Z}_p^*| = p - 1$
    - $[a] \in \mathbb{Z}_p \mid [a] = [0] \implies [0^p]=[0]$, che è vero $\forall p \in \mathbb{P}$
    - $[a] \in \mathbb{Z}_p \mid [a] \neq [0] \implies [a] \in \mathbb{Z}_p^*$ per osservazione precedente
      - per dimostrazione precedente, $[a]^{|\mathbb{Z}_p^*|}=[1] \iff [a]^{p - 1} = [1] \iff [a]^p \cdot [a]^{-1} = [1] \iff [a]^p = [a]$
   
## Cor

- **Hp**
  - $p \in \mathbb{P}$
  - $[a] \in \mathbb{Z}_{p}-\{0\}$
- **Th**
  - $[a]^{-1}=\left[a\right]^{p-2}$
- **Dim**
  - $[a] \neq [0] \implies \exists[a]^{-1} \in \mathbb{Z}_p$, poiché, per dimostrazione precedente $\mathbb{Z}_p^* = \mathbb{Z_p} - \{0\}$
  -  per il teorema di Fermat $[a]^p = [a] \iff [a]^p \cdot [a]^{-1} = [a] \cdot [a]^{-1} \iff [a]^{p -1} = [1] \iff [a] \cdot [a]^{p -2} = [1]\iff [a]^{-1} = [a]^{p-2}$

## Cor

- **Hp**
    - $p \in \mathbb{P}$
- **Th**
    - $\displaystyle \prod_{0 \lt a \lt p} (x - a) \equiv x^{p - 1} - 1 \ (\bmod \ p)$
- **Dim**
    - per il piccolo teorema di Fermat $a^p \equiv a \iff a^{p - 1} \equiv 1  \iff a^{p - 1} - 1 \equiv 0\ (\bmod \ p)$, che è equivalente a dire che $[a]$ è radice del polinomio $x^{p -1 } - [1] \in \mathbb{Z}_p[x]$
    - per dimostrazione precedente $\forall 0 \lt a \lt p \quad [a]^{p - 1} - 1 = [0] \implies x - [a] \mid x^{p -1} - [1]$, ovvero $\displaystyle \prod_{0 \lt a \lt p} (x - [a]) \mid x^{p - 1} - [1] \implies \exists c \in \mathbb{N} \mid x^{p - 1} - [1] = c \cdot \displaystyle \prod_{0 \lt a \lt p} (x - [a])$
    - poiché $x^{p- 1}-[1]$ e $\displaystyle \prod_{0 \lt a \lt p} (x - [a])$ sono due polinomi il cui coefficiente direttore è $1$, allora necessariamente $c = 1$, per cui segue la tesi

## Cor

- ⚠️ **NON HO CAPITO UN CAZZO**

****

# Teorema di Eulero

- **Hp**
    - $a, n \in \mathbb{N} \mid \textrm{MCD}(a, n) = 1$
- **Th**
    - $a^{\varphi(n)} \equiv 1 \ (\bmod \ n)$
- **Dim**
    - per dimostrazione precedente $\textrm{MCD}(a, n) = 1 \implies [a] \in \mathbb{Z}_n^*$
    - per dimostrazione precedente $[a] ^ {|\mathbb{Z}_n^*|} = [1]$
    - per definizione $\varphi(n) := |\mathbb{Z}_n^*|$, e dunque $a ^{\varphi(n)} \equiv 1 \ (\bmod \ n)$

****

# Teorema fondamentale di isomorfismo

- **Hp**
    - $A, B$ anelli
    - $f: A \rightarrow B$ morfismo di anelli
- **Th**
    - $A / \textrm{ker}(f) \cong \textrm{im}(f)$, ovvero $\exists \varphi \mid \varphi : A / \textrm{ker}(f) \rightarrow \textrm{im}(f): [a] \rightarrow f(a)$ isomorfismo di anelli
- **Dim**
    - $\varphi$ è ben definita
    - $\varphi$ è ben definita $\iff [x] = [y] \implies f(x) = f(y) \quad \forall x, y \in A$
    - $[x] = [y] \iff x \equiv y \ (\bmod \ \textrm{ker}(f)) \implies y - x \in \textrm{ker}(f) \implies f(y - x) = 0_B$ per definizione
    - $f(y - x) = f(y + (-x))$, e $-x \in A$ perche $A$ è un anello
    - per dimostrazione precedente $f$ morfismo $\implies f(x^{-1}) = f(x)^{-1}$, e dunque rispetto a $+$ in $A$ si ottiene che $\forall x \in A \quad f(-x) = -f(x)$
    - dunque, $f(y-x) = f(y)-f(x) \iff 0_B = f(y) - f(x) \iff f(y) = f(x)$
    - $\varphi$ morfismo di anelli
    - $\varphi$ morfismo di anelli $\iff \varphi([a]) \cdot \varphi([b]) = \varphi([a]\cdot [b])$ e $\varphi([a]) + \varphi([b]) = \varphi([a]+ [b])$
      - $\varphi([a]) \cdot \varphi([b]) = f(a) \cdot f(b)$ per definizione di $\varphi$
      - $f(a) \cdot f(b) = f(a\cdot b)$ per morfismo di $f$
      - $f(a \cdot b ) = \varphi([a \cdot b])$ per definizione di $\varphi$
      - $\varphi([a \cdot b]) = \varphi([a] \cdot [b])$ per definizione di $\cdot$
      - per $+$ vale il ragionamento analogo
    - $\varphi$ isomorfismo di anelli $\iff \varphi$ iniettiva e suriettiva
    - $\varphi$ iniettiva
      - $\varphi$ iniettiva $\iff \textrm{ker}(\varphi)=\{[0_A]\}$ per dimostrazione precedente
      - $x \in \textrm{ker}(f) \iff x - 0_A \in \textrm{ker}(f) \implies x \equiv 0_A \ (\bmod \ \textrm{ker}(f)) \implies [x] = [0_A] \implies \varphi([x]) = \varphi([0_A])$, poiché $\varphi$ è ben definita, dunque $f(x) = 0_B$
    - $\varphi$ suriettiva
      - $\varphi : A / \textrm{ker}(f) \rightarrow \textrm{im}(f) \implies$ l'insieme di arrivo di $\varphi$ coincide è proprio l'insieme delle immagini di $f$, quindi $\varphi$ è suriettiva per costruzione

## Oss

- **Hp**
  - $G, H$ gruppi
  - $f: G \rightarrow H$ morfismo di gruppi
- **Th**
  - $G / \textrm{ker}(f) \cong \textrm{im}(f)$, o alternativamente $\exists \varphi \mid \varphi : G / \textrm{ker}(f) \rightarrow \textrm{im}(f): [g] \rightarrow f(g)$ isomorfismo di gruppi
- **Dim**
  - la dimostrazione è analoga al caso degli anelli

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $V, W$ spazi vettoriali su $\mathbb{K}$
    - $f:V \rightarrow W$ trasformazione lineare
- **Th**
    - $V/\ker(f) \cong \textrm{im}(f)$, o alternativamente $\exists \varphi \mid \varphi : V/\ker(f) \rightarrow \textrm{im}(f):[v] \rightarrow f(v)$
- **Dim**
    - la dimostrazione è analoga al caso degli anelli

****

# Teorema di Cauchy

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
  - $G \cong \mathbb{Z}_4$ oppure $G \cong K_4$
- **Dim**
  - ⚠️ **L'HO SCRITTA MA NON HO CAPITO NIENTE IN QUESTA DIMOSTRAZIONE**
  - preso $a \in G \mid a \neq 1$, per dimostrazione precedente $o(a) \bigg\vert |G| \implies o(a)=1 \lor o(a) =2 \lor o(a) = 4$, ma $a \neq 1 \implies o(a) \neq 1$
  - 2 casi
    - $\exists x \in G \mid o(x)=4 \implies G \cong \mathbb{Z}_4$ **⚠️ PERCHÉ?**
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
      - quindi $G \cong K_4$ **⚠️ PERCHÉ? non mancano altre cose?**

****

# Teorema di Carnot

- **Hp**
    - $n \in \mathbb{N} - \{0\}$ 
    - $u, v \in \mathbb{K}^n \mid u = \left(\begin{array}{c}x_1 \\ \vdots \\ x_n \end{array}\right), v = \left(\begin{array}{c}y_1 \\ \vdots \\ y_n \end{array}\right)$
    - $\theta$ l'angolo compreso tra $u$ e $v$
- **Th**
    - $||v - u||^2 = ||u||^2 + ||v||^2 - 2\cos(\theta) \cdot||u||\cdot ||v||$

## Cor

- **Hp**
    - $n \in \mathbb{N} - \{0\}$ 
    - $u, v \in \mathbb{K}^n \mid u = \left(\begin{array}{c}x_1 \\ \vdots \\ x_n \end{array}\right), v = \left(\begin{array}{c}y_1 \\ \vdots \\ y_n \end{array}\right)$
    - $\theta$ l'angolo compreso tra $u$ e $v$
- **Th**
    - $\cos(\theta)= \dfrac{u \cdot v}{||u|| \cdot ||v||}$
- **Dim**
    - per il teorema di Carnot $||v - u||^2 = ||u||^2 + ||v||^2 - 2\cos(\theta) \cdot ||u||\cdot ||v|| \iff - 2\cos(\theta) \cdot||u||\cdot ||v|| = ||v - u||^2 - ||u||^2 - ||v||^2 = \displaystyle \sum_{i = 1}^n{(y_i -x_i)^2}- \sum_{i= 1}^n{y_i^2} - \sum_{i = 1}^n{x_i^2} = \sum_{i = 1}^n{\left((y_i - x_i)^2 - x_i^2 - y_i^2 \right)} = \sum_{i = 1}^n{\left(y_i^2 - 2y_ix_i + x_i^2 -y_i^2 -x_i^2 \right)} = - 2 \sum_{i = 1}^n{x_iy_i} = -2(u \cdot v)$
    - $-2\cos(\theta) \cdot ||u|| \cdot ||v|| = -2(u \cdot v) \iff \cos(\theta)= \dfrac{u \cdot v}{||u|| \cdot ||v||}$
****

# Teorema del rango

- **Hp**
    - $\mathbb{K}$ campo
    - $V, W$ spazi vettoriali su $\mathbb{K}$
    - $f:V \rightarrow W$ trasformazione lineare
- **Th**
    - $\textrm{rk}(f) = \dim(V) - \dim(\ker(f))$
- **Dim**
    - per dimostrazione precedente di ha che $\ker(f) \subset V$ sottospazio vettoriale
    - allora, per dimostrazione precedente si ottiene che $\dim(V/\ker(f)) = \dim(V) - \dim(\ker(f))$
    - per il teorema di isomorfismo tra spazi vettoriali, si ha che $V/\ker(f) \cong \textrm{im}(f)$, e per dimostrazione precedente questo implica che $\dim(V/\ker(f)) = \dim(\textrm{im}(f))$
    - allora, segue che $\textrm{rk}(f) := \dim(\textrm{im}(f)) = \dim(V) - \dim(\ker(f))$

****

# Teorema di Rouché-Capelli

- **Hp**
    - $\mathbb{K}$ campo
    - $m, n \in \mathbb{N} - \{0\}$
    - $A \in \textrm{Mat}_{m \times n}(\mathbb{K})$
    - $b \in \textrm{Mat}_{m \times 1}(\mathbb{K})$
- **Th**
    - $\exists x \in \textrm{Mat}_{n \times 1}(\mathbb{K}) \mid A\cdot x = b \iff \textrm{rk}(A) = \textrm{rk}(A_b)$
- **Dim**
    - $\exists x \in \textrm{Mat}_{n \times 1}(\mathbb{K}) \mid A\cdot x = b \iff \exists x_1, \ldots, x_n \in \mathbb{K} \mid x_1A^1 + \ldots + x_nA^n=b \iff b \in \textrm{span}(A^1, \ldots, A^n) \subset \textrm{span}(A^1, \ldots, A^n, b)$
    - $b \in \textrm{span}(A^1, \ldots, A^n) \implies \exists \mu_1, \ldots, \mu_n \mid v = \mu_1A^1 + \ldots + \mu_n A^n$
    - $\forall v \in \textrm{span}(A^1, \ldots, A^n, b) \quad \exists \lambda_1, \ldots, \lambda_n, c \in \mathbb{K} \mid v = \lambda_1A^1 + \ldots + \lambda_nA^n + cb = \lambda_1A^1 + \ldots + \lambda_nA^n + c(\mu_1A^1 + \ldots + \mu_nA^n) = (\lambda_1 + c\mu_1)A^1 + \ldots + (\lambda_n + c\mu_n)A^n \implies v \in \textrm{span}(A^1, \ldots, A^n) \implies \textrm{span}(A^1, \ldots, A^n, b) \subset \textrm{span}(A^1, \ldots, A^n)$
    - allora $\textrm{span}(A^1, \ldots, A^n) = \textrm{span}(A^1, \ldots, A^n, b) \iff \dim(\textrm{span}(A^1, \ldots, A^n)) = \dim(\textrm{span}(A^1, \ldots, A^n, b))$
    - per dimostrazione precedente $\dim(\textrm{span}(A^1, \ldots, A^n)) = \textrm{rk}(A)$, e analogamente $\dim(\textrm{span}(A^1, \ldots, A^n, b)) = \textrm{rk}(A_b)$
    - allora $\dim(\textrm{span}(A^1, \ldots, A^n)) = \dim(\textrm{span}(A^1, \ldots, A^n, b)) \iff \textrm{rk}(A) = \textrm{rk}(A_b)$

****

# Teorema di Cramer

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N} - \{0\}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K}) \mid \det(A) \neq 0$
    - $b \in \textrm{Mat}_{n \times 1}(\mathbb{K})$
- **Th**
    - $\left\{\begin{array}{c}x_1 = \dfrac{1}{\det(A)} \cdot \det\left(\begin{array}{cccc}b_1 & a_{1,2} &\cdots & a_{1,n} \\ \vdots & \vdots & \ddots & \vdots \\ b_n & a_{n, 2} & \cdots & a_{n,n}\end{array}\right) \\ \vdots \\ x_n = \dfrac{1}{\det(A)} \cdot \det\left(\begin{array}{cccc}a_{1,1} & \cdots & a_{1,n-1} & b_1\\ \vdots & \ddots & \vdots & \vdots \\ a_{n, 1} & \cdots & a_{n,n-1} & b_n\end{array}\right) \end{array}\right.$ sono le componenti del vettore $x \in \textrm{Mat}_{n \times 1}(\mathbb{K}) \mid A \cdot x = b$

****

# Teorema di Kronecker

- **Hp**
    - $\mathbb{K}$ campo
    - $n, r, r' \in \mathbb{N} - \{0\} \mid r \lt r' \lt n$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
    - $M_1 \in \textrm{Mat}_{r \times r}(\mathbb{K}) \mid M_1$ minore di $A \land \det(A) \neq 0$
- **Th**
    - $\textrm{rk}(A)=r \iff \forall M_1'$ orlato di $M_1 \quad \det(M_1') = 0 \iff \forall M_2 \in \textrm{Mat}_{r' \times r'}(\mathbb{K}) \mid M_2$ minore di $A \quad \det(M_2) = 0$

****

# Teorema di Binet

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N} - \{0\}$
    - $A, B \in \textrm{Mat}_{n \times n}(\mathbb{K})$
- **Th**
    - $\det(A \cdot B) = \det(A) \cdot \det(B)$

## Cor

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N} - \{0\}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K})$
- **Th**
    - $\det(A)^{-1}=\det(A^{-1})$
- **Dim**
    - $\det(A\cdot A^{-1})=\det(I_n)=1$
    - $\det(A \cdot A^{-1}) = \det(A) \cdot \det(A^{-1})$ per il teorema di Binet
    - allora $\det(A) \cdot \det(A^{-1}) = 1 \iff \det(A)^{-1}=\det(A^{-1})$

****

# Teorema spettrale

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N} - \{0\}$
    - $A \in \textrm{Mat}_{n \times n}(\mathbb{K}) \mid A$ simmetrica
    1. $\forall \lambda \in \textrm{sp}(A) \quad \lambda \in \mathbb{R}$
    2. $A$ diagonalizzabile
    3. $\exists B^1, \ldots, B^n$ autovettori di $A \mid B^1, \ldots, B^n$ base ortonormale di $\mathbb{R}^n$
    4. $\exists B \in O(n) \mid B^{-1}AB$ diagonale
- **Th**
    - le proposizioni sono equivalenti
