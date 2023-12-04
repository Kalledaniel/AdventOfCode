
def main ():
    print("Day 2")
    data = get_text()

    success = 0
    for i in range(len(data)):
        if checkColor(data[i]):
            success += i+1
            print((i) + 1, "success")
        else:
            print((i) + 1, "fail")
    print(success)
    
    sum = 0
    for i in range(len(data)):
        sum += getsum(data[i])
    print("the sum is : " + str(sum))
        
        

def checkColor(text):
    RedMax = 12 
    GreenMax = 13
    BlueMax = 14
    text = text.split(":")
    games = text[1].split(";")
    biggest_red = 0
    biggest_green = 0
    biggest_blue = 0

    for game in games:
        pull = game.split(",")
        for pull in pull:
            if "red" in pull:
                num = pull.split("red")
                red = int(num[0])
                if red > biggest_red:
                    biggest_red = red
                
            elif "green" in pull:
                num = pull.split("green")
                green = int(num[0])
                if green > biggest_green:
                    biggest_green = green
            elif "blue" in pull:
                num = pull.split("blue")
                blue = int(num[0])
                if blue > biggest_blue:
                    biggest_blue = blue
    if biggest_red > RedMax or biggest_green > GreenMax or biggest_blue > BlueMax:
        return False
    else:
        return True
      

def getsum(text):
    text = text.split(":")
    games = text[1].split(";")
    biggest_red = 0
    biggest_green = 0
    biggest_blue = 0

    for game in games:
        pull = game.split(",")
        for pull in pull:
            if "red" in pull:
                num = pull.split("red")
                red = int(num[0])
                if red > biggest_red:
                    biggest_red = red
                
            elif "green" in pull:
                num = pull.split("green")
                green = int(num[0])
                if green > biggest_green:
                    biggest_green = green
            elif "blue" in pull:
                num = pull.split("blue")
                blue = int(num[0])
                if blue > biggest_blue:
                    biggest_blue = blue
    return biggest_red * biggest_green * biggest_blue

def get_text():
    game = []
    read_file = open("day2data.txt", "r")
    for line in read_file:
        game.append(line)
    read_file.close()
    return game 

main()