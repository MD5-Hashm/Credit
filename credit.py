#Made by MD5-Hashm with love :)
import sys
from pathlib import Path
noargs = True
credit_text = "#The following code has been completely written by MD5-Hashm on github\n"
if len(sys.argv) > 1:
    file = sys.argv[1]
    noargs = False
else:
    pass
if noargs == True:
    file = Path(input("File: "))
with open(file, 'r') as f:
    contents = f.read()
with open(file, 'w') as f:
    f.write(credit_text)
    f.write(contents)