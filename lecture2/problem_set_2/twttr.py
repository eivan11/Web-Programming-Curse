def delet_vowels(text):
    vowels = ["a","e","i","o","u"]
    for pos in vowels:
        text = text.replace(pos,"")
    return text

def main():
    tr= delet_vowels(input("Input: "))
    print(f"Output: {tr}")

main()
