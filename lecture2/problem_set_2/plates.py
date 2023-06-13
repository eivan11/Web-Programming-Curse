import string
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    marks = string.punctuation.split()
    if s.isupper() and  2 <= len(s) <=6 and s[0].isalpha() and s[1].isalpha() and not s in marks :
        print(marks)
        return True

         
    else:
        return False


main()