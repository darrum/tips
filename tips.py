def main():
    dollars = dollars_to_float(input("How much was the meal? ").rstrip())
    percent = percent_to_float(input("What percentage would you like to tip? ").rstrip())
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):  
    return float(d.replace(",", ".").replace("$", ""))


def percent_to_float(p):
    return float(p.replace(",", ".").replace("%", ""))/100


if __name__ == "__main__":
    main()
