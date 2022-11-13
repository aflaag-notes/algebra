# Criteri di divisibilità

\*\*\*\*

# Funzione (totiente) $\varphi$ di Eulero

- $[a] \in \mathbb{Z}_n^\*, \quad \varphi(n) := \mid \mathbb{Z}_n^\* \mid = \{0 \lt a \lt n \mid \textrm{MCD}(a, n) = 1\}$
  - $\textrm{MCD}(m, n) = 1 \implies \varphi(m \cdot n) = \varphi(m) \cdot \varphi(n)$
    - $[a]  \in \mathbb{Z}_{m n}^{\*} \iff [a] \in \mathbb{Z}_{m}^{\*} \land [a] \in \mathbb{Z}^\*_{n}$
      - _prima implicazione_
        - $a \ (\bmod n) \in \mathbb{Z}_{mn}^\* \implies \exists x \in \mathbb{Z} \mid ax \equiv 1 \ (\bmod mn)$
        - $\left.\begin{array}{l}a \mid b \\ x \equiv y \ (\bmod b)\end{array}\right\} x \equiv y \ (\bmod a) \implies \left\{\begin{array}{l}m, n \mid m n \\ a x \equiv 1\ (\bmod m n)\end{array}\iff\left\{\begin{array}{l}a x \equiv 1\ (\bmod m) \\ a x \equiv 1 \ ( \bmod n)\end{array}\right.\right.$ $\implies\left\{\begin{array}{l}{[a] \in \mathbb{Z}_{m}^{\*}} \\ {[a] \in \mathbb{Z}_{n}^{\*}}\end{array}\right.$
      - _seconda implicazione_
        - $[a] \in \mathbb{Z}_{m}^{\*} \wedge[a] \in \mathbb{Z}_{n}^{\*} \Longrightarrow \exists y, z \mid\left\{\begin{array}{l}a y \equiv 1 \ (\bmod m) \\ a z \equiv 1\ (\bmod n )\end{array}\right.$, e per il teorema cinese dei resti $\exists ! [x] \in \mathbb{Z}_{mn}$, che troviamo ponendo $\left\{\begin{array}{l}x \equiv y\ (\bmod m) \\ x \equiv z\ (\bmod n)\end{array}\right. \implies \left\{\begin{array}{l}a x \equiv a y\ (\bmod m) \\ a x \equiv a z\ (\bmod n)\end{array}\right.$ moltiplicando entrambe le equazioni per $a$, e per il sistema precedente $\left\{\begin{array}{ll}a x\equiv1 \ (\bmod m) \\ a x\equiv1 \ (\bmod n)\end{array}\right.$, e poiché $m$ e $n$ sono coprimi in ipotesi, per il teorema cinese dei resti $ax \equiv 1 \ (\bmod mn) \implies [a ] \in \mathbb{Z}_{mn}^\*$
    - allora, esiste una biezione definita come $\mathbb{Z}_{m n}^{\*} \rightarrow \mathbb{Z}_{m}^{\*} \times \mathbb{Z}_{n}^{\*}$
      - $\varphi(m \cdot n):=\left|\mathbb{Z}_{m n}^{\*}\right|=\left|\mathbb{Z}_{m}^{\*} \times \mathbb{Z}_{n}^{\*}\right|$ perché è una biezione, e dunque è pari a $\left|\mathbb{Z}_{m}^{\*}\right| \cdot\left|\mathbb{Z}_{n}^{\*}\right|=\varphi(m) \cdot \varphi(n)$

- $p \in \mathbb{P}, k \ge 1 \implies \phi(p^k) = p^{k -1}(p-1)$
  - $0 \le a \lt p^k \in \mathbb{Z}_{p^k}^\* \iff \textrm{MCD}(a, p^k)=1$, che è vero quando $p \nmid a$ poiché $p \in \mathbb{P}$
  - simmetricamente, $0 \le a \lt p^k \notin \mathbb{Z}_{p^k}^\* \iff \exists n \in \mathbb{Z} \mid a = np$
    - i multipli di $p$ sono tutti $0 \leq n p<p^{k} \implies 0 \leq n \lt p ^{k - 1}$ \*\*⚠️ INCOMPLETA\*\*
  - $\varphi \left( p^{k}\right):=\left|\mathbb{Z}_{p^{k}}^{\*}\right|=$$\left| \mathbb{Z}_{p^{k}}-\left\{[a] \in \mathbb{Z}_{p^{k}} \mid\nexists[a]^{-1} \in \mathbb{Z}_{p^{k}}\right\} \right|$ = $p^k - p^{k - 1} = p^{k - 1}(p - 1)$
- dato $n=p_{1}^{i_{1}} \cdot \ldots \cdot p_{k}^{i_k} \mid p_1, \ldots, p_k \in \mathbb{P}, i_1, \ldots, i_k \ge 1$ scomposto in fattori primi, $\varphi(n) =\varphi\left(p_{1}^{i_{1}}\right) \cdot \ldots \cdot \varphi\left(p_{k}^{i_{k}}\right)= p_1^{i_1 - 1}(p_1 - 1) \cdot \ldots \cdot p_k^{i_k - 1}(p_k -1) = p_1^{i_1} \cdot \ldots \cdot p_k^{i_k} \cdot \dfrac{p_1 - 1}{p_1} \cdot \ldots \cdot \dfrac{p_k - 1}{p_k}= n \cdot \dfrac{p_1 - 1}{p_1} \cdot \ldots \cdot \dfrac{p_k - 1}{p_k} \implies$ $\displaystyle{ \varphi(n)=n \cdot \prod_{p \mid n}\left(1-\frac{1}{p}\right) }$

## Teorema di Eulero

- $\textrm{MCD}(a, n) = 1 \implies a^{\varphi(n)} \equiv 1 \ (\bmod n)$
  - $G$ gruppo finito, $g \in G \implies o(g)   \bigg\vert \left| G \right| \implies g^{\left| G \right|} = e$
    - $a$ tale che $\textrm{MCD}(a, n)= 1 \implies [a] \in \mathbb{Z}_n^\*=[a]^{|\mathbb{Z}_n^\*|}=[a]^{\varphi(n)}=[1] \implies a^{\varphi(n)} \equiv 1 \ (\bmod n)$

\*\*\*\*

# RSA

- $p, q \in \mathbb{P} \mid p \neq q \quad n:= pq, \ \lambda(n) := \textrm{mcm}(p-1, q-1)$
  - $\lambda(n) \bigg\vert \varphi(n) = (p-1)(q-1)$ poiché $p, q \in \mathbb{P}$ \*\*⚠️ NON CAPISCO\*\*
- $\textrm{MCD}(a, n)= 1 \iff p\nmid a \land q \nmid a \implies a ^\lambda(n) \equiv 1 \ (\bmod n)$
  - $\lambda(n)$ per definizione $\implies \exists i, j \in \mathbb{Z} \mid \lambda(n)=(p-1)\cdot i = (q-1)\cdot j$
  - $p \nmid a \implies a^{p-1}\equiv 1 \ (\bmod p)$ per il piccolo teorema di Fermat
  - \*\*⚠️ NON HO CAPITO NIENTE\*\*
 
- \*\*procedimento per RSA\*\*
  - $p \neq q \in \mathbb{P}$ \*\*molto grandi\*\*
  - $n := p q$
  - $\lambda(n) := \textrm{mcm}(p-1, q-1)$
  - $e \mid 1 \lt e \lt \lambda(n) : \textrm{MCD}(e, \lambda(n))=1 \implies [e] \in \mathbb{Z}_{\lambda(n)}^\*$
    - si trova un'identità di Bézout per $e$ e $\lambda(n)$ del tipo $1 = e\cdot d + \lambda(n) \cdot k$ per certi $d, k$, ma per definizione quest'identità implica che $e  d \equiv 1 \ (\bmod \lambda(n))$
  - $d:= e^{-1} \ (\bmod \lambda(n))$ viene calcolato tramite l'algoritmo di Euclide
  - $n, e$ \*\*pubbliche\*\*, $d$ \*\*privata\*\*
      - $n, d, e$ sono tali che $(a^e)^d \equiv a  \ (\bmod n), \ \textrm{MCD}(a, n)=1$
        - $\left\{\begin{array}{l}e d \equiv 1\ (\bmod \lambda(n)) \\ a^{\lambda(n)} \equiv 1\ (\bmod n)\end{array}\right.$
        - \*\*⚠️ NON HO CAPITO NIENTE\*\*
