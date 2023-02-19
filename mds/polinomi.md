# Polinomi

## Def

- **Polinomio**

> - $\mathbb{K}$ campo
> - $a(x) := \displaystyle{\sum_{k = 0}^na_kx^k} = a_0x^0 + \ldots + a_nx^n$ è detto **polinomio**
>   - $a_n$ è detto _coefficiente direttore_
> - $\mathbb{K}[x] := \{a_0x^0 + \ldots + a_n x^n \mid a_0, \ldots, a_n \in \mathbb{K}\}$ è l'**insieme dei polinomi a coefficienti in $\mathbb{K}$**

- **Polinomio monico**

> - $\mathbb{K}$ campo
> - $p(x) = a_0x^0 + \ldots + a_nx^n \in \mathbb{K}[x]$
> - $p(x)$ è detto **polinomio monico** $\iff a_n = 1$

## Oss

- **Hp**
    - ($\mathbb{K}, +, \cdot)$ anello commutativo
    - $+, \cdot : \mathbb{K}[x] \times \mathbb{K}[x] \rightarrow \mathbb{K}[x]$
- **Th**
    - $(\mathbb{K}[x], +, \cdot)$ anello commutativo
- **Dim**
    - le operazioni $+$ e $\cdot$ sono ben definite
        - $p(x), q(x) \in \mathbb{K}[x] \mid \left \{ \begin{array}{l} p(x) =  \displaystyle{\sum_{i = 0}^n a_ix^i} \\ q(x) = \displaystyle{\sum_{j = 0}^m b_jx^j} \end{array} \right.$
        - allora $p(x) + q(x) = \displaystyle{\sum_{k = 0}^{+\infty}{(a_k + b_k)}}x^k$
            - poiché ogni termine presente in solo uno dei due polinomi vale $0$ nell'altro, la sommatoria che va a $+ \infty$ ha significato
        - $p(x) \cdot q(x) = \displaystyle \sum_{i = 0}^n \left( \sum_{j = 0}^{m}{a_ib_j x^{i + j }}\right)$
    - $(\mathbb{K}[x], +)$ gruppo abeliano
        - per come $+$ è definita, è associativa
        - l'elemento neutro rispetto a $+$ è costituito dal polinomio nullo $a(x) = 0$
        - $\forall a(x) := \displaystyle{\sum_{i = 0}^{n}{a_i x^i}}\in \mathbb{K}[x] \quad \exists-a(x)= - \displaystyle {\sum_{i = 0}^n{a_i x^i}}$
        - per come $+$ è definita, è commutativa
    - $(\mathbb{K}[x], \cdot)$ monoide
        - per come $\cdot$ è definita, è associativa
        - l'elemento neutro rispetto a $\cdot$ è costituito da $a(x) = 1\cdot x^0 = 1$
    - per come $+$ e $\cdot$ sono definite $\forall a(x), b(x), c(x) \in \mathbb{K}[x] \quad a(x) \cdot (b(x) + c(x)) = a(x) \cdot b(x) + a(x) \cdot c(x)$

## Def

- **Grado di un polinomio**

> - $\mathbb{K}$ campo
> - $a(x) = a_0x^0 + \ldots + a_nx^n \in \mathbb{K}[x]$
> - $\deg(a(x)):=\left\{\begin{array}{ll} n & a(x) \neq 0 \\ - \infty & a(x) = 0\end{array}\right.$ è detto **grado di $a(x)$**

- **Polinomio costante**

> - $\mathbb{K}$ campo
> - $p(x) \in \mathbb{K}[x]$ è detto **polinomio costante** $\iff \deg(p(x)) = 0$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $a(x), b(x) \in \mathbb{K}[x]$
- **Th**
    - $\deg(a(x) \cdot b(x)) = \deg(a(x)) + \deg(b(x))$
- **Dim**
    - $a(x) \neq 0 \implies \exists n \in \mathbb{N} - \{0\} \mid a(x) = a_0x^0 + \ldots + a_nb^n \implies \deg(a(x)) =: n$
    - $b(x) \neq 0 \implies \exists m \in \mathbb{N} - \{0\} \mid b(x) = b_0x^0 + \ldots + b_mx^m \implies \deg(b(x)) =: m$
    - dunque $\deg(a(x)) + \deg(b(x)) = n + m$
    - $a(x) \cdot b(x) = a_0b_0\cdot x^0 + \ldots + a_nb_m\cdot x^{n + m} \implies \deg(a(x) \cdot b(x)) = n + m$
        - per dimostrazione precedente $\mathbb{K}$ campo $\implies \mathbb{K}$ dominio di integrità, e dunque in $\mathbb{K}$ vale la legge di annullamento del prodotto, per cui $a_n, b_m \neq 0 \implies a_n \cdot b_m \neq 0 \implies \deg(a(x) \cdot b(x)) \ge n + m$ necessariamente
    - di conseguenza $\deg(a(x) \cdot b(x)) = n + m = \deg(a(x)) + \deg(b(x))$
        - l'equazione è verificata anche quando almeno uno dei due polinomi è nullo, in quanto $\forall n \in \mathbb{N} \quad \left \{ \begin{array}{l} -\infty \pm n = -\infty \\ -\infty -\infty = -\infty \end{array} \right.$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
- **Th**
    - $\mathbb{K}[x]^* = \mathbb{K}^* \subseteq \mathbb{K} \subset \mathbb{K}[x]$
- **Dim**
    - $a(x) \in \mathbb{K}[x] \mid \deg(a(x)) \ge 1$, dunque $a(x)$ non è un polinomio costante
    - $\forall b(x) \in \mathbb{K}[x] - \{0\} \quad \deg(a(x) \cdot b(x)) \ge \deg(a(x)) \ge 1$
    - per assurdo, ipotizzando $\exists a^{-1}(x) \in \mathbb{K}[x] - \{0\} \mid a(x) \cdot a^{-1}(x) = 1 \quad \deg(a(x) \cdot a^{-1}(x)) = \deg(1) = \deg(1 \cdot x^0) = 0 \ \bot$
    - allora $\nexists a^{-1}(x) \in \mathbb{K}[x]$, dunque gli unici polinomi invertibili rispetto a $\cdot$ sono i polinomi costanti, e poiché $0$ non è invertibile, allora $\mathbb{K}[x]^* = \mathbb{K}^* \subseteq \mathbb{K} \subset \mathbb{K}[x]$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
- **Th**
    - $\mathbb{K}[x]$ dominio di integrità

## Def

- **Radici di un polinomio**

> - $\mathbb{K}$ campo
> - $p(x) \in \mathbb{K}[x]$
> - $c \in \mathbb{K} \mid p(c) = 0$ è detta **radice di $p(x)$**
>   - in particolare $\{c \in \mathbb{K} \mid p(c) = 0\}$ è l'**insieme delle radici di $p(x)$**

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $p(x) \in \mathbb{K}[x]$
    - $c \in \mathbb{K}$
- **Th**
    - $p(c) = 0 \iff (x - c) \mid p(x)$
- **Dim**
    - _prima implicazione_
        - per il teorema della divisione con il resto tra polinomi, dividendo $p(x)$ per $(x - c)$ si ottiene che $\exists!q(x), r(x) \in \mathbb{K}[x] \mid p(x) = q(x) \cdot (x - c) + r(x)$
        - $0 = p(c) = q(c) (c - c) + r(c) = 0 + r(c) \iff r(c) = 0$, allora r(x) è il polinomio nullo $\implies p(x) = q(x)(x - c) \implies (x- c) \mid p(x)$
    - _seconda implicazione_
        - $x - c \mid p(x) \iff \exists p(x) \in \mathbb{K}[x] \mid p(x) = q(x)\cdot (x - c)$, allora $p(c) = q(c) \cdot (c - c) = 0 \implies c$ radice di $p(x)$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $p(x) \in \mathbb{K}[x]$
    - $n := \deg(p(x))$
- **Th**
    - $|\{c \in \mathbb{K} \mid p(c) = 0\}| \le n$
- **Dim**
    - per assurdo $N :=|\{c \in \mathbb{K} \mid p(c) = 0\}| \gt n$
    - allora, sia $\{c_1, \ldots, c_N\}$ l'insieme delle radici di $p(x)$
    - per dimostrazione precedente $p(c_1) = 0 \iff x - c_1 \mid p(x) \iff \exists q_1(x) \in \mathbb{K}[x] \mid q_1(x)(x-c_1)=p(x)$
    - analogamente $p(c_2) = 0 \iff p(c_2) = q_1(c_2)(c_2 - c_1) = 0$
    - per assurdo $\exists i, j \in [1, N] ,i \neq j \mid c_i = c_j \implies |\{c \in \mathbb{K} \mid p(c) = 0 \}| \lt N \implies$ le soluzioni sono necessariamente tutte distinte, e in particolare $c_2 \neq c_1 \iff c_2 - c_1 \neq 0$
    - $\mathbb{K}[x]$ dominio di integrità $\implies q_1(c_2) = 0 \land c_2 - c_1 \neq 0 \implies q_1(c_2) = 0$
    - per dimostrazione precedente $q_1(c_2) = 0 \iff x- c_2 \mid q_1(x) \implies \exists q_2(x) \in \mathbb{K}[x] \mid q_2(x) (x-c_2) = q_1(x)$, che sostituendo implica che $p(x) = q_2(x)(x-c_2)(x-c_1)$
    - applicando il ragionamento analogo ad ogni soluzione, si ha che $\exists q_n(x) \in \mathbb{K}[x] \mid q_n(x) (x-c_1) \cdot \ldots \cdot(x-c_N) = p(x) \implies (x-c_1) \cdot \ldots \cdot (x-c_N) \mid p(x)$
    - ma $\deg\left((x - c_1) \cdot \ldots \cdot (x - c_N)\right) = N$, mentre $\deg(p(x)) = n$, dove $N \gt n \ \bot$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $I \subset \mathbb{K}[x]$ ideale
- **Th**
    - $\exists  p(x) \in I \mid I = I(p(x))$, o equivalentemente, in $\mathbb{K}[x]$ ogni ideale è principale
- **Dim**
    - $p(x) = 0 \implies I = \{0\} \implies I = I(0)$, ovvero l'ideale principale generato da $0$
    - $p(x) \in I - \{0\} \mid \deg(p(x))$ sia il minore possibile, allora $\forall q(x) \in I \mid \deg(q(x)) \lt \deg(p(x)) \implies q(x) \in I(0) \implies q(x) = 0$, di conseguenza è unico in quanto l'elemento minore in $I - \{0\}$ è unico
    - per osservazione precedente $\exists p(x) \in I - \{0\} \mid I = I(p(x))$, dove $p(x)$ è il polinomio di grado minore in $I - \{0\}$
    - $I = I(p(x)) \iff I \subseteq I(p(x)) \land I(p(x)) \subseteq I$
        - $I \subseteq I(p(x))$
            - per il teorema della divisione con il resto tra polinomi $\forall a(x) \in I \quad \exists ! q(x), r(x) \mid a(x) = p(x) \cdot q(x) + r(x) \quad \deg(r(x)) \lt \deg(p(x)) \implies r(x) = a(x) - p(x) \cdot q(x)$
            - $\left.\begin{array}{l} a(x) \in I \\ p(x) \in I - \{0\} \implies p(x) \cdot q(x) \in I \end{array}\right\} \implies r(x) \in I$
            - ma poiché $\deg(r(x)) \lt \deg(p(x))$, e $p(x)$ è stato preso con il grado minore possibile, per osservazione precedente segue necessariamente che $r(x) = 0$, e dunque $a(x) = p(x) \cdot q(x) \implies a(x) \in I(p(x))$
        - $I(p(x)) \subseteq I$
            - $p(x) \in I - \{0\}$ e $I$ è un ideale per ipotesi, dunque in particolare $\mathbb{K}[x] \cdot I \subseteq I$, allora $\forall q(x) \in \mathbb{K}[x] \quad q(x) \cdot p(x) \in I$
            - $\forall a(x) \in I(p(x)) \quad \exists q(x) \in \mathbb{K}[x] \mid q(x)\cdot p(x) = a(x)$, dunque $a(x) \in I$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $\exists d(x) \in \mathbb{K}[x]\mid I(a_1(x), \ldots, a_n(x)) = I(d(x))$
- **Th**
    - $d(x)=\textrm{MCD}(a_1(x), \ldots, a_n(x))$
- **Dim**
    - la dimostrazione è analoga al caso di $\mathbb{Z}$
    - in particolare, $\textrm{MCD}(a_1(x), \ldots, a_n(x))$ è ben definito in quanto, per dimostrazione precedente, la divisione con il resto tra polinomi è ben definita, ed è dunque possibile calcolare il massimo comun divisore attraverso, ad esempio, l'algoritmo di Euclide
    - inoltre, $d(x)$ è ben definito a meno di una costante moltiplicativa non nulla

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $I(a_1(x)), \ldots, I(a_n(x)) \subset \mathbb{K}[x]$ ideali
    - $\exists m(x) \in \mathbb{K}[x] \mid I(a_1(x)) \cap \ldots \cap I(a_1(x)) = I(m(x))$
- **Th**
    - $m(x)=\textrm{mcm}(a_1(x), \ldots, a_n(x))$
- **Dim**
    - la dimostrazione è analoga al caso in $\mathbb{Z}$
    - in particolare, $\textrm{mcm}(a_1(x), \ldots, a_n(x))$ è ben definito in quanto il teorema fondamentale dell'aritmetica è applicabile anche ai polinomi
    - inoltre, $m(x)$ è ben definito a meno di una costante moltiplicativa non nulla

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $a_1(x), \ldots ,a_n(x) \in \mathbb{K}[x]$
    - $c \in \mathbb{K}$
    - $d(x):= \textrm{MCD}(a_1(x), \ldots, a_n(x))$
- **Th**
    - $a_1(c) = \ldots = a_n(c) = 0 \iff d(c) = 0$
- **Dim**
    - _prima implicazione_
        - $\forall i \in [1, n] \quad a_i(c) = 0 \iff (x - c) \mid a_i(x)$
        - per definizione $\forall i \in [1, n] \quad d(x) \mid a_i(x)$, e poiché $d(x)$ è il massimo tra i divisori comuni, allora necessariamente $(x - c) \mid d(x) \iff d(c) = 0$
    - _seconda implicazione_
        - per definizione $\forall i \in [1, n] \quad d(x) \mid a_i(x)$
        - per dimostrazione precedente $d(c) = 0 \iff (x - c) \mid d(x)$
        - allora $\forall i \in [1, n] \quad (x - c) \mid d(x) \land d(x) \mid a_i(x) \implies (x - c) \mid a_i(x) \iff a_i(c) = 0$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $p(x) \in \mathbb{K}[x]$
- **Th**
    - $p(x)$ irriducibile $\iff p(x)$ primo
- **Dim**
    - _prima implicazione_
        - $p(x) \in \mathbb{K}[x]$ irriducibile, allora per definizione $\exists d(x), q(x) \in \mathbb{K}[x] \mid p(x) = d(x) q(x) \implies d(x) \in \mathbb{K}[x]^*=\mathbb{K}^* \lor q(x) \in \mathbb{K}[x]^* = \mathbb{K}^*$
        - siano $a(x), b(x) \in \mathbb{K}[x] : p(x) \mid a(x)b(x) \iff \exists k(x) \in \mathbb{K}[x] \mid p(x)k(x) = a(x)b(x)$
        - se $p(x) \nmid a(x) \implies \textrm{MCD}(a(x), p(x))= 1$, allora per l'identità di Bézout $\exists f(x), g(x) \in \mathbb{K}[x] \mid 1 = f(x)a(x) + g(x)p(x) \iff b(x) = a(x)b(x)f(x) + p(x)g(x)b(x) = p(x)k(x)f(x) +p(x)g(x)b(x) = p(x)[k(x)f(x) + g(x)b(x)] \implies p(x) \mid b(x)$
        - allora $p(x) \mid a(x)b(x) \land p(x) \nmid a(x) \implies p(x) \mid b(x)$
        - ripetendo analogamente il ragionamento, è possibile dimostrare che $p(x) \mid a(x)b(x) \land p(x) \nmid b(x) \implies p(x) \mid a(x)$
        - allora, per definizione $p(x)$ primo
    - _seconda implicazione_
        - $\mathbb{K}[x]$ è un dominio di integrità, e dunque, per dimostrazione precedente, implica che ogni elemento primo è anche irriducibile

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $p(x) \in \mathbb{C}[x]$
- **Th**
    - $p(x)$ irriducibile $\iff \deg(p(x)) = 1$
- **Dim**
    - _prima implicazione_    
        - ipotizzando che $\deg(p(x)) \gt 1 \implies \exists z \in \mathbb{C} \mid p(z) = 0$ per il teorema fondamentale dell'algebra
        - per dimostrazione precedente $p(z) = 0 \iff (x - z) \mid p(x) \iff \exists q(x) \in \mathbb{C}[x] \mid p(x) = (x - z) \cdot q(x)$
        - poiché $\deg(x - z) = 1$, allora necessariamente $\deg(q(x)) = \deg(p(x)) - 1$
        - $\deg(p(x)) \gt 1 \implies \deg(q(x)) = \deg(p(x)) - 1 \gt 0 \implies p(x)$ non è irriducibile $\bot$
    - _seconda implicazione_
        - per dimostrazione precedente $\forall a(x), b(x), c(x) \in \mathbb{K}[x] \quad a(x) = b(x) \cdot c(x) \implies \deg(a(x)) = \deg(b(x)) + \deg(c(x))$
        - $\deg(p(x)) = 1$, allora se $\exists a(x), b(x) \in \mathbb{C}[x] \mid p(x) = a(x) \cdot b(x)$, allora $\deg(a(x)) = 1 \land \deg(b(x)) = 0$ oppure $\deg(a(x)) = 0 \land \deg(b(x)) = 1$
        - dunque, ad esempio se $\deg(a(x)) = 1 \land \deg(b(x)) = 0 \implies b(x) \in \mathbb{C}[x]^* \implies p(x)$ è irriducibile
        - si noti che questa implicazione è vera in ogni campo

## Oss

- **Hp**
    - $p(x) \in \mathbb{R}[x]$
- **Th**
    - $p(x)$ irriducibile $\iff \deg(p(x)) = 1 \lor \left \{ \begin{array}{l} \deg(p(x)) = 2 \\ \Delta \lt 0 \end{array} \right.$, dove $p(x) = ax^2 + bx + c \implies \Delta := b^2 - 4ac$
- **Dim**
    - _prima implicazione_
        - se $\deg(p(x)) = 1$, allora segue la dimostrazione precedente, poiché $\mathbb{R}[x] \subset \mathbb{C}[x]$
        - allora sia $p(x) \in \mathbb{R}[x] \subset \mathbb{C}[x] \mid \deg(p(x)) \ge 2 \implies p(x)$ è della forma $p(x) := a_0x^0 + \ldots + a_nx^n$, per certi $a_0, \ldots, a_n \in \mathbb{R}$ e $n \ge 2$
        - per il teorema fondamentale dell'algebra $\exists z \in \mathbb{C} \mid p(z) = 0 \iff (x - z) \mid p(x)$
        - si noti che $\forall a \in \mathbb{R} \quad \overline{a} = a$
        - allora si ha che $p(\overline{z}) = a_0 (\overline{z})^0 + \ldots + a_n (\overline{z})^n = \overline{a_0}(\overline{z}^0) + \ldots + \overline{a_n}(\overline{z})^n = \overline{a_0x^0 + \ldots + a_nx^n} = \overline{p(z)} = \overline{0} = 0 \implies p(\overline{z}) = 0 \iff (x - \overline{z}) \mid p(x)$
        - siano $a, b \in \mathbb{R} \mid z:= a + i b$
        - $\left \{ \begin{array}{l}(x - z) \mid p(x) \iff \exists q(x) \in \mathbb{R}[x] \mid (x - z) q(x) = p(x) \\ (x - \overline{z}) \mid p(x) \iff \exists k(x) \in \mathbb{R}[x] \mid (x - \overline{z})k(x) = p(x) \end{array} \right.$
        - $x = z \implies (z - \overline{z})k(z) = p(z) = 0$, e poiché $\mathbb{R}[x]$ è un dominio di integrità, $(z - \overline{z}) = 0 \lor k(z) = 0$
        - $b = 0$
            - allora si ha che $z \in \mathbb{R} \implies z = \overline{z}$ per osservazione precedente
            - $\deg(p(x)) \ge 2 \implies p(x) = q(x) (x - z)$ implica necessariamente che $\deg(q(x)) \ge 1$, e in particolare $\deg(q(x)), \deg(x - z) \neq 0 \iff q(x),(x - z) \notin \mathbb{R}[x]^* \implies p(x)$ non irriducibile $\bot$
            - allora, segue esclusivamente il caso in cui $b \neq 0$
        - $b \neq 0$
            - allora si ha che $z \in \mathbb{C} - \mathbb{R} \implies z - \overline{z} = a + ib - (a - ib) =a +ib - a + ib = 2ib \neq 0 \implies k(z) = 0$ necessariamente
            - $k(z) = 0 \iff (x - z) \mid k(x) \iff \exists h(x) \in \mathbb{R}[x] \mid (x - z)h(x) = k(x)$
            - allora si ha che $(x - \overline{z})k(x) = (x - \overline{z})(x -z)h(x) = p(x) \iff (x - \overline{z})(x - z) \mid p(x) \iff (x^2 - \overline{z}x -zx + z\overline{z}) \mid p(x) \iff [x^2 - (a - ib)x-(a + ib)x + (a^2 + b^2)] \mid p(z) \iff (x^2 - ax - ibx - ax + ibx + a^2 + b^2) \mid p(x) \iff (x^2 - 2ax + a^2 + b^2) \mid p(x)$
            - $p(x)$ irriducibile, e poiché $\deg(x^2 - 2ax + a^2 + b^2) \neq 0 \iff (x ^2 - 2ax +a^2 + b^2) \notin \mathbb{R}[x]^*$, allora necessariamente $\exists k \in \mathbb{R}[x]^* = \mathbb{R}^* \mid p(x) = k(x^2 - 2ax + a^2 + b^2) = kx^2 -2kax +ka^2+kb^2 \implies \Delta = (-2ka)^2 - 4k(ka^2+kb^2) =4k^2a^2 -4k^2a^2 -4k^2b^2=-4k^2b^2 \lt 0$, per ogni scelta di $k,b \in \mathbb{R}[x]^* = \mathbb{R}^*$
    - _seconda implicazione_
        - $\deg(p(x)) = 1 \implies p(x)$ irriducibile
            - segue la dimostrazione precedente, poiché questa implicazione è valida in ogni campo
        - $\deg(p(x)) = 2 \land \Delta \lt 0 \implies p(x)$ irriducibile
            - per assurdo, sia $p(x)$ non irriducibile, allora $\exists a(x), b(x) \in \mathbb{R}[x] \mid p(x) = a(x)b(x) \implies a(x), b(x) \notin \mathbb{R}[x]^* \implies \deg(a(x)), \deg(b(x)) \neq 0 \implies \deg(a(x)) = \deg(b(x)) = 1$ poiché $\deg(p(x)) = 2$ in ipotesi
            - dunque $a(x)$ e $b(x)$ sono della forma $a(x) = cx + d$, dove $c \in \mathbb{R} - \{0\}$, ma allora $x' := -c^{-1}d$ è radice di $a(x)$, e dunque necessariamente è anche radice di $p(x)$
            - allora $\deg(p(x)) = 2 \land \exists x' \in \mathbb{R} \mid p(x') = 0 \implies \Delta \ge 0 \ \bot$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $p(x) \in \mathbb{K}[x] - \{0\}$
- **Th**
    - $\exists ! q_1(x), \ldots ,q_k(x) \in \mathbb{K}[x]$ irriducibili e monici$, c \in \mathbb{K}^* \mid p(x) = c \cdot q_1(x) \cdot \ldots \cdot q_k(x)$
        - in particolare, i polinomi sono unici a meno di riordinamento
- **Dim**
    - _esistenza_:
        - dimostrazione per induzione sul grado di $p(x)$
        - $\deg(p(x)) = 1$
            - allora $p(x)$ è della forma $p(x) = ax + b$, con $a, b, k \in \mathbb{K}^* \implies p(x) = a \cdot \left(x + \dfrac{b}{a}\right)$, dove $\deg \left( x + \dfrac{b}{a}\right ) = 1 \iff \left( x + \dfrac{b}{a}\right)$ irriducibile
        - $\deg(p(x)) \gt 1$
            - per dimostrazione precedente $\deg(p(x)) \neq 1 \iff p(x)$ non irriducibile $\iff \exists a(x), b(x) \in \mathbb{K}[x] - \mathbb{K}[x]^* \mid p(x) = a(x) b(x)$
        - ⚠️  **poi?**
    - _unicità_
        - $\deg(p(x)) = 0$
            - allora $p(x)$ è della forma $p(x) = c$, con $c \in \mathbb{K}$, allora $p(x) = c \cdot (1 \cdot x^0)$
        - $\deg(p(x)) \gt 0$
            - per assurdo $\exists q_1(x), \ldots, q_k(x), q_1'(x), \ldots, q_k'(x) \in \mathbb{K}[x]$ irriducibili e monici, $c, c' \in \mathbb{K}^* \mid c \cdot q_1(x) \cdot \ldots \cdot q_k(x) = p(x) = c' \cdot q_1'(x) \cdot \ldots \cdot q_k'(x)$
            - allora, ad esempio $q_1(x) \mid p(x) = c' \cdot q_1'(x) \cdot \ldots \cdot q_k'(x) \implies q_1(x) \mid q_1'(x) \lor \ldots \lor q_1(x) \mid q_k'(x)$
            - ipotizzando $q_1 \mid q_1'(x)$, poiché $\deg(q_1(x)) = \deg(q_1'(x))$, allora necessariamente $q_1 \mid q_1'(x) \iff \exists k \in \mathbb{K}^* \mid q_1(x) \cdot k = q_1'(x)$
            - allora $c \cdot q_1(x) \cdot \ldots \cdot q_k(x) = p(x) = c' \cdot q_1'(x) \cdot \ldots \cdot q_k'(x) = c' \cdot k \cdot q_1(x) \cdot \ldots, \cdot q_k'(x)$
            - ⚠️  **tutto sbagliato che palle**

## Oss

- **Hp**
    - $a_0, \ldots, a_n \in \mathbb{Z} \mid a_0, a_n \neq 0$
    - $p(x) \in \mathbb{Z}[x] \mid p(x) = a_0 + \ldots + a_nx^n$
    - $a, b \in \mathbb{Z} \mid \textrm{MCD}(a, b) = 1$
    - $p\left(\frac{a}{b}\right) = 0$
- **Th**
    - $a \mid a_0 \land b \mid a_n$
- **Dim**
    - $0 = p\left(\frac{a}{b}\right) = a_n\left(\frac{a}{b}\right)^n + a_{n - 1}\left(\frac{a^{n - 1}}{b^{n - 1}}\right) + \ldots + a_0$
    - moltiplicando entrambe i membri dell'equazione per $b^n$ si ottiene $0 = a_na^n + a_{n -1}a^{n - 1}b + \ldots + a_1a^1b^{n -1 } + a_0b^n$
    - allora $a_na^n = - a_{n - 1} a^{n - 1}b - \ldots - a_1a^1 b^{n - 1}- a_0b^n \implies b \mid a_na^n$ poiché ogni termine del secondo membro dell'equazione contiene una potenza di $b$
    - $\textrm{MCD}(a, b) = 1 \implies \textrm{MCD}(a^n, b) = 1$, ma allora $b \mid a_na^n \implies b \mid a_n$
    - è possibile ripetere il ragionamento analogo per $a_0b^n$, e dall'equazione ottenuta si noterà che $a \mid a_0b^n$, che per ragionamento analogo all'osservazione precedente deve necessariamente implicare che $a \mid a_0$

