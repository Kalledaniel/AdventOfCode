import math
class SpeedRecord:
  def __init__(self, hold, dis) -> None:
    self.hold = hold
    self.dis = dis
  
  def printer(self):
    print(self.hold, self.dis)
  
  def calc(self):
    newrecs = 0
    a = 0
    hold = self.hold
    oldrec = self.dis
    for i in range (hold):
     if (a * (hold - a)) > oldrec:
        newrecs += 1
     a+=1
    return newrecs



def get_text(txt):
    game = []
    read_file = open(txt, "r")
    for line in read_file:
        game.append(line.rstrip('\n'))  # Remove newline characters
    read_file.close()
    return game 

def part1():
  text = get_text("day6data.txt")
  print("start day 6")

  hold = text[0].split(":")
  hold = hold[1].split()

  dis = text[1].split(":")
  dis = dis[1].split()
  
  records = []
  it = 0
  for i in hold:
     rec = SpeedRecord(int(i),int(dis[it]))
     it += 1
     records.append(rec)
  wins = []
  for i in records:
     i.printer()
     wins.append(i.calc())
  
  print(wins)
  result = 1
  for i in wins:
     result *= i
  print(result)

  tal1 = 71530 / 2#(54708275/2 - 0.5)
  tal2 = 71530 / 2# (54708275/2 + 0.5)
  print(round(tal2))
  print(round(tal1))
  max = round(tal1) * round(tal2)
  print(max)
  record = 940200# 239114212951253
  total = max - record
  print(total)
  new = math.sqrt(total) * 2
  print(new)

  



  tsvar = SpeedRecord(54708275, 239114212951253)
  svar = tsvar.calc()
  print(svar)


  
  # hello = SpeedRecord((54708275),(239114212951253))
  
  



part1()