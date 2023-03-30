def main():
    imp = input().split()
    for opt in range(len(imp)):
        if opt+1 < len(imp):
            print(imp[opt], end="")
            print("...", end="")
        else:
            print(imp[opt])

    
if __name__ == "__main__":
    main()