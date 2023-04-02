def check_words(word):
    word = word.lower()
    if word == "hello" or "hello" in word:
        return 0
    elif  word.startswith("h") and word != "hello":
        return 20
    else:
        return 100
    
def main():
    print(f"${check_words(input('Greeting: '))}")


if __name__ == "__main__":
    main()