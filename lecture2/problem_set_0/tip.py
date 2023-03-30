def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
        d = float(d.lstrip("$"))
        #d = d.split(".")
        return d


def percent_to_float(p):
    h = p.rstrip('%')
    h = int(h) / 100
    return h


if __name__ == "__main__":
    main()