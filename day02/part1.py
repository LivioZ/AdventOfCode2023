with open("input.txt") as file:
    lines = file.read().strip().split("\n")

max_red = 12
max_green = 13
max_blue = 14

answer = 0

for line in lines:
    game, cube_sets = line.split(": ")
    game_id = int(game.split(" ")[1])
    impossible_cubes = False
    for cube_set in cube_sets.split("; "):
        if impossible_cubes:
            break
        for cubes in cube_set.split(", "):
            num, color = cubes.split()

            if color == "red" and int(num) > max_red:
                impossible_cubes = True
                break
            if color == "green" and int(num) > max_green:
                impossible_cubes = True
                break
            if color == "blue" and int(num) > max_blue:
                impossible_cubes = True
                break

    if not impossible_cubes:
        answer += game_id

print(answer)
