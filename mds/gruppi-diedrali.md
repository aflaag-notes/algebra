# Gruppi diedrali

## Def

- **Gruppo diedrale**

> - $n \in \mathbb{N}_{\ge 2}$
> - $\mathcal{D}_n$ è l'**insieme delle simmetrie dell'$n$-gono regolare**
>   - l'insieme delle rotazioni che lasciano l'$n$-gono invariato, e delle riflessioni rispetto agli assi di simmetria
> - $\rho :=$ rotazione di $\frac{360°}{n}$ gradi di un $n$-gono regolare
> - $\sigma_i :=$ riflessione rispetto all'$i$-esimo asse di simmetria dell'$n$-gono regolare

## Oss

- **Hp**
  - $n \in \mathbb{N}_{\ge 2}$
  - $\mathcal{D}_n$ insieme delle simmetrie dell'$n$-gono regolare
- **Th**
  - $|\mathcal{D}_n| = 2n$
- **Dim**
  - $\rho := \frac{360°}{n} \implies$le rotazioni che lasciano l'$n$-gono invariato sono esattamente $n$
  - gli assi di simmetria di un $n$-gono sono $n$, dunque si hanno esattamente $n$ possibili riflessioni
  - $\mathcal{D}_n := \{\rho^0, \ldots, \rho^{n - 1}, \sigma_0, \ldots, \sigma_{n-1}\} \implies |\mathcal{D}_n| = 2n$

## Oss

- **Hp**
  - $n \in \mathbb{N}_{\ge 2}$
  - $\mathcal{D}_n$ insieme delle simmetrie dell'$n$-gono regolare
  - $\cdot$ è l'operazione di composizione delle simmetrie
- **Th**
  - $(\mathcal{D}_n, \cdot)$ è un gruppo
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
  - $\mathcal{D}_n$ gruppo diedrale
- **Th**
  - $\mathcal{D}_n \hookrightarrow \mathcal{S}_n$
  - $\exists X \subset \mathcal{S}_n$ sottogruppo di $\mathcal{S}_n$ $\mid \mathcal{D}_n \cong X$
    - $\mathcal{D}_3 \cong \mathcal{S}_3$
- **Dim**
  - per ogni simmetria in $\mathcal{D}_n$, è possibile trovare l'unica permutazione equivalente in $\mathcal{S}_n$
    - ad esempio, con $n = 3$, numerando ogni vertice del triangolo equilatero, partendo dal vertice in basso a destra, si ottiene
      - $\rho^0=$$\left(\begin{array}{lll}1 & 2 & 3 \\ 1&2&3\end{array}\right)$$=\textrm{id}$
      - $\rho^1=$$\left(\begin{array}{lll}1 & 2 & 3 \\ 2 & 3 & 1\end{array}\right)$
      - $\rho^2=$$\left(\begin{array}{lll}1 & 2 & 3 \\ 3&1&2\end{array}\right)$
      - $\sigma_0=$$\left(\begin{array}{lll}1 & 2 & 3 \\ 1&3&2\end{array}\right)$
      - $\sigma_1=$$\left(\begin{array}{lll}1 & 2 & 3 \\ 2&1&3\end{array}\right)$
      - $\sigma_2=$$\left(\begin{array}{lll}1 & 2 & 3 \\ 3&2&1\end{array}\right)$
  - poiché la permutazione equivalente è unica, funzione che manda una simmetria in $\mathcal{D}_n$ nella corrispondente permutazione in $\mathcal{S}_n$ è iniettiva
  - allora $\mathcal{D}_n \hookrightarrow \mathcal{S}_n$, ovvero, l'inclusione è iniettiva ma non suriettiva in generale
    - $|\mathcal{D}_n| \le |\mathcal{S}_n|$, poiché in generale $\mathcal{S}_n$ contiene più permutazioni di $\mathcal{D}_n$
  - ma per ragionamento analogo, è sempre possibile trovare un sottogruppo $X \subset \mathcal{S}_n \mid |X| = |\mathcal{D}_n| \implies$ l'inclusione è biiettiva
    - dunque, $\mathcal{D}_3$ risulta essere il caso particolare in cui $X = \mathcal{S}_n$
  - $|\mathcal{D}_n| \cong X$
    
    - $f: \mathcal{D}_n \rightarrow \mathcal{S}_n : a \rightarrow \sigma_a$ è un morfismo
      - $v_i$ vertice $i$-esimo
      - $a: v_i \rightarrow v_j$ è la simmetria che manda $v_i$ in $v_j$, che corrisponde a $\sigma_a: i \rightarrow j$ attraverso $f$
        - $f(a) = \sigma_a$
      - $b: v_j \rightarrow v_k$ è la simmetria che manda $v_j$ in $v_k$, che corrisponde a $\sigma_b: j \rightarrow k$ attraverso $f$
        - $f(b) = \sigma_b$
      - $f$ morfismo $\iff b \cdot a = v_{\sigma_b \cdot \sigma_{a}}$
          - $\left.\begin{array}{l}a(v_i) = v_j \\ b(v_j) = v_k\end{array}\right\} \implies b \cdot a = b(a(v_i)) = v_k$
          - $\left.\begin{array}{l}\sigma_a(i) = j \\ \sigma_b(j) = k\end{array}\right\} \implies \sigma_b \cdot \sigma_a =\sigma_b(\sigma_a(i)) = k$
          - quinidi $b \cdot a = b(a(v_i)) = v_k = v_{\sigma_b(\sigma_a(i))} = v_{\sigma_b \cdot \sigma_a}$
    - poiché $|\mathcal{D}_n| = |X|$, allora l'inclusione data da $f$ è anche suriettiva, e quindi biiettiva, dunque $f$ è un isomorfismo
  - in particolare, $\mathcal{D}_3 \cong \mathcal{S}_3$, poiché $X$ è tutto $\mathcal{S}_3$

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
