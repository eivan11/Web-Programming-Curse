def convert_camel_case(frase):
    newFrase = []

    for apn in frase:
        if apn.isupper() and not apn.isspace():
            newFrase.append("_")
            apn=apn.swapcase()
            newFrase.append(apn)
        else:
            newFrase.append(apn)
        
    return newFrase



def main():
    frase = convert_camel_case(input("camelCase: "))
    print("snake_case: ",end="")
    for pos in frase:
        print(f"{pos}", end="")
    print('')

if __name__ == "__main__":
    main()