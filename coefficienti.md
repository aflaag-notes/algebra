# Coefficienti binomiali

- \( \left(\begin{array}{l}n \\ k\end{array}\right):=\left\{\begin{array}{ll}\frac{n !}{n !(n-k) !} & k \leqslant n \\ 0 & k>n\end{array}\right. \)
  - $0! := 1$
- \( \left(\begin{array}{l}n \\ k\end{array}\right)=\left(\begin{array}{c}n \\ n-k\end{array}\right) \)
  - \( \left(\begin{array}{c}n \\ n-k\end{array}\right)=\dfrac{n !}{(n-k) !(n-(n-k)) !}=\dfrac{n !}{(n-k) ! k !}= \left(\begin{array}{l}n \\ n\end{array}\right) \)
- \( \left(\begin{array}{l}n \\ k\end{array}\right)=\left(\begin{array}{l}n-1 \\ k+1\end{array}\right)+\left(\begin{array}{c}n-1 \\ k\end{array}\right) \)
   - $\binom{n - 1}{k +1}+ \binom{n - 1}{k}=$\(\frac{(n-1) !}{(k+1) !(n-1-(k+1)) !}+\frac{(n-1) !}{k !(n-1-k) !} \) \(=\frac{(n-1) !}{(k+1) k !(n-2-k) !}+\frac{(n-1) !}{k !(n-1-k) !} =\) $\frac{(n-1-k)(n-1) !+(k+1)(n-1) !}{(k+1) !(n-k-1) !}=$ \( \frac{(n-1) !(n-1-k+k+1)}{(k+1) !(n-1-k) !}= \) \( \frac{(n-1) ! \cdot n}{(n+1) !(n-1-k) !} =\) \( \frac{n !}{(k+1) !(n-k-1) !}=\binom{n}{k + 1} \)

****

# Teorema del binomio di newton

- $\forall a, b \in A$ anello commutativo, $\forall n \in \mathbb{N} \quad (a+b )^n = \displaystyle{\sum_{k = 0}^{n}{\binom{n}{k} a^k b ^{n - k}}}$
  - $n = 0 \implies (a+b)^0 = \displaystyle{\sum_{k = 0}^{0}{\binom{0}{k}a^kb^{0 - k}}} = \binom{0}{0}a^0b^0=1$
  - $(a+ b)^{n + 1} = (a+b)^{n }\cdot (a+b)$
  - ⚠️ **INCOMPLETA**

****

## Lemma

- $p \in \mathbb{P} \implies$ \( p \ \bigg\vert  \left(\begin{array}{l}p \\ k\end{array}\right) \quad \forall 0<k<p \)
  - \( \displaystyle{\binom{p}{k}=\frac{p !}{k !(\rho-k) !} = \frac{p \cdot (p - 1) !}{k!(p - k)!} = p \cdot \frac{(p - 1)!}{k!(p- k)!}} \implies p\) è nella fattorizzazione di $\displaystyle{\binom{n}{k}}$
  - poiché $p$ è primo in ipotesi, non è possibile semplificarlo con nessun fattore del denominatore
    - $k \lt p \implies p$ non può essere nella fattorizzazione di $k!$
    - $p - k \lt p \implies p$ non può essere nella fattorizzazione di $(p - k)!$
- \( \forall n \in \mathbb{Z}, p \in \mathbb{P},[a] \in \mathbb{Z}_{p} \quad p \mid n \implies n \cdot [a] = [0]\)
  - $p \mid n \implies \exists k \in \mathbb{Z} | pk = n$
  - \( n \cdot[a]=[a]+\ldots+[a] = [n \cdot a]\)
    - $[pk \cdot a] = p \cdot [ka] \implies [pka]$ è multiplo di $p$, e quindi $n \cdot[a] = [pka] = [0]$ in $\mathbb{Z}_p$
  - per il lemma precedente, $\displaystyle{p \ \bigg\vert \binom{p}{k}}$, quindi $\displaystyle{\binom{p}{k} \cdot [a] = [0]} \quad \forall [a] \in \mathbb{Z}_p, k \in \mathbb{Z} \mid 0 \lt k \lt p$

## Corollario

- \( \forall p \in \mathbb{P} \quad ([a]+[b])^{p}=[a]^{p}+[b]^{p} \  \) in $\mathbb{Z}_p$
  - \( ([a]+[b])^{p}=\)\(\displaystyle \sum_{k=0}^{p}\left(\begin{array}{l}p \\ k\end{array}\right)[a]^{k}\cdot[b]^{p-k}=\sum_{k=0}^{p}\left(\begin{array}{l}p \\ k\end{array}\right)\left[a^{k} \cdot b^{p-k}\right] \)
    - \( p \in \mathbb{P} \implies \displaystyle{p \ \bigg\vert \left(\begin{array}{l}p \\ k\end{array}\right)} \implies \left(\begin{array}{l}p \\ k\end{array}\right)\left[\begin{array}{l}a^{k} \cdot b^{p-k}\end{array}\right]= [0] \quad \forall k \in \mathbb{Z} \mid 0 \lt k \lt p\)
      - di conseguenza, nella sommatoria tutti i termini con $k \in (0, p)$ si annullano, in quanto congruenti a $[0]$ in $\mathbb{Z}_p$
      - \(\displaystyle ([a]+[b])^{p}=\sum_{k=0}^{p}\left(\begin{array}{l}p \\ k\end{array}\right)\left[a^{k} \cdot b^{p-k}\right]= \left(\begin{array}{l}p \\ 0\end{array}\right)[b]^{p}+\left(\begin{array}{l}p \\ p\end{array}\right)[a]^{p}=[a]^{p}+[b]^{p} \)
- \( \left(\left[a_{1}\right]+\ldots+\left[a_{n}\right]\right)^{p}=\left[a_{1}\right]^{p}+\ldots+\left[a_{n}\right]^{p} \)
  - $n = 1 \implies$ \( \left[a_{1}\right]^{p}=\left[a_{1}\right]^{p} \)
  - \( n>1 \implies\left(\left[a_{1}\right]+\ldots+\left[a_{n}\right]+\left[a_{n+1}\right]\right)^{p}=  \left[a_{1}\right]^{p}+\ldots+\left[a_{n}\right]^{p}+\left[a_{n+1}\right]^{p} \)
    - per ipotesi induttiva, \( \left[a_{1}\right]^{p}+\ldots+\left[a_{n}\right]^{p}+\left[a_{n+1}\right]^{p}=  \left(\left[a_{1}\right]+\ldots+\left[a_{n}\right]\right)^{p}+\left[a_{n+1}\right]^{p}=  \left(\left[a_{1}\right]+\ldots+\left[a_{n+1}\right]\right)^{p} \)
