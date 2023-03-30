def main():
    imput = input().split()
    new_text = []

    for pos in imput:
        if pos ==":)":
            new_text.append("🙂")
        elif pos == ":(":
            new_text.append("🙁")
        else:
            new_text.append(pos)
    
    print(*new_text)
main()