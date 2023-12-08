def get_text():
    game = []
    read_file = open("day4data.txt", "r")
    for line in read_file:
        game.append(line.rstrip('\n'))  # Remove newline characters
    read_file.close()
    return game 

def dosomething2(text):
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

def dosomething(text):
    text = text.split(":")
    games = text[1].split("|")
    winning_numbers = games[0].split()
    numbers = games[1].split()
    points = 0
    for number in numbers:
      for winning_number in winning_numbers:   
           if number == winning_number:
              if points == 0: 
                points = 1
              else:
                points = points * 2
    return points            
                
def main2():
    games = get_text()
    point = 0
    total_cards = 0
    cards = []
    while len(cards) < len(games):
        cards.append(1)
    
    for i in range(len(games)):
      total_cards += cards[i]
      point = dosomething2(games[i])

      if point > 0:
        for k in range(point):
          if i + k +  1 < len(cards):
            cards[i + k + 1] += cards[i]

    print(total_cards)
      
    # for i in range(len(games)):
    #     print("on card = " + str(i))
    #     point = 0
    #     for j in range(cards[i]):
    #         total_cards += 1
    #         if point == 0:
    #           point = dosomething(games[i])
    #         for k in range(point):
    #             if i + k +  1 < len(cards):
    #               cards[i + k + 1] += 1
    print(point)
    print(total_cards)

def main():
    games = get_text()
    point = 0
    for game in games:
      point += dosomething(game)
    print(point)

main()

main2()