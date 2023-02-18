# Altro

## Lem

- **Hp**
    - $a, b, c, \in \mathbb{Z}$
- **Th**
    - $a \mid b \land a \mid c \implies \forall z \in I(b, c) \quad a \mid z$
- **Dim**
    - $\left \{ \begin{array}{l}a \mid b \iff \exists k \in \mathbb{Z} \mid ak = b \\ a \mid c \iff \exists h \in \mathbb{Z} \mid ah = c \end{array} \right.$
    - $\forall z \in I(b, c) \quad \exists x, y \in \mathbb{Z} \mid z = bx + cy = akx + ahy = a(kx + cy) \iff a \mid z$

## Alg

- **In**
    - $a, b \in \mathbb{Z} \mid 0 \lt a \le b$
- **Out**
    - $d:=\textrm{MCD}(a, b)$
- **Alg**
    - $r_0:=b$
    - $r_1:=a$
    - $r_i = r_0q_0 + r_1$
    - $\texttt{while} \ r_i \neq 0 \texttt{:}$
        - $r_{i + 1} = r_{i - 1}q_{i - 1} + r_i$
        - $r_i := r_{i + 1}$
    - $\texttt{return} \ r_i$
- **Th**
    - $r_n = d$
- **Dim**
    - siano $i \in [0, n + 1]$ le iterazioni dell'algoritmo, dove $r_{n + 1} = 0$
    - $d \mid r_n$
        - _caso base_
            - si noti che, per dimostrazione precedente, $I(a, b) = I(d)$
            - $r_0:= b \in I(a,b)$
            - $r_1:=a \in I(a,b)$
            - $r_2 \equiv r_0 \ (\bmod \ r_1) \iff \exists q_1 \in \mathbb{Z} \mid r_0 = r_1q_1 + r_2 \iff r_2 = r_0 - r_1q_1 = b - aq_1 \in I(a,b) = I(d)$
        - _ipotesi induttiva forte_
            - $\forall i \in [0, n] \quad r_i \in I(a,b) = I(d)$
        - _passo induttivo_
            - $r_{i + 1} \equiv r_{i - 1} \ (\bmod \ r_i) \iff \exists q_i \in \mathbb{Z} \mid r_{i - 1} = r_iq_i + r_{i + 1} \iff r_{i + 1} = r_{i - 1} - r_iq_i$
            - $r_{i - 1}, r_i \in I(a, b) = I(d)$ per ipotesi induttiva forte $\implies r_{i - 1} - r_iq_i \in I(a, b) = I(d)$
        - in particolare, si ha che $r_n \in I(a,b) = I(d) \iff \exists p \in \mathbb{Z} \mid dp = r_n \iff d \mid r_n$
    - $r_n \mid d$
        - $\left \{ \begin{array}{l} r_{n + 1} = 0 \\  0 \equiv r_{n + 1} \equiv r_{n - 1} \ (\bmod \ r_n) \iff \exists q_n \in \mathbb{Z} \mid r_{n- 1} = r_nq_n \end{array} \iff r_n \mid r_{n - 1}\right.$
        - $r_n \equiv r_{n - 2} \ (\bmod r_{n - 1}) \iff \exists q_{n - 1} \in \mathbb{Z} \mid r_n =r_{n - 1} q_{n - 1} + r_{n - 2} \iff r_{n - 2} = r_n - r_{n - 1}q_{n - 1} \in I(r_n, r_{n - 1})$
        - per dimostrazione precedente $r_n \mid r_n \land r_n \mid r_{n - 1} \implies \forall z \in I(r_n, r_{n - 1}) \quad r_n \mid z$, e in particolare $r_2 \in I(r_n, r_{n - 1}) \implies r_n \mid r_{n-2}$
        - è possibile riptere il ragionamento analogo ottenendo $\left \{ \begin{array}{c} r_n \mid r_n \land r_n \mid r_{n - 1} \implies r_n \mid r_{n -2} \\ r_n \mid r_{n - 1} \land r_n \mid r_{n - 2} \implies r_n \mid r_{n - 3} \\ \vdots \\ r_n \mid r_{n - i} \land r_i \mid r_{n - (i + 1)} \implies r_n \mid r_{n - (i + 2)} \\ \vdots \\ r_n \mid r_2 \land r_n \mid r_1 \implies r_n \mid r_0 \end{array} \right.$
        - $d := \textrm{MCD}(a,b) \implies d \mid a \land d \mid b$, e poiché $r_n \mid r_0 =: b \land r_n \mid r_1 =: a \implies r_n \mid d$
    - $d \mid r_n \land r_n \mid d \implies r_n = d$

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
    - allora, ponendo $p(x) := c_0 p_0(x) + \ldots + c_np_n(x)$, ad esempio per $x = b_0$ si ha che $p(x) = c_0 p_0(b_0) + \ldots + c_np_n(b_0) = c_0 \cdot 1 + c_1 \cdot 0 + \ldots + c_n \cdot 0 = c_0$

