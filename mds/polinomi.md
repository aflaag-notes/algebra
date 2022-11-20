# Polinomi

## Def

- **Polinomi**
> - $\mathbb{K}$ campo
> - $a(x) := \displaystyle{\sum_{k = 0}^na_kx^k} = a_0x^0 + \ldots + a_nx^n$ è un **polinomio**
> - $\mathbb{K}[x] := \{a_0x^0 + \ldots + a_n x^n \mid a_0, \ldots, a_n \in \mathbb{K}\}$ è l'**insieme dei polinomi a coefficienti in $\mathbb{K}$**
> - $p(x) = a_0x^0 + \ldots + a_nx^n \in \mathbb{K}[x]$ è detto **polinomio monico** $\iff a_n = 1$

## Oss

- **Hp**
    - ($\mathbb{K}, +, \cdot)$ anello
- **Th**
    - $(\mathbb{K}[x], +, \cdot)$ è un anello
- **Dim**
    - le operazioni $+$ e $\cdot$ sono ben definite
        - $p(x), q(x) \in \mathbb{K}[x] \mid p(x) =  \displaystyle{\sum_{i = 0}^n a_ix^i} \land q(x) = \displaystyle{\sum_{j = 0}^m b_jx^j}$
        - $p(x) + q(x) = \displaystyle{\sum_{k = 0}^{+\infty}{(a_k + b_k)}}x^k$
            - ogni termine presente in solo uno dei due polinomi, varra $0$ nell'altro, di conseguenza la sommatoria che va a $+ \infty$ ha significato
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

- **Grado del polinomio**
> - $\mathbb{K}$ campo
> - $a(x) = a_0x^0 + \ldots + a_nx^n \in \mathbb{K}[x]$
> - $\deg(a(x)):=\left\{\begin{array}{ll} n & a(x) \neq 0 \\ - \infty & a(x) = 0\end{array}\right.$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $a(x), b(x) \in \mathbb{K}[x]$
- **Th**
    - $\deg(a(x) \cdot b(x)) = \deg(a(x)) + \deg(b(x))$
- **Dim**
    - $a(x) \neq 0 \implies a(x) = a_0x^0 + \ldots + a_nb^n \implies \deg(a(x)) = n$
    - $b(x) \neq 0 \implies b(x) = b_0x^0 + \ldots + b_mx^m \implies \deg(b(x)) = m$
    - dunque $\deg(a(x)) + \deg(b(x)) = n + m$
    - $a(x) \cdot b(x) = a_0b_0\cdot x^0 + \ldots + a_nb_m\cdot x^{n + m} \implies \deg(a(x) \cdot b(x)) = n + m$
        - per dimostrazione precedente $\mathbb{K}$ campo $\implies \mathbb{K}$ dominio di integrità, e dunque in $\mathbb{K}$ vale la legge di annullamento del prodotto, per cui $a_n, b_m \neq 0 \implies a_n \cdot b_m \neq 0$
    - di conseguenza $\deg(a(x) \cdot b(x)) = n + m = \deg(a(x)) + \deg(b(x))$
    - l'equazione è verificata anche quando almeno uno dei due polinomi è nullo, in quanto $\forall n \in \mathbb{N} \quad -\infty \pm n = -\infty \land -\infty -\infty = -\infty$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $a(x) \in \mathbb{K}[x] \mid \deg(a(x)) \ge 1$
- **Th**
    - $\nexists a^{-1}(x) \in \mathbb{K}[x]$
- **Dim**
    - $\forall b(x) \neq 0 \quad \deg(a(x) \cdot b(x)) \ge \deg(a(x)) \ge 1$
    - $\deg(1 \cdot x^0) = \deg(1) = 0$
    - ipotizzando che $\exists a^{-1}(x) \in \mathbb{K}[x]$, allora $a(x) \cdot a^{-1}(x) = 1$, dunque $\deg(a(x) \cdot a^{-1}(x)) = 0$, ma $\forall b(x) \quad \deg(a(x) \cdot b(x)) \ge 1 \ \bot$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
- **Th**
    - $\mathbb{K}[x]^* = \mathbb{K}^* \subset \mathbb{K}[x]$
- **Dim**
    - $\mathbb{K}[x]^* = \mathbb{K}^*$
        - $\forall a(x) \in\mathbb{K}[x] \mid a(x) = a_0 \neq 0$ polinomio costante non nullo, il polinomio inverso sarà costituito esclusivamente dal suo coefficiente $a_0^{-1} \in \mathbb{K}$
        - per dimostrazione precedente $\mathbb{K}$ campo $\implies \forall a_0 \in \mathbb{K} - \{0\} \quad \exists a_0^{-1} \in \mathbb{K} - \{0\}$
        - dunque $\exists a^{-1}(x) \quad a(x) \cdot a^{-1}(x) = a_0 \cdot a_0^{-1} = 1$
    - $\mathbb{K}^* \subset \mathbb{K}[x]$
        - $\mathbb{K}^* \subset \mathbb{K} \subset \mathbb{K}[x]$
        - per dimostrazione precedente, gli unici elementi invertibili in $\mathbb{K}[x]$ sono i polinomi costanti, che costituiscono un sottoinsieme di $\mathbb{K}[x]$, che coincide proprio con $\mathbb{K}$ poiché i polinomi costanti si identificano con un singolo coefficiente

## Oss

- **Hp**
    - $\mathbb{K}$ campo
- **Th**
    - $\mathbb{K}[x]$ è un dominio
- **Dim**
    - ⚠️  **MANCA UNA DIMOSTRAZIONE**


## Def

- **Radici di un polinomio**
> - $\mathbb{K}$ campo
> - $p(x) \in \mathbb{K}[x]$
> - $\{c \in \mathbb{K}\ \mid p(c) = 0\}$ è l'**insieme delle radici di $p(x)$**

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $p(x) \in \mathbb{K}[x]$
    - $c \in \mathbb{K}$
- **Th**
    - $p(c) = 0 \iff x - c \mid p(x)$
- **Hp**
    - _prima implicazione_
        - per il teorema della divisione con il resto tra polinomi, dividendo $p(x)$ per $(x - c)$ si ottiene che $\exists!q(x), r(x) \in \mathbb{K}[x] \mid p(x) = q(x) \cdot (x - c) + r(x)$
        - $r_0 := r(x)$
        - $p(c) = q(c) (c - c) + r_0 = r_0$, ma $p(c) = 0$ in ipotesi, e dunque $r_0 = 0$
        - $r_0 = 0 \implies p(x) = q(x)(x - c) \implies x- c \mid p(x)$
    - _seconda implicazione_
        - $x - c \mid p(x) \implies \exists p(x) \in \mathbb{K}[x] : p(x) = q(x)\cdot (x - c)$, allora $p(c) = q(c) \cdot (c - c) = 0 \implies c$ radice di $p(x)$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $p(x) \in \mathbb{K}[x]$
    - $n := \deg(p(x))$
- **Th**
    - $|\{c \in \mathbb{K} \mid p(c) = 0\}| \le n$
- **Dim**
    - ipotizzando $N :=|\{c \in \mathbb{K} \mid p(c) = 0\}| \gt n \implies \{c_1, \ldots, c_N\}$ sia l'insieme delle radici
    - per dimostrazione precedente $\left.\begin{array}{c} x - c_1 \mid p(x) \\ \vdots \\ x-c_N \mid p(x) \end{array}\right\} \implies (x - c_1) \cdot \ldots \cdot (x - c_N) \mid p(x)$
    - ⚠️  **MANCA LA DIMOSTRAZIONE**
    - ma $\deg\left((x - c_1) \cdot \ldots \cdot (x - c_N)\right) = N$, mentre $\deg(p(x)) = n$, dove $M \gt n \ \bot$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $I \subset \mathbb{K}[x]$ ideale
- **Th**
    - $I$ è un ideale principale
- **Dim**
    - _unicità_
        - $I = \{0\} \implies I = I(0)$, ovvero l'ideale principale generato da $0$
        - preso $p(x) \in I - \{0\} \mid \deg(p(x))$ sia il minore possibile, allora $\forall q(x) \in I \mid \deg(q(x)) \lt \deg(p(x)) \implies q(x) \in I(0) \implies q(x) = 0$, di conseguenza è unico in quanto l'elemento minore in $I - \{0\}$ è unico
    - _esistenza_
        - $\exists p(x) \in I - \{0\} \mid I = I(p(x))$, dove $p(x)$ è il polinomio di grado minore in $I - \{0\}$
            - $I \subset I(p(x))$
                - per il teorema della divisione con il resto tra polinomi $\forall a(x) \in I \quad \exists ! q(x), r(x) \mid a(x) = p(x) \cdot q(x) + r(x) \quad \deg(r(x)) \lt \deg(p(x)) \implies r(x) = a(x) - p(x) \cdot q(x)$
                - $\left.\begin{array}{l} a(x) \in I \\ p(x) \in I - \{0\} \implies p(x) \cdot q(x) \in I \end{array}\right\} \implies r(x) \in I$
                - ma poiché $\deg(r(x)) \lt \deg(p(x))$, e $p(x)$ è stato preso con il grado minore possibile, per osservazione precedente segue necessariamente che $r(x) = 0$, e dunque $a(x) = p(x) \cdot q(x) \implies a(x) \in I(p(x)) \implies I \subset I(p(x))$
            - $I(p(x)) \subset I$
                - $p(x) \in I - \{0\}$ e $I$ è un ideale per ipotesi, dunque in particolare $\mathbb{K}[x] \cdot I \subset I$, quindi $\forall q(x) \in \mathbb{K}[x] \quad q(x) \cdot p(x) \in I$
                - $\forall a(x) \in I(p(x)) \quad \exists q(x) \in \mathbb{K}[x] \mid q(x)\cdot p(x) = a(x)$, dunque $a(x) \in I$ per osservazione precedente, allora $I(p(x)) \subset I$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $I(a_1(x)), \ldots, I(a_n(x)) \subset \mathbb{K}[x]$ ideali
    - $\exists d(x) \in \mathbb{K}[x]\mid I(a_1(x), \ldots, a_n(x)) = I(d(x))$
- **Th**
    - $d(x)=\textrm{MCD}(a_1(x), \ldots, a_n(x))$
- **Dim**
    - la dimostrazione è analoga al caso di $\mathbb{Z}$
    - in particolare, $\textrm{MCD}(a_1(x), \ldots, a_n(x))$ è ben definito in quanto, per dimostrazione precedente, la divisione con il resto tra polinomi è ben definita, ed è dunque possibile calcolare il massimo comun divisore attraverso, ad esempio, l'algoritmo di Euclide
    - inoltre, $d(x)$ è ben definito a meno di una costante moltiplicativa non nulla
        - ad esempio $d(x) = x + 1$, allora $\forall a \in \mathbb{K} \quad a(x + 1)$ è ancora divisore

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
        - ad esempio $m(x) = x + 1$, allora $\forall a \in \mathbb{K} \quad a(x + 1)$ è ancora multiplo

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
        - ⚠️  **MANCA LA DIMOSTRAZIONE**
    - _seconda implicazione_
        - per definizione $\forall i \in [1, n] \quad d(x) \mid a_i(x)$
        - per dimostrazione precedente $d(c) = 0 \iff (x - c) \mid d(x)$
        - per dimostrazione precedente, $\mid$ è un ordine parziale, e in particolare transitiva, e dunque $\forall i \in [1, n] \quad (x - c) \mid d(x) \land d(x) \mid a_i(x) \implies (x - c) \mid a_i(x)$, e riapplicando lo stesso teorema $\forall i \in [1, n]\quad (x - c) \mid a_i(x) \iff a(c) = 0$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $p(x) \in \mathbb{K}[x]$
- **Th**
    - $p(x) \in \mathbb{K}[x]$ irriducibile $\iff p(x)$ primo
- **Dim**
    - _prima implicazione_
        - $p(x) \in \mathbb{K}[x]$ irriducibile$
        - si supponga $\exists d(x) \in \mathbb{K}[x] : d(x) \mid p(x) \implies \exists e(x) \in \mathbb{K}[x] \mid p(x) = p(x) \cdot e(x)$
        - ⚠️  **NON HO CAPITO NULLA QUI C'È UN BUCO**
        - $p(x) \nmid a(x) \implies \textrm{MCD}(a(x), p(x))= 1$ ⚠️  **NON SO IL PERCHÉ**
            - per l'identità di Bézout $\exists f(x), g(x) \in \mathbb{K}[x] \mid 1 = f(x)a(x) + g(x)p(x) \iff b(x) = a(x)b(x)f(x) + p(x)g(x)b(x)$
        - ⚠️  **NON HO CAPITO NULLA QUI C'È UN BUCO**
    - _seconda implicazione_
        - per dimostrazione precedente $\mathbb{K}[x]$ è un dominio di integrità, e dunque, per dimostrazione precedente, implica che ogni elemento primo è anche irriducibile

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $p(x) \in \mathbb{K}[x] - \{0\}$
- **Th**
    - $\exists ! q_1(x), \ldots ,q_k(x) \in \mathbb{K}[x]$ irriducibili e monici$, c \in \mathbb{K} - \{0\} \mid p(x) = c \cdot q_1(x) \cdot \ldots \cdot q_k(x)$
    - in particolare, i polinomi sono unici a meno di un riordinamento
- **Dim**:
    - _esistenza_:
        - $\deg(p(x)) = 1$
            - ⚠️  **NON HO CAPITO NULLA**
        - $\deg(p(x)) \gt 1$
            - ⚠️  **NON HO CAPITO NULLA**
    - _unicità_
        - ⚠️  **NON HO CAPITO SU COS'È L'INDUZIONE**
        - $\deg(p(x)) = 0$
            - ⚠️  **NON HO CAPITO NULLA**
        - $\deg(p(x)) \gt 0$
            - si supponga $\exists q_1(x), \ldots q_k(x), q_1'(x), \ldots, q_j'(x) \in \mathbb{K}[x], c, c' \in \mathbb{K} \mid c \cdot q_1(x) \cdot \ldots \cdot q_i(x) = p(x) = c'\cdot q_1'(x) \cdot \ldots \cdot q_j'(x)$ dove $c \neq c', \forall k \in [1, i] \quad q_k(x) \neq q_k'(x)$
            - ⚠️  **DOVE HA DIMOSTRATO CHE $i = k$????**

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $p(x) \in \mathbb{K}[x]$
- **Th**
    - $p(x)$ irriducibile $\iff \deg(p(x)) = 1$
- **Dim**
    - _prima implicazione_    
        - ipotizzando che $\deg(p(x)) \gt 1 \implies \exists z \in \mathbb{C} \mid p(z) = 0$ per il teorema fondamentale dell'algebra
        - per dimostrazione precedente $p(z) = 0 \iff x - z \mid p(x) \implies \exists q(x) \in \mathbb{K}[x] \mid p(x) = (x - z) \cdot q(x)$
        - poiché $\deg(x - z) = 1$, allora necessariamente $\deg(q(x)) = \deg(p(x)) - 1$
        - $\deg(p(x)) \gt 1 \implies \deg(q(x)) = \deg(p(x)) - 1 \gt 0 \implies p(x)$ non è irriducibile $\bot$
    - _seconda implicazione_
        - per dimostrazione precedente $\forall a(x), b(x), c(x) \in \mathbb{K}[x] \quad a(x) = b(x) \cdot c(x) \implies \deg(a(x)) = \deg(b(x)) + \deg(c(x))$
        - $\deg(p(x)) = 1$, se $\exists a(x), b(x) \in \mathbb{K}[x] \mid p(x) = a(x) \cdot b(x)$, allora $\deg(p(x)) = \deg(a(x))+\deg(b(x)) \implies \deg(a(x)) = 1 \land \deg(b(x)) = 0$ oppure $\deg(a(x)) = 0 \land \deg(b(x)) = 1$
        - dunque, ad esempio se $\deg(a(x)) = 1 \land \deg(b(x)) = 0 \implies b(x) \in \mathbb{K}[x]^*$, e dunque $p(x)$ è dato dal prodotto di un polinomio irriducibile e una costante, e dunque $p(x)$ è irriducibile

## Def

- ⚠️  **MOLTEPLICITÀ (?)**

## Oss

- **Hp**
    - $p(x) \in \mathbb{R}[x]$
- **Th**
    - $p(x)$ irriducibile $\iff \deg(p(x)) = 1$ oppure $\deg(p(x)) = 2 \land \Delta \lt 0$
- **Dim**
    - per dimostrazione precedente $\mathbb{R}$ campo $\implies \forall p(x) \in \mathbb{R}[x]$ irriducibile $\iff \deg(p(x)) = 1$, dunque segue la prima tesi
    - $p(x)$ irriducibile $\iff \deg(p(x)) = 2 \land \Delta \lt 0$
        - _prima implicazione_
        - _seconda implicazione_
            - ipotizzando $p(x)$ non irriducibile $\exists a(x), b(x) \in \mathbb{R}[x] \mid p(x) = a(x) \cdot b(x) \implies \deg(a(x)) = \deg(b(x)) = 1$ per dimostrazione precedente
            - dunque $a(x)$ e $b(x)$ sono della forma $a(x) = cx + d \quad c \in R - \{0\}$, ma allora $x' := -c^{-1}d$ è radice di $a(x)$, e dunque necessariamente è anche radice di $p(x)$
            - $\deg(p(x)) = 2 \land \exists x' \in \mathbb{R} \mid p(x') = 0 \implies p(x)$ non è irriducibile $\bot$

## Oss

- **Hp**
    - $a_0, \ldots, a_n \in \mathbb{Z} \mid a_0, a_n \neq 0$
    - $p(x) \in \mathbb{Z}[x] \mid p(x) = a_0 + \ldots + a_nx^n$
    - $a, b \in \mathbb{Z} \mid \textrm{MCD}(a, b) = 1$
    - $p(\frac{a}{b}) = 0$
- **Th**
    - $a \mid a_0 \land b \mid a_n$
- **Dim**
    - $0 = p(\frac{a}{b}) = a_n(\frac{a}{b})^n + a_{n - 1}\left(\frac{a^{n - 1}}{b^{n - 1}}\right) + \ldots + a_0$
    - moltiplicando entrambe i membri dell'equazione per $b^n$ si ottiene $0 = a_na^n + a_{n -1}a^{n - 1}b + \ldots + a_1a^1b^{n -1 } + a_0b^n$
    - allora $a_na^n = - a_{n - 1} a^{n - 1}b - \ldots - a_1a^1 b^{n - 1}- a_0b^n$
    - poiché ogni sottraendo del secondo membro di tale equazione è un multiplo di $b$, mettendo in evidenza $b$ si ottiene che $b \mid a_na^n$
    - $\textrm{MCD}(a, b) = 1 \implies \textrm{MCD}(a^n, b) = 1$, ma allora $b \mid a_na^n \implies b \mid a_n$
    - è possibile ripetere il ragionamento analogo per $a_0b^n$, e dall'equazione ottenuta si noterà che $a \mid a_0b^n$, che per ragionamento analogo all'osservazione precedente deve necessariamente implicare che $a \mid a_0$

## Oss

- ⚠️  **MANCA UN TEOREMA ENORME**
