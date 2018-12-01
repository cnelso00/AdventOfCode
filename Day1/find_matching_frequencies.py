master_encounters = {}
freq = 0

def add_freq_channel(encounters, freq):
        with open("Input.txt","r") as file:
            lines = file.readlines()
            for line in lines:
                sign = line[0]
                value = int(line[1:])
                if sign == "-":
                    value = value * -1
                freq = freq + value
                if encounters.get(freq, None) == True:
                    print(freq)
                    exit()
                else:
                    encounters[freq] = True
        return freq

always_loop = True
while(always_loop):
    freq = add_freq_channel(master_encounters, freq)
