# Coefficienti binomiali

## Def

- **Coefficiente binomiale**
> - $0! := 1$
> - $n, k \in \mathbb{N}$
> - $\left(\begin{array}{l}n \\ k\end{array}\right):=\left\{\begin{array}{ll}\frac{n !}{n !(n-k) !} & k \leqslant n \\ 0 & k>n\end{array}\right.$

## Oss

- **Hp**
  - $n, k \in \mathbb{N}$
- **Th**
  - $\left(\begin{array}{l}n \\ k\end{array}\right)=\left(\begin{array}{c}n \\ n-k\end{array}\right)$
- **Dim**
  - $\left(\begin{array}{c}n \\ n-k\end{array}\right)=\dfrac{n !}{(n-k) !(n-(n-k)) !}=\dfrac{n !}{(n-k) ! k !}= \left(\begin{array}{l}n \\ n\end{array}\right)$

## Oss

- **Hp**
  - $n, k \in \mathbb{N}$
- **Th**
  - $\left(\begin{array}{c}n \\ k+1\end{array}\right)=\left(\begin{array}{l}n-1 \\ k+1\end{array}\right)+\left(\begin{array}{c}n-1 \\ k\end{array}\right)$
- **Dim**
   - $\binom{n - 1}{k +1}+ \binom{n - 1}{k}=$$\frac{(n-1) !}{(k+1) !(n-1-(k+1)) !}+\frac{(n-1) !}{k !(n-1-k) !}$ $=\frac{(n-1) !}{(k+1) k !(n-2-k) !}+\frac{(n-1) !}{k !(n-1-k) !} =$ $\frac{(n-1-k)(n-1) !+(k+1)(n-1) !}{(k+1) !(n-k-1) !}=$ $\frac{(n-1) !(n-1-k+k+1)}{(k+1) !(n-1-k) !}=$ $\frac{(n-1) ! \cdot n}{(n+1) !(n-1-k) !} =$ $\frac{n !}{(k+1) !(n-k-1) !}=\binom{n}{k + 1}$

## Lem

- **Hp**
  - $p \in \mathbb{P}$
  - $k \in \mathbb{N} \mid 0 \lt k \lt p$
- **Th**
  - $p \ \bigg\vert  \left(\begin{array}{l}p \\ k\end{array}\right)$
- **Dim**
  - $\displaystyle{\binom{p}{k}=\frac{p !}{k !(p-k) !} = \frac{p \cdot (p - 1) !}{k!(p - k)!} = p \cdot \frac{(p - 1)!}{k!(p- k)!}} \implies p$ è nella fattorizzazione di $\displaystyle{\binom{p}{k}}$
  - poiché $p$ è primo in ipotesi, non è possibile semplificarlo con nessun fattore del denominatore
    - $k \lt p \implies p$ non può essere nella fattorizzazione di $k!$
    - $p - k \lt p \implies p$ non può essere nella fattorizzazione di $(p - k)!$
  - quindi necessariamente $p \ \bigg\vert  \left(\begin{array}{l}p \\ k\end{array}\right)$

## Oss

- **Hp**
  - $n \in \mathbb{Z}$
  - $p \in \mathbb{P} : p \mid n$
  - $[a] \in \mathbb{Z}_{p}$
- **Th**
  - $n \cdot [a] = [0]$ in $\mathbb{Z}_p$
- **Dim**
  - $p \mid n \implies \exists k \in \mathbb{Z} \mid pk = n$
  - $n \cdot[a]=[a]+\ldots+[a] = [n \cdot a] = [pk \cdot a] = p \cdot [ka]$
  - $[pka]$ è multiplo di $p$ per definizione, e quindi $[pka] = [0]$ in $\mathbb{Z}_p$, quindi $n \cdot [a] = [pka] = [0]$ in $\mathbb{Z}_p$

## Oss

- **Hp**
  - $n \in \mathbb{Z}$
  - $p \in \mathbb{P} : p \mid n$
  - $[a] \in \mathbb{Z}_{p}$
  - $k \in \mathbb{N} \mid 0 \lt k \lt p$
- **Th**
  - $\displaystyle \binom{p}{k} \cdot [a] = [0]$ in $\mathbb{Z}_p$
- **Dim**
  - $\left(\begin{array}{l}p \\ k\end{array}\right) \cdot[a]=\left[\left(\begin{array}{l}p \\ k\end{array}\right) \cdot a\right]$
  - per il dimostrazione precedente, $\displaystyle{p \ \bigg\vert \binom{p}{k}}$, quindi $\left(\begin{array}{l}p \\ k\end{array}\right) \cdot a$ è anch'esso multiplo di $p$, e di conseguenza  $\left[\left(\begin{array}{l}p \\ k\end{array}\right) \cdot a\right] = [0]$ in $\mathbb{Z}_p$

## Cor

- **Hp**
  - $p \in \mathbb{P}$
  - $[a], [b] \in \mathbb{Z}_p$
- **Th**
  - $([a]+[b])^{p}=[a]^{p}+[b]^{p}$ in $\mathbb{Z}_p$
- **Dim**
  - per il teorema del binomio di Newton $([a]+[b])^{p}=$$\displaystyle \sum_{k=0}^{p}\left(\begin{array}{l}p \\ k\end{array}\right)[a]^{k}\cdot[b]^{p-k}=\sum_{k=0}^{p}\left(\begin{array}{l}p \\ k\end{array}\right)\left[a^{k} \cdot b^{p-k}\right]$
  -  per dimostrazione precedente $p \in \mathbb{P} \implies \left(\begin{array}{l}p \\ k\end{array}\right)\left[\begin{array}{l}a^{k} \cdot b^{p-k}\end{array}\right]= [0] \quad \forall k \in \mathbb{Z} \mid 0 \lt k \lt p$
    - di conseguenza, nella sommatoria del binomio di Newton tutti i termini con $k \in (0, p)$ si annullano, in quanto congruenti a $[0]$ in $\mathbb{Z}_p$
    - $\displaystyle ([a]+[b])^{p}=\sum_{k=0}^{p}\left(\begin{array}{l}p \\ k\end{array}\right)\left[a^{k} \cdot b^{p-k}\right]= \left(\begin{array}{l}p \\ 0\end{array}\right)[b]^{p}+\left(\begin{array}{l}p \\ p\end{array}\right)[a]^{p}=[a]^{p}+[b]^{p}$

## Cor

- **Hp**
  - $p \in \mathbb{P}$
  - $[a_1], \ldots, [a_n] \in \mathbb{Z}_p$
- **Th**
  - $\left(\left[a_{1}\right]+\ldots+\left[a_{n}\right]\right)^{p}=\left[a_{1}\right]^{p}+\ldots+\left[a_{n}\right]^{p}$ in $\mathbb{Z}_p$
- **Dim**

  - $n = 1 \implies$ $\left[a_{1}\right]^{p}=\left[a_{1}\right]^{p}$ per dimostrazione precedente
  - $n>1 \implies\left(\left[a_{1}\right]+\ldots+\left[a_{n}\right]+\left[a_{n+1}\right]\right)^{p}=  \left[a_{1}\right]^{p}+\ldots+\left[a_{n}\right]^{p}+\left[a_{n+1}\right]^{p}$
    - per ipotesi induttiva, $\left[a_{1}\right]^{p}+\ldots+\left[a_{n}\right]^{p}+\left[a_{n+1}\right]^{p}=  \left(\left[a_{1}\right]+\ldots+\left[a_{n}\right]\right)^{p}+\left[a_{n+1}\right]^{p}$
    - allora, ancora per ipotesi induttiva $\left(\left[a_{1}\right]+\ldots+\left[a_{n}\right]\right)^{p}+\left[a_{n+1}\right]^{p}=  \left(\left[a_{1}\right]+\ldots+\left[a_{n+1}\right]\right)^{p}$
