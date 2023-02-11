import os
import re

def filter_content(parts):
    text_part = ""

    k = part.split("\n")

    for i, line in enumerate(k):
        if line == "- **Dim**":
            for j in range(i + 1, len(k)):
                if k[j] == "****":
                    return text_part + "\n".join(k[j-1:]), False
            return text_part, False

        text_part += line + "\n"

    return text_part, "> -" in text_part

out = "# Everything\n\n## DISCLAIMER\n\nQuesto è un file che contiene una lista di tutti i teoremi, osservazioni, definizioni, esempi, lemmi, corollari, formule e proposizioni **senza alcuna dimostrazione**, di conseguenza molte informazioni risulteranno essere senza alcun contesto se già non si conosce la materia. Detto questo, buona lettura.\n\n****\n"

i = 1
d = 1

order = {
    "gruppi-e-anelli.md": 0,
    "ideali.md": 1,
    "relazioni.md": 2,
    "insieme-quoziente.md": 3,
    "permutazioni.md": 4,
    "morfismi.md": 5,
    "gruppi-diedrali.md": 6,
    "polinomi.md": 7,
    "spazi-vettoriali.md": 8,
    "matrici.md": 9,
    "determinante.md": 10,
    "numeri-complessi.md": 11,
    "coefficienti-binomiali.md": 12,
    "induzione.md": 13,
    "altro.md": 14,

    "index.md": -1,
    "teoremi-fondamentali.md": -1,
    "everything.md": -1,
}

for file in sorted(os.listdir("mds/"), key=lambda name: order[name]):
    if file != "everything.md" and file != "index.md" and file != "teoremi-fondamentali.md":
        with open("mds/" + file) as md:
            parts = re.split("## Teorema cinese dei resti|## Ex|## Oss|## Def|## Lem|## Cor|## Alg|## Formula di de Moivre|## Formula di Eulero|## Formula di Grassmann|## Formula di Leibniz|## Formula di Laplace", md.read())
            
            for y, part in enumerate(parts):
                if (a := filter_content(part)):
                    s, isdef = a

                    if y != 0:
                        if isdef:
                            out += "\n## Definizione " + str(d) + "\n"
                            d += 1
                        else:
                            out += "\n## Teorema " + str(i) + "\n"
                            i += 1

                    out += s

            out += "\n\n****\n"

with open("mds/teoremi-fondamentali.md") as TF:
    parts = TF.read().split("****")

    for part in parts:
        s2 = []

        indim = False

        for line in part.split("\n"):
            if line == "- **Dim**":
                indim = True

            if line.startswith("## Oss") or line.startswith("## Cor") or line.startswith("## Lem") or line.startswith("## Ex") or line.startswith("## Alg"):
                s2.append("\n## Teorema " + str(i) + "\n")
                i += 1

                indim = False
                continue

            if not indim:
                s2.append(line)

        out += "\n".join(s2) + "\n\n****\n"

with open("mds/everything.md", "w+") as f:
    f.write("\n".join(out.split("\n")[:-2]))
