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
