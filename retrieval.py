import Path
import sys
import os
import json
import python-docx


chunks = {}

output = "output.json"

dfolder = "corpus"
infofolder = "chunkeddata"
infopath = infofolder + "/" + output
file = "file.txt"

if not Path.exists(infopath):
    with open(infopath, "w") as f:
        json.dumps({}, f)


try:
    with open(dfolder + "/" + file) as f:
        json.load(f)

except FileNotFoundError:
    raise FileNotFoundError("File not found: " + dfolder + "/" + file)

for 
