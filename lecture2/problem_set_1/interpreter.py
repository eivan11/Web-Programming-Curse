import sys
def operation_math(inpu):
    a, b, c = inpu.split()
    a  = int(a)
    c  = int(c)
    if b == "/" and b == 0 :
        sys.exit()
    match(b):
        case "+": result = a + c
        case "-": result = a - c
        case "*": result = a * c
        case "/": result = a / c
        case _: result = 0
    return result
    

def main():
    resp = operation_math(input("Expression: "))
    print(float(resp))

if __name__ == "__main__":
    main()