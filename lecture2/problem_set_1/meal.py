import sys

def main():
    resp = convert(input("What time is it? "))
    if 7.0 <= resp <= 8.0:
        print("breakfast Time")
    elif 12 <= resp <= 13: 
        print("lunch Time")
    elif 18 <= resp <= 19:
         print("dinner Time")
    else:
        sys.exit()
   

def convert(time):
    hor, min = time.split(":")
    min = float(int(min)/60)
    hor = float(hor)
    return hor + min
   


if __name__ == "__main__":
    main()