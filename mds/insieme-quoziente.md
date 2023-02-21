# Insieme quoziente

## Def

- **Insieme quoziente**

> - $G$ gruppo
> - $\sim$ relazione di equivalenza in $G$
> - $x \in G$
> - $[x]:=\{y \in G \mid x \sim y\}$
> - $G/\sim := \{[x] \mid x \in G\}$ è detto **insieme quoziente**
>   - corrisponde all'insieme delle classi di equivalenza determinate da $\sim$

## Def

- **Insieme quoziente $\mathbb{Z}_n$**

> - $n \in \mathbb{Z}$
> - $\mathbb{Z}_n := \mathbb{Z} / \equiv$ è detto **insieme quoziente $\mathbb{Z}_n$**

## Oss

- **Hp**
    - $n \in \mathbb{Z}$
    - $I(n) := \{nk \mid k \in \mathbb{Z}\}$
- **Th**
    - $\mathbb{Z}_n = \{[0], [1], \ldots, [n - 1]\}$
- **Dim**
    - $\forall x \in \mathbb{Z} \quad [x] := \{ y \in \mathbb{Z} \mid x \equiv y \ (\bmod \ n) \iff n \mid x - y \iff \exists q \in \mathbb{Z} \mid n q = x - y \iff x - y \in I(n)\} \implies \mathbb{Z}/I(n) = \mathbb{Z}/\equiv \ =: \mathbb{Z}_n$
    - allora necessariamente $\mathbb{Z}_n = \{[0], [1], \ldots, [n - 1]\}$

## Oss

- **Hp**
  - $n \in \mathbb{Z}$
- **Th**
  - $\mathbb{Z}_n$ dominio di integrità $\iff n \in \mathbb{P}$
- **Dim**
  - _prima implicazione_
    - per assurdo, $n \notin \mathbb{P} \implies \exists a, b \in (0, n) \mid n = ab$, in particolare $a, b \neq 0$
    - $n = ab \implies [0] = [n] = [ab]$ in $\mathbb{Z}_n$
    - $\mathbb{Z}_n$ dominio di integrità $\implies$ in $\mathbb{Z}_n$ vale la legge di annullamento del prodotto, allora $[ab] = [0] \iff [a] = 0 \lor [b] = [0] \ \bot$
  - _seconda implicazione_
    - per assurdo, $\mathbb{Z}_n$ non dominio di integrità $\implies \exists[a] \in \mathbb{Z}_n - \{[0]\} : a \mid 0 \iff \exists b \in \mathbb{Z} - \{[0]\} \mid [0] = [a][b] = [ab] \iff 0 \equiv ab \ (\bmod \  n) \iff n \mid ab$
    - $n \in \mathbb{P}$, allora $n \mid ab \implies n \mid a \lor n \mid b$ per dimostrazione precedente, allora
      - $n \mid a \implies [a] = [n] = [0]$ in $\mathbb{Z}_n \ \bot$
      - $n \mid b \implies [b] = [n] = [0]$ in $\mathbb{Z}_n \ \bot$

## Oss

- **Hp**
  - $n \in \mathbb{Z}$
  - $[a] \in \mathbb{Z}_n \quad$
- **Th**
  - $[a] \in \mathbb{Z}^*_n \iff \textrm{MCD}(a, n) = 1$
- **Dim**
  - _prima implicazione_
    - $[a] \in \mathbb{Z}_n^* \implies \exists b \in \mathbb{Z} \mid [a][b] = [1] \quad 0 \lt b \lt n \iff ab \equiv 1 \ (\bmod \ n) \iff n \mid 1 - ab \iff \exists k \in \mathbb{Z} \mid nk = 1 - ab \iff 1 = nk + ab$
    - $d : = \textrm{MCD}(a, n) \implies d \mid a \land d \mid n \implies \left \{ \begin{array}{l} d \mid a \implies \exists x \in \mathbb{Z} \mid dx = a \\ d \mid n \implies \exists y \in \mathbb{Z} \mid dy = n \end{array} \right. \implies 1 = nk + ab \iff 1 = dyk + dxb = d(yk + xb) \implies \exists yk + xb \in \mathbb{Z} \mid 1 = d(yk +xb) \implies d \mid 1$
    - $d \mid 1 \iff d = \pm 1$, ma $d := \textrm{MCD}(a, n) \implies d \ge 0 \implies d = 1$
  - _seconda implicazione_
    - ⚠️ **questo verso non è totalmente corretto**
    - $d := \textrm{MCD}(a, n) = 1$
    - per dimostrazione precedente, $I(d) = I(a, n) \implies d \in I(a, n) \implies \exists b, k \in \mathbb{Z} \mid d = ab + nk$ per definizione di $I(a, n)$, allora $d = 1 = ab + nk \iff nk = 1 - ab \iff n \mid 1 - ab \iff ab \equiv 1 \ (\bmod \ n) \implies [a][b] = [1]$ in $\mathbb{Z}_n \iff [a] \in \mathbb{Z}_n^*$

## Oss

- **Hp**
  - $p \in \mathbb{P}$
- **Th**
  - $\mathbb{Z}_p$ campo
- **Dim**
  - $\mathbb{Z}_p^* := \{[x] \in \mathbb{Z}_p \mid \exists[x]^{-1} \in \mathbb{Z}_p\}$
  - $p \in \mathbb{P} \implies \forall x \in [1, p - 1] \quad \textrm{MCD}(x, p) = 1$
  - allora $\mathbb{Z}_p^* = \mathbb{Z}_p - \{[0]\} \implies \mathbb{Z}_p$ campo

## Oss

- **Hp**
    - $p \in \mathbb{P}$
- **Th**
    - $(\mathbb{Z}_p, \cdot)$ ciclico
- **Dim**
    - ⚠️ **manca la dimostrazione**

****

# Funzione totiente di Eulero

## Def

- **Funzione totiente di Eulero**

> - $\varphi(n) : \mathbb{N} \rightarrow \mathbb{N}: n \rightarrow |\mathbb{Z}_n^* |$ è detta **funzione totiente di Eulero**

## Oss

- **Hp**
  - $m, n \in \mathbb{N} \mid \textrm{MCD}(m, n) = 1$
- **Th**
  - $\varphi(m \cdot n) = \varphi(m) \cdot \varphi(n)$
- **Dim**
    - sia $f: \mathbb{Z}_{m n}^{*} \rightarrow \mathbb{Z}_{m}^{*} \times \mathbb{Z}_{n}^{*}$
    - per il teorema cinese dei resti, si ha che $[a] \in \mathbb{Z}_{mn}^* \iff \exists x \in \mathbb{Z} \mid ax \equiv 1 \ (\bmod \ \ mn) \iff \left\{\begin{array}{l}a x \equiv 1\ (\bmod \ m) \\ a x \equiv 1 \ ( \bmod \ n)\end{array}\right.\iff\left\{\begin{array}{l}{[a] \in \mathbb{Z}_{m}^{*}} \\ {[a] \in \mathbb{Z}_{n}^{*}}\end{array}\right. \iff f$ biettiva $\implies \phi(m \cdot n) := \left|\mathbb{Z}_{m n}^{*}\right|=\left|\mathbb{Z}_{m}^{*} \times \mathbb{Z}_{n}^{*}\right|=\left|\mathbb{Z}_{m}^{*}\right| \cdot\left|\mathbb{Z}_{n}^{*}\right| =\varphi(m) \cdot \varphi(n)$

## Oss

- **Hp**
    - $p \in \mathbb{P}$
    - $k \in \mathbb{N} - \{0\}$
- **Th**
    - $\varphi(p^k) = p^{k -1}(p-1)$
- **Dim**
  <!-- - $\forall 0 \le a \lt p^k  \quad [a]\in \mathbb{Z}_{p^k}^* \iff \textrm{MCD}(a, p^k)=1$, che è vero quando $p \nmid a$ poiché $p \in \mathbb{P}$ -->
  - $\forall 0 \le a \lt p^k \quad [a] \notin \mathbb{Z}_{p^k}^* \iff \textrm{MCD}(a, p^k) \neq 1 \iff p \mid a$, poiché $p \in \mathbb{P}$
  - $\forall 0 \le a \lt p^k \quad p \mid a \iff \exists n \in \mathbb{Z} \mid a = np \implies 0 \leq n p<p^{k} \iff 0 \leq n \lt p ^{k - 1} \implies$ gli elementi non invertibili in $\mathbb{Z}_{p^k}$ sono $p^{k - 1}$
  - allora $\varphi \left( p^{k}\right):=\left|\mathbb{Z}_{p^{k}}^{*}\right|=$$\left| \mathbb{Z}_{p^{k}}-\left\{[a] \in \mathbb{Z}_{p^{k}} \mid\nexists[a]^{-1} \in \mathbb{Z}_{p^{k}}\right\} \right|$ = $p^k - p^{k - 1} = p^{k - 1}(p - 1)$

## Oss

- **Hp**
    - $k \in \mathbb{N} - \{0\}$
    - $p_1, \ldots, p_k \in \mathbb{P}$
    - $i_1, \ldots, i_k \in \mathbb{Z}_{\ge 1}$
    - $n \in \mathbb{N} \mid n = p_1^{i_1} \cdot \ldots \cdot p_k^{i_k}$ 
- **Th**
    - $\displaystyle\varphi(n)=n \cdot \prod_{p \mid n}\left(1-\frac{1}{p}\right)$
- **Dim**
  - per dimostrazione precedente $\varphi(n) =\varphi\left(p_{1}^{i_{1}}\right) \cdot \ldots \cdot \varphi\left(p_{k}^{i_{k}}\right)= p_1^{i_1 - 1}(p_1 - 1) \cdot \ldots \cdot p_k^{i_k - 1}(p_k -1) = p_1^{i_1} \cdot \ldots \cdot p_k^{i_k} \cdot \dfrac{p_1 - 1}{p_1} \cdot \ldots \cdot \dfrac{p_k - 1}{p_k}= n \cdot \dfrac{p_1 - 1}{p_1} \cdot \ldots \cdot \dfrac{p_k - 1}{p_k} \implies$ $\displaystyle{ \varphi(n)=n \cdot \prod_{p \mid n}\left(1-\frac{1}{p}\right) }$

