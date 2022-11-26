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
        - è stata omessa dal professore, se stai leggendo questa frase sappi che hai bei piedi
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
    - ⚠️ **INCOMPLETA**
    - _prima implicazione_
    - _seconda implicazione_

****

# Morfismi

## Def

- **Morfisimi di spazi vettoriali**
> - $\mathbb{K}$ campo
> - $V$ e $W$ spazi vettoriali su $\mathbb{K}$
> - $f: V \rightarrow W$ **morfismo di spazi vettoriali** $\iff \forall x, y \in V \quad f(x + y) = f(x) + f(y)$ e $\forall v \in V, \lambda \in \mathbb{K} \quad f(\lambda k) = \lambda f(v)$

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

- ⚠️ **QUI C'È UN BUCONE**

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
    - $w_{i_1} \neq 0 \implies w_{i_1}$ linearmente indipendente, ma non può costituire un generatore poiché sono meno di $n$ vettori $\implies \textrm{span}(w_{i_1}) \subsetneqq W \implies \exists w_{i_2} \notin \textrm{span}(w_{i_1})$, allora per dimostrazione precedente $w_{i_1}, w_{i_2}$ sono linearmente indipendenti
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
        - per assurdo, siano $w_1, \ldots, w_n$ linearmente indipendenti ma non generatori di $W \implies \textrm{span}(w_1, \ldots, w_n) \subsetneqq W \implies \exists w_{n + 1} \notin \textrm{span}(w_1, \ldots, w_n)$, ma per dimostrazione precedente $w_1, \ldots, w_{n + 1}$ linearmente indipendenti $\bot$
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
    - ⚠️ **INCOMPLETA**
