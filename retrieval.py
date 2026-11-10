import Path

chunks = {}

output = output.json

folder = "corpus"
file = "file.txt"


try:
    with open(folder + "/" + file) as f:
        for line in f:
            chunks[chunk] = folder + "/" + file

except FileNotFoundError:
    raise FileNotFoundError("File not found: " + folder + "/" + file)
