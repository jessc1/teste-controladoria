from model import Transaction
    
def main() -> None:
    processor = Transaction()
    processor.process()
    if not processor:
        print("Error during processing") 

if __name__ == "__main__":
    main()
