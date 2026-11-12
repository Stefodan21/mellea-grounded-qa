
import dbloader
import chunker

def main():
    dbloader.load_documents()
    chunker.chunk_documents()

if __name__ == "__main__":
    main()
