# Spazi Vettoriali

## Def 

- **Spazio vettoriale**

> - $V$ insieme
> - $\mathbb{K}$ campo
> - $+: V \times V \rightarrow V$
> - $\cdot : \mathbb{K} \times V \rightarrow V$
> - $V$ è detto **spazio vettoriale su $\mathbb{K}$** $\iff$
>   - $(V, +)$ gruppo abeliano
>   - $\exists 1 \in \mathbb{K} \mid \forall v \in V \quad 1v = v$
>      - in particolare, deve esistere l'_elemento neutro per il prodotto per scalare_
>   - $\forall u, v \in V, k \in \mathbb{K} \quad k(u + v) = ku + kv$
>     - in particolare, deve valere la _proprietà distributiva a destra del prodotto per scalare_
>   - $\forall v \in V, k, h \in \mathbb{K} \quad (k + h)v = kv + hv$
>     - in particolare, deve valere la _proprietà distributiva a sinistra del prodotto per scalare_
>   - $\forall v \in V, k, h \in \mathbb{K} \quad (kh)v = k(hv)$
>      - in particolare, deve valere la _proprietà associativa del prodotto per scalare_
> - $x \in \mathbb{K}$ è detto **scalare**
> - $x \in V$ è detto **vettore**

## Ex

- **Hp**
    - $n \in \mathbb{N}$
    - $\mathbb{K}$ campo
- **Th**
    - $\mathbb{K}^n$ spazio vettoriale su $\mathbb{K}$, ed è detto _spazio di coordinate_
- **Dim**
    - $\forall v \in \mathbb{K}^n \quad \exists t_1, \ldots, t_n \in \mathbb{K} \mid v = (t_1, \ldots, t_n)$
    - $\forall w \in \mathbb{K}^n \quad \exists s_1, \ldots, s_n \in \mathbb{K} \mid w = (s_1, \ldots, s_n)$
    - $\forall \lambda \in \mathbb{K} \quad \lambda \cdot v := (\lambda \cdot t_1, \ldots, \lambda \cdot t_n)$
    - $v + w := (s_1 + t_1, \ldots, s_n + t_n)$
    - avendo definito $+$ e $\cdot$ in questo modo, gli assiomi di spazio vettoriale sono rispettati necessariamente

## Def

- **Sottospazio vettoriale**

> - $\mathbb{K}$ campo
> - $V$ spazio vettoriale su $\mathbb{K}$
> - $W \subseteq V$
> - $W \subset V$ è detto **sottospazio vettoriale di $V$** $\iff$
>   - $(W, +) \leqslant (V, +)$
>   - $\mathbb{K} \cdot W \subseteq W$

## Def

- **Span di vettori**

> - $n \in \mathbb{N}$
> - $\mathbb{K}$ campo
> - $V$ spazio vettoriale su $\mathbb{K}$
> - $v_1, \ldots, v_n \in V$
> - $\textrm{span}(v_1, \ldots, v_n) := \{\lambda_1 v_1 + \ldots + \lambda_n v_n \mid \lambda_1, \ldots , \lambda_n \in \mathbb{K}\}$ è detto **span degli $v_1, \ldots v_n$**
>   - in particolare, costituisce l'insieme delle _combinazioni lineari degli $v_1, \ldots, v_n$_

## Oss

- **Hp**
    - $n \in \mathbb{N}$
    - $\mathbb{K}$ campo
    - $V$ spazio vettoriale su $\mathbb{K}$
    - $v_1, \ldots, v_n \in V$
- **Th**
    - $\textrm{span}(v_1, \ldots, v_n) \subset V$ sottospazio vettoriale
- **Dim**
    - $(\textrm{span}(v_1, \ldots, v_n), +) \leqslant (V, +)$
        - $0_V = 0v_1 + \ldots + 0v_n \implies 0 \in \textrm{span}(v_1, \ldots, v_n)$
        - $\forall u, v \in \textrm{span}(v_1, \ldots, v_n) \quad \exists \lambda_1, \ldots , \lambda_n, \mu_1 \ldots \mu_n \in \mathbb{K} \mid \left \{ \begin{array}{l}u= \lambda_1v_1 + \ldots + \lambda_n v_n \\ w = \mu_1 v_1+ \ldots + \mu_nv_n \end{array} \right. \implies v + w = (\lambda_1 \mu_1) v_1 + \ldots + (\lambda_n \mu_n) v_n \implies v + w \in \textrm{span}(v_1, \ldots, v_n)$
        - $\forall u \in \textrm{span}(v_1, \ldots, v_n) \quad \exists \lambda_1 , \ldots \lambda_n \in \mathbb{K} \mid u = \lambda_1 v_1 + \ldots + \lambda_n v_n \iff - u = (-\lambda _1) v_1 + \ldots + (- \lambda_n) v_n \implies -u \in \textrm{span}(v_1, \ldots, v_n)$
    - $\forall w \in \textrm{span}(v_1, \ldots, v_n) \quad \exists \lambda_1 , \ldots , \lambda_n \in \mathbb{K} \mid w = \lambda_1 v_1 + \ldots + \lambda_n v_n \implies \forall c \in \mathbb{K} \quad c\cdot w = c \cdot (\lambda_1v_1 + \ldots + \lambda_n v_n) =(c\lambda_1) v_1 + \ldots + (c\lambda_n) v_n \implies c\cdot w \in \textrm{span}(v_1, \ldots, v_n)$

## Def

- **Generatori di uno spazio vettoriale**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N}$
> - $V$ spazio vettoriale su $\mathbb{K}$
> - $v_1, \ldots, v_n \in V$
> - $v_1, \ldots, v_n$ sono detti **generatori di $V$** $\iff V \subseteq \textrm{span}(v_1, \ldots, v_n)$
>     - equivalentemente, ogni vettore in $V$ è una combinazione lineare degli $v_1, \ldots, v_n$
>     - si noti che è sempre vero che $\textrm{span}(v_1, \ldots, v_n) \subseteq V$, di conseguenza è possibile considerare nella definizione $\textrm{span}(v_1, \ldots, v_n) = V$ senza perdita di generalità

- **Indipendenza lineare**

> - $n \in \mathbb{N}$
> - $\mathbb{K}$ campo
> - $V$ spazio vettoriale su $\mathbb{K}$
> - $v_1, \ldots, v_n \in V - \{0_V\}$
> - $v_1, \ldots, v_n$ sono detti **linearmente indipendenti** $\iff$
>    - $\lambda_1 v_1 + \ldots + \lambda_n v_n = 0_V \iff \lambda_1 = \ldots = \lambda_n = 0_{\mathbb{K}}$
>    - equivalentemente, nessuno degli $v_1, \ldots, v_n$ è combinazione lineare degli altri
>    - si noti che il secondo verso dell'implicazione è sempre verificato

- **Base di uno spazio vettoriale**

> - $n \in \mathbb{N}$
> - $\mathbb{K}$ campo
> - $V$ spazio vettoriale su $\mathbb{K}$
> - $v_1, \ldots, v_n \in V - \{0_V\}$
> - $v_1, \ldots, v_n$ costituiscono una **base di $V$** $\iff v_1, \ldots, v_n$ linearmente indipendenti e generatori di $V$
>   - in particolare, $n$ è detta _cardinalità della base $v_1, \ldots, v_n$_

## Ex

- **Hp**
    - $n \in \mathbb{N}$
    - $\mathbb{K}$ campo
    - $\left \{ \begin{array}{c} e_1 := (1, 0, \ldots, 0) \\ \vdots \\e_n :=(0, \ldots, 0, 1) \end{array} \right. \in \mathbb{K}^n$
- **Th**
    - $e_1, \ldots, e_n$ sono una base di $\mathbb{K}^n$, ed è detta _base canonica_
- **Dim**
    - $e_1, \ldots, e_n$ sono generatori di $\mathbb{K}^n$
        - $\forall v \in \mathbb{K}^n \quad \exists t_1, \ldots, t_n \in \mathbb{K} \mid v = (t_1, \ldots, t_n) \implies v = (t_1, 0, \ldots, 0) + \ldots + (0, \ldots, 0, t_n) = t_1 \cdot e_1 + \ldots + t_n \cdot e_n \implies v \in \textrm{span}(e_1, \ldots, e_n)$
    - $e_1, \ldots, e_n$ sono linearmente indipententi
        - $\forall \lambda_1, \ldots, \lambda_n \in \mathbb{K} \quad \left \{ \begin{array}{c} \lambda_1e_1=(\lambda_1, 0, \ldots, 0) \\ \vdots \\\lambda_n e_n = (0, \ldots, 0, \lambda_n) \end{array} \right. \implies \lambda_1 e_1 + \ldots + \lambda_n e_n = (\lambda_1, \ldots , \lambda_n)$, e questo vettore è pari al vettore nullo $0_{\mathbb{K}^n}$ solamente quando $\lambda _1 = \ldots = \lambda_n = 0_{\mathbb{K}}$

## Lem

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N}$
    - $V$ spazio vettoriale su $\mathbb{K}$
    - $v_1, \ldots, v_n \in V - \{0_V\}$
- **Th**
    - $v_1, \ldots, v_n$ linearmente indipendenti $\iff v_1, \ldots, v_{n - 1}$ linearmente indipendenti $\land v_n \notin \textrm{span}(v_1, \ldots, v_{n - 1})$
- **Dim**
    - _prima implicazione_
        - _omessa dal professore_
    - _seconda implicazione_
        - per assurdo $\exists \lambda_n \in \mathbb{K} - \{0\}, \lambda_1, \ldots, \lambda_{n - 1} \in \mathbb{K} \mid \lambda_1 v_1 + \ldots + \lambda_n v_n = 0_V \iff -\lambda_n v_n = \lambda_1 v_1 + \ldots + \lambda_{n-1} v_{n-1} \iff v_n = (-\lambda_n^{-1})\lambda_1 v_1 + \ldots + (-\lambda_n^{-1})\lambda_{n - 1}v_{n - 1} \iff v_n \in \textrm{span}(v_1, \ldots, v_{n - 1}) \ \bot \implies \lambda_n = 0_V$
        - $v_1, \ldots, v_{n - 1}$ linearmente indipendenti $\implies \exists \lambda_1, \ldots, \lambda_{n-1} \mid \lambda_1 v_1 + \ldots + \lambda_{n - 1} v_{n - 1} = 0_V \implies \lambda_1 = \ldots = \lambda_{n - 1} = 0_V = \lambda_n \implies v_1, \ldots, v_n$ linearmente indipendenti

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $n, k \in \mathbb{N}$
    - $V$ spazio vettoriale su $\mathbb{K}$
    - $w_1, \ldots, w_n \in V$
    - $v_1, \ldots, v_k \in \textrm{span}(w_1, \ldots, w_n) \mid v_1, \ldots, v_k$ linearmente indipendenti
- **Th**
    - $k \le n$
- **Dim**
    - dimostrazione per induzione sui $k$ vettori
    - _caso base_
        - bisogna dimostrare che per $i = 1$ vettori linearmente indipendenti si ha che $\textrm{span}(v_1, w_2, \ldots, w_n) = \textrm{span}(w_1, \ldots, w_n)$
            - la tesi equivale a dimostrare che $v_1$ e $w_1$ sono intercambiabili nello span
            - $v_1 \in \textrm{span}(w_1, \ldots, w_n) - \{0_V\} \iff \exists \lambda_1, \ldots, \lambda_n \in \mathbb{K} \mid v_1 = \lambda_1 w_1 + \ldots + \lambda_n w_n$, e in particolare $v_1 \neq 0_V \iff \exists i \in [1, n] \mid \lambda_i \neq 0$
            - a meno di riordinamento, si può assumere $\lambda_1 \neq 0$
            - allora $v_1 = \lambda_1 w_1 + \ldots + \lambda_n w_n \iff \lambda_1w_1 = v_1 + (-\lambda_2w_2) + \ldots + (-\lambda_nw_n) \iff w_1 = (\lambda_1^{-1})v_1 + (-\lambda_1^{-1}\lambda_2)w_2 + \ldots + (-\lambda_1^{-1}\lambda_n)w_n \implies w_1 \in \textrm{span}(v_1, w_2, \ldots, w_n)$
        - $\textrm{span}(v_1, w_2, \ldots, w_n) \subseteq \textrm{span}(w_1, \ldots, w_n)$
            - $u \in \textrm{span}(v_1, w_2, \ldots, w_n) \iff \exists \mu_1, \ldots \mu_n \in \mathbb{K} \mid u = \mu_1 v_1 + \mu_2 w_2 + \ldots + \mu_n w_n = \mu_1(\lambda_1 w_1 + \ldots + \lambda_nw_n) + \mu_2w_2 + \ldots + \mu_nw_n = (\mu_\ \lambda_1)w_1+(\mu_1 \lambda_2 \mu_2)w_2 + \ldots + (\mu_1\lambda_n\mu_n)w_n \implies u \in \textrm{span}(w_1, \ldots, w_n)$
        - $\textrm{span}(w_1, \ldots, w_n) \subseteq \textrm{span}(v_1, w_2, \ldots, w_n)$
            - siano $\mu_1, \ldots, \mu_n \in \mathbb{K} \mid w_1 = \mu_1 v_1 + \mu_2 w_2 + \ldots + \mu_n w_n$
            - $u \in \textrm{span}(w_1, \ldots, w_n) \iff \exists \lambda_1, \ldots, \lambda_n \in \mathbb{K} \mid u = \lambda_1 w_1 + \ldots + \lambda_n w_n = \lambda_1 (\mu_1 v_1 + \mu_2 w_2 + \ldots + \mu_n w_n) + \lambda_2 w_2 + \ldots + \lambda_nw_n = (\lambda_1 \mu_1)v_1 + (\lambda_1 \mu_2 \lambda_2)w_2 + \ldots + (\lambda_1 \mu_n \lambda_n)w_n \implies u \in \textrm{span}(v_1, w_2, \ldots, w_n)$
    - _ipotesi induttiva forte_
        - si assume che per $1 \le i \le n$ vettori linearmente indipendenti si ha che $\textrm{span}(v_1, \ldots, v_i, w_{i + 1}, \ldots, w_n) = \textrm{span}(w_1, \ldots, w_n)$
            - l'ipotesi equivale a supporre che $v_1, \ldots, v_i$ e $w_1, \ldots, w_i$ siano intercambiabili nello span
    - _passo induttivo_
        - bisogna dimostrare che per $i + 1 \le n$ vettori linearmente indipendenti si ha che $\textrm{span}(v_1, \ldots, v_i, v_{i + 1}, w_{i + 2}, \ldots, w_n) = \textrm{span}(w_1, \ldots, w_n)$
            - la tesi equivale a dimostrare che, assumendo l'ipotesi induttiva forte, $v_{i + 1}$ e $w_{i + 1}$ sono intercambiabili
            - $v_{i + 1} \in \textrm{span}(w_1, \ldots, w_n) = \textrm{span}(v_1, \ldots, v_i, w_{i + 1}, \ldots, w_n) \iff \exists \mu_1, \ldots, \mu_i, \lambda_{i + 1}, \ldots, \lambda_n \in \mathbb{K} \mid v_{i + 1} = \mu_1 v_1 + \ldots + \mu_i v_i + \lambda_{i + 1}w_{i + 1} + \ldots + \lambda_nw_n$
            - per assurdo, ipotizzando $\lambda_{i + 1} = \ldots = \lambda_n = 0_{\mathbb{K}} \implies v_{i + 1} = \mu_1 v_1 + \ldots + \mu_n v_i \implies v_1, \ldots, v_{i + 1}$ non sarebbero linearmente indipendenti $\bot$
            - allora $\exists j \in [i + 1, n] \mid \lambda_j \neq 0$, e in particolare $v_{i + 1} \neq 0_V$
            - a meno di riordinamento, si può assumere $\lambda_{i + 1} \neq 0$
            - allora $v_{i + 1} = \mu_1 v_1 + \ldots + \mu_i v_i + \lambda_{i + 1} w_{i + 1}+ \ldots + \lambda_nw_n \iff\lambda_{i + 1}w_{i + 1} = v_{i + 1} + (-\mu_1v_1) + \ldots + (-\mu_iv_i) + (-\lambda_{i + 2}w_{i + 2}) + \ldots + (-\lambda_nw_n) \iff w_{i + 1} = (\lambda_{i + 1}^{-1})v_{i + 1} + (-\lambda_{i + 1}^{-1}\mu_1)v_1 + \ldots + (-\lambda_{i +1}^{-1}\mu_i)v_i + (-\lambda_{i + 1}^{-1}\lambda_{i + 2})w_{i + 2} + \ldots + (-\lambda_{i + 1}^{-1}\lambda_n)w_n \implies w_{i + 1} \in \textrm{span}(v_1, \ldots, v_i, v_{i + 1}, w_{i + 2}, \ldots w_n)$
        - $\textrm{span}(v_1, \ldots, v_i, v_{i + 1}, w_{i + 2}, \ldots, w_n) \subseteq \textrm{span}(w_1, \ldots, w_n)$
            - $u \in \textrm{span}(v_1, \ldots, v_i, v_{i + 1}, w_{i + 2} \ldots , w_n) \iff \exists \eta_1, \ldots, \eta_i, \eta_{i + 1}, \varepsilon_{i + 2}, \dots, \varepsilon_n \in \mathbb{K} \mid u = \eta_1v_1 + \ldots + \eta_iv_i + \eta_{i + 1}v_{i +1} + \varepsilon_{i + 2}w_{i + 2} + \ldots + \varepsilon_nw_n =\eta_1v_1 + \ldots+\eta_iv_i+\eta_{i +1}(\mu_1v_1 + \ldots + \mu_iv_i + \lambda_{i + 1}w_{i + 1} + \ldots + \lambda_nw_n)+ \varepsilon_{i + 2}w_{i + 2} + \ldots + \varepsilon_nw_n = (\eta_1\eta_{i+1}\mu_1)v_1+ \ldots + (\eta_i\eta_{i + 1}\mu_i)v_i+(\eta_{i + 1}\lambda_{i + 1})w_{i + 1} +(\varepsilon_{i + 2}\eta_{i + 1}\lambda_{i + 1})w_{i + 2} + \ldots + (\varepsilon_n\eta_{i + 1}\lambda_n)w_n \implies u \in \textrm{span}(v_1, \ldots, v_i, w_{i + 1}, \ldots, n) = \textrm{span}(w_1, \ldots, w_n)$ per ipotesi induttiva
        - $\textrm{span}(w_1, \ldots, w_n) \subseteq \textrm{span}(v_1, \ldots, v_i, v_{i + 1}, w_{i + 2}, \ldots, w_n)$
            - siano $\eta_1, \ldots, \eta_i, \eta_{i + 1}, \varepsilon_{i + 2} \ldots, \varepsilon_n \in \mathbb{K} \mid w_{i + 1} = \eta_1 v_1 + \ldots + \eta_iv_i + \eta_{i + 1} v_{i + 1} + \varepsilon_{i + 2}w_{i + 2} + \ldots +\varepsilon_nw_n$
            - $u \in \textrm{span}(w_1, \ldots, w_n) = \textrm{span}(v_1, \ldots, v_i, w_{i + 1}, \ldots, w_n)$ per ipotesi induttiva $\implies \exists \mu_1, \ldots, \mu_i, \lambda_{i + 1}, \ldots, \lambda_n \in \mathbb{K} \mid u = \mu_1v_1 + \dots + \mu_iv_i+ \lambda_{i + 1}w_{i + 1} + \ldots + \lambda_nw_n = \mu_1 v_1 + \ldots + \mu_i v_i + \lambda_{i + 1}(\eta_1 v_1 + \ldots + \eta_iv_i + \eta_{i + 1} v_{i + 1} + \varepsilon_{i + 2}w_{i + 2} + \ldots +\varepsilon_nw_n) + \lambda_{i + 2}w_{i + 2} + \ldots + \lambda_nw_n =(\mu_1\lambda_{i + 1}\eta_1)v_1 + \ldots + (\mu_i\lambda_{i + 1}\eta_i)v_i + (\lambda_{i + 1}\eta_{i + 1})v_{i + 1} + (\lambda_{i + 2}\lambda_{i+1}\varepsilon_{i + 2})w_{i + 2} + \ldots + (\lambda_n\lambda_{i + 1}\varepsilon_n)w_n \implies u \in \textrm{span}(v_1, \ldots, v_i, v_{i + 1}, w_{i + 2}, \ldots w_n)$
    - allora l'ipotesi induttiva è verificata, e per il caso $i = n$ si ha che $\textrm{span}(v_1, \ldots, v_n) = \textrm{span}(w_1, \ldots, w_n)$
    - per assurdo $\exists v_{n + 1} \in \textrm{span}(w_1, \ldots, w_n) \mid v_{n + 1}$ linearmente indipendente con $v_1, \ldots, v_n$, allora $v_{n + 1} \in \textrm{span}(w_1, \ldots, w_n) = \textrm{span}(v_1, \ldots, v_n) \implies v_{n + 1}$ è combinazione lineare degli altri $\bot$
    - allora necessariamente $i \le n$
 
## Cor

- **Hp**
    - $\mathbb{K}$ campo
    - $n, m \in \mathbb{N}$
    - $V$ spazio vettoriale su $\mathbb{K}$
    - $w_1, \ldots, w_m \in V \mid w_1, \ldots, w_m$ base di $V$
    - $v_1, \ldots, v_n \in V \mid v_1, \ldots, v_n$ base di $V$
- **Th**
    - $n = m$, il che implica che la cardinalità delle basi di uno spazio vettoriale è unica
- **Dim**
    - $v_1, \ldots, v_n$ e $w_1, \ldots, w_m$ basi di $V \implies \textrm{span}(v_1, \ldots, v_n) = \textrm{span}(w_1, \ldots, w_m) = V$ poiché generatori di $V$
    - $v_1, \ldots, v_n$ e $w_1, \ldots, w_m$ basi di $V \implies v_1, \ldots, v_n$ e $w_1, \ldots w_m$ linearmente indipendenti
        - $v_1, \ldots , v_n \in V = \textrm{span}(w_1, \ldots, w_m) \implies n \le m$ per dimostrazione precedente
        - $w_1, \ldots, w_m \in V = \textrm{span}(v_1, \ldots, v_n) \implies m \le n$ per dimostrazione precedente
    - dunque necessariamente $n = m$

## Def

- **Dimensione di uno spazio vettoriale**

> - $\mathbb{K}$ campo
> - $V$ spazio vettoriale su $\mathbb{K}$
> - $v_1, \ldots, v_n$ base di $V$
> - $\dim(V) = n$ è detta **dimensione di $V$**
>   - in particolare, coincide con la cardinalità delle basi di $V$, che per dimostrazione precedente è unica
> - $V$ si dice avere **dimensione infinita** $\iff$ non esiste un insieme finito di generatori in $V$

## Ex

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N}$
    - $\mathbb{K}[x]_{\le n} := \{p(x) \in \mathbb{K}[x] \mid \deg(p(x)) \le n\}$
- **Th**
    - $\mathbb{K}[x]_{\le n}$ spazio vettoriale su $\mathbb{K}$
    - $\dim(\mathbb{K}[x]_{\le n}) = n + 1$
- **Dim**
    - sia $p(x) \in \mathbb{K}[x]_{\le n} \mid \deg(p(x)) = n$
    - allora $\exists a_0, \ldots, a_n \in \mathbb{K} \mid p(x) = a_0x^0 + \ldots + a_nx^n$, che di fatto costituisce una combinazione lineare dei $x^0, \ldots, x^n$ attraverso i coefficienti $a_0, \ldots, a_n$
    - allora, si vede facilmente che $\{1, x, x^2, \ldots, x^n\}$ costituiscono una base di $\mathbb{K}[x]_{\le n}$, il che implica che $\dim(\mathbb{K}[x]_{\le n}) = n + 1$
        - si noti che di fatto si ha $n + 1$ per via del termine noto nei polinomi 
        - inoltre, questo dimostra che $\mathbb{K}[x]$ ha dimensione infinita, poiché non c'è limite al grado di un polinomio in $\mathbb{K}[x]$, dunque la cardinalità delle basi è necessariamente infinita

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N}$
    - $V$ spazio vettoriale su $\mathbb{K}$
    - $v_1, \ldots, v_n \in V$
- **Th**
    - $v_1, \ldots, v_n$ base di $V \iff \forall v \in V \quad \exists ! \lambda_1, \ldots, \lambda_n \in \mathbb{K} \mid v = \lambda_1 v_1 + \ldots + \lambda_n v_n$
- **Dim**
    - _prima implicazione_
        - _esistenza_
            - $v_1, \ldots, v_n$ base di $V$, allora per definizione $\forall v \in V \quad \exists \lambda_1, \ldots, \lambda_n \in \mathbb{K} \mid v = \lambda_1v_1 + \ldots + \lambda_n v_n$
        - _unicità_
            - per assurdo $\forall v \in V \quad \exists \lambda_1, \ldots, \lambda_n , \mu_1, \ldots, \mu_n \in \mathbb{K} \mid \lambda_1 v_1 + \ldots + \lambda_n v_n = v = \mu_1 v_1 + \ldots + \mu_n v_n \iff \lambda_1 v_1 + \ldots + \lambda_n v_n + (-\mu_1 ) v_1 + \ldots + (-\mu_n) v_n = 0_V \iff (\lambda_1 - \mu_1) v_1 + \ldots + (\lambda_n - v_n) v_n = 0_V$
            - $v_1, \ldots, v_n$ base di $V \implies v_1, \ldots, v_n$ linearmente indipendenti, allora $(\lambda_1 - \mu_1) v_1 + \ldots + (\lambda_n - \mu_n) v_n = 0_V \implies \lambda_1 - \mu_1 = \ldots = \lambda_n - \mu_n = 0_{\mathbb{K}} \iff \left \{ \begin{array}{c} \lambda_1 = \mu_1 \\ \vdots \\ \lambda_n = \mu_n \end{array} \right.$
    - _seconda implicazione_
        - _omessa dal professore_

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $W$ spazio vettoriale su $\mathbb{K}$
    - $n:= \dim(W)$
    - $k \in \mathbb{N} \mid k \lt n$
    - $w_1, \ldots, w_k \in W$ linearmente indipendenti
- **Th**
    - $\exists w_{k + 1}, \ldots, w_n \in W \mid w_1, \ldots, w_n$ base di $W$
- **Dim**
    - $k \lt n \implies \textrm{span}(w_1, \ldots, w_k) \subsetneqq W \implies \exists w_{k + 1} \in W \mid w_{k + 1} \notin \textrm{span}(w_1, \ldots, w_k)$, allora per dimostrazione precedente $w_1, \ldots, w_{k +1}$ sono linearmente indipendenti
    - per ragionamento analogo, è possibile estendere $w_1, \ldots, w_{k + 1}$ fino ad avere $w_1, \ldots, w_n$ vettori linearmente indipendenti
    - sia $v_1, \ldots, v_n$ base di $W$
    - per dimostrazione precedente, poiché $w_1, \ldots, w_n$ e $v_1, \ldots, v_1$ linearmente indipendenti, si ha che $W=\textrm{span}(v_1, \ldots, v_n) = \textrm{span}(w_1, \ldots, w_n) \implies w_1, \ldots, w_n$ base di $W$
        - si noti che, per lo stesso teorema, non è possibile avere $w_{n + 1} \in W \mid w_1, \ldots, w_{n +1}$ siano linearmente indipendenti

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $W$ spazio vettoriale su $\mathbb{K}$
    - $n := \dim(W)$
    - $m \in \mathbb{N} \mid m \ge n$
    - $w_1, \ldots, w_m \in W \mid w_1, \ldots, w_m$ generatori di $W$
- **Th**
    - $\exists 1 \le i_1, \ldots, i_n \le m \mid w_{i_1}, \ldots, w_{i_n}$ base di $W$
- **Dim**
    - è possibile assumere che $w_{i_1}$ non sia nullo, poiché $w_1, \ldots, w_m$ sono sicuramente non tutti nulli in quanto generatori di $W$
    - $w_{i_1} \neq 0 \implies w_{i_1}$ linearmente indipendente, ma non può costituire un generatore poiché sono meno di $n$ vettori $\implies \textrm{span}(w_{i_1}) \subsetneqq W \implies \exists w_{i_2} \in W \mid w_{i_2} \notin \textrm{span}(w_{i_1})$, allora per dimostrazione precedente $w_{i_1}, w_{i_2}$ linearmente indipendenti
    - è possible ripetere il ragionamento fino ad ottenere esattamente $n$ vettori, ottenendo $w_{i_1}, \ldots, w_{i_n}$ vettori linearmente indipendenti
        - analogamente al teorema precedente, non è possibile ripetere il ragionamento $n + 1$ volte

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $W$ spazio vettoriale su $\mathbb{K}$
    - $n:= \dim(W)$
    - $w_1, \ldots, w_n \in W$
- **Th**
    - $w_1, \ldots, w_n$ linearmente indipendenti $\iff w_1, \ldots, w_n$ generatori di $W$
- **Dim**
    - _prima implicazione_
        - per assurdo, siano $w_1, \ldots, w_n$ linearmente indipendenti ma non generatori di $W \implies \textrm{span}(w_1, \ldots, w_n) \subsetneqq W \implies \exists w_{n + 1} \in W \mid w_{n + 1} \notin \textrm{span}(w_1, \ldots, w_n)$, ma allora $w_1, \ldots, w_{n + 1}$ linearmente indipendenti, mentre i vettori linearmente indipendenti possono essere al massimo $n$ $\bot$
    - _seconda implicazione_
        - per assurdo, siano $w_1, \ldots, w_n$ generatori di $W$ ma non linearmente indipendenti $\implies \exists \lambda_1, \ldots, \lambda_n \in \mathbb{K} \mid \lambda_1w_1 + \ldots + \lambda_nw_n = 0_W$ dove $\exists i \in [1, n] \mid \lambda_i \neq 0 \implies w_i = -\lambda_i^{-1} \lambda_1w_1 - \ldots - \lambda_i^{-1} \lambda_nw_n$, dunque $w_i$ è combinazione lineare degli altri vettori, in simboli $w_i \in \textrm{span}(w_1, \ldots, \hat{w_i}, \ldots, w_n)$
        - inoltre $w_i \in \textrm{span}(w_1, \ldots, w_n)$, poiché $w_1, \ldots, w_n$ generatori di $W$, allora $\textrm{span}(w_1, \ldots, w_n) \subseteq \textrm{span}(w_1, \ldots, \hat{w_i}, \ldots, w_n)$
        - in generale, per qualsiasi insieme di vettori minore di $n$ si ha che $\textrm{span}(w_1, \ldots, \hat{w_i}, \ldots, w_n) \subseteq \textrm{span}(w_1, \ldots, w_n)$
        - allora segue che $\textrm{span}(w_1, \ldots, \hat{w_i}, \ldots, w_n) = \textrm{span}(w_1, \ldots, w_n)$, ma questo non è possibile in queanto $w_1, \ldots, \hat{w_i}, \ldots, w_n$ sono $n - 1$ generatori, e i generatori non possono essere meno di $n \ \bot$

## Def

- **$+$ tra spazi vettoriali**

> - $\mathbb{K}$ campo
> - $U, V$ spazi vettoriali su $\mathbb{K}$
> - $U + V := \{u + v \mid u \in U, v \in V\}$ è detta **somma tra $U$ e $V$**

- **$\cap$ tra spazi vettoriali**

> - $\mathbb{K}$ campo
> - $U, V$ spazi vettoriali su $\mathbb{K}$
> - $U \cap V := \{w \mid w \in U \land w \in V\}$ è detta **intersezione tra $U$ e $V$**

## Formula di Grassmann

- **Hp**
    - $\mathbb{K}$ campo
    - $W$ spazio vettoriale su $\mathbb{K}$
    - $U, V \subset W$ sottospazi vettoriali
- **Th**
    - $\dim(U + V) = \dim(U) + \dim(V) - \dim(U \cap V)$
- **Dim**
    - $k:=\dim(U \cap V)$
    - $m:=\dim(U)$
    - $n := \dim (V)$
    - sia $w_1, \ldots, w_k$ base di $U \cap V$
    - $\mathcal{B}_1 := \{w_1, \ldots, w_k, u_{k + 1}, \ldots, u_m\}$ base di $U$
    - $\mathcal{B}_2 := \{w_1, \ldots, w_k, v_{k + 1}, \ldots, v_n\}$ base di $V$
    - $\mathcal{B}_1 \cup \mathcal{B}_2 := \{w_1, \ldots w_k, u_{k + 1}, \ldots, u_m, v_{k + 1}, \ldots, v_n\}$
    - $u + v \in U + V \iff \exists u \in U, v \in V \mid \left \{ \begin{array}{l}u := \displaystyle \sum_{i = 1}^k{\lambda_iw_i} + \sum_{j = k + 1}^m{\lambda_j u_j} \\ \displaystyle v :=\sum_{i = 1}^k{\mu_iw_i} + \sum_{h = k + 1}^n {\mu_hv_h} \end{array} \right.\iff  \displaystyle u + v =\sum_{i = 1}^k{(\lambda_i + \mu_i)w_i} + \sum_{j = k + 1}^m{\lambda_j u_j} + \sum_{h = k + 1}^n {\mu_hv_h} \iff u + v \in \textrm{span}(\mathcal{B}_1 \cup \mathcal{B}_2)$
    - allora $U + V = \textrm{span}(\mathcal{B}_1 \cup \mathcal{B}_2) \implies \mathcal{B}_1 \cup \mathcal{B}_2$ generatori di $U + V$
    - $a := \displaystyle \sum_{i = 1}^k{\lambda_iw_i}$
    - $b := \displaystyle \sum_{j = k +1}^m{\mu_j u_j } \implies b \in \textrm{span}(u_{k +1 }, \ldots, u_k) \subsetneqq U \implies b \in U$
    - $c := \displaystyle \sum_{h = k + 1} ^n{\eta_hv_h}$
    - siano i coefficienti tali che $a + b + c= 0_W \iff b = - a - c$
    - $b \in U$ per osservazione precedente, mentre $a + c \in V \implies -(a + c) \in V \implies b = - a- c \in V \implies b \in U \cap V$, allora $b$ deve essere generato dalla base $w_1, \ldots, w_k$ di $U \cap V \implies \displaystyle \exists \alpha_1, \ldots, \alpha_k \in \mathbb{K} \mid \sum_{j = k +1}^m{\mu_j u_j }=:b = \displaystyle \sum_{i = 1}^k {\alpha_i w_i} \implies \sum_{j = k +1}^m{\mu_j u_j } - \displaystyle \sum_{i = 1}^k {\alpha_i w_i} = 0_W$
    - poiché per ipotesi $w_1, \ldots, w_k, u_{k +1}, \ldots, u_m$ è una base di $U$, in $U$ tali vettori sono linearmente indipendenti, dunque segue che ogni $\alpha_i$ e $\mu_j$ deve essere necessariamente $0_{\mathbb{K}}$
    - in particolare, si ha che $\forall j \in [k +1, m] \quad \mu_j =0 \implies b = 0_W \implies a + c = 0_W$
    <!-- - per ragionamento analogo, sapendo che $c = - a- b$ si otterrà che $c = 0_W$, e dunque $a + b + c = 0_W \iff a = 0_W$ -->
    - poiché $a + c = 0_W$, e $a + c$ è combinazione lineare di $\mathcal{B}_2$, allora i coefficienti della combinazione lineare saranno necessariamente nulli
    - dunque, l'equazione di partenza $a + b + c = 0_W$ è verificata solamente per coefficienti della combinazione lineare nulli, il che implica che i vettori che generano $a + b + c$, ovvero $\mathcal{B}_1 \cup \mathcal{B}_2$, sono linearmente indipendenti
    - allora, poiché generatori di $U + V$ e linearmente indipendenti, $\mathcal{B}_1 \cup \mathcal{B}_2$ sono una base di $U + V$
    - per definizione, la dimensione di uno spazio vettoriale è la cardinalità di una delle sue basi, e dunque la cardinalità di $\mathcal{B}_1 \cup \mathcal{B}_2$ è pari a $k + (m - k) + (n - k) = m + n - k \implies \dim(U + V) = \dim(U) + \dim(V) - \dim(U \cap V)$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $V$ spazio vettoriale su $\mathbb{K}$
    - $W \subset V$ sottospazio vettoriale
- **Th**
    - $V/W$ sottospazio vettoriale
- **Dim**
    - $+$ è ben definito per dimostrazione analoga a dimostrazioe precedente
    - è necessario dimostrare che $\cdot: \mathbb{K} \times V/W \rightarrow V/W$ è ben definito, allora $\forall [v], [w] \quad [v] = [w] \iff w - v \in W \implies \forall k \in \mathbb{K} \quad k(w - v) = kw - kv \in W \iff [kw] = [kv]$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $V$ spazio vettoriale su $\mathbb{K}$
    - $W \subset V$ sottospazio vettoriale
- **Th**
    - $\dim(V/W) = \dim(V) - \dim(W)$
- **Dim**
    - $n := \dim(V)$
    - $k := \dim(W)$
    - sia $w_1, \ldots, w_k$ base di $W$
    - $\textrm{span}(w_1, \ldots, w_k) \subsetneqq V \implies \exists v_{k + 1} \in V \mid v_{k + 1} \notin \textrm{span}(w_1, \ldots, w_k)$, allora per dimostrazione precedente $w_1, \ldots, w_k, v_{k + 1}$ linearmente indipendenti
    - dunque, è possibile estendere la base di $W$ scelta, fino ad ottenere una base di $V$ della forma $w_1, \ldots, w_k, v_{k +1}, \ldots, v_n$, dove i vettori aggiunti sono proprio $n - k$, che per definizione equivale a $\dim(V) - \dim(W)$
    - $\forall v \in \textrm{span}(w_1, \ldots, w_k, v_{k +1}, \ldots, v_n) \quad \exists \lambda_1, \ldots, \lambda_n \in \mathbb{K} \mid v = \lambda_1 w_1 + \ldots + \lambda_k w_k + \lambda_{k + 1} v_{k +1} + \ldots + \lambda_nv_{n} \implies \forall [v] \in V/W \quad [v] = \lambda_1 [w_1] + \ldots + \lambda_n[w_k] + \lambda_{k +1} [v_{k +1 }] + \lambda_n[v_n]$
    - per dimostrazione precedente $W = [0_V] \in V/W \implies [w_1] = \ldots = [w_k] = 0_V \implies [v] = \lambda_{k +1}[v_{k +1}] + \ldots + \lambda_n[v_n] \implies [v_{k +1}], \ldots, [v_n]$ generatori di $V/W$
    - $[v_{k +1}], \ldots, [v_n]$ generatori di $V/W$, in particolare implica che $\exists \lambda_{k +1}, \ldots, \lambda_n \in \mathbb{K} \mid W = [0_V] = \lambda_{k +1}[v_{k+ 1}] + \ldots+ \lambda_n[v_n] = [\lambda_{k +1} v_{k+1} + \ldots + \lambda_nv_n]$, e in particolare $u:=\lambda_{k + 1}v_{k + 1} + \ldots + \lambda_nv_n \in W$
    - $u \in W \implies \exists \lambda_1, \ldots, \lambda_k \in \mathbb{K} \mid u = \lambda_1 w_1 + \ldots + \lambda_k w_k \implies \lambda_1w_1+ \ldots + \lambda_kw_k = \lambda_{k +1} v_{k +1} + \ldots + \lambda_nv_n \iff \lambda_1w_1+ \ldots + \lambda_kw_k - \lambda_{k +1} v_{k +1} - \ldots - \lambda_nv_n = 0_V$
    - per osservazione precedente $w_1, \ldots, w_k, v_{k +1}, \ldots v_k$ è una base di $V$, allora $\lambda_1= \ldots= \lambda_k= -\lambda_{k +1}= \ldots= -\lambda_{n} = 0_V$, e in particolare $-\lambda_{k+1} = \ldots = -\lambda_n = 0_V \implies [v_{k +1}], \ldots, [v_n]$ linearmente indipendenti in $V/W$
    - allora $[v_{k +1}], \ldots, [v_n]$ sono una base di $V/W$ di cardinalità $n - k \implies \dim(V/W) = \dim(V)-\dim(W)$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $k \in \mathbb{N}$
    - $V_1, \ldots, V_k$ spazi vettoriali su $\mathbb{K}$
- **Th**
    - $\dim(V_1 \times \ldots \times V_k) = \dim(V_1) \cdot \ldots \cdot \dim(V_k)$

****

# Trasformazioni lineari

## Def

- **Applicazioni lineari**

> - $\mathbb{K}$ campo
> - $V, W$ spazi vettoriali su $\mathbb{K}$
> - $f: V \rightarrow W$ è detta **trasformazione lineare** $\iff$
>   - $\forall v, w \in V \quad f(v + w) = f(v) + f(w)$
>      - in particolare, deve essere _morfismo rispetto a $+$_
>   - $\forall v \in V, \lambda \in \mathbb{K} \quad f(\lambda v) = \lambda f(v)$
> - si noti che $V \cong W \iff \exists f: V \rightarrow W \mid f$ trasformazione lineare biettiva

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $V$ spazio vettoriale su $\mathbb{K}$
    - $n:= \dim(V)$
- **Th**
    - $V \cong \mathbb{K}^n$
- **Dim**
    - sia $v_1, \ldots, v_n \in V$ base di $V$
    - sia $f: \mathbb{K}^n \rightarrow V: (t_1, \ldots, t_n) \rightarrow t_1v_1 + \ldots + t_nv_n$
    - $f$ biettiva
        - $v_1, \ldots, v_n$ basi di $V$, in particolare linearmente indipendenti $\implies f$ iniettiva
        - $v_1, \ldots, v_n$ basi di $V$, in particolare generatori di $V \implies f$ suriettiva
        - allora $f$ biettiva
    - $f$ trasformazione lineare
        - $x, y \in \mathbb{K}^n \mid \left \{ \begin{array}{l} x = (x_1, \ldots, x_n) \\ y=(y_1, \ldots, y_n) \end{array} \right.$ si ha che $f(x + y) = (x_1 + y_1)v_1 + \ldots + (x_n + y_n) v_n = x_1v_1+ \ldots + x_nv_n + y_1v_1 + \ldots + y_nv_n = f(x) + f(y)$
        - $\forall x \in V, \lambda \in \mathbb{K} \quad f(\lambda x) = \lambda x_1v_1 + \ldots + \lambda x_n v_n = \lambda(x_1v_1 + \ldots + x_n v_n) = \lambda f(x)$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $V, W$ spazi vettoriali su $\mathbb{K} \mid \dim(V), \dim(W)$ finita
- **Th**
    - $V \cong W \iff \dim(V) = \dim(W)$
- **Dim**
    - _prima implicazione_
        - $V \cong W \implies \exists f : V \rightarrow W \mid f$ trasformazione lineare biettiva
        - sia $v_1, \ldots, v_n$ base di $V$
        - allora $\forall v \in V \quad \exists \lambda_1, \ldots, \lambda_n \in \mathbb{K} \mid v = \lambda_1 v_1 + \ldots + \lambda_n v_n \iff f(v) = f(\lambda_1 v_1 + \ldots + \lambda_n v_n) = f(\lambda_1v_1) + \ldots + f(\lambda_n v_n) = \lambda_1 f(v_1) + \ldots + \lambda_n f(v_n)$
        - $f$ suriettiva, allora $f(v_1), \ldots f(v_n)$ generatori di $W$, e in particolare $\exists \lambda_1, \ldots, \lambda_n \in \mathbb{K} \mid 0_W = \lambda_1f(v_1) + \ldots + \lambda_nf(v_n) = f(\lambda_1v_1 + \ldots + \lambda_nv_n)$
        - $f$ iniettiva, allora $\ker(f) = \{0_V\} \implies 0_W = f(\lambda_1v_1 + \ldots + \lambda_n v_n) \iff 0_V = \lambda_1 v_1 + \ldots + \lambda_nv_n$
        - $v_1, \ldots, v_n$ linearmente indipendenti $\implies 0_V = \lambda_1v_1 + \ldots + \lambda_nv_n \iff \lambda_1 = \ldots = \lambda_n = 0_\mathbb{K}$
        - allora si ha che $0_W = \lambda_1f(v_1) + \ldots + \lambda_nf(v_n) \iff \lambda_1 = \ldots = \lambda_n = 0_{\mathbb{K}} \implies f(v_1), \ldots, f(v_n)$ linearmente indipendenti
        - allora $f(v_1), \ldots, f(v_n)$ base di $W$, ed ha cardinalità $n$, pari alla cardinalità della base $v_1, \ldots, v_n$ di $V$, dunque per definizione $\dim(V) = \dim(W)$
    - _seconda implicazione_
        - $n:=\dim(V) = \dim(W)$
        - allora, per dimostrazione precedente si ha che $V \cong \mathbb{K}^n \land W \cong \mathbb{K}^n$
        - poiché $\cong$ è una relazione di equivalenza per dimostrazione precedente, allora si ha che $V \cong W$

## Def

- **Kernel e immagine di spazi vettoriali**

> - $\mathbb{K}$ campo
> - $V, W$ spazi vettoriali su $\mathbb{K}$
> - $f : V \rightarrow W$ trasformazione lineare
> - $\ker(f) = \{v \in V \mid f(v) = 0_W\}$ è detto **kernel/nucleo di $f$**
> - $\textrm{im}(f) = \{w \in W \mid \exists v \in V : w = f(v)\}$ è detta **immagine di $f$**

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $V, W$ spazi vettoriali su $\mathbb{K}$
    - $f : V \rightarrow W$ trasformazione lineare
- **Th**
    - $\ker(f) \subset V$ sottospazio
- **Dim**
    - $(\ker(f), +) \leqslant (V, +)$
        - $f$ morfismo rispetto a $+ \implies f(0_V) = 0_W \implies 0_V \in \ker(f)$
        - $v, w \in \ker(f) \iff f(v) = 0_W = f(w) \implies 0_W = f(v) + f(w) = f(v + w) \implies v + w \in \ker(f)$
        - $v \in \ker(f) \implies f(v) = 0_W$, e poiché $f$ morfismo rispetto a $+$ si ha che $f(-v) = -f(v) = 0_W \implies -v \in \ker(f)$
    - $\forall v \in \ker(f), \lambda \in \mathbb{K} \quad f(v) = 0_W$, e poiché $f$ trasformazione lineare $f(\lambda v) = \lambda f(v) = \lambda 0_W = 0_W \implies \lambda v \in \ker(f)$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $V, W$ spazi vettoriali su $\mathbb{K} \mid V, W$ hanno dimensione finita
    - $f : V \rightarrow W$ trasformazione lineare
- **Th**
    - $\textrm{im}(f) \subset W$ sottospazio
- **Dim**
    - $(\textrm{im}(f), +) \leqslant (V, +)$
        - $f$ morfismo rispetto a $+ \implies f(0_V) = 0_W \implies 0_W \in \textrm{im}(f)$
        - $v, w \in \textrm{im}(f) \implies \exists v', w'\in V \mid \left \{ \begin{array}{l} f(v') = v \\ f(w') = w \end{array} \right. \implies f(v' + w')= f(v') + f(w') = v + w \implies v + w \in \textrm{im}(f)$
        - $v \in \textrm{im}(f) \quad \exist v' \in V \mid f(v') = v \iff -f(v') = -v$, e poiché $f$ morfismo rispetto a $+$ si ha che $f(-v') = -f(v')=-v \implies -v \in \textrm{im}(f)$
    - $\forall v \in \textrm{im}(f), \lambda \in \mathbb{K} \quad \exists v' \in V \mid f(v') = v \iff \lambda f(v') = \lambda v$, e poiché $f$ trasformazione lineare $f(\lambda v') = \lambda f(v') = \lambda v \implies \lambda v \in \textrm{im}(f)$

## Def

- **Rango di un'applicazione lineare**

> - $\mathbb{K}$ campo
> - $V, W$ spazi vettoriali su $\mathbb{K}$
> - $f: V \rightarrow W$ applicazione lineare
> - $\textrm{rk}(f) := \dim(\textrm{im}(f))$ è detto **rango di $f$**

****

# Spazi affini

## Def

- **Spazio affine**

> - $\mathbb{K}$ campo
> - $V$ spazio vettoriale su $\mathbb{K}$
> - $+: A \times V \rightarrow A: (P, v) \rightarrow P + v$
> - $(A, +)$ è detto **spazio affine a $V$ su $\mathbb{K}$** $\iff$
>   - $\forall P \in A \quad +_P:V \rightarrow A : v \rightarrow P + v$ biettiva
>   - $\forall P \in A, v, w \in V \quad (P + v) + w = P + (v + w)$
>     - in particolare, deve valere la _proprietà associativa mista_

- **Sottospazio affine**

> - $\mathbb{K}$ campo
> - $V$ spazio vettoriale su $\mathbb{K}$
> - $W \subset V$ sottospazio vettoriale
> - $v \in V$
> - $S := v + W := \{v + w \mid w \in W\}$ è detto **sottospazio di $V$ affine a $W$**
>   - in particolare, si tratta di una classe laterale rispetto a $+$ di $W$
>   - può essere visualizzato graficamente come traslazione di $W$ di un fattore pari a $v$
>   - in particolare, questo mostra che $\dim(S) = \dim(W)$, poiché è stata applicata solamente una traslazione senza alterarne la dimensione
> - $\textrm{Giac}(S) = W$ è detta **giacitura di $S$**

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $m, n \in \mathbb{N}$
    - $A \in \textrm{Mat}_{m \times n}(\mathbb{K})$
    - $b \in \mathbb{K}^m$
    - $X := \{x \in \mathbb{K}^n \mid A x = b\} \neq \varnothing$, dunque il sistema ammette almeno una soluzione
- **Th**
    - $X$ sottospazio di $\mathbb{K}^n$ affine a $\ker(\mathscr{L}_A)$
    - $\dim(X) = n - \textrm{rk}(A)$
- **Dim**
    - $\ker(\mathscr{L}_A) := \{x \in \mathbb{K}^n \mid Ax = 0\} \subset \mathbb{K}^n$ sottospazio per dimostrazione precedente
    - sia $x_0 \in X$, che esiste poiché $X \neq \varnothing$ in ipotesi
    - allora $x_0 + \ker(\mathscr{L}_A) := \{x_0 + x \mid x \in \ker(\mathscr{L}_A)\}$ sottospazio di $\mathbb{K}^n$ affine a $\ker(\mathscr{L}_A)$, dove $\textrm{Giac}(x_0 + \ker(\mathscr{L}_A)) = \ker(\mathscr{L}_A)$
    - $\forall x \in X \quad Ax = b = Ax_0 \iff A(x - x_0) = 0 \iff x - x_0 \in \ker(\mathscr{L}_A) \iff x \in x_0 + \ker(\mathscr{L}_A)$, di conseguenza le soluzioni in $X$ generano un sottospazio di $\mathbb{K}^n$ affine a $\ker(\mathscr{L}_A)$
    - allora, per il teorema del rango $\dim(X) = \dim(x_0 + \ker(f)) = \dim(\textrm{Giac}(x_0 + \ker(f))) = \dim(\ker(\mathscr{L}_A)) = n - \textrm{rk}(\mathscr{L}_A) = n - \textrm{rk}(A)$

****

# Interpretazione geometrica dei vettori

## Def

- **Prodotto scalare**

> - $n \in \mathbb{N}$
> - $\mathbb{K}$ campo
> - $u, v \in \mathbb{K}^n \mid u = \left(\begin{array}{c}x_1 \\ \vdots \\ x_n \end{array}\right), v = \left(\begin{array}{c}y_1 \\ \vdots \\ y_n \end{array}\right)$
> - $u \cdot v := \displaystyle \sum_{i = 1}^n{x_i \cdot y_i}$ è detto **prodotto scalare tra $u$ e $v$**

- **Spazio di Hilbert**

> - $\mathbb{K}$ campo
> - $V$ spazio vettoriale su $\mathbb{K}$
> - $V$ è detto **spazio di Hilbert** $\iff$ in $V$ è ben definito il prodotto scalare

- **Base ortogonale di uno spazio di Hilbert**

> - $n \in \mathbb{N}$
> - $\mathbb{K}$ campo
> - $V$ spazio di Hilbert su $\mathbb{K}$
> - $v_1, \ldots, v_n$ base di $V$
> - $v_1, \ldots, v_n$ è detta **base ortogonale di $V$** $\iff \forall i, j \in [1, n], i \neq j \quad v_i \cdot v_j = 0$

- **Base ortonormale di uno spazio di Hilbert**

> - $n \in \mathbb{N}$
> - $\mathbb{K}$ campo
> - $V$ spazio di Hilbert su $\mathbb{K}$
> - $v_1, \ldots, v_n$ base ortogonale di $V$
> - $v_1, \ldots, v_n$ è detta **base ortonormale** di $V \iff \forall i, j \in [1, n] \quad v_i \cdot v_j = \left\{\begin{array}{cc} 1 & i = j \\ 0 & i \neq j \end{array}\right.$
>   - di fatto, una base ortonormale è una base ortogonale normalizzata
>   - in particolare, è possibile ottenere $v_1, \ldots, v_n$ a partire da $e_1, \ldots, e_n$ tramite rotazioni e riflessioni

## Oss

- **Hp**
    - $n \in \mathbb{N}$
    - $u, v \in \mathbb{K}^n$
- **Th**
    - $u \cdot v = v \cdot u$
    - $\forall \lambda \in \mathbb{K} \quad u \cdot (\lambda v) = \lambda(u \cdot v) = (\lambda u) \cdot v$
    - $\forall w \in \mathbb{K}^n \quad w \cdot (u + v) = w \cdot u + w \cdot v$
    - $\forall w \in \mathbb{K}^n \quad (u + v) \cdot w = u \cdot w + v \cdot w$

## Def

- **Norma di un vettore**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N}$
> - $u \in \mathbb{K}^n \mid u = \left(\begin{array}{c}x_1 \\ \vdots \\ x_n \end{array}\right)$
> - $||u|| := \sqrt{x_1^2 + \ldots + x_n^2}$ è detta **norma di $u$**
>   - graficamente, corrisponde alla lunghezza del vettore $u$ nel piano cartesiano

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N}$
    - $u \in \mathbb{K}^n \mid u = \left(\begin{array}{c}x_1 \\ \vdots \\ x_n \end{array}\right)$
- **Th**
    - $||u|| = \sqrt{u \cdot u}$
- **Dim**
    - $||u|| = \sqrt{x_1^2 + \ldots + x_n^2} = \displaystyle \sqrt{\sum_{i= 1}^n{x_i^2}}=\sqrt{u\cdot u}$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N}$
    - $v \in \mathbb{K}^n$
    - $v_1, \ldots, v_n$ base ortonormale di $\mathbb{K}^n$
- **Th**
    - $v = (v \cdot v_1)v_1 + \ldots + (v \cdot v_n)v_n$

## Def

- **Sottospazio ortogonale**

> - $\mathbb{K}$ campo
> - $n \in \mathbb{N}$
> - $V \subset \mathbb{K}^n$ sottospazio vettoriale
> - $V^{\perp} := \{w \in \mathbb{K}^n \mid \forall v \in V \quad w \cdot v = 0_{\mathbb{K}^n}\}$ è detto **sottospazio di $\mathbb{K}^n$ ortogonale a $V$**
>     - la definizione ha significato poiché il prodotto scalare tra due vettori è nullo esattamente quando i due vettori sono perpendicolari tra loro

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N}$
    - $V \subset \mathbb{K}^n$ sottospazio vettoriale
- **Th**
    - $V^{\bot} \subset \mathbb{K}^n$ sottospazio vettoriale
- **Dim**
    - $(V^{\bot}, +) \leqslant (\mathbb{K}^n, +)$
        - $\forall v \in V \quad 0 \cdot v = 0 \implies 0 \in V^{\bot}$
        - $w_1, w_2 \in V^{\bot} \implies \forall v \in V \quad \left \{ \begin{array}{l} w_1 \cdot v = 0 \\ w_2 \cdot v = 0 \end{array} \right. \implies w_1 \cdot v + w_2 \cdot v = 0 \iff (w_1 + w_2) \cdot v = 0 \implies w_1 + w_2 \in V^{\bot}$
        - $w \in V^{\bot} \implies \forall v \in V \quad w \cdot v = 0 \iff - (w \cdot v) = 0 \iff (-w) \cdot v = 0 \implies -w \in V^{\bot}$
    - $w \in V^{\bot} \implies \forall v \in V \quad w \cdot v = 0 \iff \forall k \in \mathbb{K} \quad k(w \cdot v) = 0 \iff (kw) \cdot v = 0 \implies kw \in V^{\bot}$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $n \in \mathbb{N}$
    - $V \subset \mathbb{K}^n$ sottospazio vettoriale
- **Th**
    - $\dim(V^{\bot}) + \dim(V) = \dim(\mathbb{K}^n)$

