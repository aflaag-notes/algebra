# Gruppi diedrali

## Def

- **Gruppo diedrale**
> - $n \in \mathbb{N}_{\ge 2}$
> - $D_n$ è l'**insieme delle simmetrie dell'$n$-gono regolare**
>   - l'insieme delle rotazioni che lasciano l'$n$-gono invariato, e delle riflessioni rispetto agli assi di simmetria
> - $\rho :=$ rotazione di $\frac{360°}{n}$ gradi di un $n$-gono regolare
> - $\sigma_i :=$ riflessione rispetto all'$i$-esimo asse di simmetria dell'$n$-gono regolare

## Oss

- **Hp**
  - $n \in \mathbb{N}_{\ge 2}$
  - $D_n$ insieme delle simmetrie dell'$n$-gono regolare
- **Th**
  - $|D_n| = 2n$
- **Dim**
  - $\rho := \frac{360°}{n} \implies$le rotazioni che lasciano l'$n$-gono invariato sono esattamente $n$
  - gli assi di simmetria di un $n$-gono sono $n$, dunque si hanno esattamente $n$ possibili riflessioni
  - $D_n := \{\rho^0, \ldots, \rho^{n - 1}, \sigma_0, \ldots, \sigma_{n-1}\} \implies |D_n| = 2n$

## Oss

- **Hp**
  - $n \in \mathbb{N}_{\ge 2}$
  - $D_n$ insieme delle simmetrie dell'$n$-gono regolare
  - $\cdot$ è l'operazione di composizione delle simmetrie
- **Th**
  - $(D_n, \cdot)$ è un gruppo
- **Dim**
  - la composizione di funzioni è associativa
  - $\rho^0 = 1 = \textrm{id}$ è l'elemento neutro
  - $\left\{\begin{array}{l}\rho^{i} \cdot \rho^{j}=\rho^{i+j \ (\bmod \ n)} \\ \sigma_{i} \cdot \sigma_{j}=\rho^{i-j \ (\bmod \ n)} \\ \rho^{i} \cdot \sigma_{j}=\sigma_{i+j \ (\bmod \ n)} \\ \sigma_{i} \cdot \rho^{j}=\sigma_{i-j \ (\bmod \ n)}\end{array}\right.$, dunque è possibile trovare l'inverso per ogni permutazione e simmetria utilizzando queste regole

## Oss

- **Hp**
  - $D_2$ gruppo diedrale
- **Th**
  - $(D_2, \cdot)$ è l'unico gruppo diedrale abeliano
- **Dim**
  - $D_2 = \{1, \rho, \sigma_0, \sigma_1\} \implies$ per le regole di composizione definite precedentemente $\left\{\begin{array}{l}\rho^{0} \cdot \sigma_{0}=\sigma_{0+0 \ (\bmod \ 2)}=\sigma_{0}=\sigma_{0-0 \ (\bmod \ 2)}=\sigma_{0} \cdot \rho^{0} \quad i=j=0 \\ \rho^{0} \cdot \sigma_{1}=\sigma_{0+1 \ (\bmod \ 2)}=\sigma_{1}=\sigma_{1-0 \ (\bmod \ 2)}=\sigma_{1} \cdot \rho^{0} \quad i = 0, j = 1 \\ \rho^{1} \cdot \sigma_{0}=\sigma_{1+0 \ (\bmod \ 2 )}=\sigma_{1}=\sigma_{0-1 \ (\bmod \ 2 )}=\sigma_{0} \cdot \rho^1 \quad i = 1, j = 0 \\ \rho^{1} \cdot \sigma_{1}= \sigma_{1 + 1 \ (\bmod \ 2)} = \sigma_0 = \sigma_{1-1 \ (\bmod\  2)} = \sigma_1 \cdot \rho ^1 \quad i = j = 1\end{array}\right.$, quindi il gruppo è commutativo, e dunque abeliano
  - per le regole di composizione definite precedentemente, per $n \ge 3$ la commutatività non è sempre rispettata, quindi $(D_2, \cdot)$ è anche l'unico gruppo abeliano

## Oss

- **Hp**
  - $D_n$ gruppo diedrale
- **Th**
  - $D_n \hookrightarrow S_n$
  - $\exists X \subset S_n$ sottogruppo di $S_n$ $\mid D_n \cong X$
    - $D_3 \cong S_3$
- **Dim**
  - per ogni simmetria in $D_n$, è possibile trovare l'unica permutazione equivalente in $S_n$
    - ad esempio, con $n = 3$, numerando ogni vertice del triangolo equilatero, partendo dal vertice in basso a destra, si ottiene
      - $\rho^0=$$\left(\begin{array}{lll}1 & 2 & 3 \\ 1&2&3\end{array}\right)$$=\textrm{id}$
      - $\rho^1=$$\left(\begin{array}{lll}1 & 2 & 3 \\ 2 & 3 & 1\end{array}\right)$
      - $\rho^2=$$\left(\begin{array}{lll}1 & 2 & 3 \\ 3&1&2\end{array}\right)$
      - $\sigma_0=$$\left(\begin{array}{lll}1 & 2 & 3 \\ 1&3&2\end{array}\right)$
      - $\sigma_1=$$\left(\begin{array}{lll}1 & 2 & 3 \\ 2&1&3\end{array}\right)$
      - $\sigma_2=$$\left(\begin{array}{lll}1 & 2 & 3 \\ 3&2&1\end{array}\right)$
  - poiché la permutazione equivalente è unica, funzione che manda una simmetria in $D_n$ nella corrispondente permutazione in $S_n$ è iniettiva
  - allora $D_n \hookrightarrow S_n$, ovvero, l'inclusione è iniettiva ma non suriettiva in generale
    - $|D_n| \le |S_n|$, poiché in generale $S_n$ contiene più permutazioni di $D_n$
  - ma per ragionamento analogo, è sempre possibile trovare un sottogruppo $X \subset S_n \mid |X| = |D_n| \implies$ l'inclusione è biiettiva
    - dunque, $D_3$ risulta essere il caso particolare in cui $X = S_n$
  - $|D_n| \cong X$
    
    - $f: D_n \rightarrow S_n : a \rightarrow \sigma_a$ è un morfismo
      - $v_i$ vertice $i$-esimo
      - $a: v_i \rightarrow v_j$ è la simmetria che manda $v_i$ in $v_j$, che corrisponde a $\sigma_a: i \rightarrow j$ attraverso $f$
        - $f(a) = \sigma_a$
      - $b: v_j \rightarrow v_k$ è la simmetria che manda $v_j$ in $v_k$, che corrisponde a $\sigma_b: j \rightarrow k$ attraverso $f$
        - $f(b) = \sigma_b$
      - $f$ morfismo $\iff b \cdot a = v_{\sigma_b \cdot \sigma_{a}}$ ⚠️ **RIVEDI, PERCHÉ**
          - $\left.\begin{array}{l}a(v_i) = v_j \\ b(v_j) = v_k\end{array}\right\} \implies b \cdot a = b(a(v_i)) = v_k$
          - $\left.\begin{array}{l}\sigma_a(i) = j \\ \sigma_b(j) = k\end{array}\right\} \implies \sigma_b \cdot \sigma_a =\sigma_b(\sigma_a(i)) = k$
          - quinidi $b \cdot a = b(a(v_i)) = v_k = v_{\sigma_b(\sigma_a(i))} = v_{\sigma_b \cdot \sigma_a}$
    - poiché $|D_n| = |X|$, allora l'inclusione data da $f$ è anche suriettiva, e quindi biiettiva, dunque $f$ è un isomorfismo
  - in particolare, $D_3 \cong S_3$, poiché $X$ è tutto $S_3$

## Def

- **Gruppo di Klein**
> - $K_4 := \{1, a, b, c\}$
> - $a^2=b^2=c^2=1$
> - $ab=c=ba$
> - $ac=b=ca$
> - $cb=a=bc$

## Oss

- **Hp**
  - $K_4$ è il gruppo di Klein
- **Th**
  - $K_4 \cong D_2$
- **Dim**
  - $K_4:=\{1, a, b, c\}$
  - $D_2 = \{1, \rho, \sigma_0, \sigma_1\}$, quindi associando gli elementi $a=\rho, b= \sigma_0, c= \sigma_1$ si ottiene lo stesso gruppo
