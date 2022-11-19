import os
import re

if not os.path.isdir("./temp"):
    os.mkdir("temp")

for file in os.listdir("mds"):
    name_no_ext = file.split(".")[0]

    with open("mds/" + file) as F:
        content = re.sub("⚠️", "!!!", F.read())
        content = re.sub("\\\\lt", "<", content)
        content = re.sub("\\\\gt", ">", content)

    with open("temp/" + name_no_ext + ".md", "w") as NF:
        NF.write(content)

    print("Processing " + name_no_ext + ".md")

    os.system("pandoc temp/" + name_no_ext + ".md -t pdf -V geometry:a4paper -o pdfs/" + name_no_ext + ".pdf")

os.system("rm -rf ./temp")
