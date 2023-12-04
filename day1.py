
def part1():
    print("Hello World!")
    words = get_text().split()
    outputs = []
    for word in words:
        first_digit = get_first_digit(word)
        last_digit = get_last_digit(word)
        number = (first_digit * 10) + last_digit
        outputs.append(number)
    print(outputs)
    Answer = calculate(outputs)
    print(Answer)

def calculate(output):
    Answer = 0
    for numbers in output:
        Answer += numbers
    return Answer
        

def get_first_digit(string):
    for i in string:
        if i.isdigit():
            return int(i)


def get_last_digit(string):
    for i in range(len(string)-1, -1, -1):
        if string[i].isdigit():
            return int(string[i])

def get_text():
    read_file = open("data.txt", "r")
    text = read_file.read()
    read_file.close()
    return text  

# part1()



def part2():
    words = get_text().split()
    words = make_string_to_number(words)
    outputs = []
    for word in words:
        first_digit = get_first_digit(word)
        last_digit = get_last_digit(word)
        number = (first_digit * 10) + last_digit
        outputs.append(number)
    Answer = calculate(outputs)
    print(Answer)


def make_string_to_number(string):
    number = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    replace = ["o1e", "t2o", "t3e", "f4r", "f5e", "s6x", "s7n", "e8t", "n9e"]
    
    new = []
    for word in string:
        for i in range(len(number)):
            
            word = word.replace(number[i], replace[i])
        new.append(word)
    return new
  
part2()


    