with open("Day1Input.txt","r") as file:
    lines = file.readlines()
    freq = 0
    for line in lines:
        sign = line[0]
        value = int(line[1:])
        if sign == "-":
            value = value * -1
        freq = freq + value
    print(freq)


