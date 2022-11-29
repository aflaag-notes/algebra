# Spazi Vettoriali

## Def 

- **Spazio vettoriale**

> - $\mathbb{K}$ campo
> - $x \in \mathbb{K}$ è detto **scalare**
> - $V$ è **spazio vettoriale su $\mathbb{K}$** $\iff (V, +)$ gruppo abeliano, è ben definita un'operazione di $\cdot: K \times V \rightarrow V$ che ammetta elemento neutro, inoltre $\forall s, t \in \mathbb{K}, v \in V \quad s\cdot (t \cdot v) = (s \cdot t) \cdot v, (s + t) \cdot v = s\cdot v + t \cdot v$ e infine $\forall s \in \mathbb{K}, v, w \in V \quad s \cdot (v + w) = s \cdot v + s \cdot w$
> - $x \in V$ è detto **vettore**

## Ex

- **Hp**
    - $n \in \mathbb{N}$
    - $\mathbb{K}$ campo
- **Th**
    - $\mathbb{K}^n$ spazio vettoriale su $\mathbb{K}$
- **Dim**
    - è possibile definire operazioni $+$ e $\cdot$ tra scalari e vettori che verificano gli assiomi per spazi vettoriali
    - $\forall v \in \mathbb{K}^n \quad \exists t_1, \ldots, t_n \in \mathbb{K}^n \mid v = (t_1, \ldots, t_n)$ per definizione
    - $\forall w \in \mathbb{K}^n \quad \exists s_1, \ldots, s_n \in \mathbb{K}^n \mid v = (s_1, \ldots, s_n)$ per definizione
    - $\forall \lambda \in \mathbb{K} \quad \lambda \cdot v := (\lambda \cdot t_1, \ldots, \lambda \cdot t_n)$
    - $v + w := (s_1 + t_1, \ldots, s_n + t_n)$
    - con queste definizioni, segue che gli assiomi per gli spazi vettoriali sono necessariamente rispettati

## Def

- **Sottospazio vettoriale**

> - $\mathbb{K}$ campo
> - $V$ spazio vettoriale su $\mathbb{K}$
> - $W$ è **sottospazio vettoriale di $V$** $\iff (W, +) \subset (V, +)$ sottogruppo, e $\forall w \in W, \lambda \in \mathbb{K} \quad \lambda \cdot w \in W$

## Def

- **Span di vettori**

> - $n \in \mathbb{N}$
> - $\mathbb{K}$ campo
> - $V$ spazio vettoriale su $\mathbb{K}$
> - $v_1, \ldots, v_n \in V$
> - $\textrm{span}(v_1, \ldots, v_n) := \{\lambda_1 v_1 + \ldots + \lambda_n v_n \mid \lambda_1, \ldots , \lambda_n \in \mathbb{K}\}$, ovvero l'insieme delle combinazioni lineari degli $v_1, \ldots, v_n$


## Oss

- **Hp**
    - $n \in \mathbb{N}$
    - $\mathbb{K}$ campo
    - $V$ spazio vettoriale su $\mathbb{K}$
    - $v_1, \ldots, v_n \in V$
- **Th**
    - $\textrm{span}(v_1, \ldots, v_n)$ è un sottospazio vettoriale di $V$
- **Dim**
    - **⚠️ APPUNTO SU $0$ bla bla bla**
    - $(\textrm{span}(v_1, \ldots, v_n), +) \subset (V, +)$ sottogruppo
        - $0_V = 0v_1 + \ldots + 0v_n \implies 0 \in \textrm{span}(v_1, \ldots, v_n)$
        - $\forall u, v \in \textrm{span}(v_1, \ldots, v_n) \quad \exists \lambda_1, \ldots , \lambda_n, \mu_1 \ldots \mu_n \in \mathbb{K} \mid u= \lambda_1v_1 + \ldots + \lambda_n v_n \land w = \mu_1 v_1+ \ldots + \mu_1v_1 \implies v + w = (\lambda_1 \mu_1) v_1 + \ldots + (\lambda_n \mu_n) v_n \implies v + w \in \textrm{span}(v_1, \ldots, v_n)$
        - $\forall u \in \textrm{span}(v_1, \ldots, v_n) \quad \exists \lambda_1 , \ldots \lambda_n \in \mathbb{K} \mid u = \lambda_1 v_1 + \ldots + \lambda_n v_n \iff - u = (-\lambda _1) v_1 + \ldots + (- \lambda_n) v_n \implies -u \in \textrm{span}(v_1, \ldots, v_n)$
    - $\forall w \in \textrm{span}(v_1, \ldots, v_n) \quad \exists \lambda_1 , \ldots , \lambda_n \in \mathbb{K} \mid w = \lambda_1 v_1 + \ldots + \lambda_n v_n \implies \forall c \in \mathbb{K} \quad c\cdot w = c \cdot (\lambda_1v_1 + \ldots + \lambda_n v_n) =(c\lambda_1) v_1 + \ldots + (c\lambda_n) v_n \implies c\cdot w \in \textrm{span}(v_1, \ldots, v_n)$

## Def

- **Vettori generatori**

> - $n \in \mathbb{N}$
> - $\mathbb{K}$ campo
> - $V$ spazio vettoriale su $\mathbb{K}$
> - $v_1, \ldots, v_n \in V$
> - $v_1, \ldots, v_n$ sono **generatori di $V$** $\iff \textrm{span}(v_1, \ldots, v_n) = V$
>     - equivalentemente, ogni altro vettore in $V$ è una combinazione lineare degli $v_1, \ldots, v_n$

- **Indipendenza lineare**

> - $n \in \mathbb{N}$
> - $\mathbb{K}$ campo
> - $V$ spazio vettoriale su $\mathbb{K}$
> - $v_1, \ldots, v_n \in V$
> - $v_1, \ldots, v_n$ sono **linearmente indipendenti** se e solo se $\lambda_1 v_1 + \ldots + \lambda_n v_n = 0_V \iff \lambda_1 = \ldots = \lambda_n = 0_{\mathbb{K}}$
>    - equivalentemente, nessuno degli $v_1, \ldots, v_n$ è combinazione lineare degli altri

- **Base di uno spazio vettoriale**

> - $n \in \mathbb{N}$
> - $\mathbb{K}$ campo
> - $V$ spazio vettoriale su $\mathbb{K}$
> - $v_1, \ldots, v_n \in V$
> - $v_1, \ldots, v_n$ sono una **base di $V$** $\iff$ $v_1, \ldots, v_n$ sono generatori di $V$ e linearmente indipendenti
> - $n$ è detta **cardinalità della base di $V$**

## Ex

- **Hp**
    - $n \in \mathbb{N}$
    - $\mathbb{K}$ campo
    - $e_1 := (1, 0, \ldots, 0), \ldots, e_n :=(0, \ldots, 0, 1) \in \mathbb{K}^n$
- **Th**
    - $e_1, \ldots, e_n$ sono una base di $\mathbb{K}^n$, ed è detta _base canonica_
- **Dim**
    - $e_1, \ldots, e_n$ sono generatori di $\mathbb{K}^n$
        - $\forall v \in \mathbb{K}^n \quad \exists t_1, \ldots, t_n \in \mathbb{K} \mid v = (t_1, \ldots, t_n) \implies v = (t_1, 0, \ldots, 0) + \ldots + (0, \ldots, 0, t_n) = t_1 \cdot e_1 + \ldots + t_n \cdot e_n \implies v \in \textrm{span}(e_1, \ldots, e_n)$
    - $e_1, \ldots, e_n$ sono linearmente indipententi
        - $\forall \lambda_1, \ldots, \lambda_n \in \mathbb{K} \quad \lambda_1e_1=(\lambda_1, 0, \ldots, 0), \ldots, \lambda_n e_n = (0, \ldots, 0, \lambda_n) \implies \lambda_1 e_1 + \ldots + \lambda_n e_n = (\lambda_1, \ldots , \lambda_n)$, e questo vettore è pari al vettore nullo $0_{\mathbb{K}^n}$ solamente quando $\lambda _1 = \ldots = \lambda_n = 0_{\mathbb{K}}$
        - $\forall v_1, \ldots, v_n \in \mathbb{K}^n \quad \lambda _1 = \ldots = \lambda_n = 0_{\mathbb{K}} \implies \lambda_1v_1 + \ldots + \lambda_nv_n = 0_{\mathbb{K}^n}$, e in particolare questa osservazione vale per $e_1, \ldots, e_n$

## Lem

- **Hp**
    - $n \in \mathbb{N}$
    - $\mathbb{K}$ campo
    - $V$ spazio vettoriale su $\mathbb{K}$
    - $v_1, \ldots, v_n \in V$
- **Th**
    - $v_1, \ldots, v_n$ linearmente indipendenti $\iff v_1, \ldots, v_{n - 1}$ linearmente indipendenti $\land v_n \notin \textrm{span}(v_1, \ldots, v_{n - 1})$
- **Dim**
    - _prima implicazione_
        - è stata omessa dal professore, se stai leggendo questa frase sappi che hai dei bei piedi
    - _seconda implicazione_
        - ⚠️ **MANCA LA DIMOSTRAZIONE**

## Oss

- **Hp**
    - $m, k \in \mathbb{N}$
    - $\mathbb{K}$ campo
    - $V$ spazio vettoriale su $\mathbb{K}$
    - $w_1, \ldots, w_m \in V$
    - $v_1, \ldots, v_k \in \textrm{span}(w_1, \ldots, w_m) \mid v_1, \ldots, v_k$ linearmente indipendenti
- **Th**
    - $k \le m$
- **Dim**
    - ⚠️ **MANCA LA DIMOSTRAZIONE, È NOIOSISSIMA TE GIURO**

## Cor

- **Hp**
    - $n, m \in \mathbb{N}$
    - $\mathbb{K}$ campo
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
    - dunque $n \le m \land m \le n \implies n = m$

## Def

- **Dimensione di uno spazio vettoriale**

> - $\mathbb{K}$ campo
> - $V$ spazio vettoriale su $\mathbb{K}$
> - $\dim(V)$ è detta **dimensione di $V$**, ed è la cardinalità delle basi di $V$

## Oss

- **Hp**
    - $n \in \mathbb{N}$
    - $\mathbb{K}$ campo
    - $V$ spazio vettoriale su $\mathbb{K}$
    - $v_1, \ldots, v_n \in V$
- **Th**
    - $v_1, \ldots, v_n$ base di $V \iff \forall v \in V \quad \exists ! \lambda_1, \ldots, \lambda_n \in \mathbb{K} \mid v = \lambda_1 v_1 + \ldots + \lambda_n v_n$
- **Dim**
    - ⚠️ **TODO**
    - _prima implicazione_
    - _seconda implicazione_

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $W$ spazio vettoriale su $\mathbb{K}$
    - $n:= \dim(W)$
    - $k \in \mathbb{N} \mid k \lt n$
    - $w_1, \ldots, w_k \in W$ linearmente indipendenti
- **Th**
    - $\exists w_{k + 1}, \ldots, w_n \in W \mid w_1, \ldots, w_n$ è una base di $W$
- **Dim**
    - $k \lt n \implies \textrm{span}(w_1, \ldots, w_k) \subsetneqq W \implies \exists w_{k + 1} \in W \mid w_{k + 1} \notin \textrm{span}(w_1, \ldots, w_k)$, allora per dimostrazione precedente $w_1, \ldots, w_{k +1}$ sono linearmente indipendenti
    - per ragionamento analogo, è possibile estendere $w_1, \ldots, w_{k + 1}$ fino ad avere $w_1, \ldots, w_n$ vettori linearmente indipendenti

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $W$ spazio vettoriale su $\mathbb{K}$
    - $n := \dim(W)$
    - $m \in \mathbb{N} \mid m \ge n$
    - $w_1, \ldots, w_m \in W \mid w_1, \ldots, w_m$ generatori di $W$
- **Th**
    - $\exists 1 \le i_1, \ldots, i_n \le m \mid w_{i_1}, \ldots, w_{i_n}$ è una base di $W$
- **Dim**
    - è possibile assumere che $w_{i_1}$ non sia nullo, poiché $w_1, \ldots, w_m$ sono sicuramente non tutti nulli in quanto generatori di $W$
    - $w_{i_1} \neq 0 \implies w_{i_1}$ linearmente indipendente, ma non può costituire un generatore poiché sono meno di $n$ vettori $\implies \textrm{span}(w_{i_1}) \subsetneqq W \implies \exists w_{i_2} \in W \mid w_{i_2} \notin \textrm{span}(w_{i_1})$, allora per dimostrazione precedente $w_{i_1}, w_{i_2}$ sono linearmente indipendenti
    - è possiible ripetere il ragionamento fino ad ottenere esattamente $n$ vettori, ottenendo $w_{i_1}, \ldots, w_{i_n}$ vettori linearmente indipendenti

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
        - per assurdo, siano $w_1, \ldots, w_n$ linearmente indipendenti ma non generatori di $W \implies \textrm{span}(w_1, \ldots, w_n) \subsetneqq W \implies \exists w_{n + 1} \in W \mid w_{n + 1} \notin \textrm{span}(w_1, \ldots, w_n)$, ma per dimostrazione precedente $w_1, \ldots, w_{n + 1}$ linearmente indipendenti $\bot$
    - _seconda implicazione_
        - per assurdo, siano $w_1, \ldots, w_n$ generatori di $W$ ma non linearmente indipendenti $\implies \exists \lambda_1, \ldots, \lambda_n \mid \lambda_1w_1 + \ldots + \lambda_nw_n = 0_W$ dove $\exists i \in [1, n] \mid \lambda_i \neq 0 \implies w_i = -\lambda_i^{-1} \lambda_1w_1 - \ldots - \lambda_i^{-1} \lambda_nw_n$, dunque $w_i$ è combinazione lineare degli altri vettori, in simboli $w_i \in \textrm{span}(w_1, \ldots, \hat{w_i}, \ldots, w_n) \implies \textrm{span}(w_1, \ldots, w_n) \subseteq \textrm{span}(w_1, \ldots, \hat{w_i}, \ldots, w_n)$
        - per qualsiasi insieme di vettori minore di $n$ si ha che $\textrm{span}(w_1, \ldots, \hat{w_i}, \ldots, w_n) \subseteq \textrm{span}(w_1, \ldots, w_n)$
        - allora segue che $\textrm{span}(w_1, \ldots, \hat{w_i}, \ldots, w_n) = \textrm{span}(w_1, \ldots, w_n)$, ma questo non è possibile in queanto $w_1, \ldots, \hat{w_i}, \ldots, w_n$ sono $n - 1$ generatori, e i generatori non possono essere meno di $n \ \bot$

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
    - $w_1, \ldots, w_k \in U \cap V$ base di $U \cap V$
    - $B_1 := w_1, \ldots, w_k, u_{k + 1}, \ldots, u_m \in U$ base di $U$
    - $B_2 := w_1, \ldots, w_k, v_{k + 1}, \ldots, v_n \in V$ base di $V$
    - $B_1 \cup B_2 := w_1, \ldots w_k, u_{k + 1}, \ldots, u_m, v_{k + 1}, \ldots, v_n$
    - $\forall u \in U, v \in V \mid u := \displaystyle \sum_{i = 1}^k{\lambda_iw_i} + \sum_{j = k + 1}^m{\lambda_j u_j} \land \displaystyle v :=\sum_{i = 1}^k{\mu_iw_i} + \sum_{h = k + 1}^n {\mu_hv_h} \quad u + v =\sum_{i = 1}^k{(\lambda_i + \mu_i)w_i} + \sum_{j = k + 1}^m{\lambda_j u_j} + \sum_{h = k + 1}^n {\mu_hv_h} \implies u + v \in \textrm{span}(w_1, \ldots w_k, u_{k + 1}, \ldots, u_m, v_{k + 1}, \ldots, v_n) \implies B_1 \cup B_2$ generatori di $U + V$, poiché $u + v \in U + V$
    - $a := \displaystyle \sum_{i = 1}^k{\lambda_iw_i}$
    - $b := \displaystyle \sum_{j = k +1}^m{\mu_j u_j } \implies b \in \textrm{span}(u_{k +1 }, \ldots, u_k) \subsetneqq U \implies b \in U$
    - $c := \displaystyle \sum_{h = k + 1} ^n{\eta_hv_h}$
    - siano i coefficienti tali che $a + b + c= 0_W \iff b = - a - c$
    - $b \in U$ per osservazione precedente, mentre $a + c = v \in V \implies -(a + c) \in V \implies - a- c \in V$, e dunque $b \in U \cap V$
    - allora, $b$ deve essere generato dalla base $w_1, \ldots, w_k$ di $U \cap V \implies \displaystyle \exists \alpha_1, \ldots, \alpha_k \in \mathbb{K} \mid \sum_{j = k +1}^m{\mu_j u_j }=:b = \displaystyle \sum_{i = 1}^k {\alpha_i w_i} \implies \sum_{j = k +1}^m{\mu_j u_j } - \displaystyle \sum_{i = 1}^k {\alpha_i w_i} = 0_W$
    - poiché per ipotesi $w_i, \ldots, w_k, u_{k +1}, \ldots, u_m$ è una base di $U$, in $U$ tali vettori sono linearmente indipendenti, dunque segue che ogni $\alpha_i$ e $\mu_j$ deve essere necessariamente $0_{\mathbb{K}}$
    - in particolare, si ottiene che $\forall j \in [k +1, m] \quad \mu_j =0 \implies b = 0_W \implies a + c = 0_W$
    - per ragionamento analogo, sapendo che $c = - a- b$ si otterrà che $c = 0_W$, e dunque $a + b + c = 0_W \iff a = 0_W$
    - per definizione $a$ è combinazione lineare della base di $U \cap V$, e poichè $a = 0_W$ si ha necessariamente che i coefficienti di $a$ sono tutti nulli
    - dunque, l'equazione di partenza $a + b + c = 0_W$ è verificata solamente per coefficienti di $a$, $b$ e $c$ nulli, il che implica che i vettori che generano $a + b + c$ sono linearmente indipendenti
    - $B_1 \cup B_2$ generatori di $U + V \implies a + b + c \in U + V$, e poiché $w_1, \ldots, w_k, u_{k + 1}, \ldots, u_m, v_{k + 1}, \ldots, v_n$ sono sia generatori che linearmente indipendenti, allora sono una base di $U + V$
    - per definizione, la dimensione di uno spazio vettoriale è la cardinalità di una delle sue basi, e dunque la cardinalità di $B_1 \cup B_2$ è pari a $k + (m - k) + (n - k) = k + m - k + n - k = m + n - k$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $V$ spazio vettoriale su $\mathbb{K}$
    - $W \subset V$ sottospazio vettoriale
- **Th**
    - $V/W$ sottospazio vettoriale
- **Dim**
    - ⚠️ **TODO**

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
    - $\dim(V) \gt k$
        - per dimostrazione precedente $w_1, \ldots, w_k$ non è base di $V$, e in particolare non generano $V \implies \textrm{span}(w_1, \ldots, w_k) \subsetneqq V \implies \exists v_{k + 1} \in V \mid v_{k + 1} \notin \textrm{span}(w_1, \ldots, w_k)$
        - per dimostrazione precedente $w_1, \ldots w_k$ linearmente indipendenti e $v_{k + 1} \notin \textrm{span}(w_1, \ldots, w_k) \implies w_1, \ldots, w_k, v_{k + 1}$ linearmente indipendenti
    - $\dim(V) \gt k + 1$
        - per ragionamento analogo si otterrà che $w_1, \ldots, w_k, v_{k +1}, v_{k +2}$ linearmente indipendenti
    - dunque, è possibile estendere la base di $W$ scelta, fino ad ottenere una base di $V$ della forma $w_1, \ldots, w_k, v_{k +1}, \ldots, v_n$, dove i vettori aggiunti sono proprio $n - k$, che per definizione equivale a $\dim(V) - \dim(W)$
    - $\forall v \in \textrm{span}(w_1, \ldots, w_k, v_{k +1}, \ldots, v_n) \quad \exists \lambda_1, \ldots, \lambda_n \mid v = \lambda_1 w_1 + \ldots + \lambda_k w_k + \lambda_{k + 1} v_{k +1} + \ldots + \lambda_nv_{n} \implies [v] = \lambda_1 [w_1] + \ldots + \lambda_n[w_k] + \lambda_{k +1} [v_{k +1 }] + \lambda_n[v_n]$ in $V / W$
    - per dimostrazione precedente $W = [0_V] \in V/W \implies [v] = \lambda_{k +1}[v_{k +1}] + \ldots + \lambda_n[v_n] \implies [v_{k +1}], \ldots, [v_n]$ generatori di $V/W$
    - $[v_{k +1}], \ldots, [v_n]$ generatori di $V/W \implies \forall [v] \in V/W \quad \exists \lambda_{k +1}, \ldots, \lambda_n \mid [v] = \lambda_{k +1} [v_1] + \ldots + \lambda_n[v_n]$, allora in particolare $\exists \lambda_{k +1}, \ldots, \lambda_n \mid [0_V] = \lambda_{k +1}[v_{k+ 1}] + \ldots+ \lambda_n[v_n] = [\lambda_{k +1} v_{k+1} + \ldots + \lambda_nv_n]$
    - per osservazione precedente $W = [0_V] \in V/W, e in particolare $[0_V] \subseteq W \implies \forall v \in [0_V] \quad v \in W$, allora si ha che $[0_V] = [\lambda_{k +1} v_{k+1} + \ldots + \lambda_nv_n] \implies \lambda_{k +1}v_{k +1} + \ldots + \lambda_nv_n \in W$
    - $u:=\lambda_{k +1}v_{k +1} +\ldots + \lambda_nv_n \in W$
    - $u \in W \implies \exists \lambda_1, \ldots, \lambda_k \mid u = \lambda_1 w_1 + \ldots + \lambda_k w_k \implies \lambda_1w_1+ \ldots + \lambda_kw_k = \lambda_{k +1} v_{k +1} + \ldots + \lambda_nv_n \iff \lambda_1w_1+ \ldots + \lambda_kw_k - \lambda_{k +1} v_{k +1} - \ldots - \lambda_nv_n = 0_V$
    - per osservazione precedente $w_1, \ldots, w_k, v_{k +1}, \ldots v_k$ è una base di $V$, allora $\lambda_1= \ldots= \lambda_k= -\lambda_{k +1}= \ldots= -\lambda_{n} = 0_V$, e in particolare $-\lambda{k+1} = \ldots = -\lambda_n = 0_V \implies v_{k +1}, \ldots, v_n$ sono linearmente indipendenti, e dunque $[v_{k +1}], \ldots, [v_n] linearmente indipendenti$
    - allora $[v_{k +1}], \ldots, [v_n]$ sono una base di $V/W$ di cardinalità $n - k$, il che dimostra che $\dim(V/W) = \dim(V)-\dim(W)$

****

# Applicazioni lineari

## Def

- **Applicazioni lineari**

> - $\mathbb{K}$ campo
> - $V$ e $W$ spazi vettoriali su $\mathbb{K}$
> - $f: V \rightarrow W$ **morfismo di spazi vettoriali** $\iff \forall x, y \in V \quad f(x + y) = f(x) + f(y)$ e $\forall v \in V, \lambda \in \mathbb{K} \quad f(\lambda k) = \lambda f(v)$
>     - un morfismo su spazi vettoriali è detto anche **applicazione lineare** o **trasformazione lineare**

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $V$ spazio vettoriale su $\mathbb{K}$
    - $n:= \dim(V)$
- **Th**
    - $V \cong \mathbb{K}^n$
- **Dim**
    - sia $v_1, \ldots, v_n \in V$ una base di $V$
        - ⚠️ **MANCA LA DIMOSTRAZIONE PER CUI ALMENO UNA BASE ESISTE SEMPRE**
    - per dimostrare la tesi è necessario dimostrare che $f: \mathbb{K}^n \rightarrow V: (t_1, \ldots, t_n) \rightarrow t_1v_1 + \ldots + t_nv_n$ è un isomorfismo
    - $f$ morfismo
        - $\forall \lambda \in\mathbb{K}, x, y \in \mathbb{K}^n \mid x = (x_1, \ldots, x_n) \land y=(y_1, \ldots, y_n)$ si ha che $f(x + y) = (x_1 + y_1)v_1 + \ldots + (x_n + y_n) v_n = (x_1v_1+ \ldots + x_nv_n) + (y_1v_1 + \ldots + y_nv_n) = f(x) + f(y)$, dunque è verificata la prima condizione, e inoltre $f(\lambda x) = \lambda x_1v_1 + \ldots + \lambda x_n v_n = \lambda(x_1v_1 + \ldots + x_n v_n) = \lambda f(x)$, dunque è verificata anche la seconda
    - $f$ biiettiva
        - ⚠️ **MANCA LA DIMOSTRAZIONE**

## Oss

- ⚠️ **QUI C'È UN BUCO DI COSE CHE NON HO CAPITO**

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $V, W$ spazi vettoriali su $\mathbb{K}$
- **Th**
    - $V \cong W \iff \dim(V) = \dim(W)$
- **Dim**
    - _prima implicazione_
        - $V \cong W \implies \exists f : V \rightarrow W \mid f$ isomorfismo
        - sia $v_1, \ldots, v_n$ una base di $V$
        - $f$ isomorfismo, in particolare $f$ biiettiva, e in particolare $f$ suriettiva ed iniettiva
        - $f$ suriettiva $\iff \forall w \in W \quad \exists v \in V \mid w = f(v)$
        - $v_1, \ldots, v_n$ base di $V$, e in particolare generatori di $W \implies \forall v \in V \quad \exists \lambda_1, \ldots, \lambda_n \mid v = \lambda_1 v_1 + \ldots + \lambda_n v_n \iff f(v) = f(\lambda_1 v_1 + \ldots + \lambda_n v_n) = f(\lambda_1v_1) + \ldots + f(\lambda_n v_n) = \lambda_1 f(v_1) + \ldots + \lambda_n f(v_n)$ perché $f$ morfismo
        - $v \in V \implies f(w) \in W$, e inoltre $f(v) = \lambda_1f(v_1) + \ldots + \lambda_nf(v_n) \implies f(v_1), \ldots f(v_n)$ generatori di $W$
        - per osservazione precedente $f(v_1), \ldots, f(v_n)$ generatori di $W \implies \forall w \in W \quad \exists \lambda_1, \ldots, \lambda_n \mid w = \lambda_1f(v_1) + \ldots + \lambda_nf(v_n)$, e in particolare $\exists \lambda_1, \ldots, \lambda_n \mid 0_W = \lambda_1f(v_1) + \ldots + \lambda_nf(v_n) = f(\lambda_1v_1 + \ldots + \lambda_nv_n)$
        - $f$ iniettiva, allora $0_W = f(\lambda_1v_1 + \ldots + \lambda_n v_n) \implies 0_V = \lambda_1 v_1 + \ldots + \lambda_nv_n$
        - $v_1, \ldots, v_n$ linearmente indipendenti di $W \implies 0_V = \lambda_1v_1 + \ldots + \lambda_nv_n \iff \lambda_1 = \ldots = \lambda_n = 0_V$
        - allora $\exists \lambda_1, \ldots, \lambda_n \mid 0_W = \lambda_1 f(v_1) + \ldots + \lambda_nf(v_n) \implies \lambda_1 = \ldots = \lambda_n = 0_V$ corrisponde alla definizione di indipendenza lineare degli $f(v_1), \ldots, f(v_n)$
        - allora $f(v_1), \ldots, f(v_n)$ base di $W$, ed ha cardinalità $n$, pari alla cardinalità della base $v_1, \ldots, v_n$ di $V$, dunque per definizione $\dim(V) = \dim(W)$
    - _seconda implicazione_
        - $n:=\dim(V) = \dim(W)$
        - allora, per dimostrazione precedente si ha che $V \cong \mathbb{K}^n \land W \cong \mathbb{K}^n$
        - poiché $\cong$ è una relazione di equivalenza, allora si ha che $V \cong W$

## Def

- **Kernel e immagine**

> - $\mathbb{K}$ campo
> - $V, W$ spazi vettoriali su $\mathbb{K}$
> - $f : V \rightarrow W$ trasformazione lineare
> - $\ker(f) = \{v \in V \mid f(v) = 0_W\}$
> - $\textrm{im}(f) = \{w \in W \mid \exists v \in V : w = f(v)\}$

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $V, W$ spazi vettoriali su $\mathbb{K}$
    - $f : V \rightarrow W$ trasformazione lineare
- **Th**
    - $\ker(f) \subset V$ sottospazio
- **Dim**
    - ⚠️ **TODO**

## Oss

- **Hp**
    - $\mathbb{K}$ campo
    - $V, W$ spazi vettoriali su $\mathbb{K}$
    - $f : V \rightarrow W$ trasformazione lineare
- **Th**
    - $\textrm{im}(f) \subset W$ sottospazio
- **Dim**
    - ⚠️ **TODO**
