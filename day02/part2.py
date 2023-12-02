with open("input.txt") as file:
    lines = file.read().strip().split("\n")

answer = 0
for line in lines:
    game, cube_sets = line.split(": ")
    game_id = int(game.split(" ")[1])
    max_red = 0
    max_green = 0
    max_blue = 0
    for cube_set in cube_sets.split("; "):
        for cubes in cube_set.split(", "):
            num, color = cubes.split()
            if color == "red":
                max_red = max(max_red, int(num))
            if color == "green":
                max_green = max(max_green, int(num))
            if color == "blue":
                max_blue = max(max_blue, int(num))

    answer += max_red * max_green * max_blue

print(answer)
