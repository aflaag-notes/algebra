# Numeri complessi

## Def

- **Insieme dei complessi**
> - $\mathbb{C}:=\left\{a+i b \mid a, b \in \mathbb{R}, \  i : i^{2}=-1\right\}$ è l'**insieme dei complessi**
> - $z \in \mathbb{C} \implies\left\{\begin{array}{l}a:=\operatorname{Re}(z) \\ b:=\operatorname{Im}(z)\end{array}\right.$

## Oss

- $\left\{\begin{array}{l}z=a+i b \\ w=c+i d \end{array}\right. \implies \left\{\begin{array}{l}z + w = (a+b)+i (c +d)\\ z\cdot w=(a c-b d)+i(ad+ bc) \end{array}\right.$

## Def

- **Coniugato**

> - $z=a+i b$
> - $\bar{z}:=a-i b$ è il **coniugato** di $z$

## Oss

- $\overline{z}+\overline{w}=\overline{z+w}$
- $\overline{z} \cdot \overline{w}=\overline{z \cdot w}$

## Formula di Eulero

- $\forall \theta \quad e^{i \theta}=\cos \theta+i \sin \theta$

## Def

- **Raggio**
> - $z = a+ib$
> - $|z|:=\sqrt{a^{2}+b^{2}}$ è il **raggio** di $z$
>   - è la distanza di $z$ dall'origine nel piano di Gauss

## Forma polare

- $\forall z \in \mathbb{C}-0 \implies z=|z|\cdot e^{i \theta}$

## Def

> - $\arg(z) \subset \mathbb{R}$ è l'**insieme delle soluzioni** del sistema $\left\{\begin{array}{l}\cos \theta=\frac{a}{|z|} \\ \sin \theta=\frac{b}{|z|}\end{array}\right.$
> - per definizione, $\textrm{arg}(z) \implies \exists ! \theta \mid 0 \leq \theta \le 2 \pi$ tale che $\theta$ sia soluzione del sistema, e questo prende il nome di $\textrm{Arg}(z)$, detta **soluzione principale**

## Oss

- **Hp**
  - $(\mathbb{C}, +, \cdot)$ è un gruppo
- **Th**
  - $(\mathbb{C}, +, \cdot )$ è un campo
- **Dim**
  - $
\left.\begin{array}{l}
z \cdot \bar{z}=(a+i b)(a-i b)=a^{2}-(i b)^{2} \\
i^{2}=-1
\end{array} \right \} \implies a^{2}-i^{2} b^{2}=a^{2}+b^{2}=|z|^{2} 
$
  - $z \cdot \bar{z}=|z|^{2} \iff z=\dfrac{|z|^{2}}{\bar{z}} \iff z^{-1}=\dfrac{z}{|z|^{2}} = \dfrac{a}{a^2+b^2}- i \dfrac{b}{a^2+b^2} \implies \mathbb{C}$ ammette inversi moltiplicativi $\implies (\mathbb{C}, +, \cdot)$ è un campo

## Oss

- $|z \cdot w|=|z|\cdot |w| \quad \arg(z\cdot w)=\arg(z) + \arg(w)$
- $|\overline{w}|=|w| \quad \arg(\overline{w})=-\arg(w)$
- $|w^{-1}|={|w|}^{-1}\quad \arg(w^{-1})=-\arg(w)$
- $\left|\dfrac{z}{w}\right|=\dfrac{|z|}{|w|} \quad \arg\left(\dfrac{z}{w}\right)=\arg(z) - \arg(w)$

## Formula di de Moivre
  - $z^{n}=|z|^{n} e^{i n \theta} \quad \arg \left(z^{n}\right)=n \arg (z)$
