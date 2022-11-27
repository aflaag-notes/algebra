import os

print("Extracting...", end="")

os.system("python py/extractor.py")

print("Extraction completed.\n")

os.system("python py/md2html.py")

print()

os.system("python py/charcounter.py")
