import sys
import os
import json
import python-docx
import pathlib
import dbloader as dbl
import LangChain as Lan

# checks if the text.json exists
if not dbl.outputfile.exists():
    raise FileNotFoundError("the json file doesn't exist. Try running dbloader.py first.")

# then opens load the json file as f
with open(dbl.outputfile, "r") as f:
    documents = json.load(f)
    
for doc in documents:
    

       
    
    
    
    

if __name__ == "__main__":
    main()