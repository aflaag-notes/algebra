import os
import re

if not os.path.isdir("./temp"):
    os.mkdir("temp")

if not os.path.isdir("./html"):
    os.mkdir("html")

for file in os.listdir("mds"):
    name_no_ext = file.split(".")[0]

    with open("mds/" + file) as F:
        content = F.read()

        if name_no_ext == "everything":
            content = re.sub("⚠️", "!!!", content)
            content = re.sub("✅", "", content)
            content = re.sub("\\\\lt", "<", content)
            content = re.sub("\\\\gt", ">", content)

    with open("temp/" + name_no_ext + ".md", "w") as NF:
        NF.write(content)

    os.system(f"pandoc --standalone --katex --metadata title=\" \" -f markdown -t html temp/" + name_no_ext + ".md -o temp/" + name_no_ext + ".html")

    with open("temp/" + name_no_ext + ".html") as B:
        content = B.read()
        content = re.sub("#fdfdfd", "#1f1f1f", content)
        content = re.sub("#1a1a1a", "#fdfdfd", content)
        content = re.sub("#606060", "#adbac7", content)

        with open("html/" + name_no_ext + ".html", "w") as NB:
            NB.write(content)

    print(name_no_ext + ".html was successfully created")

    if name_no_ext == "everything":
        os.system("pandoc temp/" + name_no_ext + ".md -t pdf -V geometry:a4paper -o " + name_no_ext + ".pdf")

        print(name_no_ext + ".pdf was successfully created")

os.system("rm -rf ./temp")
