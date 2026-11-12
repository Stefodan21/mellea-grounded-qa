import sys
import config as c
import os
import json
import python-docx
import pathlib
import dbloader as dbl
from langchain_text_splitters import RecursiveCharacterTextSplitter as rcts



# checks if the text.json exists
if not dbl.outputfile.exists():
    raise FileNotFoundError("the json file doesn't exist. Try running dbloader.py first.")

# then opens load the json file as f
with open(dbl.outputfile, "r") as f:
    documents = json.load(f)
    
    
splitter = rcts.from_tiktoken_encoder(
    encoding_name=c.TOKENIZER,
    chunk_size=c.CHUNK_SIZE,
    chunk_overlap=c.CHUNK_OVERLAP
)
for doc in documents:

    

       
    
    
    
    

if __name__ == "__main__":
    main()