# Altro

## Alg

- ⚠️ **algoritmo di euclide todo**

## Def

- **RSA**

> - L'RSA è un algoritmo di crittografia asimmetrica che permette il trasferimento di messaggi, in sicurezza, senza l'utilizzo di un canale sicuro per scambio di chiavi, poiché vengono utilizzati chiavi pubbliche e private, dove le chiavi pubbliche servono solamente a crittare, mentre le chiavi private servono solamente a decrittare
> - $A, B$ interlocutori
> - $m$ messaggio che $B$ vuole mandare a $A$
> - $\texttt{pub}_A, \texttt{priv}_A$ chiavi rispettivamente pubblica e privata di $A$
> - allora $B$ manda ad $A$ la versione crittata di $m$ tramite la chiave pubblica di $A$, ovvero $\texttt{pub}_A(m)$
> - per poter leggere il messaggio, $A$ userà la sua chiave privata per decrittare il messaggio crittato ricevuto da $B$, ovvero $\texttt{priv}_A(\texttt{pub}_A(m)) = m$

## Alg

- **In**
    - $A$ interlocutore
    - $p, q \in \mathbb{P} \mid p \neq q$, con $p, q$ sufficientemente grandi
    - $m$ messaggio ricevuto da $A \mid \textrm{MCD}(m, n) = 1$
- **Out**
    - $\texttt{pub}_A, \texttt{priv}_A$
- **Alg**
    - $n := pq$
    - $\lambda(n) := \textrm{mcm}(p-1, q-1)$
    - $e \in \mathbb{N} \mid \left \{ \begin{array}{l} 1 \lt e \lt \lambda(n) \\ \textrm{MCD}(e, \lambda(n))= 1 \end{array} \right.$
    - $d:= e^{-1} \ (\bmod \ \lambda(n))$
    - $\texttt{pub}_A = (n, e)$
    - $\texttt{priv}_A = (n, d)$
- **Oss**
    - $p \mid m \implies m^{ed} \equiv m \equiv 0 \ (\bmod \ p)$, il che comporterebbe una perdita di informazione
- **Th**
    - $\texttt{priv}_A(\texttt{pub}_A(m)) = m$
- **Dim**
    - $\left \{ \begin{array}{l} (p-1) \mid \lambda(n) \\ (q - 1) \mid \lambda(n) \end{array} \right. \implies \exists i, j \in \mathbb{Z} \mid \lambda(n) = (p-1) \cdot i  = (q - 1) \cdot j$
    - $\textrm{MCD}(m, n) = 1 \implies p \nmid m \land q \nmid m \implies \left \{ \begin{array}{l}p \nmid m \implies m^p \equiv m \iff m^{p-1} \equiv 1  \implies m^{\lambda(n)} \equiv m^{(p-1)\cdot i} \equiv 1 \ (\bmod \ p) \\ q \nmid m \implies m^q \equiv m \iff m^{q-1} \equiv 1 \implies m^{\lambda(n)} \equiv m^{(q-1)\cdot j} \equiv 1 \ (\bmod \ q) \end{array} \right. \iff m^{\lambda(n)} \equiv 1 \ (\bmod \ n)$
    - $\textrm{MCD}(e, \lambda(n)) = 1 \iff [e] \in \mathbb{Z}^*_{\lambda(n)} \implies \exists ! [d] \in \mathbb{Z}^*_{\lambda(n)} \mid ed \equiv 1 \ (\bmod \ \lambda(n)) \implies \forall k \in \mathbb{Z} \quad ed = 1 + k \cdot\lambda(n)$
    - allora si ha che $(m^e)^d \equiv m^{1 + k \cdot \lambda(n)} \equiv m \cdot (m^{\lambda(n)})^k \equiv m \ (\bmod \ n)$
    - allora $m^e$ sarà il messaggio crittato ricevuto da $A$, e $(m^e)^d \ (\bmod \ n)$ restituirà $m$

## Alg

- ⚠️ **regola di ruffini**

