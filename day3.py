def get_text():
    game = []
    with open("day3data.txt", "r") as read_file:
        for line in read_file:
            game.append(line.rstrip('\n'))  # Remove newline characters
    return game

class PartNumber:
    def __init__(self, number, x, y):
        self.number = number
        self.x = x
        self.y = y

    def get_number(self):
        return self.number

    def set_number(self, number):
        self.number = number

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def check_left(self, data):
        if self.x != 0:
            # check top left
            if self.y != 0:
                if data[self.y-1][self.x-1] != "." and not data[self.y-1][self.x-1].isdigit():
                    return True
            # check left
            if data[self.y][self.x-1] != "." and not data[self.y][self.x-1].isdigit():
                return True
            # check bottom left
            if self.y != len(data)-1:
                if data[self.y+1][self.x-1] != "." and not data[self.y+1][self.x-1].isdigit():
                    return True
        return False

    def check_right(self, data):
        if self.x < (len(data[self.y]) - len(str(self.number))):
            # check top right
            if self.y != 0:
                if data[self.y-1][self.x + len(str(self.number))] != "." and not data[self.y-1][self.x + len(str(self.number))].isdigit():
                    return True
            # check right
            if data[self.y][self.x + len(str(self.number))] != "." and not data[self.y][self.x + len(str(self.number))].isdigit():
                return True
            # check bottom right
            if self.y != len(data)-1:
                if data[self.y+1][self.x + len(str(self.number))] != "." and not data[self.y+1][self.x + len(str(self.number))].isdigit():
                    return True
        return False

    def check_top(self, data):
        if self.y != 0:
            for i in range(len(str(self.number))):
                if data[self.y-1][self.x+i] != "." and not data[self.y-1][self.x+i].isdigit():
                    return True
        return False

    def check_bottom(self, data):
        if self.y != len(data)-1:
            for i in range(len(str(self.number))):
                if data[self.y+1][self.x+i] != "." and not data[self.y+1][self.x+i].isdigit():
                    return True
        return False

    def check_all(self, data):
        if (
            self.check_left(data) or
            self.check_right(data) or
            self.check_top(data) or
            self.check_bottom(data)
        ):
            return True
        else:
            return False

class PartNumber2:
    def __init__(self, number, x, y):
        self.number = number
        self.x = x
        self.y = y
        self.starcordinates = []

    def get_number(self):
        return self.number

    def set_number(self, number):
        self.number = number

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y

    def get_starcordinates(self):
        return self.starcordinates
    

    def check_left(self, data):
        if self.x != 0:
            # check top left
            if self.y != 0:
                if data[self.y-1][self.x-1] == "*":
                    self.starcordinates.append([self.y-1, self.x-1])
            # check left
            if data[self.y][self.x-1] == "*":
                self.starcordinates.append([self.y, self.x-1])
            # check bottom left
            if self.y != len(data)-1:
                if data[self.y+1][self.x-1] == "*":
                    self.starcordinates.append([self.y+1, self.x-1])

    def check_right(self, data):
        if self.x < (len(data[self.y]) - len(str(self.number))):
            # check top right
            if self.y != 0:
                if data[self.y-1][self.x + len(str(self.number))] == "*":
                    self.starcordinates.append([self.y-1, self.x + len(str(self.number))])
            # check right
            if data[self.y][self.x + len(str(self.number))] == "*":
                self.starcordinates.append([self.y, self.x + len(str(self.number))])
            # check bottom right
            if self.y != len(data)-1:
                if data[self.y+1][self.x + len(str(self.number))] == "*":
                    self.starcordinates.append([self.y+1, self.x + len(str(self.number))])
        

    def check_top(self, data):
        if self.y != 0:
            for i in range(len(str(self.number))):
                if data[self.y-1][self.x+i] == "*":
                    self.starcordinates.append([self.y-1, self.x+i])

    def check_bottom(self, data):
        if self.y != len(data)-1:
            for i in range(len(str(self.number))):
                if data[self.y+1][self.x+i] == "*":
                    self.starcordinates.append([self.y+1, self.x+i])

    def do_stuff(self, data):
        self.check_left(data) 
        self.check_right(data) 
        self.check_top(data)
        self.check_bottom(data)

          
def main():
    print("Day 3")
    data = get_text()
    total = 0  # total number
    current = 0  # current number
    partnumbers = []  # list of partnumbers
    con = False  # continue

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j].isdigit():
                if not con:
                    current_partnumber = PartNumber(int(data[i][j]), j, i)
                    con = True
                current = current * 10 + int(data[i][j])
            else:
                if con:
                    current_partnumber.set_number(current)
                    partnumbers.append(current_partnumber)
                    con = False
                    # Create a new instance for the next part number
                    current_partnumber = None
                current = 0

    nums = 0
    for i in range(len(partnumbers)):
        if partnumbers[i].check_all(data):
            total += partnumbers[i].get_number()
            nums += 1
            print (partnumbers[i].get_number() , " X:" , partnumbers[i].get_x() , "Y:" , partnumbers[i].get_y())



    

    print("Here is total: ")
    print(total)
    print("Here is the number of partnumbers: " , nums)
    print("Here is the number of numbers: " , len(partnumbers))
    # 509943 problem with right side
    # 554594 some problem dont know?
    print("Testing: ")
    for i in range(len(partnumbers)):
        X = partnumbers[i].get_x()
        Y = partnumbers[i].get_y()
        length = len(str(partnumbers[i].get_number()))
        number = str(partnumbers[i].get_number())
        
        for j in range(length):
            if data[Y][X+j] != number[j]:
                print("Error" , number[j] , "X:" , X+j , "Y:" , Y)


    # 551094 Correct for per
    # 553079 correft for me But i get 554594?

# main()

class Star:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cordinates = []
        self.partnumbers = []

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y

    def get_cordinates(self):
        return self.cordinates

    def get_partnumbers(self):
        return self.partnumbers

    def set_cordinates(self, cordinates):
        self.cordinates = cordinates

    def set_partnumbers(self, partnumbers):
        self.partnumbers = partnumbers

    def add_cordinates(self, cordinates):
        self.cordinates.append(cordinates)

    def add_partnumbers(self, partnumbers):
        self.partnumbers.append(partnumbers)

    def check_cordinates(self, cordinates):
        for i in range(len(self.cordinates)):
            if self.cordinates[i] == cordinates:
                return True
        return False

    def check_partnumbers(self, partnumbers):
        for i in range(len(self.partnumbers)):
            if self.partnumbers[i] == partnumbers:
                return True
        return False

    def check_all(self, cordinates, partnumbers):
        if self.check_cordinates(cordinates) or self.check_partnumbers(partnumbers):
            return True
        else:
            return False


def test2():
    print("Day 3")
    data = get_text()
    total = 0  # total number
    current = 0  # current number
    partnumbers = []  # list of partnumbers
    con = False  # continue
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j].isdigit():
                if not con:
                    current_partnumber = PartNumber2(int(data[i][j]), j, i)
                    con = True
                current = current * 10 + int(data[i][j])
            else:
                if con:
                    current_partnumber.set_number(current)
                    partnumbers.append(current_partnumber)
                    con = False
                    # Create a new instance for the next part number
                    current_partnumber = None
                current = 0

   #create 2d array with same size as data
    w, h = len(data[0]), len(data)
    stars = [[0 for x in range(w)] for y in range(h)]
    
    for i in range(len(data)):
        for j in range(len(data[i])):
                stars[i][j] = Star(j, i)
    
    for i in range(len(partnumbers)):
        partnumbers[i].do_stuff(data)
        for j in range(len(partnumbers[i].get_starcordinates())):
            x = partnumbers[i].get_starcordinates()[j][1]
            y = partnumbers[i].get_starcordinates()[j][0]
            stars[y][x].add_cordinates([y,x])
            stars[y][x].add_partnumbers(partnumbers[i].get_number())
    
    for i in range(len(stars)):
        for j in range(len(stars[i])):
            if len(stars[i][j].get_partnumbers()) == 2:
                total += stars[i][j].get_partnumbers()[0] * stars[i][j].get_partnumbers()[1]
                print(stars[i][j].get_partnumbers()[0], " And ", stars[i][j].get_partnumbers()[1] , " X:" , stars[i][j].get_x() , "Y:" , stars[i][j].get_y())

    for i in range(len(partnumbers)):
        Valid = partnumbers[i].get_starcordinates()
        word = " !!! STAR !!!= "
        if len(Valid) > 0:
            for each in Valid:
                word += f"* x {each[1]} y {each[0]} "
            print(partnumbers[i].get_number() , " X:" , partnumbers[i].get_x() , "Y:" , partnumbers[i].get_y(), word)
            

    print("Here is numbers: " , len(partnumbers))
    print(total)

test2()




