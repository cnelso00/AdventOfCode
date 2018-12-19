def check_for_id_match(id_str):
    with open("day2.input","r") as file: 
        lines = file.readlines()
        for line in lines:
            line = line.split("\n")[0]
            answer = line
            """
            super useful trick from here: https://stackoverflow.com/questions/24226451/iterate-through-two-strings-returning-the-count-when-characters-at-the-same-ind
            """ 
            diff = len(list(filter(lambda xy: xy[0] != xy[1], zip(id_str, line))))
            if diff == 1:
                print("id_str: " + id_str)
                print("ans: " + answer)


def search_all_str():
    with open("day2.input","r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.split("\n")[0]
            check_for_id_match(line)

search_all_str()
            

