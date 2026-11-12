import sys
import config as c
import os
import json
import python-docx
import pathlib
from docx import Document

# Paths for the output JSON file and the folder containing Word documents
outputfile = pathlib.Path("textjson/text.json")
folder = pathlib.Path("corpus")

# Make sure the output folder exists
outputfile.parent.mkdir(parents=True, exist_ok=True)

# Create the JSON file if it doesn't exist
if not outputfile.exists():
    with open(outputfile, "w") as f:
        json.dump([], f)

# Store the documents
documents = []

# Read each Word document
try:
    for file in folder.iterdir():
        doc = Document(file)
        
        text = "\n".join([p.text for p in doc.paragraphs])
        documents.append({
            "file": str(file),
            "text": text
            })

# If any error occurs while processing a file, it will be raised with the file name included
except Exception as e:
    raise Exception("Error processing file: " + str(file)) from e
    
# Write the documents to the JSON file
with open(outputfile, "w", encoding="utf-8") as f:
    json.dump(
        documents, 
        f, 
        indent=c.JSON_INDENT,
        ensure_ascii=c.JSON_ENSURE_ASCII,
        sort_keys=c.JSON_SORT_KEYS
    )
    

if __name__ == "__main__":
    main()

# chunks = {}

# output = "output.json"

# dfolder = "corpus"
# infofolder = "chunkeddata"
# infopath = infofolder + "/" + output
# file = "file.txt"

# if not Path.exists(infopath):
#     with open(infopath, "w") as f:
#         json.dumps({}, f)


# try:
#     with open(dfolder + "/" + file) as f:
#         json.load(f)

# except FileNotFoundError:
#     raise FileNotFoundError("File not found: " + dfolder + "/" + file)

# for 
