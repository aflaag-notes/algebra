import os
import re

def filter_content(parts):
    text_part = ""

    for line in part.split("\n"):
        if line == "- **Dim**":
            return text_part

        text_part += line + "\n"

    if "> -" not in text_part:
        return text_part 

out = "# DISCLAIMER\n\nQuesto è un file che contiene una lista di tutti i teoremi, osservazioni, esempi, lemmi, corollari, formule e proposizioni **senza alcuna dimostrazione né definizione**, di conseguenza molte informazioni risulteranno essere senza alcun contesto se già non si conosce la materia. Detto questo, buona lettura.\n\n****\n"

i = 1

for file in os.listdir("mds/"):
    if file != "everything.md":
        with open("mds/" + file) as md:
            parts = re.split("## Ex|## Oss|## Def|## Lem|## Cor|## Formula di de Moivre|## Formula di Eulero", md.read())
            
            for y, part in enumerate(parts):
                if (s := filter_content(part)):
                    out += s

                    if y != len(parts) - 1:
                        out += "\n## Teorema " + str(i) + "\n"

                        i += 1

            out += "\n\n****\n"

with open("mds/everything.md", "w+") as f:
    f.write(out)
