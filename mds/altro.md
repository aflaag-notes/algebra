# Altro

## Def

- **Algoritmo di Euclide**

> - ⚠️ **todo**

## Alg

- **In**
    - $A$ interlocutore
    - $p, q \in \mathbb{P} \mid p \neq q$, con $p, q$ sufficientemente grandi
    - $m$ messaggio $\mid \textrm{MCD}(m, n) = 1$
- **Out**
    - $\texttt{pub}_A, \texttt{priv}_A$
- **Alg**
    - $n := pq$
    - $\lambda(n) := \textrm{mcm}(p-1, q-1)$
    - $e \in \mathbb{N} \mid \left \{ \begin{array}{l} 1 \lt e \lt \lambda(n) \\ \textrm{MCD}(e, \lambda(n))= 1 \end{array} \right.$
    - $d:= e^{-1} \ (\bmod \ \lambda(n))$
    - $\texttt{pub}_A(m, e, n) := m^e \ (\bmod \ n)$
    - $\texttt{priv}_A(m, d, n) := (m^e)^d \ (\bmod \ n)$
- **Oss**
    - se $p,q$ non fossero sufficientemente grandi, poiché $n$ è pubblico, si rischierebbe di poter trovare $p$ e $q$, permettendo di decrittare il messaggio anche da chi non possiede $d$
    - $p \mid m \implies m^{ed} \equiv m \equiv 0 \ (\bmod \ p)$, il che comporterebbe una perdita di informazione
- **Th**
    - $\texttt{priv}_A(\texttt{pub}_A(m, e, n), d, n) = m$
- **Dim**
    - $\left \{ \begin{array}{l} (p-1) \mid \lambda(n) \\ (q - 1) \mid \lambda(n) \end{array} \right. \implies \exists i, j \in \mathbb{Z} \mid \lambda(n) = (p-1) \cdot i  = (q - 1) \cdot j$
    - $\textrm{MCD}(m, n) = 1 \implies p \nmid m \land q \nmid m \implies \left \{ \begin{array}{l}p \nmid m \implies m^p \equiv m \iff m^{p-1} \equiv 1  \implies m^{\lambda(n)} \equiv m^{(p-1)\cdot i} \equiv 1 \ (\bmod \ p) \\ q \nmid m \implies m^q \equiv m \iff m^{q-1} \equiv 1 \implies m^{\lambda(n)} \equiv m^{(q-1)\cdot j} \equiv 1 \ (\bmod \ q) \end{array} \right. \iff m^{\lambda(n)} \equiv 1 \ (\bmod \ n)$
    - $\textrm{MCD}(e, \lambda(n)) = 1 \iff [e] \in \mathbb{Z}^*_{\lambda(n)} \implies \exists ! [d] \in \mathbb{Z}^*_{\lambda(n)} \mid ed \equiv 1 \ (\bmod \ \lambda(n)) \implies \forall k \in \mathbb{Z} \quad ed = 1 + k \cdot\lambda(n)$
    - allora si ha che $(m^e)^d \equiv m^{1 + k \cdot \lambda(n)} \equiv m \cdot (m^{\lambda(n)})^k \equiv m \ (\bmod \ n)$

## Alg

- **In**
    - $n \in \mathbb{N}$
    - $b_0, \ldots, b_n, c_0, \ldots, c_n \in \mathbb{K} \left \{ \begin{array}{c}(b_0, c_0) \\ \vdots \\ (b_n, c_n) \end{array} \right.$ sono punti del $p(x)$ da trovare, e inoltre $\forall i \in [1, n], i \neq j \quad b_i \neq b_j$
- **Out**
    - $p(x) \in \mathbb{K}[x]_{\le n} \mid \left \{ \begin{array}{c} c_0 := a_0 + a_1b_0 + a_2b_0^2 + \ldots + a_nb_0^n = p(b_0) \\ c_1:=a_0 + a_1b_1 + a_2b_1^2 + \ldots + a_nb_1^n = p(b_1) \\ \vdots \\ c_n := a_0 + a_1b_n + a_2b_n^2 + \ldots + a_nb_n^n = p(b_n) \end{array} \right.$
- **Alg**
    - $\forall i \in [0, n] \quad p_i(x) := \displaystyle \prod_{\begin{subarray}{c}0 \le  j \le n \\ i \neq\ j \end{subarray}}{\dfrac{x - b_j}{b_i - b_j}}$
    - $p(x) := c_0p_0(x) + \ldots + c_n p_n(x)$
- **Oss**
    - è possibile sfruttare questo algoritmo per lo scambio di messaggi, ponendo il messaggio da inviare all'interno del termine noto di $p(x)$
    - una volta reperito $p(x)$ a partire dai punti $\left \{ \begin{array}{c}(b_0, c_0) \\ \vdots \\ (b_n, c_n) \end{array} \right.$, basterà porre $p(0)$ per recuperare il messaggio
    - la sicurezza di tale algoritmo è fornita dal fatto che è impossibile ricostruire $p(x)$ senza avere _tutti_ i punti necessari, altrimenti non è possibile ricostruire $p(x)$ come combinazione lineare in $\mathbb{K}[x]_{\le n}$
- **Dim**
    - si noti che la matrice dei coefficienti del sistema considerato in ipotesi è una matrice di Vandermonde a coefficienti $V(b_0, \ldots, b_n)$, dunque per dimostrazione precedente $\det(V(b_0, \ldots, b_n)) \neq 0$ poiché $b_0, \ldots, b_n$ sono stati scelti distinti
    - per dimostrazione precedente $\mathbb{K}[x]_{\le n}$ è uno spazio vettoriale, e in particolare $\dim(\mathbb{K}[x]_{\le n}) = n + 1$
    - allora $\mathcal{P} :=\{p_0(x), \ldots, p_n(x)\}$ base di $\mathbb{K}[x]_{\le n}$, e dunque determineranno univocamente il polinomio cercato
    - si noti inoltre che $\forall i \in [1, n] \quad p_i(x)= \dfrac{(x-b_n)(x - b_{n - 1})\cdot \ldots \cdot (x-b_{i + 1})(x - b_{i - 1})\cdot \ldots \cdot (x-b_1)(x-b_0)}{(b_i-b_n)(b_i - b_{n - 1})\cdot \ldots \cdot (b_i-b_{i + 1})(b_i - b_{i - 1})\cdot \ldots \cdot (b_i -b_1)(b_i-b_0)} \implies p_i(b_j) = \left \{ \begin{array}{l} 1 & i = j \\ 0 & i \neq j \end{array} \right.$
        - $(x - b_i)$ non è presente nel numeratore, ma $(x - b_j)$ sarà sicuramente presente
    - allora, ponendo $p(x) := c_0 p_0(x) + \ldots + c_np_n(x)$, ad esempio per $b_i = 0$ si ha che $p(x) = c_0 p_0(b_0) + \ldots + c_np_n(b_0) = c_0 \cdot 1 + c_1 \cdot 0 \ldots + c_n \cdot 0 = c_0$

