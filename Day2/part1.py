with open("day2.input","r") as file: 
    lines = file.readlines()
    two_count = 0
    three_count = 0
    for line in lines:
        letters = dict()
        line = line.split("\n")[0]
        for character in line:
            if letters.get(character, None) == None:
                letters[character] = 1
            else:
                letters[character] = letters.get(character, 0) +  1
        two_encountered = False
        three_encountered = False
        for key, value in letters.items():
            if value == 2 and not two_encountered:
                two_count += 1
                two_encountered = True
            if value == 3 and not three_encountered:
                three_encountered = True
                three_count += 1
            if two_encountered and three_encountered:
                break

    checksum = two_count * three_count
    print(str(checksum))
