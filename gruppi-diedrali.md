# Gruppi diedrali

## Def

- \*\*Gruppo diedrale\*\*
> - $n \in \mathbb{N}\_{\ge 2}$
> - $D\_n$ è l'\*\*insieme delle simmetrie dell'$n$-gono regolare\*\*
>   - l'insieme delle rotazioni che lasciano l'$n$-gono invariato, e delle riflessioni rispetto agli assi di simmetria
> - $\rho :=$ rotazione di $\frac{360°}{n}$ gradi di un $n$-gono regolare
> - $\sigma\_i :=$ riflessione rispetto all'$i$-esimo asse di simmetria dell'$n$-gono regolare

## Oss

- **Hp**
  - $n \in \mathbb{N}\_{\ge 2}$
  - $D\_n$ insieme delle simmetrie dell'$n$-gono regolare
- **Th**
  - $|D\_n| = 2n$
- **Dim**
  - $\rho := \frac{360°}{n} \implies$le rotazioni che lasciano l'$n$-gono invariato sono esattamente $n$
  - gli assi di simmetria di un $n$-gono sono $n$, dunque si hanno esattamente $n$ possibili riflessioni
  - $D\_n := \{\rho^0, \ldots, \rho^{n - 1}, \sigma\_0, \ldots, \sigma\_{n-1}\} \implies |D\_n| = 2n$

## Oss

- **Hp**
  - $n \in \mathbb{N}\_{\ge 2}$
  - $D\_n$ insieme delle simmetrie dell'$n$-gono regolare
  - $\cdot$ è l'operazione di composizione delle simmetrie
- **Th**
  - $(D\_n, \cdot)$ è un gruppo
- **Dim**
  - la composizione di funzioni è associativa
  - $\rho^0 = 1 = \textrm{id}$ è l'elemento neutro
  - $\left\{\begin{array}{l}\rho^{i} \cdot \rho^{j}=\rho^{i+j \ (\bmod \ n)} \\ \sigma\_{i} \cdot \sigma\_{j}=\rho^{i-j \ (\bmod \ n)} \\ \rho^{i} \cdot \sigma\_{j}=\sigma\_{i+j \ (\bmod \ n)} \\ \sigma\_{i} \cdot \rho^{j}=\sigma\_{i-j \ (\bmod \ n)}\end{array}\right.$, dunque è possibile trovare l'inverso per ogni permutazione e simmetria utilizzando queste regole

## Oss

- **Hp**
  - $D\_2$ gruppo diedrale
- **Th**
  - $(D\_2, \cdot)$ è l'unico gruppo diedrale abeliano
- **Dim**
  - $D\_2 = \{1, \rho, \sigma\_0, \sigma\_1\} \implies$ per le regole di composizione definite precedentemente $\left\{\begin{array}{l}\rho^{0} \cdot \sigma\_{0}=\sigma\_{0+0 \ (\bmod \ 2)}=\sigma\_{0}=\sigma\_{0-0 \ (\bmod \ 2)}=\sigma\_{0} \cdot \rho^{0} \quad i=j=0 \\ \rho^{0} \cdot \sigma\_{1}=\sigma\_{0+1 \ (\bmod \ 2)}=\sigma\_{1}=\sigma\_{1-0 \ (\bmod \ 2)}=\sigma\_{1} \cdot \rho^{0} \quad i = 0, j = 1 \\ \rho^{1} \cdot \sigma\_{0}=\sigma\_{1+0 \ (\bmod \ 2 )}=\sigma\_{1}=\sigma\_{0-1 \ (\bmod \ 2 )}=\sigma\_{0} \cdot \rho^1 \quad i = 1, j = 0 \\ \rho^{1} \cdot \sigma\_{1}= \sigma\_{1 + 1 \ (\bmod \ 2)} = \sigma\_0 = \sigma\_{1-1 \ (\bmod\  2)} = \sigma\_1 \cdot \rho ^1 \quad i = j = 1\end{array}\right.$, quindi il gruppo è commutativo, e dunque abeliano
  - per le regole di composizione definite precedentemente, per $n \ge 3$ la commutatività non è sempre rispettata, quindi $(D\_2, \cdot)$ è anche l'unico gruppo abeliano

## Oss

- **Hp**
  - $D\_n$ gruppo diedrale
- **Th**
  - $D\_n \hookrightarrow S\_n$
  - $\exists X \subset S\_n$ sottogruppo di $S\_n$ $\mid D\_n \cong X$
    - $D\_3 \cong S\_3$
- **Dim**
  - per ogni simmetria in $D\_n$, è possibile trovare l'unica permutazione equivalente in $S\_n$
    - ad esempio, con $n = 3$, numerando ogni vertice del triangolo equilatero, partendo dal vertice in basso a destra, si ottiene
      - $\rho^0=$$\left(\begin{array}{lll}1 & 2 & 3 \\ 1&2&3\end{array}\right)$$=\textrm{id}$
      - $\rho^1=$$\left(\begin{array}{lll}1 & 2 & 3 \\ 2 & 3 & 1\end{array}\right)$
      - $\rho^2=$$\left(\begin{array}{lll}1 & 2 & 3 \\ 3&1&2\end{array}\right)$
      - $\sigma\_0=$$\left(\begin{array}{lll}1 & 2 & 3 \\ 1&3&2\end{array}\right)$
      - $\sigma\_1=$$\left(\begin{array}{lll}1 & 2 & 3 \\ 2&1&3\end{array}\right)$
      - $\sigma\_2=$$\left(\begin{array}{lll}1 & 2 & 3 \\ 3&2&1\end{array}\right)$
  - poiché la permutazione equivalente è unica, funzione che manda una simmetria in $D\_n$ nella corrispondente permutazione in $S\_n$ è iniettiva
  - allora $D\_n \hookrightarrow S\_n$, ovvero, l'inclusione è iniettiva ma non suriettiva in generale
    - $|D\_n| \le |S\_n|$, poiché in generale $S\_n$ contiene più permutazioni di $D\_n$
  - ma per ragionamento analogo, è sempre possibile trovare un sottogruppo $X \subset S\_n \mid |X| = |D\_n| \implies$ l'inclusione è biiettiva
    - dunque, $D\_3$ risulta essere il caso particolare in cui $X = S\_n$
  - $|D\_n| \cong X$
    
    - $f: D\_n \rightarrow S\_n : a \rightarrow \sigma\_a$ è un morfismo
      - $v\_i$ vertice $i$-esimo
      - $a: v\_i \rightarrow v\_j$ è la simmetria che manda $v\_i$ in $v\_j$, che corrisponde a $\sigma\_a: i \rightarrow j$ attraverso $f$
        - $f(a) = \sigma\_a$
      - $b: v\_j \rightarrow v\_k$ è la simmetria che manda $v\_j$ in $v\_k$, che corrisponde a $\sigma\_b: j \rightarrow k$ attraverso $f$
        - $f(b) = \sigma\_b$
      - $f$ morfismo $\iff b \cdot a = v\_{\sigma\_b \cdot \sigma\_{a}}$ ⚠️ \*\*RIVEDI, PERCHÉ\*\*
          - $\left.\begin{array}{l}a(v\_i) = v\_j \\ b(v\_j) = v\_k\end{array}\right\} \implies b \cdot a = b(a(v\_i)) = v\_k$
          - $\left.\begin{array}{l}\sigma\_a(i) = j \\ \sigma\_b(j) = k\end{array}\right\} \implies \sigma\_b \cdot \sigma\_a =\sigma\_b(\sigma\_a(i)) = k$
          - quinidi $b \cdot a = b(a(v\_i)) = v\_k = v\_{\sigma\_b(\sigma\_a(i))} = v\_{\sigma\_b \cdot \sigma\_a}$
    - poiché $|D\_n| = |X|$, allora l'inclusione data da $f$ è anche suriettiva, e quindi biiettiva, dunque $f$ è un isomorfismo
  - in particolare, $D\_3 \cong S\_3$, poiché $X$ è tutto $S\_3$

## Def

- \*\*Gruppo di Klein\*\*
> - $K\_4 := \{1, a, b, c\}$
> - $a^2=b^2=c^2=1$
> - $ab=c=ba$
> - $ac=b=ca$
> - $cb=a=bc$

## Oss

- **Hp**
  - $K\_4$ è il gruppo di Klein
- **Th**
  - $K\_4 \cong D\_2$
- **Dim**
  - $K\_4:=\{1, a, b, c\}$
  - $D\_2 = \{1, \rho, \sigma\_0, \sigma\_1\}$, quindi associando gli elementi $a=\rho, b= \sigma\_0, c= \sigma\_1$ otteniamo lo stesso gruppo