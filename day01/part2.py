with open("input.txt") as file:
    data = file.read()

total = 0
numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for line in data.strip().split():
    digit1 = None
    digit2 = None
    for i in range(len(line)):
        c = line[i]
        current_num = None
        if c.isdigit():
            current_num = int(c)

        for j, num in enumerate(numbers):
            if line[i : i + len(num)] == num:
                current_num = j + 1
                break

        if current_num:
            if digit1 is None:
                digit1 = current_num
            digit2 = current_num

    total += digit1 * 10 + digit2

print(total)
