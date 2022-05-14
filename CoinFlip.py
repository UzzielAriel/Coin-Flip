import random, datetime, time
coins = 100
class flipcoin:
  def __init__(self, aoc, pick, bet):
    self.aoc = aoc
    self.pick = pick
    self.bet = bet
  def getrandom(self):
    random.seed(datetime.datetime.now().strftime("%f"))
    self.randomnumber = random.randint(1,2)
    if self.randomnumber == 1:
      self.hot = "heads"
    else:
      self.hot = "tails"
  def checkbet(self):
    if self.bet > self.aoc:
      print("You don't have that many coins")
      time.sleep(2)
      flipcoinx(self.aoc)
    elif self.bet < 0:
      print("Invalid bet")
      time.sleep(2)
      flipcoinx(self.aoc)
    elif self.bet == self.aoc:
      print("Can't place this bet - the same as your coin balance")
      time.sleep(2)
      flipcoinx(self.aoc)
  def check(self):
    if self.pick.lower() == self.hot:
      print("You guessed correct")
      coins = self.aoc + self.bet
      print(str(coins) + " is your new coin balance")
      time.sleep(2)
      
      flipcoinx(coins)
    else:
      print("You guessed wrong")
      coins = self.aoc - self.bet
      print(str(coins) + " is your new coin balance")
      time.sleep(2)
      
      flipcoinx(coins)

def flipcoinx(coins):
  
  print("You have "+ str(coins) + " coins")
  bet = float(input("Enter your bet: "))
  hotobject = flipcoin(coins, input("Heads or tails?\n"), bet)
  hotobject.getrandom()

  hotobject.checkbet()

  hotobject.check()


flipcoinx(coins)
