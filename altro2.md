# Criteri di divisibilità

****

# RSA

- $p, q \in \mathbb{P} \mid p \neq q \quad n:= pq, \ \lambda(n) := \textrm{mcm}(p-1, q-1)$
  - $\lambda(n) \bigg\vert \varphi(n) = (p-1)(q-1)$ poiché $p, q \in \mathbb{P}$ ** NON CAPISCO**
- $\textrm{MCD}(a, n)= 1 \iff p\nmid a \land q \nmid a \implies a ^\lambda(n) \equiv 1 \ (\bmod n)$
  - $\lambda(n)$ per definizione $\implies \exists i, j \in \mathbb{Z} \mid \lambda(n)=(p-1)\cdot i = (q-1)\cdot j$
  - $p \nmid a \implies a^{p-1}\equiv 1 \ (\bmod p)$ per il piccolo teorema di Fermat
  - **z NON HO CAPITO NIENTE**
 
- **procedimento per RSA**
  - $p \neq q \in \mathbb{P}$ **molto grandi**
  - $n := p q$
  - $\lambda(n) := \textrm{mcm}(p-1, q-1)$
    - si trova un'identità di Bézout per $e$ e $\lambda(n)$ del tipo $1 = e\cdot d + \lambda(n) \cdot k$ per certi $d, k$, ma per definizione quest'identità implica che $e  d \equiv 1 \ (\bmod \lambda(n))$
  - $d:= e^{-1} \ (\bmod \lambda(n))$ viene calcolato tramite l'algoritmo di Euclide
  - $n, e$ **pubbliche**, $d$ **privata**
      - $n, d, e$ sono tali che $(a^e)^d \equiv a  \ (\bmod n), \ \textrm{MCD}(a, n)=1$
        - $\left\{\begin{array}{l}e d \equiv 1\ (\bmod \lambda(n)) \\ a^{\lambda(n)} \equiv 1\ (\bmod n)\end{array}\right.$
        - ** NON HO CAPITO NIENTE**
