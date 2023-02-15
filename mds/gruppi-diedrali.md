# Gruppi diedrali

## Def

- **Gruppo diedrale**

> - $n \in \mathbb{N}_{\ge 2}$
> - $\mathcal{D}_n$ è l'**insieme delle simmetrie dell'$n$-gono regolare**, ed è detto **gruppo diedrale di ordine $n$**
>   - è formato dall'insieme delle rotazioni che lasciano l'$n$-gono invariato, e delle riflessioni rispetto agli assi di simmetria
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
  - $\mathcal{D}_2$ gruppo diedrale
- **Th**
  - $(\mathcal{D}_2, \cdot)$ è l'unico gruppo diedrale abeliano
- **Dim**
  - $\mathcal{D}_2 = \{1, \rho, \sigma_0, \sigma_1\} \implies$ per le regole di composizione definite precedentemente $\left\{\begin{array}{l}\rho^{0} \cdot \sigma_{0}=\sigma_{0+0 \ (\bmod \ 2)}=\sigma_{0}=\sigma_{0-0 \ (\bmod \ 2)}=\sigma_{0} \cdot \rho^{0} \quad i=j=0 \\ \rho^{0} \cdot \sigma_{1}=\sigma_{0+1 \ (\bmod \ 2)}=\sigma_{1}=\sigma_{1-0 \ (\bmod \ 2)}=\sigma_{1} \cdot \rho^{0} \quad i = 0, j = 1 \\ \rho^{1} \cdot \sigma_{0}=\sigma_{1+0 \ (\bmod \ 2 )}=\sigma_{1}=\sigma_{0-1 \ (\bmod \ 2 )}=\sigma_{0} \cdot \rho^1 \quad i = 1, j = 0 \\ \rho^{1} \cdot \sigma_{1}= \sigma_{1 + 1 \ (\bmod \ 2)} = \sigma_0 = \sigma_{1-1 \ (\bmod\  2)} = \sigma_1 \cdot \rho ^1 \quad i = j = 1\end{array}\right.$, dunque il gruppo è abeliano
  - per le regole di composizione definite precedentemente, per $n \ge 3$ la commutatività non è sempre rispettata, quindi $(\mathcal{D}_2, \cdot)$ è anche l'unico gruppo abeliano

## Oss

- **Hp**
  - $\mathcal{D}_n$ gruppo diedrale
- **Th**
  - $\mathcal{D}_n \hookrightarrow \mathcal{S}_n$
  - $\exists \mathcal{X} \leqslant \mathcal{S}_n \mid \mathcal{D}_n \cong \mathcal{X}$, e in particolare $\mathcal{D}_3 \cong \mathcal{S}_3$
- **Dim**
  - per ogni simmetria in $\mathcal{D}_n$, è possibile trovare l'unica permutazione equivalente in $\mathcal{S}_n$, e dunque è ben definita $f: \mathcal{D}_n \rightarrow \mathcal{S}_n : \alpha \rightarrow \sigma_\alpha$
    - _esempio_
        - per $n = 3$, numerando ogni vertice del triangolo equilatero, partendo dal vertice in basso a destra, si ottiene $\left \{ \begin{array}{l} f(\rho^0)=\left(\begin{array}{lll}1 & 2 & 3 \\ 1&2&3\end{array}\right)=\textrm{id} \\ f(\rho^1)=\left(\begin{array}{lll}1 & 2 & 3 \\ 2 & 3 & 1\end{array}\right) \\ f(\rho^2)=\left(\begin{array}{lll}1 & 2 & 3 \\ 3&1&2\end{array}\right) \\ f(\sigma_0)=\left(\begin{array}{lll}1 & 2 & 3 \\ 1&3&2\end{array}\right) \\ f(\sigma_1)=\left(\begin{array}{lll}1 & 2 & 3 \\ 2&1&3\end{array}\right) \\ f(\sigma_2)=\left(\begin{array}{lll}1 & 2 & 3 \\ 3&2&1\end{array}\right) \end{array} \right.$
  - poiché la permutazione equivalente è unica, $f$ iniettiva
  - allora $\mathcal{D}_n \hookrightarrow \mathcal{S}_n$, ovvero, l'inclusione è iniettiva ma non necessariamente suriettiva, infatti in generale si ha $|\mathcal{D}_n| \le |\mathcal{S}_n|$
  - ma per ragionamento analogo $\exists \mathcal{X} \leqslant \mathcal{S}_n \ \big\vert \ |\mathcal{X}| = |\mathcal{D}_n| \implies f$ suriettiva $\implies f$ biettiva
  - in particolare, $\mathcal{D}_3$ risulta essere il caso in cui $\mathcal{X} = \mathcal{S}_n$
  - $\mathcal{D}_n \cong \mathcal{X}$
    - siano $\alpha, \beta \in \mathcal{D}_n, \sigma_\alpha, \sigma_\beta \in \mathcal{S}_n \mid \left \{ \begin{array}{l} f(\alpha)= \sigma_\alpha \\ f(\beta) = \sigma_\beta \\ \alpha, \sigma_\alpha: i \rightarrow j \\ \beta, \sigma_\beta : j \rightarrow k \end{array} \implies \beta \alpha, \sigma_\beta \sigma_\alpha : i \rightarrow k \right .$
    - allora $f(\beta \alpha) = \sigma_{\beta\alpha} = \sigma_\beta \sigma_\alpha= f(\beta ) f(\alpha) \iff f$ morfismo
        - in particolare, restringendo $f: \mathcal{D}_n \rightarrow \mathcal{X} \implies f$ suriettiva $\implies f$ isomorfismo
            - in particolare, $\mathcal{D}_3 \cong \mathcal{S}_3$

## Def

- **Gruppo di Klein**

> - $a, b, c \mid \left \{ \begin{array}{l} a^2=b^2=c^2=1 \\ ab=c=ba \\ ac=b=ca \\ cb=a=bc \end{array} \right.$
> - $\mathcal{K}_4 := \{1, a, b, c\}$ è detto **gruppo di Klein**
>   - in particolare $\left \{ \begin{array}{l} o(1) = 1 \\ o(a) = o(b) = o(c) = 2 \end{array} \right .$
>   - in particolare, presi $3$ elementi in $\mathcal{K}_4 - \{1\}$, moltiplicandone due tra loro si ottiene il terzo

## Oss

- **Hp**
  - $\mathcal{K}_4$ è il gruppo di Klein
- **Th**
  - $\mathcal{K}_4 \cong \mathcal{D}_2$
- **Dim**
  - $\mathcal{K}_4:=\{1, a, b, c\}$
  - $\mathcal{D}_2 = \{1, \rho, \sigma_0, \sigma_1\}$, allora associando gli elementi $a=\rho, b= \sigma_0, c= \sigma_1$ si ottiene lo stesso gruppo

## Oss

- **Hp**
    - $G$ gruppo $\bigg\vert |G|=4$
- **Th**
    - $G \cong \mathbb{Z}_4 \lor G \cong \mathcal{K}_4$
- **Dim**
    - $\forall a \in G - \{1\} \quad$per il teorema di Lagrange $o(a) \bigg\vert |G| \implies o(a)=1 \lor o(a) =2 \lor o(a) = 4$
    - $a \neq 1 \implies o(a) \neq 1 \implies o(a) = 2 \lor o(a) = 4$
    - se $o(a)=4 \implies G$ cicliico $\implies G \cong \mathbb{Z}_4$
    - in particolare $\exists x \in G \mid o(x) = 4 = |G| \iff G$ ciclico, allora è necessario studiare il caso in cui $G$ non ciclico $\iff \nexists x \in G \mid o(x) = 4 \implies \forall x \in G - \{1\} \quad o(x) = 2$ per ragionamento precedente $\implies G = \{1, a, b, c\}$, dove $o(a)=o(b)=o(c)=2 \implies a^2=b^2=c^2=1 \implies$$\left\{\begin{array}{l}a=a^{-1} \\ b=b^{-1} \\ c=c^{-1}\end{array}\right.$
    - siano $a, b, x \in G \mid ab = x$ per un certo elemento $x = 1 \lor x = a \lor x = b \lor x = c$, allora si ha che $\left \{ \begin{array}{l} ab = 1 \implies b = a^{-1} = a \ \bot \\ ab = a \implies b = 1 \ \bot \\ ab = b \implies a = 1 \ \bot \end{array} \right. \implies ab = c$ necessariamente
    - il ragionamento è analogo per tutti gli altri prodotti, il che dimostra che presi $3$ elementi in $G - \{1\}$, moltiplicandone due tra loro si ottiene il terzo $\implies G \cong \mathcal{K}_4$

## Oss

- **Hp**
    - $G$ gruppo $\bigg\vert |G| = 6$
- **Th**
    - $G \cong \mathbb{Z}_6 \lor G \cong \mathcal{S}_3$
- **Dim**
    - ⚠️ **manca la dimostrazione**
