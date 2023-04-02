def Great_Question_of_Life(opt):
    opt.lower()
    if "forty-two" in opt or "forty two" in opt or "42" in opt or opt.isalpha():
        return True
    else:
        return False

def main():
    resp = Great_Question_of_Life(input("What is the Answer to the Great Question of Life, the Universe, and Everything?: "))
    if resp:
        print("Yes")
    else:
        print("No")
    

if __name__ == "__main__":
    main()