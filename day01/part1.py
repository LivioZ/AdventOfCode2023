def main():
    with open("input.txt") as file:
        total = 0
        for line in file:
            digit1 = None
            digit2 = None
            for c in line:
                is_num = c.isnumeric()
                if digit1 is None and is_num:
                    digit1 = c
                if is_num:
                    digit2 = c
            total += int(digit1 + digit2)
        print(total)


if __name__ == "__main__":
    main()
