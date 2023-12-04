def get_text():
    game = []
    read_file = open("day4data.txt", "r")
    for line in read_file:
        game.append(line.rstrip('\n'))  # Remove newline characters
    read_file.close()
    return game 

def dosomething(text):
    text = text.split(":")
    games = text[1].split("|")
    winning_numbers = games[0].split()
    numbers = games[1].split()
    points = 0
    for number in numbers:
      for winning_number in winning_numbers:   
           if number == winning_number:
              points += 1
              # FIRST SOLUTION
              # if points == 0: 
              #    points = 1
              # else:
              #   points = points * 2
    return points
                
                
def main():
    games = get_text()
    point = 0
    total_cards = 0
    cards = []
    while len(cards) < len(games):
        cards.append(1)
     
    for i in range(len(games)):
        for j in range(cards[i]):
            total_cards += 1
            point = dosomething(games[i])
            for k in range(point):
                if i + k +  1 < len(cards):
                  cards[i + k + 1] += 1
    

    
    print(point)
    print(total_cards)



main()